#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick batch mapping"""

import sys
sys.stdout.reconfigure(encoding='utf-8')

from concept_synthesizer.protocol import ConceptSynthesizerProtocol
from mapper.protocol import MapperProtocol
from ontology_judge.protocol import OntologyJudgeProtocol

# Initialize once
print("Initializing agents...")
synthesizer = ConceptSynthesizerProtocol()
mapper = MapperProtocol()
judge = OntologyJudgeProtocol()

concepts = [
    # Mathematics - Foundational
    "Pythagorean Theorem",
    "Fundamental Theorem of Calculus",
    "Gödel's Incompleteness Theorems",

    # Physics - Symmetry & Conservation
    "Noether's Theorem",
    "Conservation of Energy",

    # Physics - Classical
    "Newton's Laws",
    "Maxwell's Equations",
    "Second Law of Thermodynamics",

    # Physics - Modern
    "Special Relativity",
    "General Relativity",
    "Schrödinger Equation",
    "Heisenberg Uncertainty Principle"
]

results = []

for concept in concepts:
    print(f"\n{'='*60}")
    print(f"MAPPING: {concept}")
    print('='*60)

    s = synthesizer.synthesize_concept(concept)
    a = mapper.analyze_synthesis(s)
    m = mapper.propose_mapping(a)
    j = judge.judge_mapping(m)

    sigma = m.get('sigma', '?')
    judgment = j.get('judgment', '?')

    results.append((concept, sigma, judgment))

    status = '[OK]' if judgment == 'VALID' else '[INVALID]'
    print(f"{status} {concept} → {sigma}")

print("\n" + "="*60)
print("RESULTS")
print("="*60)

for concept, sigma, judgment in results:
    print(f"{concept:30s} → {sigma:10s} [{judgment}]")
