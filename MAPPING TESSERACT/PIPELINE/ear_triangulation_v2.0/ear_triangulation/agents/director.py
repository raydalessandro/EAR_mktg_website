"""
EAR Triangulation Engine — Director Agent
The brain of the system. Proposes concepts, tracks network state, handles results.
Has access to ALL documents + current network state.
Does NOT map — only decides WHAT to map and WHAT TO DO with results.
"""

import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional
from core.llm_adapter import LLMProvider


# ─── Network State Manager ───

class NetworkState:
    """
    Reads the network written by Scriba (data/network_state.json).
    Provides queries for Director. Does NOT write nodes — Scriba does that.
    Manages review_queue and reject_log in a separate director_state.json.
    """
    
    def __init__(self, network_path: str = "data/network_state.json",
                 director_state_path: str = "data/director_state.json"):
        self.network_path = Path(network_path)
        self.director_path = Path(director_state_path)
        self.review_queue = []
        self.reject_log = []
        self.history = []
        self._load_director_state()
    
    def _load_network(self) -> dict:
        """Load Scriba's network_state.json."""
        if self.network_path.exists():
            return json.loads(self.network_path.read_text())
        return {"nodes": [], "constraints": [], "stats": {"total_nodes": 0, "cells_occupied": 0}}
    
    def _load_director_state(self):
        """Load Director's own state (review queue, reject log, history)."""
        if self.director_path.exists():
            data = json.loads(self.director_path.read_text())
            self.review_queue = data.get("review_queue", [])
            self.reject_log = data.get("reject_log", [])
            self.history = data.get("history", [])
    
    def _save_director_state(self):
        """Persist Director's own state."""
        self.director_path.parent.mkdir(exist_ok=True)
        self.director_path.write_text(json.dumps({
            "review_queue": self.review_queue,
            "reject_log": self.reject_log,
            "history": self.history,
            "last_updated": datetime.now(timezone.utc).isoformat()
        }, indent=2, ensure_ascii=False))
    
    # ─── Queries (read from Scriba's network) ───
    
    def _build_cells(self) -> dict:
        """Build 72-cell view from Scriba's flat node list."""
        cells = {}
        for d in range(1, 5):
            for a in range(1, 4):
                for x in range(1, 4):
                    for p in ["+", "-"]:
                        cells[f"Σ_{d}{a}{x}{p}"] = []
        
        net = self._load_network()
        for node in net.get("nodes", []):
            sigma = node.get("sigma", "")
            if sigma in cells:
                cells[sigma].append(node)
        return cells
    
    def occupied_count(self) -> int:
        cells = self._build_cells()
        return sum(1 for v in cells.values() if v)
    
    def empty_cells(self) -> list:
        cells = self._build_cells()
        return [k for k, v in cells.items() if not v]
    
    def thin_cells(self, max_occupants: int = 1) -> list:
        cells = self._build_cells()
        return [k for k, v in cells.items() if 0 < len(v) <= max_occupants]
    
    def missing_complements(self) -> list:
        cells = self._build_cells()
        missing = []
        for d in range(1, 5):
            for a in range(1, 4):
                for x in range(1, 4):
                    plus = cells.get(f"Σ_{d}{a}{x}+", [])
                    minus = cells.get(f"Σ_{d}{a}{x}-", [])
                    if plus and not minus:
                        missing.append({"has": f"Σ_{d}{a}{x}+", "needs": f"Σ_{d}{a}{x}-"})
                    elif minus and not plus:
                        missing.append({"has": f"Σ_{d}{a}{x}-", "needs": f"Σ_{d}{a}{x}+"})
        return missing
    
    def dimension_coverage(self) -> dict:
        cells = self._build_cells()
        coverage = {1: 0, 2: 0, 3: 0, 4: 0}
        for key, v in cells.items():
            if v:
                d = int(key[2])
                coverage[d] += 1
        return coverage
    
    def summary(self) -> str:
        net = self._load_network()
        occ = self.occupied_count()
        empty = len(self.empty_cells())
        thin = len(self.thin_cells())
        compl = len(self.missing_complements())
        dim_cov = self.dimension_coverage()
        n_constraints = len(net.get("constraints", []))
        
        lines = [
            f"NETWORK STATE: {occ}/72 cells occupied ({occ/72*100:.1f}%)",
            f"Empty: {empty} | Thin (≤1 occupant): {thin} | Missing complements: {compl}",
            f"By dimension: D1={dim_cov[1]}/18 D2={dim_cov[2]}/18 D3={dim_cov[3]}/18 D4={dim_cov[4]}/18",
            f"Review queue: {len(self.review_queue)} | Reject log: {len(self.reject_log)}",
            f"Total mapped: {len(self.history)} concepts + {n_constraints} constraints",
        ]
        
        if self.missing_complements():
            lines.append(f"COMPLEMENT GAPS: {', '.join(m['needs'] for m in self.missing_complements()[:5])}...")
        if self.thin_cells():
            lines.append(f"THIN CLUSTERS: {', '.join(self.thin_cells()[:5])}...")
        
        return "\n".join(lines)
    
    # ─── Mutations (Director's own state only — Scriba writes nodes) ───
    
    def record_valid(self, concept: str, sigma: str, confidence: float, domain: str = ""):
        """Record a VALID mapping in history (Scriba already wrote to network)."""
        self.history.append({
            "concept": concept, "sigma": sigma, "status": "VALID",
            "confidence": confidence, "domain": domain
        })
        self._save_director_state()
    
    def record_constraint(self, concept: str, ref: str, confidence: float):
        """Record a constraint in history."""
        self.history.append({
            "concept": concept, "sigma": f"CONSTRAINT:{ref}", "status": "VALID",
            "confidence": confidence
        })
        self._save_director_state()
    
    def add_review(self, concept: str, reason: str, agents_data: dict):
        """Queue a REVIEW for human attention."""
        self.review_queue.append({
            "concept": concept, "reason": reason,
            "agents": agents_data,
            "added": datetime.now(timezone.utc).isoformat()
        })
        self._save_director_state()
    
    def add_reject(self, concept: str, attempt: int, reason: str):
        """Log a REJECT."""
        self.reject_log.append({
            "concept": concept, "attempt": attempt, "reason": reason,
            "added": datetime.now(timezone.utc).isoformat()
        })
        self._save_director_state()


