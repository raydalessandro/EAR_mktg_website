#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Network Diagnostics — Analisi topologica della rete concettuale mappata
Genera report dettagliato su struttura, clustering, pattern emergenti
"""

import json
import sys
from collections import defaultdict, Counter
from pathlib import Path

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def load_batch(filepath):
    """Load batch JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def parse_sigma(sigma_str):
    """Parse Σ coordinate string → (D, A, X, P)"""
    # Example: "Σ321₊" → (3, 2, 1, '+')
    if not sigma_str.startswith('Σ'):
        return None

    coords = sigma_str[1:]  # Remove Σ
    if len(coords) < 4:
        return None

    D = int(coords[0])
    A = int(coords[1])
    X = int(coords[2])
    P = coords[3] if coords[3] in ['+', '-', '₊', '₋'] else None

    # Normalize polarity
    if P == '₊':
        P = '+'
    elif P == '₋':
        P = '-'

    return (D, A, X, P)

def analyze_network():
    """Main diagnostic function"""

    print("=" * 80)
    print("NEURAL MAPPING NETWORK — DIAGNOSTIC REPORT")
    print("=" * 80)
    print()

    # Load all batches
    batches = {
        'mathematics': load_batch('batch_1_mathematics.json'),
        'classical_physics': load_batch('batch_2_classical_physics.json'),
        'cs_logic': load_batch('batch_3_cs_logic.json'),
        'thermodynamics': load_batch('batch_4_thermodynamics.json'),
        'quantum': load_batch('batch_5_quantum.json')
    }

    all_concepts = []
    for domain, concepts in batches.items():
        for c in concepts:
            c['domain'] = domain
            all_concepts.append(c)

    total = len(all_concepts)

    print(f"📊 NETWORK SIZE: {total} concepts")
    print(f"   - Mathematics: {len(batches['mathematics'])} concepts")
    print(f"   - Classical Physics: {len(batches['classical_physics'])} concepts")
    print()

    # ========================================================================
    # §1: ATTRIBUTE DOMINANCE ANALYSIS
    # ========================================================================

    print("=" * 80)
    print("§1: ATTRIBUTE DOMINANCE ANALYSIS")
    print("=" * 80)
    print()

    attr_by_domain = defaultdict(lambda: defaultdict(int))

    for c in all_concepts:
        domain = c['domain']
        attr_dom = c['synthesis']['attribute_dominant']

        # Map to numeric
        attr_map = {'Δ': 1, '⇄': 2, '⟳': 3}
        attr_num = attr_map.get(attr_dom, 0)

        if attr_num > 0:
            attr_by_domain[domain][attr_num] += 1

    # Display
    for domain in ['mathematics', 'classical_physics', 'cs_logic', 'thermodynamics', 'quantum']:
        counts = attr_by_domain[domain]
        total_domain = sum(counts.values())

        print(f"📁 {domain.upper()}:")
        for attr_num in [1, 2, 3]:
            attr_sym = {1: 'Δ', 2: '⇄', 3: '⟳'}[attr_num]
            count = counts[attr_num]
            pct = (count / total_domain * 100) if total_domain > 0 else 0
            bar = '█' * int(pct / 5)
            print(f"   {attr_sym} (A={attr_num}): {count:2d} concepts ({pct:5.1f}%) {bar}")
        print()

    # ========================================================================
    # §2: DIMENSIONAL CLUSTERING
    # ========================================================================

    print("=" * 80)
    print("§2: DIMENSIONAL CLUSTERING")
    print("=" * 80)
    print()

    dim_by_domain = defaultdict(lambda: defaultdict(list))

    for c in all_concepts:
        domain = c['domain']
        dim_hint = c['synthesis']['dimension_hints']

        # Extract D value
        if dim_hint.startswith('D='):
            D = int(dim_hint[2])
            dim_by_domain[domain][D].append(c['concept_name'])

    for domain in ['mathematics', 'classical_physics', 'cs_logic', 'thermodynamics', 'quantum']:
        print(f"📁 {domain.upper()}:")
        for D in sorted(dim_by_domain[domain].keys()):
            concepts_list = dim_by_domain[domain][D]
            count = len(concepts_list)
            print(f"   D={D}: {count} concepts")
            for name in concepts_list:
                print(f"      • {name}")
        print()

    # ========================================================================
    # §3: COORDINATE SPACE OCCUPANCY
    # ========================================================================

    print("=" * 80)
    print("§3: COORDINATE SPACE OCCUPANCY (Tesseract Grid)")
    print("=" * 80)
    print()

    # Map results files
    results_files = {
        'mathematics': 'batch_1_mathematics_results.json',
        'classical_physics': 'batch_2_classical_physics_results.json',
        'cs_logic': 'batch_3_cs_logic_results.json',
        'thermodynamics': 'batch_4_thermodynamics_results.json',
        'quantum': 'batch_5_quantum_results.json'
    }

    coord_counts = Counter()
    coord_concepts = defaultdict(list)

    for domain, results_file in results_files.items():
        if Path(results_file).exists():
            with open(results_file, 'r', encoding='utf-8') as f:
                results = json.load(f)

            # Results is direct array
            for item in results:
                sigma = item['coordinate']
                name = item['concept']

                coord_counts[sigma] += 1
                coord_concepts[sigma].append(f"{name} ({domain[:4]})")

    print(f"🎯 OCCUPIED NODES: {len(coord_counts)} / 72 Tesseract nodes")
    print(f"   Coverage: {len(coord_counts) / 72 * 100:.1f}%")
    print()

    # Show occupied coordinates
    print("Occupied coordinates (sorted by count):")
    for sigma, count in coord_counts.most_common():
        print(f"   {sigma}: {count} concepts")
        for concept in coord_concepts[sigma]:
            print(f"      • {concept}")
    print()

    # ========================================================================
    # §4: COMPLEXITY DISTRIBUTION
    # ========================================================================

    print("=" * 80)
    print("§4: COMPLEXITY DISTRIBUTION")
    print("=" * 80)
    print()

    complexity_counts = Counter()

    for c in all_concepts:
        complexity = c['synthesis']['complexity']
        complexity_counts[complexity] += 1

    print("Complexity levels:")
    for complexity, count in sorted(complexity_counts.items()):
        pct = count / total * 100
        bar = '█' * int(pct / 5)
        print(f"   {complexity}: {count} concepts ({pct:.1f}%) {bar}")
    print()

    # ========================================================================
    # §5: OSCILLATION TENSIONS
    # ========================================================================

    print("=" * 80)
    print("§5: OSCILLATION TENSIONS (P8 Collapse Events)")
    print("=" * 80)
    print()

    oscillations = []

    for c in all_concepts:
        if 'oscillation_notes' in c['synthesis']:
            oscillations.append({
                'concept': c['concept_name'],
                'domain': c['domain'],
                'notes': c['synthesis']['oscillation_notes']
            })

    if oscillations:
        print(f"Found {len(oscillations)} concepts with recorded oscillations:\n")
        for osc in oscillations:
            print(f"📍 {osc['concept']} ({osc['domain']})")
            print(f"   {osc['notes'][:200]}...")
            print()
    else:
        print("No oscillation tensions recorded (all mappings clean).")
        print()

    # ========================================================================
    # §6: PATTERN EMERGENTI
    # ========================================================================

    print("=" * 80)
    print("§6: PATTERN EMERGENTI")
    print("=" * 80)
    print()

    # Pattern 1: Physics ⇄-heavy vs Math balanced
    math_A2 = attr_by_domain['mathematics'][2]
    math_total = sum(attr_by_domain['mathematics'].values())
    phys_A2 = attr_by_domain['classical_physics'][2]
    phys_total = sum(attr_by_domain['classical_physics'].values())

    print(f"🔬 ATTRIBUTE PATTERN:")
    print(f"   Mathematics:       ⇄ = {math_A2}/{math_total} ({math_A2/math_total*100:.0f}%) — Balanced")
    print(f"   Classical Physics: ⇄ = {phys_A2}/{phys_total} ({phys_A2/phys_total*100:.0f}%) — Relation-dominant")
    print(f"   → Physics describes observable relations, Math describes structures")
    print()

    # Pattern 2: Most common coordinates
    if coord_counts:
        most_common = coord_counts.most_common(3)
        print(f"🎯 HOTSPOT COORDINATES:")
        for sigma, count in most_common:
            parsed = parse_sigma(sigma)
            if parsed:
                D, A, X, P = parsed
                attr_sym = {1: 'Δ', 2: '⇄', 3: '⟳'}[A]
                print(f"   {sigma} (D={D}, {attr_sym}, X={X}): {count} concepts")
        print()

    # Pattern 3: Dimensional preference by domain
    print(f"🌐 DIMENSIONAL PATTERNS:")
    for domain in ['mathematics', 'classical_physics']:
        dims = dim_by_domain[domain]
        if dims:
            avg_D = sum(D * len(concepts) for D, concepts in dims.items()) / sum(len(c) for c in dims.values())
            print(f"   {domain}: Average D = {avg_D:.2f}")
            most_common_D = max(dims.keys(), key=lambda D: len(dims[D]))
            print(f"      Most common: D={most_common_D} ({len(dims[most_common_D])} concepts)")
    print()

    # ========================================================================
    # §7: NEXT STEPS RECOMMENDATION
    # ========================================================================

    print("=" * 80)
    print("§7: NEXT STEPS RECOMMENDATION")
    print("=" * 80)
    print()

    # Identify gaps
    used_attrs = set()
    used_dims = set()

    for c in all_concepts:
        attr_map = {'Δ': 1, '⇄': 2, '⟳': 3}
        attr_dom = c['synthesis']['attribute_dominant']
        used_attrs.add(attr_map[attr_dom])

        dim_hint = c['synthesis']['dimension_hints']
        if dim_hint.startswith('D='):
            used_dims.add(int(dim_hint[2]))

    print("📋 COVERAGE GAPS:")

    # Attribute gaps
    all_attrs = {1, 2, 3}
    missing_attrs = all_attrs - used_attrs
    if missing_attrs:
        for A in missing_attrs:
            attr_sym = {1: 'Δ', 2: '⇄', 3: '⟳'}[A]
            print(f"   ⚠ Attribute {attr_sym} (A={A}) underrepresented")

    # Dimension gaps
    all_dims = {1, 2, 3, 4}
    missing_dims = all_dims - used_dims
    if missing_dims:
        for D in missing_dims:
            print(f"   ⚠ Dimension D={D} underrepresented")

    if not missing_attrs and not missing_dims:
        print("   ✅ All attributes and dimensions represented")

    print()
    print("🎯 SUGGESTED NEXT DOMAINS:")

    # Suggest based on gaps
    suggestions = []

    if 3 in missing_attrs or attr_by_domain['classical_physics'][3] < 3:
        suggestions.append("   • Thermodynamics (⟳-heavy: irreversible processes, entropy)")
        suggestions.append("   • Quantum mechanics (⟳: state transitions, time evolution)")

    if 1 in missing_attrs or attr_by_domain['mathematics'][1] < 5:
        suggestions.append("   • Set theory (Δ-heavy: distinctions, classifications)")
        suggestions.append("   • Logic (Δ: true/false, propositions)")

    if 4 in used_dims and attr_by_domain['classical_physics'][3] < 3:
        suggestions.append("   • General relativity (D=4 ⟳: spacetime curvature dynamics)")
        suggestions.append("   • Quantum field theory (D=4 ⟳: field evolution)")

    # Always suggest
    suggestions.append("   • Information theory (Δ/⇄: encoding, compression, channel capacity)")
    suggestions.append("   • Statistical mechanics (bridge micro↔macro scales)")

    for s in suggestions:
        print(s)

    print()
    print("=" * 80)
    print("END DIAGNOSTIC REPORT")
    print("=" * 80)

if __name__ == '__main__':
    analyze_network()
