"""
EAR Triangulation Engine — Orchestrator v2

Flow per concept:
  DIRECTOR → concept + domain
       │
       ▼ (parallel, blind to each other)
  ┌────────┬────────┬────────┬────────┐
  │ SYNTH  │  Ag-Δ  │  Ag-⇄  │  Ag-⟳  │
  │(all)   │(Rules) │(Kernel)│(Arche) │
  └───┬────┴───┬────┴───┬────┴───┬────┘
      │        │        │        │
      ▼        ▼        ▼        ▼
    REF       r-Δ      r-⇄      r-⟳
      │        │        │        │
      ▼ TRIBUNAL: r-Δ==REF? r-⇄==REF? r-⟳==REF?
      │
      ├── 3/3 ──→ SCRIBA (insert + backup)
      │
      └── <3/3 ─→ ARBITER (blind spot analysis → review list)
      │
      ▼
      wait → DIRECTOR → next concept

Mutual exclusion: per concept, either Scriba OR Arbiter runs, never both.
"""

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from core.llm_adapter import LLMProvider, create_provider
from core.tribunal import (
    parse_agent_output, run_tribunal, format_tribunal_report,
    Route, TribunalResult
)
from agents.prompts import (
    SYNTH_SYSTEM, AGENT_DELTA_SYSTEM, AGENT_REL_SYSTEM, AGENT_PROC_SYSTEM,
    ARBITER_SYSTEM, BLIND_SPOT_DOCUMENT, SCRIBA_SYSTEM
)
from agents.scriba import Scriba, format_scriba_report


