#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test v2 Integration — Full pipeline with Opus mapper
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from concept_synthesizer.protocol import ConceptSynthesizerProtocol
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol

def test_concept_v2(synthesizer, mapper, judge, concept_name):
    """Test single concept through v2 pipeline."""
    print(f"\n{'='*70}")
    print(f"TESTING: {concept_name}")
    print(f"{'='*70}\n")

    # Synthesize
    synthesis_result = synthesizer.synthesize_concept(concept_name)

    if synthesis_result.get('status') != 'success':
        print(f"[ERROR] Synthesis failed: {synthesis_result.get('error')}")
        return None

    synthesis = synthesis_result.get('synthesis', {})

    # Build text description from synthesis
    text = synthesis.get('formal_statement', '')
    structures_text = ' '.join([
        f"{s.get('evidence', '')}"
        for s in synthesis.get('ontological_structures', [])
    ])
    combined_text = f"{text} {structures_text}"

    # Map with v2
    proposal = mapper.propose_mapping(
        concept_name=concept_name,
        text=combined_text,
        synthesis=synthesis
    )

    # Judge
    judgment_dict = {
        'concept_name': concept_name,
        'sigma': str(proposal.coordinate),
        'reasoning': proposal.reasoning,
        'category': proposal.category.value,
    }
    judgment = judge.judge_mapping(judgment_dict)

    # Summary
    coord_str = str(proposal.coordinate)
    status = judgment.get('judgment', '???')
    confidence = proposal.confidence

    print(f"\n[RESULT] {concept_name:45} → {coord_str:20} [{status}] (conf: {confidence:.2f})\n")

    return {
        'concept': concept_name,
        'coordinate': coord_str,
        'category': proposal.category.value,
        'status': status,
        'confidence': confidence,
        'proposal': proposal,
        'judgment': judgment
    }

def main():
    print("Initializing agents with Opus v2 mapper...")

    synthesizer = ConceptSynthesizerProtocol()
    mapper = MapperProtocol()
    judge = OntologyJudgeProtocol()

    # Test critical cases
    test_concepts = [
        # Foundational theorems
        "Pythagorean Theorem",
        "Fundamental Theorem of Calculus",
        "Noether's Theorem",

        # Constraints (should be T/P/A, not Σ)
        "Heisenberg Uncertainty Principle",
        "Gödel's Incompleteness Theorems",

        # Laws with different dimensions
        "Newton's Laws",
        "Maxwell's Equations",
        "Conservation of Energy",

        # Modern physics
        "Special Relativity",
        "General Relativity",
        "Schrödinger Equation",
        "Second Law of Thermodynamics",
    ]

    results = []
    for concept in test_concepts:
        result = test_concept_v2(synthesizer, mapper, judge, concept)
        if result:
            results.append(result)

    # Summary table
    print("\n" + "="*90)
    print("V2 INTEGRATION TEST SUMMARY")
    print("="*90)
    print(f"{'Concept':<45} {'Category':<12} {'Coordinate':<20} {'Status':<8} {'Conf':<5}")
    print("-"*90)
    for r in results:
        print(f"{r['concept']:<45} {r['category']:<12} {r['coordinate']:<20} "
              f"{r['status']:<8} {r['confidence']:<5.2f}")
    print("="*90)

    # Count successes
    valid_count = sum(1 for r in results if r['status'] == 'VALID')
    print(f"\nVALID: {valid_count}/{len(results)}")

if __name__ == "__main__":
    main()
