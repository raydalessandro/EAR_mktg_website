#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Euler's Identity — Validation of Claude-synthesized concept
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from concept_synthesizer.protocol import ConceptSynthesizerProtocol
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol

def test_euler():
    """Test Euler's Identity through full pipeline."""

    synthesizer = ConceptSynthesizerProtocol()
    mapper = MapperProtocol()
    judge = OntologyJudgeProtocol()

    concept_name = "Euler's Identity"

    print(f"\n{'='*70}")
    print(f"TESTING CLAUDE-SYNTHESIZED CONCEPT: {concept_name}")
    print(f"{'='*70}\n")

    # Synthesize
    result = synthesizer.synthesize_concept(concept_name)

    if result.get('status') != 'success':
        print(f"[ERROR] Synthesis failed")
        return

    synthesis = result.get('synthesis', {})

    # Show synthesis
    print(f"\nSYNTHESIS:")
    print(f"  Type: {synthesis.get('concept_type')}")
    print(f"  Statement: {synthesis.get('formal_statement')}")
    print(f"  Dominant: {synthesis.get('attribute_dominant')}")
    print(f"  Dimension: {synthesis.get('dimension_hints')[:60]}...")
    print(f"  Complexity: {synthesis.get('complexity')}")
    print(f"  Elimination test: {synthesis.get('elimination_test')[:80]}...")

    # Build text
    text = synthesis.get('formal_statement', '')
    elim = synthesis.get('elimination_test', '')
    text_full = f"{text}. {elim}"

    # Map
    proposal = mapper.propose_mapping(concept_name, text_full, synthesis)

    # Judge
    judgment_dict = {
        'concept_name': concept_name,
        'sigma': str(proposal.coordinate),
        'reasoning': proposal.reasoning,
        'category': proposal.category.value,
    }
    judgment = judge.judge_mapping(judgment_dict)

    # Result
    coord_str = str(proposal.coordinate)
    status = judgment.get('judgment', '???')
    confidence = proposal.confidence

    print(f"\n{'='*70}")
    print(f"FINAL RESULT")
    print(f"{'='*70}")
    print(f"Concept: {concept_name}")
    print(f"Category: {proposal.category.value}")
    print(f"Coordinate: {coord_str}")
    print(f"Confidence: {confidence:.2f}")
    print(f"Judge Status: {status}")
    print(f"{'='*70}\n")

    # Validation
    print("VALIDATION:")
    expected = "Σ121₊"  # Expected: D=1 foundational, A=2 relation, X=1 foundational

    if coord_str == expected or coord_str == "Σ₁₂₁₊":
        print(f"  ✅ Coordinate matches expected: {expected}")
    else:
        print(f"  ⚠️  Coordinate: {coord_str}, Expected: {expected}")

    if proposal.category.value == 'node':
        print(f"  ✅ Category correct: node (not constraint)")
    else:
        print(f"  ❌ Category incorrect: {proposal.category.value}")

    # Show reasoning
    print(f"\nREASONING:")
    for key, reason in proposal.reasoning.items():
        print(f"  {key}: {reason[:80]}{'...' if len(reason) > 80 else ''}")

if __name__ == "__main__":
    test_euler()
