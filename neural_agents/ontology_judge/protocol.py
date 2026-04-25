#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ontology Judge Protocol — EAR Validator

RUOLO:
- Ha accesso a TUTTI i documenti AILA (ontologia completa)
- Valida proposte di mapping ontologicamente
- Emette giudizi: VALID / INVALID / UNCERTAIN
- Spiega reasoning basato su principi EAR

COMUNICAZIONE:
- INPUT: Mapping proposals da Mapper (Σ coordinates proposte)
- OUTPUT: Judgments per Mapper (validazione ontologica)
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add shared to path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from file_sync import FileSync


class OntologyJudgeProtocol:
    """
    Ontology Judge — EAR Validation Authority

    Responsibilities:
    1. Reads mapping proposals from Mapper
    2. Validates against EAR ontology (AILA docs)
    3. Checks coherence with Matrix 72
    4. Emits judgment (VALID/INVALID/UNCERTAIN)
    5. Provides reasoning based on principles
    """

    def __init__(self, context_path: Optional[str] = None):
        """
        Initialize Ontology Judge.

        Args:
            context_path: Path to AILA context docs (Ray will populate)
        """
        self.context_path = context_path or Path(__file__).parent / "context"
        self.sync = FileSync()
        self.judgments_history: List[Dict[str, Any]] = []

        # Load AILA context
        self.ontology_context = self._load_context()

    def _load_context(self) -> Dict[str, str]:
        """
        Load AILA ontology documents.

        Returns:
            Dictionary of document_name -> content
        """
        context = {}

        context_dir = Path(self.context_path)

        if not context_dir.exists():
            print(f"[INFO] Context directory not found: {context_dir}")
            print("[INFO] Will use placeholder ontology")
            return self._placeholder_ontology()

        # Load all .md files in context
        for doc in context_dir.glob("*.md"):
            context[doc.stem] = doc.read_text(encoding='utf-8')
            print(f"[OK] Loaded {doc.name}")

        if not context:
            print("[INFO] No context docs found, using placeholder")
            return self._placeholder_ontology()

        return context

    def _placeholder_ontology(self) -> Dict[str, str]:
        """Placeholder ontology (until Ray adds real AILA docs)."""
        return {
            "EAR_PRINCIPLES": """
# EAR Ontology Principles (Placeholder)

## Matrix 72 Structure

4 dimensions × 3 attributes × 3 complexity × 2 polarity = 72 coordinates

## Validation Rules

1. **Distinction (Δ)**: Clear identity, non-reducible
2. **Relation (⇄)**: Structural connections
3. **Process (⟳)**: Temporal dynamics

## Common Invalid Mappings

- Confusing scale with dimension
- Misattributing polarity (+ vs -)
- Ignoring complexity level
"""
        }

    def validate_mapping(self, mapping: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate mapping proposal against EAR ontology.

        Args:
            mapping: Mapping proposal from Mapper

        Returns:
            Validation result dictionary
        """
        proposed_sigma = mapping.get('sigma', '')
        phenomenon = mapping.get('phenomenon', '')
        reasoning = mapping.get('reasoning', '')

        print(f"\n{'='*60}")
        print(f"ONTOLOGY JUDGE: Validating mapping")
        print(f"{'='*60}")
        print(f"Phenomenon: {phenomenon}")
        print(f"Proposed Σ: {proposed_sigma}")
        print(f"Reasoning: {reasoning}")
        print(f"{'='*60}\n")

        # Validation logic (placeholder — Ray will refine with real ontology)
        validation = {
            'phenomenon': phenomenon,
            'proposed_sigma': proposed_sigma,
            'status': 'UNCERTAIN',  # VALID / INVALID / UNCERTAIN
            'ontological_reasoning': '',
            'concerns': [],
            'supports': [],
            'timestamp': datetime.now().isoformat()
        }

        # SPECIAL CASE: Threshold / Boundary Conditions
        if 'THRESHOLD' in proposed_sigma or 'T7' in proposed_sigma or 'T8' in proposed_sigma:
            validation['status'] = 'VALID'
            validation['ontological_reasoning'] = (
                f"{proposed_sigma} is a threshold/boundary condition, not a node. "
                "Valid ontological status per P6/T7 — represents structural limit of Tesseract."
            )
            validation['supports'].append({
                'type': 'threshold',
                'description': 'Threshold principles define Tesseract structure itself'
            })
            return validation

        # Parse Sigma (basic validation for normal nodes)
        if not proposed_sigma or not proposed_sigma.startswith('Σ'):
            validation['status'] = 'INVALID'
            validation['concerns'].append({
                'type': 'malformed_sigma',
                'description': f"Sigma '{proposed_sigma}' is malformed"
            })
            return validation

        # Check if reasoning mentions key EAR concepts
        ear_keywords = ['Δ', '⇄', '⟳', 'distinction', 'relation', 'process']
        if any(kw in reasoning for kw in ear_keywords):
            validation['supports'].append({
                'type': 'ear_aware',
                'description': 'Reasoning uses EAR concepts'
            })

        # Placeholder logic (to be refined with real AILA docs)
        if len(validation['concerns']) == 0 and len(validation['supports']) > 0:
            validation['status'] = 'VALID'
            validation['ontological_reasoning'] = "Mapping coherent with EAR principles (placeholder validation)"
        elif len(validation['concerns']) > 0:
            validation['status'] = 'INVALID'
            validation['ontological_reasoning'] = "Issues detected (placeholder validation)"
        else:
            validation['status'] = 'UNCERTAIN'
            validation['ontological_reasoning'] = "Need more information to validate (placeholder)"

        return validation

    def emit_judgment(self, validation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Emit judgment based on validation.

        Args:
            validation: Validation result

        Returns:
            Judgment dictionary
        """
        judgment = {
            'judgment': validation['status'],  # VALID / INVALID / UNCERTAIN
            'phenomenon': validation['phenomenon'],
            'proposed_sigma': validation['proposed_sigma'],
            'reasoning': validation['ontological_reasoning'],
            'concerns': validation['concerns'],
            'supports': validation['supports'],
            'timestamp': datetime.now().isoformat()
        }

        # Store in history
        self.judgments_history.append(judgment)

        # Write to shared
        self.sync.write_judgment(judgment)

        print(f"\n{'='*60}")
        print(f"JUDGMENT: {judgment['judgment']}")
        print(f"{'='*60}")
        print(f"Reasoning: {judgment['reasoning']}")

        if judgment['concerns']:
            print(f"\nConcerns:")
            for c in judgment['concerns']:
                print(f"  • {c['description']}")

        if judgment['supports']:
            print(f"\nSupports:")
            for s in judgment['supports']:
                print(f"  • {s['description']}")

        print(f"{'='*60}\n")

        return judgment

    def judge_mapping(self, mapping: Dict[str, Any]) -> Dict[str, Any]:
        """
        Complete judgment pipeline: validate → emit judgment.

        Args:
            mapping: Mapping proposal from Mapper

        Returns:
            Judgment dictionary
        """
        validation = self.validate_mapping(mapping)
        judgment = self.emit_judgment(validation)
        return judgment

    def wait_and_judge(self, timeout: int = 300) -> Dict[str, Any]:
        """
        Wait for mapping proposal and judge.

        Args:
            timeout: Maximum wait time

        Returns:
            Judgment dictionary
        """
        print("[WAITING] Ontology Judge waiting for mapping proposal...")

        try:
            mapping = self.sync.wait_for_mapping(timeout=timeout)
            return self.judge_mapping(mapping)

        except TimeoutError:
            print(f"[TIMEOUT] No mapping after {timeout}s")
            return None

    def run_loop(self, max_iterations: Optional[int] = None):
        """
        Run judge loop (wait → validate → judge → repeat).

        Args:
            max_iterations: Maximum iterations (None = infinite)
        """
        iteration = 0

        print(f"\n{'='*60}")
        print("ONTOLOGY JUDGE ONLINE — Starting validation loop")
        print(f"{'='*60}\n")

        # Show loaded context
        print(f"Loaded {len(self.ontology_context)} ontology documents:")
        for doc_name in self.ontology_context.keys():
            print(f"  • {doc_name}")
        print()

        try:
            while True:
                if max_iterations and iteration >= max_iterations:
                    print(f"\n[DONE] Reached max iterations ({max_iterations})")
                    break

                iteration += 1

                print(f"\n--- Iteration {iteration} ---\n")

                judgment = self.wait_and_judge(timeout=60)

                if judgment is None:
                    print("No mapping received, waiting...")
                    continue

                print(f"\n--- Iteration {iteration} complete ---\n")

        except KeyboardInterrupt:
            print("\n\n[STOPPED] Judge stopped by user")

        except Exception as e:
            print(f"\n[ERROR] Judge error: {e}")
            import traceback
            print(traceback.format_exc())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Ontology Judge — EAR Validator")
    parser.add_argument('--test', action='store_true', help="Run test with dummy mapping")
    parser.add_argument('--loop', action='store_true', help="Run judge loop")
    parser.add_argument('--iterations', type=int, default=None, help="Max iterations")

    args = parser.parse_args()

    judge = OntologyJudgeProtocol()

    if args.test:
        # Test with dummy mapping
        test_mapping = {
            'phenomenon': 'burst_criticality',
            'sigma': 'Σ₄₂₂₊',
            'reasoning': 'Criticality shows Δ (distinction from noise) and ⟳ (temporal avalanches)',
            'timestamp': datetime.now().isoformat()
        }

        print("Testing Ontology Judge with dummy mapping...")
        judge.judge_mapping(test_mapping)

    elif args.loop:
        judge.run_loop(max_iterations=args.iterations)

    else:
        print("Usage:")
        print("  python protocol.py --test          # Test with dummy mapping")
        print("  python protocol.py --loop          # Run judge loop")
