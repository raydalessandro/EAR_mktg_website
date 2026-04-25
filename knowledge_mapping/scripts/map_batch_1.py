#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Map Batch 1 — Mathematics Fundamentals (10 concepts)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
from pathlib import Path
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol

def map_batch(batch_file: str):
    """Map all concepts in batch file."""

    # Load batch
    batch_path = Path(batch_file)
    concepts = json.loads(batch_path.read_text(encoding='utf-8'))

    print(f"\n{'='*70}")
    print(f"BATCH MAPPING: {batch_path.name}")
    print(f"{'='*70}")
    print(f"Concepts: {len(concepts)}\n")

    # Initialize agents
    mapper = MapperProtocol()
    judge = OntologyJudgeProtocol()

    results = []

    for i, entry in enumerate(concepts, 1):
        concept_name = entry['concept_name']
        synthesis = entry['synthesis']

        print(f"\n[{i}/{len(concepts)}] Mapping: {concept_name}")
        print("-"*70)

        # Build text from synthesis
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

        result = {
            'concept': concept_name,
            'coordinate': coord_str,
            'category': proposal.category.value,
            'status': status,
            'confidence': confidence
        }

        results.append(result)

        print(f"→ {coord_str:15} [{status}] (conf: {confidence:.2f})")

    # Summary
    print(f"\n{'='*70}")
    print("BATCH SUMMARY")
    print(f"{'='*70}")
    print(f"{'Concept':<45} {'Σ':<15} {'Status':<8} {'Conf':<5}")
    print("-"*70)

    for r in results:
        print(f"{r['concept']:<45} {r['coordinate']:<15} {r['status']:<8} {r['confidence']:<5.2f}")

    print("="*70)

    # Cluster analysis
    by_dimension = {}
    by_attribute = {}

    for r in results:
        coord = r['coordinate']
        if 'Σ' in coord and len(coord) >= 3:
            d = coord[1]  # dimension
            a = coord[2]  # attribute
            by_dimension[d] = by_dimension.get(d, 0) + 1
            by_attribute[a] = by_attribute.get(a, 0) + 1

    print(f"\nCLUSTER ANALYSIS:")
    print(f"  By Dimension:")
    for dim in sorted(by_dimension.keys()):
        count = by_dimension[dim]
        print(f"    D={dim}: {count} concepts")

    print(f"  By Attribute:")
    attr_names = {'1': 'Δ distinction', '2': '⇄ relation', '3': '⟳ process'}
    for attr in sorted(by_attribute.keys()):
        count = by_attribute[attr]
        name = attr_names.get(attr, '?')
        print(f"    A={attr} ({name}): {count} concepts")

    # Save results
    output_file = batch_path.parent / f"{batch_path.stem}_results.json"
    output_file.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\n✅ Results saved to: {output_file.name}")

    return results

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        batch_file = sys.argv[1]
    else:
        batch_file = "batch_1_mathematics.json"

    map_batch(batch_file)
