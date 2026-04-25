#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Map Fundamental Concepts to Tesseract

Maps physics and mathematics pillars onto Matrix 72
"""

import sys
import json
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

from concept_synthesizer.protocol import ConceptSynthesizerProtocol
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol


def map_concept(concept_name: str) -> dict:
    """Map single concept to Tesseract."""

    synthesizer = ConceptSynthesizerProtocol()
    mapper = MapperProtocol()
    judge = OntologyJudgeProtocol()

    print(f"\n{'='*80}")
    print(f"MAPPING: {concept_name}")
    print('='*80)

    # Synthesize
    synthesis = synthesizer.synthesize_concept(concept_name)

    # Analyze
    analysis = mapper.analyze_synthesis(synthesis)

    # Propose Σ
    mapping = mapper.propose_mapping(analysis)

    # Validate
    judgment = judge.judge_mapping(mapping)

    result = {
        'concept': concept_name,
        'sigma': mapping.get('sigma', None),
        'reasoning': mapping.get('reasoning', ''),
        'judgment': judgment.get('judgment', None),
        'structures': synthesis.get('synthesis', {}).get('ontological_structures', []),
        'timestamp': datetime.now().isoformat()
    }

    status = '✅' if result['judgment'] == 'VALID' else '❌'
    print(f"\n{status} {concept_name} → {result['sigma']} [{result['judgment']}]")

    return result


def main():
    """Map fundamental concepts."""

    concepts = [
        # Mathematics
        "Pythagorean Theorem",
        "Fundamental Theorem of Calculus",

        # Physics
        "Noether's Theorem",
        "Newton's Laws",
        "Heisenberg Uncertainty Principle",
    ]

    results = []

    for concept in concepts:
        try:
            result = map_concept(concept)
            results.append(result)
        except Exception as e:
            print(f"\n❌ Error mapping {concept}: {e}")
            results.append({
                'concept': concept,
                'error': str(e)
            })

    # Save results
    output_file = Path("tesseract_mappings.json")
    output_file.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    # Summary
    print("\n" + "="*80)
    print("MAPPING SUMMARY")
    print("="*80 + "\n")

    for r in results:
        if 'error' in r:
            print(f"❌ {r['concept']:40s} ERROR: {r['error']}")
        else:
            status = '✅' if r['judgment'] == 'VALID' else '❌'
            sigma = r['sigma'] or '?'
            print(f"{status} {r['concept']:40s} → {sigma:10s}")

    print(f"\n✅ Results saved to {output_file}")
    print(f"✅ Mapped {len([r for r in results if 'error' not in r])} concepts")


if __name__ == "__main__":
    main()
