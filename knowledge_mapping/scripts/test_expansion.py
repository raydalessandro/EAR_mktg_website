#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Expansion — Nuovi concetti per validare sistema
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from concept_synthesizer.protocol import ConceptSynthesizerProtocol
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol

def test_concept(synthesizer, mapper, judge, concept_name):
    """Test single concept."""
    print(f"\n{'='*70}")
    print(f"TESTING: {concept_name}")
    print(f"{'='*70}\n")

    # Synthesize
    result = synthesizer.synthesize_concept(concept_name)

    if result.get('status') != 'success':
        print(f"[ERROR] Synthesis failed")
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
        'reasoning': proposal.reasoning
    }

def main():
    print("Initializing agents...")

    synthesizer = ConceptSynthesizerProtocol()
    mapper = MapperProtocol()
    judge = OntologyJudgeProtocol()

    # Nuovi concetti da testare — mix di dimensioni e attributi
    test_concepts = [
        # Matematica pura (dovrebbero essere D=1)
        "Euler's Identity",
        "Cantor's Diagonal Argument",

        # Fisica classica (D=2 o D=3)
        "Hooke's Law",
        "Archimedes' Principle",

        # Quantum (D=4, vari attributi)
        "Pauli Exclusion Principle",
        "Wave-Particle Duality",

        # Relativity/Cosmology (D=4)
        "Equivalence Principle",
        "Hubble's Law",

        # Thermodynamics (D=4, process)
        "Carnot Cycle",
        "Third Law of Thermodynamics",

        # Information/Computation (potrebbero essere constraint)
        "Shannon's Theorem",
        "Turing Halting Problem",
    ]

    results = []
    for concept in test_concepts:
        result = test_concept(synthesizer, mapper, judge, concept)
        if result:
            results.append(result)

    # Summary
    print("\n" + "="*90)
    print("EXPANSION TEST SUMMARY")
    print("="*90)
    print(f"{'Concept':<45} {'Category':<12} {'Coordinate':<20} {'Status':<8} {'Conf':<5}")
    print("-"*90)
    for r in results:
        print(f"{r['concept']:<45} {r['category']:<12} {r['coordinate']:<20} "
              f"{r['status']:<8} {r['confidence']:<5.2f}")
    print("="*90)

    # Analisi per categoria
    by_category = {}
    by_dimension = {}

    for r in results:
        cat = r['category']
        by_category[cat] = by_category.get(cat, 0) + 1

        coord = r['coordinate']
        if 'Σ' in coord and len(coord) >= 2:
            dim = coord[1]  # Extract dimension
            by_dimension[dim] = by_dimension.get(dim, 0) + 1

    print(f"\nBY CATEGORY:")
    for cat, count in sorted(by_category.items()):
        print(f"  {cat}: {count}")

    print(f"\nBY DIMENSION:")
    for dim, count in sorted(by_dimension.items()):
        print(f"  D={dim}: {count}")

    # Report inefficienze potenziali
    print(f"\nPOTENTIAL ISSUES:")
    uncertain = [r for r in results if r['status'] == 'UNCERTAIN']
    if uncertain:
        print(f"  {len(uncertain)} concepts marked UNCERTAIN by Judge:")
        for r in uncertain:
            print(f"    - {r['concept']}")
    else:
        print("  None — all validated!")

    unknown = [r for r in results if 'unknown' in str(r['coordinate']).lower()]
    if unknown:
        print(f"  {len(unknown)} concepts fell back to 'unknown':")
        for r in unknown:
            print(f"    - {r['concept']}")

if __name__ == "__main__":
    main()