# ─── Director Prompt ───

DIRECTOR_SYSTEM = """You are the Director of the EAR Triangulation Engine.

You have access to:
1. The complete EAR framework (Nano Kernel + Mapping Rules + Archetypes)
2. The current network state (72 cells, occupancy, gaps)
3. The history of all mapped concepts
4. The review queue and reject log

YOUR ROLE: Decide WHAT to map next. You do NOT map concepts yourself.

STRATEGIES (apply based on network state):
1. FILL GAPS: Target empty cells, especially in under-represented dimensions
2. STRENGTHEN THIN: Add concepts to cells with only 1 occupant  
3. COMPLETE COMPLEMENTS: If Σ₊ exists, find a concept for Σ₋
4. EXPLORE DOMAINS: Rotate through domains to ensure diversity
5. RETRY REJECTS: Rephrase rejected concepts for another attempt
6. CLEAR REVIEWS: Suggest how to resolve items in review queue

OUTPUT FORMAT (strict JSON):
{
  "action": "PROPOSE" or "RETRY" or "RESOLVE_REVIEW" or "REPORT",
  "concepts": [
    {
      "name": "<concept name>",
      "domain": "<domain>",
      "target_cell": "<Σ_DAXP or null if exploratory>",
      "rationale": "<why this concept, what gap does it fill>"
    }
  ],
  "strategy": "<which strategy from above>",
  "network_assessment": "<1-2 sentence assessment of current state>",
  "priority": "HIGH" or "MEDIUM" or "LOW"
}

RULES:
- Propose 3-5 concepts per batch for efficiency
- Mix strategies: don't only fill gaps, also strengthen existing clusters
- When retrying a reject, change the concept or add domain context — don't just repeat
- For reviews, suggest whether to accept majority or flag for human
- Be specific about WHY each concept was chosen
"""


