#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test refined ontological mappings
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from concept_synthesizer.protocol import ConceptSynthesizerProtocol
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol

def test_concept(synthesizer, mapper, judge, concept_name):
    """Test single concept through pipeline."""
    print(f"\n{'='*60}")
    print(f"TESTING: {concept_name}")
    print(f"{'='*60}\n")

    # Synthesize
    synthesis_result = synthesizer.synthesize_concept(concept_name)

    # Analyze
    analysis = mapper.analyze_synthesis(synthesis_result)

    # Propose mapping
    mapping = mapper.propose_mapping(analysis)

    # Judge
    judgment = judge.judge_mapping(mapping)

    # Summary
    sigma = mapping.get('sigma', '???')
    status = judgment.get('judgment', '???')

    print(f"\n[RESULT] {concept_name:40} → {sigma:15} [{status}]\n")

    return {
        'concept': concept_name,
        'sigma': sigma,
        'status': status,
        'mapping': mapping,
        'judgment': judgment
    }

def main():
    print("Initializing agents with refined ontological logic...")

    synthesizer = ConceptSynthesizerProtocol()
    mapper = MapperProtocol()
    judge = OntologyJudgeProtocol()

    # Test critical cases
    test_concepts = [
        # Relation-dominant (should be X=2)
        "Fundamental Theorem of Calculus",
        "Noether's Theorem",

        # Dimension variations
        "Newton's Laws",  # Should be D=3 (volumetric)
        "Special Relativity",  # Should be D=4, X=2 (recursive)
        "General Relativity",  # Should be D=4, X=3 (synthetic)

        # Threshold case
        "Heisenberg Uncertainty Principle"  # Should be T7.4 threshold
    ]

    results = []
    for concept in test_concepts:
        result = test_concept(synthesizer, mapper, judge, concept)
        results.append(result)

    # Summary table
    print("\n" + "="*60)
    print("REFINED MAPPINGS SUMMARY")
    print("="*60)
    for r in results:
        print(f"{r['concept']:40} → {r['sigma']:20} [{r['status']}]")
    print("="*60)

if __name__ == "__main__":
    main()
