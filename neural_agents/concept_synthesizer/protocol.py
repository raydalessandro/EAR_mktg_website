#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Concept Synthesizer Protocol v2 — Knowledge-Based Concept Analyzer

CHANGES from v1:
- ALL entries have attribute_dominant (elimination-test derived)
- PRIMARY marker gives +weight in ontological_structures  
- Unambiguous dimension_hints (single D value)
- complexity field on all entries
- Elimination test documented per entry

COMUNICAZIONE:
- INPUT: Concept name da Mapper
- OUTPUT: Ontological synthesis per Mapper
"""

import sys
import json
import traceback
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List

# Add shared to path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))

try:
    from file_sync import FileSync
except ImportError:
    class FileSync:
        def write_network_result(self, d): pass
        def wait_for_mapping(self, timeout=120): return {}


class ConceptSynthesizerProtocol:
    """
    Concept Synthesizer v2 — Uses elimination test for attribute dominance.
    
    ELIMINATION TEST (from MAPPING_RULES §2):
    For each attribute, ask: "If I remove THIS, does the concept survive?"
    - Remove Δ → concept still recognizable? → Δ is NOT dominant
    - Remove ⇄ → concept still recognizable? → ⇄ is NOT dominant  
    - Remove ⟳ → concept still recognizable? → ⟳ is NOT dominant
    The one whose removal DESTROYS the concept is dominant.
    """

    def __init__(self):
        """Initialize Concept Synthesizer."""
        self.sync = FileSync()
        self.synthesis_history: List[Dict[str, Any]] = []
        self.context = self._load_context()

    def _load_context(self) -> Dict[str, str]:
        """Load synthesis guides from context."""
        context = {}
        context_dir = Path(__file__).parent / "context"

        if context_dir.exists():
            for doc in context_dir.glob("*.md"):
                context[doc.stem] = doc.read_text(encoding='utf-8')
                print(f"[OK] Loaded {doc.name}")

        return context

    def synthesize_concept(self, concept_name: str) -> Dict[str, Any]:
        """
        Synthesize scientific concept ontologically.

        Args:
            concept_name: Name of concept

        Returns:
            Synthesis with ontological structures
        """
        print(f"\n{'='*60}")
        print(f"CONCEPT SYNTHESIZER v2: Synthesizing {concept_name}")
        print(f"{'='*60}\n")

        try:
            synthesis = self._synthesize_knowledge(concept_name)

            result = {
                'status': 'success',
                'concept_name': concept_name,
                'synthesis': synthesis,
                'synthesized_at': datetime.now().isoformat()
            }

            print(f"[SUCCESS] Synthesis complete")
            print(f"Type: {synthesis.get('concept_type', 'unknown')}")
            print(f"Dominant: {synthesis.get('attribute_dominant', 'unset')}")

        except Exception as e:
            result = {
                'status': 'error',
                'concept_name': concept_name,
                'error': str(e),
                'traceback': traceback.format_exc(),
                'synthesized_at': datetime.now().isoformat()
            }
            print(f"[ERROR] Synthesis failed: {e}")

        print(f"\n{'='*60}\n")

        self.synthesis_history.append(result)
        return result

    def _synthesize_knowledge(self, concept_name: str) -> Dict[str, Any]:
        """
        Synthesize using Claude's knowledge.

        EVERY entry has:
        - concept_type: theorem | law | theory | equation | threshold
        - formal_statement: the core claim
        - ontological_structures: ordered list, PRIMARY first
        - dimension_hints: single unambiguous D value with justification
        - attribute_dominant: single symbol with elimination-test reasoning
        - complexity: foundational(1) | recursive(2) | synthetic(3)
        - elimination_test: explicit reasoning for attribute choice
        - related: list of related concepts
        """
        knowledge = {

            # ============================================================
            # Σ₁₁₁₊ — Pythagorean Theorem
            # ============================================================
            "pythagorean theorem": {
                'concept_type': 'theorem',
                'formal_statement': 'a² + b² = c² — defines the metric boundary in Euclidean geometry',
                'ontological_structures': [
                    {'pattern': 'Δ', 'evidence': 'PRIMARY — defines the boundary between right and non-right triangles; IS a distinction/identity', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'Relates three sides structurally'},
                    {'pattern': '⟳', 'evidence': 'Minimal — static identity, no temporal process'}
                ],
                'dimension_hints': 'D=1 (point/foundational) — pure geometry, no spatial extension needed, axiomatic identity',
                'attribute_dominant': 'Δ',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove Δ (distinction a²+b²=c²) → nothing remains. Remove ⇄ (relation between sides) → you still have the identity. Remove ⟳ → already minimal. Δ is essential.',
                'related': ['Euclidean geometry', 'Distance metrics']
            },

            # ============================================================
            # Σ₁₂₁₊ — Fundamental Theorem of Calculus
            # ============================================================
            "fundamental theorem of calculus": {
                'concept_type': 'theorem',
                'formal_statement': 'Differentiation and integration are inverse operations — bidirectional correspondence',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — the theorem IS the bidirectional correspondence: derivative ↔ integral', 'primary': True},
                    {'pattern': '⟳', 'evidence': 'Process of accumulation vs rate of change'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes local (derivative) from global (integral)'}
                ],
                'dimension_hints': 'D=1 (foundational) — meta-principle of calculus structure, pure mathematical identity independent of physical space',
                'attribute_dominant': '⇄',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⇄ (correspondence derivative↔integral) → theorem vanishes. Remove Δ → you still know they correspond. Remove ⟳ → correspondence still holds statically. ⇄ is essential.',
                'related': ['Leibniz', 'Newton', 'Analysis', 'Continuity']
            },

            # ============================================================
            # Σ₄₂₃₊ — Noether's Theorem
            # ============================================================
            "noether's theorem": {
                'concept_type': 'theorem',
                'formal_statement': 'Every differentiable symmetry corresponds to a conservation law — unifies algebra, geometry, physics',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — the theorem IS the correspondence: symmetry ↔ conservation', 'primary': True},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes symmetric vs non-symmetric transformations'},
                    {'pattern': '⟳', 'evidence': 'Conservation manifests through temporal invariance'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — operates across all of spacetime, Lagrangian field structure',
                'attribute_dominant': '⇄',
                'complexity': 'synthetic (3)',
                'elimination_test': 'Remove ⇄ (symmetry↔conservation correspondence) → theorem vanishes. Remove Δ → correspondence still exists. Remove ⟳ → static symmetry still maps to conserved quantity. ⇄ is essential.',
                'related': ['Lagrangian', 'Conservation laws', 'Symmetry groups']
            },

            # ============================================================
            # Σ₄₃₁₊ — Maxwell's Equations
            # ============================================================
            "maxwell's equations": {
                'concept_type': 'law',
                'formal_statement': 'Four equations governing electromagnetic field evolution and propagation through spacetime',
                'ontological_structures': [
                    {'pattern': '⟳', 'evidence': 'PRIMARY — equations describe temporal evolution and propagation of EM fields; without dynamics, no Maxwell', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'Electric and magnetic fields mutually generate each other'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes sources (charges/currents) from fields'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — spacetime field dynamics, covariant formulation',
                'attribute_dominant': '⟳',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⟳ (propagation/evolution) → static fields, no waves, no light, no Maxwell. Remove ⇄ (E↔B coupling) → you still have propagating disturbances. Remove Δ (source distinction) → fields still propagate. ⟳ is essential.',
                'related': ['Electromagnetism', 'Light', 'Wave equation', 'Special relativity']
            },

            # ============================================================
            # Σ₄₃₁₊ — Schrödinger Equation
            # ============================================================
            "schrödinger equation": {
                'concept_type': 'law',
                'formal_statement': 'iℏ∂ψ/∂t = Ĥψ — governs temporal evolution of quantum state',
                'ontological_structures': [
                    {'pattern': '⟳', 'evidence': 'PRIMARY — the equation IS a time-evolution operator; without temporal dynamics, no Schrödinger', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'Energy eigenstates ↔ stationary states correspondence'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes quantum superposition from classical states'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — wavefunction evolves over configuration space in time',
                'attribute_dominant': '⟳',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⟳ (time evolution ∂ψ/∂t) → equation vanishes, static eigenvalue problem only. Remove ⇄ (eigenstate correspondence) → evolution still occurs. Remove Δ (classical/quantum distinction) → evolution still occurs. ⟳ is essential.',
                'related': ['Quantum mechanics', 'Wavefunction', 'Hamiltonian', 'Eigenvalue problem']
            },

            # ============================================================
            # Σ₄₃₁₋ — Second Law of Thermodynamics
            # ============================================================
            "second law of thermodynamics": {
                'concept_type': 'law',
                'formal_statement': 'Entropy of an isolated system never decreases — irreversible temporal arrow',
                'ontological_structures': [
                    {'pattern': '⟳', 'evidence': 'PRIMARY — the law IS about irreversible temporal process, arrow of time; without process, no second law', 'primary': True},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes order from disorder, possible from impossible processes'},
                    {'pattern': '⇄', 'evidence': 'Relates energy to information/organization via entropy'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — universal statistical law, operates at field level across all scales',
                'attribute_dominant': '⟳',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⟳ (irreversible process, arrow of time) → no second law, just static state counting. Remove Δ (order/disorder distinction) → entropy still increases. Remove ⇄ (energy-information relation) → entropy still increases. ⟳ is essential.',
                'related': ['Entropy', 'Statistical mechanics', 'Arrow of time', 'Information theory']
            },

            # ============================================================
            # T7.C7.4 — Heisenberg Uncertainty Principle
            # ============================================================
            "heisenberg uncertainty principle": {
                'concept_type': 'threshold',
                'formal_statement': 'ΔxΔp ≥ ℏ/2 — Cannot simultaneously minimize position and momentum uncertainty',
                'ontological_structures': [
                    {'pattern': 'Δ⇄⟳', 'evidence': 'Trans-attributo — ALL THREE inseparable (P6)'},
                    {'pattern': 'floor ε ~ ℏ', 'evidence': 'T7.C7.4: origin (0,0,0) unreachable in resource space'},
                    {'pattern': 'co-variation', 'evidence': 'Fixing one attribute forces co-variation in others'}
                ],
                'dimension_hints': 'NOT A NODE — Boundary condition of Tesseract structure itself',
                'attribute_dominant': 'trans-attributo (P6)',
                'ontological_status': 'T7.C7.4 threshold — manifestation of P6 inseparability at quantum scale',
                'complexity': 'constraint — not applicable',
                'elimination_test': 'NOT A NODE — all three attributes equally essential because it describes their inseparability. This IS P6 manifest.',
                'related': ['T7 Barrier Unity', 'P6 Inseparability', 'WAY barrier', 'Complementarity']
            },

            # ============================================================
            # Σ₃₂₁₊ — Newton's Laws
            # ============================================================
            "newton's laws": {
                'concept_type': 'law',
                'formal_statement': 'F=ma — force relates to rate of change of momentum in volumetric space',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — F=ma IS a bidirectional relation: force ↔ acceleration', 'primary': True},
                    {'pattern': '⟳', 'evidence': 'Temporal evolution of motion under force'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes inertial from non-inertial frames'}
                ],
                'dimension_hints': 'D=3 (volumetric) — operates in 3D space, NOT spacetime (no Lorentz structure)',
                'attribute_dominant': '⇄',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⇄ (force↔acceleration relation) → F=ma vanishes. Remove ⟳ (temporal evolution) → relation still holds as constraint. Remove Δ (frame distinction) → F=ma still works in any frame. ⇄ is essential.',
                'related': ['Classical mechanics', 'Inertia', 'Action-reaction', 'Galilean relativity']
            },

            # ============================================================
            # Σ₄₂₂₊ — Special Relativity
            # ============================================================
            "special relativity": {
                'concept_type': 'theory',
                'formal_statement': 'Speed of light constant in all inertial frames; space and time unified into spacetime',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — space and time reciprocally transform via Lorentz', 'primary': True},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes proper time from coordinate time, invariant vs relative quantities'},
                    {'pattern': '⟳', 'evidence': 'Causal structure defines temporal ordering'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — spacetime manifold structure',
                'attribute_dominant': '⇄',
                'complexity': 'recursive (2)',
                'elimination_test': 'Remove ⇄ (space↔time reciprocal transformation) → no SR, just separate space and time. Remove Δ (proper/coordinate distinction) → Lorentz transform still works. Remove ⟳ (causal ordering) → spacetime geometry still defined. ⇄ is essential.',
                'related': ['Minkowski spacetime', 'Lorentz transformation', 'E=mc²', 'Causality']
            },

            # ============================================================
            # Σ₄₂₃₊ — General Relativity
            # ============================================================
            "general relativity": {
                'concept_type': 'theory',
                'formal_statement': 'Gravity is curvature of spacetime caused by energy-momentum — fuses geometry + gravity + matter',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — matter curves spacetime ↔ spacetime dictates matter motion (Wheeler)', 'primary': True},
                    {'pattern': '⟳', 'evidence': 'Dynamic evolution of spacetime geometry'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes geodesic (free fall) from forced motion'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — geometric field theory over spacetime',
                'attribute_dominant': '⇄',
                'complexity': 'synthetic (3)',
                'elimination_test': 'Remove ⇄ (matter↔geometry reciprocal relation) → no GR, just flat spacetime OR just matter. Remove Δ (geodesic distinction) → curvature-matter coupling still holds. Remove ⟳ (evolution) → static GR solutions still exist. ⇄ is essential.',
                'related': ['Einstein field equations', 'Curved spacetime', 'Black holes', 'Cosmology']
            },

            # ============================================================
            # Σ₄₂₁₊ — Conservation of Energy
            # ============================================================
            "conservation of energy": {
                'concept_type': 'law',
                'formal_statement': 'Total energy of isolated system remains constant through all transformations',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — energy transforms between forms while conserved: kinetic ↔ potential ↔ thermal', 'primary': True},
                    {'pattern': '⟳', 'evidence': 'Invariance persists through temporal processes'},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes different energy forms'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — universal conservation law across all of physics',
                'attribute_dominant': '⇄',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⇄ (transformation between energy forms) → just "energy exists", not conservation. Remove ⟳ (temporal invariance) → conservation still stated as constraint. Remove Δ (form distinction) → all energy is one, still conserved. ⇄ is essential.',
                'related': ["Noether's theorem", 'Time translation symmetry', 'First law thermodynamics']
            },

            # ============================================================
            # Σ₁₂₁₊ — Euler's Identity (TEST)
            # ============================================================
            "euler's identity": {
                'concept_type': 'theorem',
                'formal_statement': 'e^(iπ) + 1 = 0 — unifies five fundamental constants in a single identity',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — the theorem IS a relation connecting five independent mathematical constants (e, i, π, 1, 0)', 'primary': True},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes these specific constants as mathematically fundamental'},
                    {'pattern': '⟳', 'evidence': 'Minimal — static identity, no temporal process'}
                ],
                'dimension_hints': 'D=1 (foundational) — pure mathematical identity, no spatial extension, axiomatic',
                'attribute_dominant': '⇄',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⇄ (relation connecting 5 constants) → identity vanishes, theorem IS the connection. Remove Δ (distinction of fundamentals) → relation still holds. Remove ⟳ → already static. ⇄ is essential.',
                'related': ['Complex analysis', 'Exponential function', 'Trigonometry', 'Mathematical beauty']
            },

            # ============================================================
            # Σ₂₂₁₊ — Hooke's Law
            # ============================================================
            "hooke's law": {
                'concept_type': 'law',
                'formal_statement': 'F = -kx — restoring force proportional to displacement from equilibrium',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — the law IS the proportional relation: force ↔ displacement', 'primary': True},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes equilibrium from displaced states'},
                    {'pattern': '⟳', 'evidence': 'Oscillatory process when system returns to equilibrium'}
                ],
                'dimension_hints': 'D=2 (linear/directional) — force acts along a line, one-dimensional displacement',
                'attribute_dominant': '⇄',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⇄ (F∝x proportionality) → law vanishes, no Hooke. Remove Δ (equilibrium distinction) → proportionality still holds. Remove ⟳ (oscillation) → static F=-kx relation still exists. ⇄ is essential.',
                'related': ['Elasticity', 'Simple harmonic motion', 'Springs', 'Young modulus']
            },

            # ============================================================
            # Σ₄₁₁₊ — Pauli Exclusion Principle
            # ============================================================
            "pauli exclusion principle": {
                'concept_type': 'principle',
                'formal_statement': 'No two identical fermions can occupy the same quantum state simultaneously',
                'ontological_structures': [
                    {'pattern': 'Δ', 'evidence': 'PRIMARY — principle IS about distinction: fermions MUST be distinguishable by at least one quantum number', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'Relates fermion statistics to state occupation'},
                    {'pattern': '⟳', 'evidence': 'Minimal — describes static constraint on configurations'}
                ],
                'dimension_hints': 'D=4 (field/quantum) — applies to quantum fields, all of spacetime',
                'attribute_dominant': 'Δ',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove Δ (distinction requirement) → principle vanishes, it IS about forced distinction. Remove ⇄ (state-occupation relation) → exclusion still holds. Remove ⟳ → already static. Δ is essential.',
                'related': ['Fermions', 'Quantum statistics', 'Antisymmetric wavefunctions', 'Spin-statistics theorem']
            },

            # ============================================================
            # Σ₄₂₁₊ — Shannon's Theorem (Channel Capacity)
            # ============================================================
            "shannon's theorem": {
                'concept_type': 'theorem',
                'formal_statement': 'C = B log₂(1 + S/N) — maximum rate of reliable information transmission through noisy channel',
                'ontological_structures': [
                    {'pattern': '⇄', 'evidence': 'PRIMARY — theorem IS the relation: channel capacity ↔ bandwidth and signal-to-noise ratio', 'primary': True},
                    {'pattern': 'Δ', 'evidence': 'Distinguishes signal from noise, reliable from unreliable transmission'},
                    {'pattern': '⟳', 'evidence': 'Information transmission is a temporal process'}
                ],
                'dimension_hints': 'D=4 (field/temporal) — applies to all communication channels, temporal information flow',
                'attribute_dominant': '⇄',
                'complexity': 'foundational (1)',
                'elimination_test': 'Remove ⇄ (C∝B,S/N relation) → theorem vanishes. Remove Δ → signal/noise distinction presupposed by S/N but structure is relational. Remove ⟳ (transmission process) → static channel capacity still defined. ⇄ is essential.',
                'related': ['Information theory', 'Entropy', 'Communication', 'Coding theory', 'Noisy channels']
            },

            # ============================================================
            # Σ₁₁₂₊ — Turing Halting Problem
            # ============================================================
            "turing halting problem": {
                'concept_type': 'theorem',
                'formal_statement': 'No algorithm can determine whether an arbitrary program will halt or run forever',
                'ontological_structures': [
                    {'pattern': 'Δ', 'evidence': 'PRIMARY — distinguishes decidable from undecidable problems, halting from non-halting', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'Self-referential relation: program analyzing itself leads to contradiction (diagonal argument)'},
                    {'pattern': '⟳', 'evidence': 'Process of program execution through time'}
                ],
                'dimension_hints': 'D=1 (foundational) — meta-mathematical result about computation itself, not physical space',
                'attribute_dominant': 'Δ',
                'complexity': 'recursive (2)',
                'elimination_test': 'Remove Δ (decidable/undecidable distinction) → theorem vanishes, it IS about that boundary. Remove ⇄ (self-reference/diagonal argument) → distinction still proven via other means. Remove ⟳ (execution) → uncomputability proven statically. Δ is essential.',
                'related': ['Computability', 'Undecidability', 'Diagonal argument', 'Gödel incompleteness', 'Church-Turing thesis']
            },

            # ============================================================
            # CONSTRAINT — Gödel's Incompleteness Theorems
            # ============================================================
            "gödel's incompleteness theorems": {
                'concept_type': 'theorem',
                'formal_statement': 'Any sufficiently powerful consistent formal system contains true statements it cannot prove',
                'ontological_structures': [
                    {'pattern': 'Δ', 'evidence': 'PRIMARY — distinguishes provable from true, syntax from semantics', 'primary': True},
                    {'pattern': '⇄', 'evidence': 'Self-referential relation between system and meta-system'},
                    {'pattern': '⟳', 'evidence': 'Recursive enumeration process reveals structural limits'}
                ],
                'dimension_hints': 'D=4 (field) — meta-mathematical, applies across all formal systems',
                'attribute_dominant': 'Δ',
                'complexity': 'recursive (2)',
                'elimination_test': 'Remove Δ (provable/true distinction) → theorem vanishes, it IS about that distinction. Remove ⇄ (self-reference) → you still have incompleteness via other constructions. Remove ⟳ → static result. Δ is essential.',
                'ontological_status': 'P6 + P1 — constraint on formal systems, inseparability of proof and truth',
                'related': ['Mathematical logic', 'Incompleteness', 'Self-reference', 'Halting problem']
            },
        }

        concept_key = concept_name.lower()

        if concept_key in knowledge:
            return knowledge[concept_key]

        # Default for unknown concepts
        return {
            'concept_type': 'unknown',
            'formal_statement': f'Concept: {concept_name}',
            'ontological_structures': [
                {'pattern': 'Δ', 'evidence': 'Has distinct identity'}
            ],
            'dimension_hints': 'To be determined',
            'attribute_dominant': 'unknown',
            'complexity': 'to be determined',
            'elimination_test': 'Not yet analyzed',
            'related': []
        }

    def report_synthesis(self, synthesis: Dict[str, Any]) -> Dict[str, Any]:
        """Report synthesis to Mapper."""
        print(f"[REPORT] Sending synthesis to Mapper...")
        self.sync.write_network_result(synthesis)
        print(f"[OK] Synthesis written\n")
        return synthesis

    def synthesize_and_report(self, concept_name: str) -> Dict[str, Any]:
        """Full pipeline: synthesize → report."""
        synthesis = self.synthesize_concept(concept_name)
        self.report_synthesis(synthesis)
        return synthesis

    def wait_and_synthesize(self, timeout: int = 300) -> Dict[str, Any]:
        """Wait for concept from Mapper and synthesize."""
        print("[WAITING] Concept Synthesizer waiting...")

        try:
            mapping = self.sync.wait_for_mapping(timeout=timeout)
            concept_name = mapping.get('concept_name', mapping.get('paper_id', 'unknown'))

            if not concept_name or concept_name == 'unknown':
                return {'status': 'error', 'error': 'No concept name'}

            return self.synthesize_and_report(concept_name)

        except TimeoutError:
            print(f"[TIMEOUT] No concept after {timeout}s")
            return None

    def run_loop(self, max_iterations: Optional[int] = None):
        """Run synthesizer loop."""
        iteration = 0

        print(f"\n{'='*60}")
        print("CONCEPT SYNTHESIZER v2 ONLINE")
        print(f"{'='*60}\n")

        try:
            while True:
                if max_iterations and iteration >= max_iterations:
                    break

                iteration += 1
                print(f"\n--- Iteration {iteration} ---\n")

                result = self.wait_and_synthesize(timeout=60)

                if result is None:
                    print("No concept received, waiting...")
                    continue

        except KeyboardInterrupt:
            print("\n\n[STOPPED] Synthesizer stopped")

        except Exception as e:
            print(f"\n[ERROR] Synthesizer error: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Concept Synthesizer v2")
    parser.add_argument('--test', type=str, help="Test with concept")
    parser.add_argument('--loop', action='store_true', help="Run loop")
    parser.add_argument('--dump-all', action='store_true', help="Dump all knowledge base entries")

    args = parser.parse_args()

    synthesizer = ConceptSynthesizerProtocol()

    if args.test:
        synthesizer.synthesize_and_report(args.test)
    elif args.dump_all:
        # Show all entries for verification
        for name in [
            "Pythagorean Theorem", "Fundamental Theorem of Calculus",
            "Noether's Theorem", "Maxwell's Equations", "Schrödinger Equation",
            "Second Law of Thermodynamics", "Heisenberg Uncertainty Principle",
            "Newton's Laws", "Special Relativity", "General Relativity",
            "Conservation of Energy", "Gödel's Incompleteness Theorems",
        ]:
            s = synthesizer.synthesize_concept(name)
            synth = s.get('synthesis', {})
            dom = synth.get('attribute_dominant', '?')
            dim = synth.get('dimension_hints', '?')[:40]
            elim = synth.get('elimination_test', '?')[:60]
            print(f"  {name:<40} dom={dom:<5} dim={dim}")
            print(f"    elim: {elim}...")
            print()
    elif args.loop:
        synthesizer.run_loop()
    else:
        print("Usage:")
        print("  python protocol.py --test \"Noether's Theorem\"")
        print("  python protocol.py --dump-all")
