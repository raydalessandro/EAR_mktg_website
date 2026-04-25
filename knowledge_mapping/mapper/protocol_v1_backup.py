#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper Protocol — Sigma Coordinate Proposer

RUOLO:
- Ha EAR base + documenti da mappare (fenomeni neurali)
- Analizza network results
- Propone coordinate Σ per fenomeni
- Itera basandosi su judgments da Ontology Judge

COMUNICAZIONE:
- INPUT: Network results da Builder, Judgments da Judge
- OUTPUT: Mapping proposals con Σ coordinates
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add shared to path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))
from file_sync import FileSync


class MapperProtocol:
    """
    Mapper — Proposes Sigma Coordinates

    Responsibilities:
    1. Reads network results (metrics, dynamics)
    2. Reads EAR base + phenomenon docs
    3. Proposes Σ coordinates for phenomena
    4. Receives judgments from Ontology Judge
    5. Iterates on proposals based on feedback
    6. Generates new network test code when needed
    """

    def __init__(self, context_path: Optional[str] = None):
        """
        Initialize Mapper.

        Args:
            context_path: Path to context docs (EAR base + phenomena to map)
        """
        self.context_path = context_path or Path(__file__).parent / "context"
        self.sync = FileSync()
        self.mappings_history: List[Dict[str, Any]] = []

        # Load context
        self.context_docs = self._load_context()

    def _load_context(self) -> Dict[str, str]:
        """
        Load context documents (EAR base + phenomena).

        Returns:
            Dictionary of document_name -> content
        """
        context = {}

        context_dir = Path(self.context_path)

        if not context_dir.exists():
            print(f"[INFO] Context directory not found: {context_dir}")
            print("[INFO] Will use placeholder context")
            return self._placeholder_context()

        # Load all .md files
        for doc in context_dir.glob("*.md"):
            if doc.name != "README.md":  # Skip README
                context[doc.stem] = doc.read_text(encoding='utf-8')
                print(f"[OK] Loaded {doc.name}")

        # Load GRAFO Tesseract JSON files
        grafo_dir = context_dir / "grafo"
        if grafo_dir.exists():
            for grafo_file in grafo_dir.glob("*.json"):
                try:
                    grafo_data = json.loads(grafo_file.read_text(encoding='utf-8'))
                    context[f"GRAFO_{grafo_file.stem}"] = grafo_data
                    print(f"[OK] Loaded {grafo_file.name} ({len(grafo_data.get('nodes', []))} nodes)")
                except Exception as e:
                    print(f"[WARNING] Could not load {grafo_file.name}: {e}")

        if not context:
            print("[INFO] No context docs found, using placeholder")
            return self._placeholder_context()

        return context

    def _placeholder_context(self) -> Dict[str, str]:
        """Placeholder context (until Ray adds docs)."""
        return {
            "EAR_BASE": """
# EAR Base Ontology

Σ = (dimension, attribute, complexity, polarity)

Dimensions: 1-4
Attributes: Δ (distinction), ⇄ (relation), ⟳ (process)
Complexity: 1 (simple), 2 (intermediate), 3 (complex)
Polarity: + (constructive), - (deconstructive)
""",
            "PHENOMENA": """
# Neural Phenomena to Map

1. **Burst Criticality**: τ ≈ 1.5 avalanche exponent
2. **STDP Convergence**: Synaptic weight stabilization
3. **E/I Balance**: Homeostatic regulation
"""
        }

    def analyze_synthesis(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze paper extraction result from Paper Analyzer.

        Args:
            result: Synthesis result from Analyzer

        Returns:
            Analysis dictionary with concepts to map
        """
        print(f"\n{'='*60}")
        print("MAPPER: Analyzing paper concepts")
        print(f"{'='*60}\n")

        status = result.get('status', 'unknown')
        synthesis = result.get('synthesis', {})
        concept_name = result.get('concept_name', 'unknown')

        analysis = {
            'analysis_status': status,
            'timestamp': datetime.now().isoformat(),
            'concept_name': concept_name,
            'synthesis': synthesis,
            'ready_for_mapping': True
        }

        if status == 'error':
            print(f"[ERROR] Synthesis failed: {result.get('error', 'unknown')}")
            analysis['ready_for_mapping'] = False
            return analysis

        # Show synthesis info
        concept_type = synthesis.get('concept_type', 'unknown')
        structures = synthesis.get('ontological_structures', [])

        print(f"Concept: {concept_name}")
        print(f"Type: {concept_type}")
        print(f"Ontological structures: {len(structures)}")
        for struct in structures:
            print(f"  - {struct.get('pattern', '?')}: {struct.get('evidence', '')[:50]}")

        print(f"\nReady for Tesseract mapping")
        print()

        return analysis

    def propose_mapping(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Propose Sigma coordinates based on analysis.

        Args:
            analysis: Network result analysis

        Returns:
            Mapping proposal
        """
        print(f"\n{'='*60}")
        print("MAPPER: Proposing Sigma coordinates")
        print(f"{'='*60}\n")

        # Check if ready for mapping
        if not analysis.get('ready_for_mapping'):
            print("[INFO] Concept not ready for mapping")
            return {
                'status': 'uncertain',
                'reasoning': 'Synthesis failed or incomplete'
            }

        # Extract synthesis info
        synthesis = analysis.get('synthesis', {})
        concept_name = analysis.get('concept_name', 'unknown')
        concept_type = synthesis.get('concept_type', 'unknown')
        structures = synthesis.get('ontological_structures', [])

        # New: Extract ontological metadata
        attribute_dominant = synthesis.get('attribute_dominant', None)
        dimension_hints = synthesis.get('dimension_hints', '')
        complexity_hint = synthesis.get('complexity', None)
        ontological_status = synthesis.get('ontological_status', None)

        # SPECIAL CASE: Threshold / Boundary Conditions
        if concept_type == 'threshold' or 'T7' in str(ontological_status):
            proposal = {
                'sigma': 'T7.4_THRESHOLD',
                'reasoning': 'NOT A NODE - Boundary condition of Tesseract (origin unreachable)',
                'note': 'If forced to assign: Σ₄₃₃₊ (synthetic trans-attributo at field level)'
            }
        else:
            # Parse dimension from hints
            dimension = self._parse_dimension(dimension_hints)

            # Parse attribute from dominant or structures
            attribute = self._parse_attribute(attribute_dominant, structures)

            # Parse complexity
            complexity = self._parse_complexity(complexity_hint, concept_type)

            # Build Sigma coordinate
            sigma = self._build_sigma(dimension, attribute, complexity, polarity='+')

            proposal = {
                'sigma': sigma,
                'reasoning': f'D={dimension} ({self._dimension_name(dimension)}), X={attribute} ({self._attribute_name(attribute)}), C={complexity}'
            }

        mapping = {
            'status': 'proposed',
            'concept_name': concept_name,
            'concept_type': concept_type,
            'sigma': proposal['sigma'],
            'reasoning': proposal['reasoning'],
            'ontological_structures': structures,
            'synthesis_analysis': analysis,
            'timestamp': datetime.now().isoformat()
        }

        print(f"Proposed mapping:")
        print(json.dumps(mapping, indent=2))
        print()

        return mapping

    def _parse_dimension(self, hints: str) -> int:
        """Parse dimension from hints."""
        hints_lower = hints.lower()
        if 'foundational' in hints_lower or 'meta-principle' in hints_lower:
            return 1
        elif 'line' in hints_lower:
            return 2
        elif 'organism' in hints_lower or 'volumetric' in hints_lower or '3d' in hints_lower:
            return 3
        elif 'field' in hints_lower or 'spacetime' in hints_lower or 'universal' in hints_lower:
            return 4
        else:
            # Default heuristic
            return 1

    def _parse_attribute(self, dominant: str, structures: List[Dict]) -> int:
        """Parse attribute (1=Δ, 2=⇄, 3=⟳)."""
        if dominant:
            if 'Δ' in dominant:
                return 1
            elif '⇄' in dominant:
                return 2
            elif '⟳' in dominant:
                return 3

        # Fallback: count patterns in structures
        counts = {'Δ': 0, '⇄': 0, '⟳': 0}
        for struct in structures:
            pattern = struct.get('pattern', '')
            for key in counts:
                if key in pattern:
                    counts[key] += 1

        # Return dominant
        if counts['Δ'] >= counts['⇄'] and counts['Δ'] >= counts['⟳']:
            return 1
        elif counts['⇄'] >= counts['⟳']:
            return 2
        else:
            return 3

    def _parse_complexity(self, hint: str, concept_type: str) -> int:
        """Parse complexity (1=foundational, 2=recursive, 3=synthetic)."""
        if hint:
            hint_lower = str(hint).lower()
            if 'foundational' in hint_lower or 'simple' in hint_lower or '1' in hint_lower:
                return 1
            elif 'recursive' in hint_lower or 'intermediate' in hint_lower or '2' in hint_lower:
                return 2
            elif 'synthetic' in hint_lower or 'complex' in hint_lower or '3' in hint_lower:
                return 3

        # Fallback heuristic
        if concept_type in ['theorem', 'axiom', 'law']:
            return 1  # Foundational
        elif concept_type in ['principle', 'equation']:
            return 2  # Recursive
        else:
            return 1  # Default foundational

    def _build_sigma(self, dimension: int, attribute: int, complexity: int, polarity: str) -> str:
        """Build Sigma coordinate string."""
        pol_symbol = '₊' if polarity == '+' else '₋'
        return f'Σ{dimension}{attribute}{complexity}{pol_symbol}'

    def _dimension_name(self, d: int) -> str:
        """Get dimension name."""
        names = {1: 'Point/Foundational', 2: 'Line/Relational', 3: 'Organism/Volumetric', 4: 'Field/Universal'}
        return names.get(d, f'D{d}')

    def _attribute_name(self, a: int) -> str:
        """Get attribute name."""
        names = {1: 'Δ distinction', 2: '⇄ relation', 3: '⟳ process'}
        return names.get(a, f'A{a}')

    def prepare_paper(self, paper_title: str = None) -> str:
        """
        Prepare paper text for analysis.

        Args:
            paper_title: Title/identifier of paper to analyze

        Returns:
            Paper text
        """
        # Placeholder papers (will be replaced with real papers later)
        papers = {
            'noether': """
Noether's Theorem

Noether's theorem states that every differentiable symmetry of the action
of a physical system has a corresponding conservation law.

Theorem (Noether, 1915): If a system has a continuous symmetry property,
then there are corresponding quantities whose values are conserved in time.

Conservation Laws:
- Time translation symmetry → Energy conservation
- Space translation symmetry → Momentum conservation
- Rotation symmetry → Angular momentum conservation

Definition: A symmetry is a transformation that leaves the action invariant.

Principle: The laws of physics are the same in all inertial reference frames.
""",
            'pythagorean': """
Pythagorean Theorem

The Pythagorean theorem describes a fundamental relationship in Euclidean geometry.

Theorem (Pythagoras, ~500 BCE): In a right triangle, the square of the hypotenuse
equals the sum of squares of the other two sides.

Mathematical form: a² + b² = c²

Definition: A right triangle is a triangle with one 90-degree angle.

This theorem is foundational to geometry and has countless applications in
mathematics, physics, and engineering.
"""
        }

        default_paper = """
Sample Scientific Paper

This is a placeholder paper for testing.

Theorem: Every action has an equal and opposite reaction (Newton's Third Law).

Definition: Force is the rate of change of momentum.

Principle of Least Action: A physical system follows the path that minimizes action.
"""

        return papers.get(paper_title, default_paper)

    def process_judgment(self, judgment: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process judgment from Ontology Judge and decide next action.

        Args:
            judgment: Judgment from Judge

        Returns:
            Next action dictionary
        """
        print(f"\n{'='*60}")
        print("MAPPER: Processing judgment")
        print(f"{'='*60}\n")

        judgment_status = judgment.get('judgment', 'UNCERTAIN')

        print(f"Judgment: {judgment_status}")
        print(f"Reasoning: {judgment.get('reasoning', '')}")

        if judgment_status == 'VALID':
            print("\n[SUCCESS] Mapping validated!")
            return {
                'action': 'accept',
                'mapping': judgment
            }

        elif judgment_status == 'INVALID':
            concerns = judgment.get('concerns', [])
            print(f"\n[INVALID] Need to revise mapping")
            print(f"Concerns: {concerns}")
            return {
                'action': 'revise',
                'concerns': concerns,
                'original_mapping': judgment
            }

        else:  # UNCERTAIN
            print(f"\n[UNCERTAIN] Need more data or refinement")
            return {
                'action': 'refine',
                'judgment': judgment
            }

    def run_cycle(self, concept_name: str = "Noether's Theorem"):
        """
        Run single mapping cycle:
        1. Send concept to Synthesizer
        2. Wait for synthesis
        3. Analyze synthesis
        4. Propose Tesseract mapping
        5. Wait for judgment
        6. Process judgment

        Args:
            concept_name: Concept to map
        """
        print(f"\n{'='*60}")
        print(f"MAPPER CYCLE START: {concept_name}")
        print(f"{'='*60}\n")

        # Step 1: Send to Synthesizer
        print("[STEP 1] Sending concept to Synthesizer...")
        self.sync.write_mapping({
            'concept_name': concept_name,
            'timestamp': datetime.now().isoformat()
        })

        # Step 2: Wait for synthesis results
        print("[STEP 2] Waiting for synthesis...")
        synthesis_result = self.sync.wait_for_network(timeout=120)

        # Step 3: Analyze synthesis
        print("[STEP 3] Analyzing synthesis...")
        analysis = self.analyze_synthesis(synthesis_result)

        # Step 4: Propose Tesseract mapping
        print("[STEP 4] Proposing Tesseract mapping...")
        mapping = self.propose_mapping(analysis)

        if mapping.get('status') == 'uncertain':
            print("[UNCERTAIN] Cannot propose mapping from current data")
            return

        # Store in history
        self.mappings_history.append(mapping)

        # Send to Judge
        print("[STEP 6] Sending mapping to Ontology Judge...")
        self.sync.write_mapping(mapping)

        # Step 7: Wait for judgment
        print("[STEP 7] Waiting for judgment...")
        judgment = self.sync.wait_for_judgment(timeout=120)

        # Step 8: Process judgment
        print("[STEP 8] Processing judgment...")
        action = self.process_judgment(judgment)

        print(f"\n{'='*60}")
        print(f"CYCLE COMPLETE: Action = {action.get('action')}")
        print(f"{'='*60}\n")

        return action


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Mapper — Sigma Coordinate Proposer")
    parser.add_argument('--test', action='store_true', help="Run test cycle")
    parser.add_argument('--phenomenon', type=str, default='burst_criticality',
                        help="Phenomenon to map")

    args = parser.parse_args()

    mapper = MapperProtocol()

    if args.test:
        print("Testing Mapper with cycle...")
        mapper.run_cycle(initial_phenomenon=args.phenomenon)

    else:
        print("Usage:")
        print("  python protocol.py --test                              # Test cycle")
        print("  python protocol.py --test --phenomenon stdp_convergence # Test specific phenomenon")