class TriangulationEngine:
    """
    Main engine v2. 7-agent architecture with mutual exclusion.
    """
    
    def __init__(self, config_path: str = "config.json"):
        self.config = self._load_config(config_path)
        self.provider = create_provider(self.config["llm"].copy())
        
        # Load reference documents
        self.rules_doc = self._load_doc(self.config["documents"]["rules"])
        self.kernel_doc = self._load_doc(self.config["documents"]["kernel"])
        self.archetypes_doc = self._load_doc(self.config["documents"]["archetypes"])
        
        # Scriba (network writer)
        network_path = self.config.get("network_path", "data/network_state.json")
        backup_dir = self.config.get("backup_dir", "data/backups")
        self.scriba = Scriba(network_path=network_path, backup_dir=backup_dir)
        
        # Results storage
        self.results_dir = Path(self.config.get("output_dir", "results"))
        self.results_dir.mkdir(exist_ok=True)
        
        # Review list (Arbiter outputs)
        self.review_dir = Path(self.config.get("review_dir", "results/review"))
        self.review_dir.mkdir(parents=True, exist_ok=True)
        
        # Stats
        self.total_tokens = 0
        self.total_calls = 0
    
    def _load_config(self, path: str) -> dict:
        with open(path, "r") as f:
            return json.load(f)
    
    def _load_doc(self, path: str) -> str:
        with open(path, "r") as f:
            return f.read()
    
    def _call_llm(self, system: str, user: str, label: str = "") -> str:
        """Call LLM with tracking."""
        t0 = time.time()
        response = self.provider.complete(system=system, user=user)
        elapsed = time.time() - t0
        
        self.total_tokens += response.tokens_in + response.tokens_out
        self.total_calls += 1
        
        if self.config.get("verbose", False):
            print(f"  [{label}] {response.tokens_in}+{response.tokens_out} tokens, {elapsed:.1f}s")
        
        return response.text
    
    # ─── 4 Parallel Mappers ───
    
    def run_synth(self, concept: str, domain: str = "") -> dict:
        """SYNTH mapper — all documents, reference benchmark."""
        system = SYNTH_SYSTEM.format(
            rules_document=self.rules_doc,
            kernel_document=self.kernel_doc,
            archetypes_document=self.archetypes_doc
        )
        user_msg = f"Concept: {concept}"
        if domain:
            user_msg += f"\nDomain: {domain}"
        
        raw = self._call_llm(system, user_msg, label="SYNTH")
        return parse_agent_output(raw)
    
    def run_agent_delta(self, concept: str, domain: str = "") -> dict:
        """Agent-Δ — Rules only."""
        system = AGENT_DELTA_SYSTEM.format(rules_document=self.rules_doc)
        user_msg = f"Concept: {concept}"
        if domain:
            user_msg += f"\nDomain: {domain}"
        
        raw = self._call_llm(system, user_msg, label="Ag-Δ")
        return parse_agent_output(raw)
    
    def run_agent_rel(self, concept: str, domain: str = "") -> dict:
        """Agent-⇄ — Kernel only."""
        system = AGENT_REL_SYSTEM.format(kernel_document=self.kernel_doc)
        user_msg = f"Concept: {concept}"
        if domain:
            user_msg += f"\nDomain: {domain}"
        
        raw = self._call_llm(system, user_msg, label="Ag-⇄")
        return parse_agent_output(raw)
    
    def run_agent_proc(self, concept: str, domain: str = "") -> dict:
        """Agent-⟳ — Archetypes only."""
        system = AGENT_PROC_SYSTEM.format(archetypes_document=self.archetypes_doc)
        user_msg = f"Concept: {concept}"
        if domain:
            user_msg += f"\nDomain: {domain}"
        
        raw = self._call_llm(system, user_msg, label="Ag-⟳")
        return parse_agent_output(raw)
    
    # ─── Post-Tribunal Paths (mutually exclusive) ───
    
    def run_arbiter(self, synth_output: dict, monodoc_outputs: dict,
                    tribunal_result: TribunalResult) -> dict:
        """Arbiter — blind spot analysis. Called only on <3/3."""
        system = ARBITER_SYSTEM.format(blind_spot_document=BLIND_SPOT_DOCUMENT)
        
        user_msg = json.dumps({
            "concept": tribunal_result.concept,
            "synth": synth_output,
            "agent_delta": monodoc_outputs.get("delta", {}),
            "agent_rel": monodoc_outputs.get("rel", {}),
            "agent_proc": monodoc_outputs.get("proc", {}),
            "tribunal_match_score": tribunal_result.total_match_score,
            "tribunal_summary": tribunal_result.summary
        }, indent=2)
        
        raw = self._call_llm(system, user_msg, label="ARBITER")
        return parse_agent_output(raw)
    
    def run_scriba(self, synth_output: dict, domain: str = ""):
        """Scriba — network insertion. Called only on 3/3."""
        return self.scriba.insert(synth_output, domain)
    
    # ─── Full Pipeline ───
    
    def map_concept(self, concept: str, domain: str = "") -> dict:
        """
        Full pipeline for one concept.
        4 parallel mappers → Tribunal → Scriba XOR Arbiter
        """
        print(f"\n{'='*60}")
        print(f"MAPPING: {concept}" + (f" [{domain}]" if domain else ""))
        print(f"{'='*60}")
        
        # ── Phase 1: 4 parallel mappers ──
        # (sequential here — can be parallelized with asyncio/threads)
        
        print("\n[1/4] SYNTH (all docs)...")
        synth = self.run_synth(concept, domain)
        synth_sigma = synth.get("sigma", "?")
        print(f"  REF → {synth_sigma}")
        
        print("[2/4] Agent-Δ (Rules)...")
        agent_delta = self.run_agent_delta(concept, domain)
        print(f"  Ag-Δ → {agent_delta.get('sigma', '?')}")
        
        print("[3/4] Agent-⇄ (Kernel)...")
        agent_rel = self.run_agent_rel(concept, domain)
        print(f"  Ag-⇄ → {agent_rel.get('sigma', '?')}")
        
        print("[4/4] Agent-⟳ (Archetypes)...")
        agent_proc = self.run_agent_proc(concept, domain)
        print(f"  Ag-⟳ → {agent_proc.get('sigma', '?')}")
        
        monodocs = {
            "delta": agent_delta,
            "rel": agent_rel,
            "proc": agent_proc
        }
        
        # ── Phase 2: Tribunal ──
        print("\n[TRIBUNAL] Comparing 3 monodoc vs Synth reference...")
        tribunal = run_tribunal(concept, synth, monodocs)
        print(format_tribunal_report(tribunal))
        
        # ── Phase 3: Mutual exclusion — Scriba XOR Arbiter ──
        arbiter_result = None
        scriba_result = None
        
        if tribunal.route == Route.SCRIBA:
            # 3/3 match → insert
            print("\n[SCRIBA] 3/3 match — inserting into network...")
            scriba_result = self.run_scriba(synth, domain)
            print(format_scriba_report(scriba_result))
        
        elif tribunal.route == Route.ARBITER:
            # <3/3 → analyze divergences
            print("\n[ARBITER] <3/3 — analyzing divergences...")
            arbiter_result = self.run_arbiter(synth, monodocs, tribunal)
            
            assessment = arbiter_result.get("overall_assessment", {})
            pv = assessment.get("possible_validation", False)
            conf = assessment.get("confidence", 0)
            print(f"  Possible validation: {'YES' if pv else 'NO'}")
            print(f"  Confidence: {conf:.2f}")
            print(f"  {assessment.get('explanation', '')}")
            
            # Save to review list
            review_file = self.review_dir / f"{concept.lower().replace(' ', '_')}_review.json"
            with open(review_file, "w") as f:
                json.dump({
                    "concept": concept,
                    "domain": domain,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "synth": synth,
                    "monodocs": monodocs,
                    "tribunal_summary": tribunal.summary,
                    "arbiter": arbiter_result
                }, f, indent=2, ensure_ascii=False)
            print(f"  Saved to review: {review_file}")
        
        # ── Build complete result ──
        result = {
            "concept": concept,
            "domain": domain,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "model": self.provider.name(),
            "phase1_mappers": {
                "synth": synth,
                "delta": agent_delta,
                "rel": agent_rel,
                "proc": agent_proc
            },
            "phase2_tribunal": {
                "route": tribunal.route.value,
                "match_score": tribunal.total_match_score,
                "synth_sigma": synth_sigma,
                "summary": tribunal.summary,
                "type_match": tribunal.type_match,
                "coordinate_matches": [
                    {
                        "coord": cm.coordinate,
                        "synth": cm.synth_value,
                        "agents": cm.agent_values,
                        "matches": cm.matches,
                        "match_count": cm.match_count,
                        "dissenters": cm.dissenters
                    }
                    for cm in tribunal.coordinate_matches
                ] if tribunal.coordinate_matches else []
            },
            "phase3_route": tribunal.route.value,
            "scriba": {
                "inserted": scriba_result.inserted if scriba_result else False,
                "sigma": scriba_result.sigma if scriba_result else None,
                "backup": scriba_result.backup_path if scriba_result else None,
                "network_size": scriba_result.network_size if scriba_result else None,
                "error": scriba_result.error if scriba_result else None
            } if scriba_result else None,
            "arbiter": arbiter_result,
            "final": {
                "sigma": synth_sigma,
                "type": synth.get("type", "node"),
                "constraint_ref": synth.get("constraint_ref"),
                "status": "VALID" if tribunal.route == Route.SCRIBA else "REVIEW",
                "confidence": 0.95 if tribunal.route == Route.SCRIBA else (
                    arbiter_result.get("overall_assessment", {}).get("confidence", 0.50)
                    if arbiter_result else 0.50
                ),
                "route": tribunal.route.value
            },
            "stats": {
                "total_tokens": self.total_tokens,
                "total_calls": self.total_calls
            }
        }
        
        # Save full result
        result_file = self.results_dir / f"{concept.lower().replace(' ', '_')}.json"
        with open(result_file, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        return result
    
    def map_batch(self, concepts: list, domain: str = "") -> list:
        """Map a batch of concepts."""
        results = []
        for i, concept in enumerate(concepts):
            print(f"\n{'#'*60}")
            print(f"  BATCH [{i+1}/{len(concepts)}]")
            print(f"{'#'*60}")
            
            try:
                result = self.map_concept(concept, domain)
                results.append(result)
            except Exception as e:
                print(f"  ERROR: {e}")
                import traceback
                traceback.print_exc()
                results.append({
                    "concept": concept,
                    "error": str(e),
                    "status": "FAILED"
                })
        
        # Save batch
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        batch_file = self.results_dir / f"batch_{timestamp}.json"
        with open(batch_file, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Summary
        print(f"\n{'='*60}")
        print(f"BATCH COMPLETE: {len(results)} concepts")
        scriba_count = sum(1 for r in results if r.get("final", {}).get("route") == "SCRIBA")
        arbiter_count = sum(1 for r in results if r.get("final", {}).get("route") == "ARBITER")
        failed = sum(1 for r in results if r.get("status") == "FAILED")
        print(f"  SCRIBA (3/3): {scriba_count} | ARBITER (<3/3): {arbiter_count} | FAILED: {failed}")
        print(f"  Total tokens: {self.total_tokens}")
        print(f"  Network: {self.scriba.get_stats()}")
        print(f"  Saved to: {batch_file}")
        
        return results
    
    def get_status(self) -> dict:
        """Get current engine status."""
        stats = self.scriba.get_stats()
        review_files = list(self.review_dir.glob("*_review.json"))
        
        return {
            "network": stats,
            "pending_reviews": len(review_files),
            "review_files": [f.name for f in review_files],
            "total_tokens_session": self.total_tokens,
            "total_calls_session": self.total_calls
        }


# ─── CLI ───

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python -m orchestrator 'Schwarzschild Metric'")
        print("  python -m orchestrator 'Schwarzschild Metric' --domain physics")
        print("  python -m orchestrator --batch concepts.txt")
        print("  python -m orchestrator --batch concepts.txt --domain physics")
        print("  python -m orchestrator --status")
        sys.exit(1)
    
    engine = TriangulationEngine()
    
    if sys.argv[1] == "--status":
        status = engine.get_status()
        print(json.dumps(status, indent=2))
    elif sys.argv[1] == "--batch":
        with open(sys.argv[2]) as f:
            concepts = [line.strip() for line in f if line.strip()]
        domain = ""
        if "--domain" in sys.argv:
            idx = sys.argv.index("--domain")
            domain = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        engine.map_batch(concepts, domain)
    else:
        concept = sys.argv[1]
        domain = ""
        if "--domain" in sys.argv:
            idx = sys.argv.index("--domain")
            domain = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else ""
        result = engine.map_concept(concept, domain)
        print(f"\nFinal: {result['final']['sigma']} [{result['final']['status']}]")
