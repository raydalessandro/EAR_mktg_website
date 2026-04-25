#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Full 17 Concepts — Validated Knowledge Base
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from concept_synthesizer.protocol import ConceptSynthesizerProtocol
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol

# Expected results for 17 validated concepts
EXPECTED = {
    # Original 12
    'pythagorean theorem':              ('node', 'Σ111₊'),
    'fundamental theorem of calculus':  ('node', 'Σ121₊'),
    'noether\'s theorem':               ('node', 'Σ423₊'),
    'maxwell\'s equations':             ('node', 'Σ431₊'),
    'schrödinger equation':             ('node', 'Σ431₊'),
    'second law of thermodynamics':     ('node', 'Σ431₋'),
    'heisenberg uncertainty principle': ('constraint', 'T7.C7.4'),
    'newton\'s laws':                   ('node', 'Σ321₊'),
    'special relativity':               ('node', 'Σ422₊'),
    'general relativity':               ('node', 'Σ423₊'),
    'conservation of energy':           ('node', 'Σ421₊'),
    'gödel\'s incompleteness theorems': ('constraint', 'P6 + P1'),

    # New 5 (validated by Opus)
    'euler\'s identity':                ('node', 'Σ121₊'),
    'hooke\'s law':                     ('node', 'Σ221₊'),
    'pauli exclusion principle':        ('node', 'Σ411₊'),
    'shannon\'s theorem':               ('node', 'Σ421₊'),
    'turing halting problem':           ('node', 'Σ112₊'),
}

def normalize_sigma(s):
    """Normalize Σ notation."""
    sub_map = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
    return s.translate(sub_map)

def test_concept(synth, mapper, judge, concept_name, expected):
    """Test single concept."""
    # Synthesize
    result = synth.synthesize_concept(concept_name)
    if result.get('status') != 'success':
        return None

    synthesis = result.get('synthesis', {})

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

    # Check
    exp_cat, exp_coord = expected
    actual_str = str(proposal.coordinate)
    actual_norm = normalize_sigma(actual_str)
    exp_norm = normalize_sigma(exp_coord)

    from mapper.protocol import ConstraintRef

    if exp_cat == 'constraint':
        match = isinstance(proposal.coordinate, ConstraintRef) and \
                any(exp_coord in r or r in exp_coord
                    for r in proposal.coordinate.references)
    else:
        match = actual_norm == exp_norm

    status = '✅' if match else '❌'

    return {
        'concept': concept_name,
        'expected': exp_coord,
        'actual': actual_str,
        'match': match,
        'status': status,
        'confidence': proposal.confidence
    }

def main():
    print("Initializing agents...")
    synth = ConceptSynthesizerProtocol()
    mapper = MapperProtocol()
    judge = OntologyJudgeProtocol()

    print(f"\n{'='*70}")
    print(f"  FULL TEST: 17 Validated Concepts")
    print(f"{'='*70}\n")

    results = []
    for concept, expected in EXPECTED.items():
        print(f"Testing: {concept:45} ", end='', flush=True)
        result = test_concept(synth, mapper, judge, concept, expected)
        if result:
            results.append(result)
            print(f"{result['status']} {result['actual']:20}")
        else:
            print("❌ FAILED")

    # Summary
    correct = sum(1 for r in results if r['match'])
    total = len(results)
    accuracy = correct / total * 100 if total > 0 else 0

    print(f"\n{'='*70}")
    print(f"  RESULTS: {correct}/{total} ({accuracy:.0f}%)")
    print(f"{'='*70}\n")

    # Failures
    failures = [r for r in results if not r['match']]
    if failures:
        print("FAILURES:")
        for r in failures:
            print(f"  ❌ {r['concept']}")
            print(f"     Expected: {r['expected']}")
            print(f"     Got:      {r['actual']}")
    else:
        print("✅ ALL TESTS PASSED!")

    # Detailed table
    print(f"\n{'='*90}")
    print("DETAILED RESULTS")
    print(f"{'='*90}")
    print(f"{'Concept':<45} {'Expected':<15} {'Actual':<15} {'Match':<6} {'Conf':<5}")
    print("-"*90)
    for r in results:
        match_str = '✅' if r['match'] else '❌'
        print(f"{r['concept']:<45} {r['expected']:<15} {r['actual']:<15} "
              f"{match_str:<6} {r['confidence']:<5.2f}")
    print("="*90)

if __name__ == "__main__":
    main()