# ─── Director Agent ───

class Director:
    """
    The Director proposes what to map, handles results, closes the loop.
    """
    
    def __init__(self, provider: LLMProvider, network: NetworkState,
                 kernel_doc: str = "", rules_doc: str = "", archetypes_doc: str = ""):
        self.provider = provider
        self.network = network
        self.kernel_doc = kernel_doc
        self.rules_doc = rules_doc
        self.archetypes_doc = archetypes_doc
    
    def propose_batch(self, domain_hint: str = "", count: int = 5) -> dict:
        """Ask Director to propose next concepts to map."""
        context = self._build_context()
        
        user_msg = f"""Current network state:
{self.network.summary()}

Recent history (last 10):
{json.dumps(self.network.history[-10:], indent=2) if self.network.history else "No history yet."}

Review queue:
{json.dumps(self.network.review_queue[:5], indent=2) if self.network.review_queue else "Empty."}

Reject log (recent):
{json.dumps(self.network.reject_log[-5:], indent=2) if self.network.reject_log else "Empty."}

{"Domain focus: " + domain_hint if domain_hint else "No domain preference — you choose."}

Propose {count} concepts for the next batch."""

        response = self.provider.complete(
            system=DIRECTOR_SYSTEM + "\n\nREFERENCE DOCUMENTS:\n" + context,
            user=user_msg,
            temperature=0.5  # slightly creative for diverse proposals
        )
        
        try:
            from core.tribunal import parse_agent_output
            return parse_agent_output(response.text)
        except Exception:
            return {"raw": response.text, "error": "Failed to parse Director output"}
    
    def handle_result(self, result: dict):
        """
        Process a mapping result from orchestrator v2.
        Routes: SCRIBA (3/3 → already inserted) or ARBITER (<3/3 → review).
        """
        concept = result.get("concept", "?")
        final = result.get("final", {})
        status = final.get("status", "REVIEW")  # VALID or REVIEW
        sigma = final.get("sigma", "?")
        confidence = final.get("confidence", 0)
        domain = result.get("domain", "")
        route = final.get("route", "ARBITER")
        
        if route == "SCRIBA" and status == "VALID":
            # Scriba already wrote to network — just record in Director's history
            if final.get("type") == "constraint":
                self.network.record_constraint(concept, final.get("constraint_ref", "?"), confidence)
                print(f"  ✓ {concept} → CONSTRAINT:{final.get('constraint_ref')} (conf: {confidence:.2f})")
            else:
                self.network.record_valid(concept, sigma, confidence, domain)
                print(f"  ✓ {concept} → {sigma} (conf: {confidence:.2f})")
        
        elif route == "ARBITER":
            # Arbiter analyzed — add to review queue
            arbiter = result.get("arbiter", {})
            assessment = arbiter.get("overall_assessment", {})
            pv = assessment.get("possible_validation", False)
            
            self.network.add_review(
                concept,
                f"Arbiter: pv={pv}, conf={assessment.get('confidence', 0):.2f}",
                {"synth_sigma": sigma, "arbiter": arbiter}
            )
            print(f"  ⚠ {concept} → REVIEW (Arbiter pv={pv})")
        
        else:
            # Fallback — shouldn't happen
            self.network.add_reject(concept, 1, f"Unknown route: {route}")
            print(f"  ✗ {concept} → UNKNOWN ROUTE")
    
    def _build_context(self) -> str:
        """Build abbreviated context from all docs (Director sees everything)."""
        parts = []
        if self.kernel_doc:
            # Just the matrix and constants sections — Director doesn't need full derivations
            parts.append("=== EAR KERNEL (summary) ===")
            parts.append("Matrix: 4D × 3A × 3X × 2P = 72 cells")
            parts.append("Attributes: Δ(distinction) ⇄(relation) ⟳(process)")
            parts.append("D: 1=linear 2=planar 3=volumetric 4=temporal")
            parts.append("X: 1=foundational 2=recursive 3=synthetic")
            parts.append("P: +=expansion -=contraction")
            parts.append("Constraints: T7(barriers) P6(inseparability) P1(minimum) P8(structural selection)")
        if self.archetypes_doc:
            parts.append("\n=== ARCHETYPES (known) ===")
            parts.append(self.archetypes_doc[:2000])  # First 2K chars has the populated cells
        return "\n".join(parts)


# ─── Autonomous Loop ───

class AutonomousLoop:
    """
    Runs the full Director → Engine → Director loop.
    Can run N cycles or until stopped.
    """
    
    def __init__(self, engine, director: Director, max_retries: int = 2):
        self.engine = engine
        self.director = director
        self.max_retries = max_retries
        self.cycle_count = 0
    
    def run_cycle(self, domain_hint: str = "", batch_size: int = 5) -> dict:
        """
        One full cycle:
        1. Director proposes concepts
        2. Engine maps each one
        3. Director handles results
        4. Return cycle summary
        """
        self.cycle_count += 1
        print(f"\n{'█'*60}")
        print(f"  CYCLE {self.cycle_count}")
        print(f"  Network: {self.director.network.occupied_count()}/72 cells")
        print(f"{'█'*60}")
        
        # 1. Director proposes
        print("\n[DIRECTOR] Proposing next batch...")
        proposal = self.director.propose_batch(domain_hint, batch_size)
        concepts = proposal.get("concepts", [])
        
        if not concepts:
            print("  Director proposed nothing. Cycle ends.")
            return {"cycle": self.cycle_count, "mapped": 0, "status": "EMPTY"}
        
        print(f"  Strategy: {proposal.get('strategy', '?')}")
        print(f"  Assessment: {proposal.get('network_assessment', '?')}")
        for c in concepts:
            target = c.get('target_cell', '?')
            print(f"    → {c['name']} [{c.get('domain', '')}] target={target}")
        
        # 2. Map each concept
        results = []
        for concept_info in concepts:
            name = concept_info["name"]
            domain = concept_info.get("domain", domain_hint)
            
            try:
                result = self.engine.map_concept(name, domain)
                results.append(result)
                
                # 3. Director handles result
                self.director.handle_result(result)
                
            except Exception as e:
                print(f"  ERROR mapping {name}: {e}")
                results.append({"concept": name, "error": str(e), "status": "FAILED"})
        
        # Summary
        valid = sum(1 for r in results if r.get("final", {}).get("status") == "VALID")
        review = sum(1 for r in results if r.get("final", {}).get("status") == "REVIEW")
        reject = sum(1 for r in results if r.get("final", {}).get("status") == "REJECT")
        
        summary = {
            "cycle": self.cycle_count,
            "proposed": len(concepts),
            "valid": valid,
            "review": review,
            "reject": reject,
            "network_size": self.director.network.occupied_count(),
            "strategy": proposal.get("strategy"),
        }
        
        print(f"\n  CYCLE {self.cycle_count} SUMMARY: {valid}✓ {review}⚠ {reject}✗")
        print(f"  Network now: {self.director.network.occupied_count()}/72 cells")
        
        return summary
    
    def run(self, cycles: int = 5, domain_hint: str = ""):
        """Run multiple cycles."""
        summaries = []
        for i in range(cycles):
            summary = self.run_cycle(domain_hint)
            summaries.append(summary)
            
            if summary.get("status") == "EMPTY":
                print("\nDirector has nothing to propose. Stopping.")
                break
        
        # Final report
        print(f"\n{'═'*60}")
        print(f"  AUTONOMOUS RUN COMPLETE: {len(summaries)} cycles")
        total_valid = sum(s.get("valid", 0) for s in summaries)
        total_review = sum(s.get("review", 0) for s in summaries)
        total_reject = sum(s.get("reject", 0) for s in summaries)
        print(f"  Total: {total_valid}✓ {total_review}⚠ {total_reject}✗")
        print(f"  Network: {self.director.network.occupied_count()}/72 cells")
        print(f"{'═'*60}")
        
        return summaries
