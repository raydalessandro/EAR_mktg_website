#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mapper Protocol v2.1 — Ontological Sigma Coordinate Proposer

CHANGES from v2.0:
- §2 FIX: attribute_dominant is a weighted vote (+3), NOT an oracle early-return
- §2 ADD: concept-type priors (law/equation + evolution keywords → ⟳ bonus)
- §2 ADD: PRIMARY-marked structures get +3, non-primary get +1
- §1 FIX: explicit D=N extraction from dimension_hints
- §1 FIX: concept_type → dimension priors (law → D≥3, field theory → D=4)

Implements MAPPING_RULES.md decision tree for EAR Tesseract coordinate assignment.
"""

import re
import sys
import json

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple, Union
from dataclasses import dataclass, field, asdict
from enum import Enum

# Add shared to path
sys.path.insert(0, str(Path(__file__).parent.parent / "shared"))

try:
    from file_sync import FileSync
except ImportError:
    class FileSync:
        def write_mapping(self, d): pass
        def wait_for_network(self, timeout=120): return {}
        def wait_for_judgment(self, timeout=120): return {}


# ============================================================
# §0. ONTOLOGICAL CATEGORY: NODE vs CONSTRAINT
# ============================================================

class OntologicalCategory(Enum):
    NODE = "node"
    CONSTRAINT = "constraint"
    COMPOUND = "compound"


CONSTRAINT_SIGNALS = {
    'impossible', 'cannot', 'forbidden', 'no system can',
    'it is impossible', 'there exists a limit', 'unreachable',
    'you cannot simultaneously', 'no-go', 'exclusion',
    'floor', 'bound', 'barrier', 'ceiling', 'limit',
    'complementarity', 'trade-off', 'uncertainty principle',
    'incompleteness', 'undecidable', 'no-cloning',
    'inseparability', 'origin unreachable', 'selective violation',
}

KNOWN_CONSTRAINTS = {
    'heisenberg uncertainty':      'T7.C7.4',
    'uncertainty principle':       'T7.C7.4',
    'third law thermodynamics':    'T7.C7.4',
    'absolute zero':               'T7.C7.4',
    'bell theorem':                'P8 + T7.C7.3',
    'bell inequality':             'P8 + T7.C7.3',
    'gödel incompleteness':        'P6 + P1',
    'goedel incompleteness':       'P6 + P1',
    # 'pauli exclusion':           'P6',  # REMOVED: Pauli is a node (Σ411₊), not constraint
    'speed of light limit':        'T7.⟳',
    'no-cloning theorem':          'T7.C7.3',
    'no cloning':                  'T7.C7.3',
    'landauer principle':          'T7.⇄',
    'landauer limit':              'T7.⇄',
    'lieb-robinson bound':         'T7.⟳',
    'wigner-araki-yanase':         'T7.Δ',
}


# ============================================================
# §1-4. SIGNAL DICTIONARIES
# ============================================================

# --- DIMENSION signals ---
D1_SIGNALS = {
    'pure geometry', 'number theory', 'abstract algebra',
    'definition', 'identity', 'for any', 'for all',
    'euclidean', 'metric space', 'axiomatic',
    'meta-principle', 'mathematical identity',
}

D2_SIGNALS = {
    'vector', 'direction', 'force along', 'one-dimensional',
    'sequence', 'linear', 'trajectory', 'ray', 'line',
    'before and after', 'inertia',
}

D3_SIGNALS = {
    'volume', 'surface', 'organism', 'population', 'network',
    'fluid', 'many-body', 'three-dimensional', '3d', 'bulk',
    'biological', 'statistical', 'ensemble', 'gas', 'pressure',
    'volumetric',
}

D4_SIGNALS = {
    'field', 'spacetime', 'evolution', 'propagation', 'wave',
    'conservation', 'symmetry', 'universal', 'covariant',
    'lagrangian', 'hamiltonian', 'action', 'entropy',
    'electromagnetic', 'quantum', 'relativistic', 'gauge',
    'thermodynamic', 'cosmological', 'temporal',
}

# --- ATTRIBUTE signals ---
A_DELTA_SIGNALS = {
    'separates', 'defines', 'distinguishes', 'bounds',
    'classifies', 'categorizes', 'boundary', 'partition',
    'taxonomy', 'discrete', 'either...or', 'divides',
    'necessary condition', 'sufficient condition',
    'identity',
}

A_REL_SIGNALS = {
    'connects', 'relates', 'maps', 'equals', 'conserves',
    'equivalence', 'correspondence', 'isomorphism', 'duality',
    'if and only if', 'between', 'mutual', 'reciprocal',
    'proportion', 'ratio', 'balance', 'symmetry',
    'bidirectional', 'inverse operations',
}

A_PROC_SIGNALS = {
    'evolves', 'transforms', 'propagates', 'flows', 'grows',
    'decays', 'oscillates', 'diffuses', 'radiates', 'moves',
    'dynamic', 'kinetic', 'rate of change', 'derivative',
    'differential equation', 'time-dependent', 'irreversible',
    'temporal evolution', 'time evolution', 'arrow of time',
    'wave equation', 'propagation',
}

# --- COMPLEXITY signals ---
X2_SIGNALS = {
    'self-referential', 'recursive', 'fractal', 'self-similar',
    'renormalization', 'iteration', 'feedback', 'bootstrap',
    'applies to itself', 'meta-',
}

X3_SIGNALS = {
    'unifies', 'synthesizes', 'fuses', 'combines',
    'from multiple domains', 'interdisciplinary',
    'geometry and gravity', 'statistics and mechanics',
    'algebra and physics', 'information and thermodynamics',
}


# ============================================================
# DATACLASSES
# ============================================================

@dataclass
class SigmaCoordinate:
    D: int
    A: int
    X: int
    P: str

    def __str__(self):
        pol = '₊' if self.P == '+' else '₋'
        return f'Σ{self.D}{self.A}{self.X}{pol}'

    def to_dict(self):
        return {'D': self.D, 'A': self.A, 'X': self.X, 'P': self.P,
                'notation': str(self)}


@dataclass
class ConstraintRef:
    references: List[str]
    reason: str
    forced_sigma: Optional[SigmaCoordinate] = None

    def __str__(self):
        return ' + '.join(self.references)

    def to_dict(self):
        d = {'references': self.references, 'reason': self.reason,
             'notation': str(self)}
        if self.forced_sigma:
            d['forced_sigma'] = self.forced_sigma.to_dict()
        return d


@dataclass
class MappingProposal:
    concept_name: str
    category: OntologicalCategory
    coordinate: Union[SigmaCoordinate, ConstraintRef]
    reasoning: Dict[str, str]
    confidence: float
    secondary: Optional[SigmaCoordinate] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        d = {
            'concept_name': self.concept_name,
            'category': self.category.value,
            'coordinate': self.coordinate.to_dict(),
            'notation': str(self.coordinate),
            'reasoning': self.reasoning,
            'confidence': self.confidence,
            'timestamp': self.timestamp,
        }
        if self.secondary:
            d['secondary'] = self.secondary.to_dict()
        return d


# ============================================================
# MAPPER ENGINE
# ============================================================

class MapperProtocol:
    """
    Mapper v2.1 — Ontological coordinate proposer.

    Key change: Synthesizer hints are VOTES, not oracles.
    All axes use weighted scoring with multiple evidence sources.
    """

    def __init__(self, context_path: Optional[str] = None):
        self.context_path = context_path or Path(__file__).parent / "context"
        self.sync = FileSync()
        self.history: List[MappingProposal] = []

        # Anchor mappings for cluster validation (§5)
        self.anchors = {
            'pythagorean theorem':     SigmaCoordinate(1, 1, 1, '+'),
            'euler identity':          SigmaCoordinate(1, 2, 1, '+'),
            'ftc':                     SigmaCoordinate(1, 2, 1, '+'),
            'fundamental theorem calculus': SigmaCoordinate(1, 2, 1, '+'),
            'noether theorem':         SigmaCoordinate(4, 2, 3, '+'),
            'newton second law':       SigmaCoordinate(3, 2, 1, '+'),
            'newton first law':        SigmaCoordinate(2, 1, 1, '+'),
            'hooke law':               SigmaCoordinate(2, 2, 1, '+'),
            'pauli exclusion':         SigmaCoordinate(4, 1, 1, '+'),
            'shannon theorem':         SigmaCoordinate(4, 2, 1, '+'),
            'halting problem':         SigmaCoordinate(1, 1, 2, '+'),
            'special relativity':      SigmaCoordinate(4, 2, 2, '+'),
            'general relativity':      SigmaCoordinate(4, 2, 3, '+'),
            'schrödinger equation':    SigmaCoordinate(4, 3, 1, '+'),
            'maxwell equations':       SigmaCoordinate(4, 3, 1, '+'),
            'second law thermodynamics': SigmaCoordinate(4, 3, 1, '-'),
            'conservation of energy':  SigmaCoordinate(4, 2, 1, '+'),
        }

    # --------------------------------------------------------
    # §0. FIRST GATE: NODE OR CONSTRAINT?
    # --------------------------------------------------------

    def classify_category(self, concept: str, text: str,
                          synthesis: Dict[str, Any]) -> Tuple[OntologicalCategory, Optional[str]]:
        """§0: Node vs Constraint classification."""
        concept_lower = concept.lower().strip()
        text_lower = text.lower() if text else ''
        combined = f"{concept_lower} {text_lower}"

        # Check known constraints first
        for key, ref in KNOWN_CONSTRAINTS.items():
            if key in concept_lower:
                return OntologicalCategory.CONSTRAINT, key

        # Check synthesis ontological_status
        ont_status = str(synthesis.get('ontological_status', '')).lower()
        if any(tag in ont_status for tag in ['t7', 'p6', 'p8', 'constraint', 'threshold']):
            return OntologicalCategory.CONSTRAINT, None

        # Check constraint signals in text
        constraint_score = 0
        for signal in CONSTRAINT_SIGNALS:
            if signal in combined:
                constraint_score += 1

        concept_type = str(synthesis.get('concept_type', '')).lower()
        if concept_type == 'threshold':
            constraint_score += 3

        if constraint_score >= 3:
            return OntologicalCategory.CONSTRAINT, None

        return OntologicalCategory.NODE, None

    # --------------------------------------------------------
    # §1. DIMENSION (D) — FIXED: explicit D=N extraction
    # --------------------------------------------------------

    def derive_dimension(self, text: str, synthesis: Dict[str, Any]) -> Tuple[int, str]:
        """
        §1: Derive dimension.
        
        Priority:
        1. Explicit D=N in dimension_hints (highest trust)
        2. Signal scoring from text + hints combined
        3. Concept type heuristic fallback
        """
        text_lower = text.lower() if text else ''
        hints = str(synthesis.get('dimension_hints', '')).lower()
        combined = f"{text_lower} {hints}"

        # --- Priority 1: Extract explicit D=N from hints ---
        # Matches patterns like "D=4", "D=1 (foundational)", etc.
        d_match = re.search(r'd\s*=\s*(\d)', hints)
        if d_match:
            explicit_d = int(d_match.group(1))
            if 1 <= explicit_d <= 4:
                return explicit_d, f"D={explicit_d}: explicit from synthesis dimension_hints"

        # Also match "Field level (4)", "Point/Line level (1-2)" etc.
        level_match = re.search(r'(?:level|type)\s*\((\d)', hints)
        if level_match:
            explicit_d = int(level_match.group(1))
            if 1 <= explicit_d <= 4:
                return explicit_d, f"D={explicit_d}: extracted from synthesis level hint"

        # --- Priority 2: Signal scoring ---
        scores = {1: 0, 2: 0, 3: 0, 4: 0}

        for signal in D1_SIGNALS:
            if signal in combined:
                scores[1] += 1
        for signal in D2_SIGNALS:
            if signal in combined:
                scores[2] += 1
        for signal in D3_SIGNALS:
            if signal in combined:
                scores[3] += 1
        for signal in D4_SIGNALS:
            if signal in combined:
                scores[4] += 1

        # --- Concept-type priors ---
        concept_type = str(synthesis.get('concept_type', '')).lower()
        if concept_type in ('law', 'theory') and scores[4] >= 1:
            scores[4] += 2  # Laws/theories with ANY field signal → strong D=4 boost

        best_d = max(scores, key=scores.get)
        best_score = scores[best_d]

        # --- Priority 3: Fallback ---
        if best_score == 0:
            if concept_type in ('law', 'theory'):
                best_d = 4
            elif concept_type == 'theorem':
                best_d = 1
            else:
                best_d = 1

        d_names = {1: 'point/foundational', 2: 'linear/directional',
                   3: 'volumetric/organismic', 4: 'temporal/field'}
        reason = f"D={best_d} ({d_names[best_d]}): scores {scores}"

        return best_d, reason

    # --------------------------------------------------------
    # §2. ATTRIBUTE (A) — FIXED: no early return, weighted voting
    # --------------------------------------------------------

    def derive_attribute(self, text: str, synthesis: Dict[str, Any]) -> Tuple[int, str]:
        """
        §2: Derive dominant attribute (1=Δ, 2=⇄, 3=⟳).
        
        THREE evidence sources, all contribute votes:
        1. Text signal scoring (+1 per keyword match)
        2. Synthesis attribute_dominant (+3 vote, NOT oracle)
        3. Synthesis ontological_structures (PRIMARY: +3, non-primary: +1)
        4. Concept-type priors (law/equation + evolution → ⟳ bonus)
        """
        text_lower = text.lower() if text else ''

        scores = {1: 0, 2: 0, 3: 0}  # Δ, ⇄, ⟳

        # --- Source 1: Text signal scoring ---
        for signal in A_DELTA_SIGNALS:
            if signal in text_lower:
                scores[1] += 1
        for signal in A_REL_SIGNALS:
            if signal in text_lower:
                scores[2] += 1
        for signal in A_PROC_SIGNALS:
            if signal in text_lower:
                scores[3] += 1

        # --- Source 2: Synthesis attribute_dominant (VOTE, not oracle) ---
        dominant = str(synthesis.get('attribute_dominant', ''))
        dominant_raw = synthesis.get('attribute_dominant', '')

        SYNTH_DOMINANT_WEIGHT = 3

        if 'Δ' in str(dominant_raw) or 'δ' in dominant.lower():
            # Only count as Δ if NOT marked trans-attributo
            if 'trans' not in dominant.lower():
                scores[1] += SYNTH_DOMINANT_WEIGHT
        if '⇄' in str(dominant_raw):
            scores[2] += SYNTH_DOMINANT_WEIGHT
        if '⟳' in str(dominant_raw):
            scores[3] += SYNTH_DOMINANT_WEIGHT

        # --- Source 3: Ontological structures (PRIMARY-weighted) ---
        for struct in synthesis.get('ontological_structures', []):
            pattern = str(struct.get('pattern', ''))
            is_primary = struct.get('primary', False)
            weight = 3 if is_primary else 1

            if 'Δ' in pattern and 'Δ⇄⟳' not in pattern:
                scores[1] += weight
            if '⇄' in pattern and 'Δ⇄⟳' not in pattern:
                scores[2] += weight
            if '⟳' in pattern and 'Δ⇄⟳' not in pattern:
                scores[3] += weight

        # --- Source 4: Concept-type priors ---
        concept_type = str(synthesis.get('concept_type', '')).lower()

        # Laws/equations with evolution language → ⟳ gets bonus
        evolution_keywords = {
            'evolution', 'propagat', 'time-dependent', 'dynamic',
            'irreversible', 'arrow of time', 'wave equation',
            'temporal', '∂/∂t', '∂ψ/∂t',
        }
        formal = str(synthesis.get('formal_statement', '')).lower()
        combined_text = f"{text_lower} {formal}"

        if concept_type in ('law', 'equation'):
            evolution_hits = sum(1 for kw in evolution_keywords if kw in combined_text)
            if evolution_hits >= 1:
                scores[3] += 2  # Process bonus for dynamic laws

        # Identity/theorem with static character → Δ gets bonus
        static_keywords = {'identity', 'defines', 'static', 'a² + b²', 'if and only if'}
        if concept_type == 'theorem':
            static_hits = sum(1 for kw in static_keywords if kw in combined_text)
            if static_hits >= 1:
                scores[1] += 1

        # --- Winner ---
        best_a = max(scores, key=scores.get)
        if scores[best_a] == 0:
            best_a = 2  # Default to relation

        a_names = {1: 'Δ distinction', 2: '⇄ relation', 3: '⟳ process'}
        reason = (f"A={best_a} ({a_names[best_a]}): "
                  f"scores Δ={scores[1]}, ⇄={scores[2]}, ⟳={scores[3]}")

        return best_a, reason

    # --------------------------------------------------------
    # §3. COMPLEXITY (X)
    # --------------------------------------------------------

    def derive_complexity(self, text: str, synthesis: Dict[str, Any]) -> Tuple[int, str]:
        """§3: Derive complexity (1=foundational, 2=recursive, 3=synthetic)."""
        text_lower = text.lower() if text else ''

        # Check explicit hint from synthesis
        hint = str(synthesis.get('complexity', '')).lower()

        # Extract explicit X=N
        x_match = re.search(r'(\d)', hint)
        if x_match:
            val = int(x_match.group(1))
            if val in (1, 2, 3):
                label = {1: 'foundational', 2: 'recursive', 3: 'synthetic'}[val]
                return val, f"X={val} ({label}): explicit from synthesis"

        if 'synthetic' in hint:
            return 3, "X=3 (synthetic): explicit from synthesis"
        if 'recursive' in hint:
            return 2, "X=2 (recursive): explicit from synthesis"
        if 'foundational' in hint:
            return 1, "X=1 (foundational): explicit from synthesis"

        # Signal scoring
        x3_score = sum(1 for s in X3_SIGNALS if s in text_lower)
        x2_score = sum(1 for s in X2_SIGNALS if s in text_lower)

        if x3_score >= 2:
            return 3, f"X=3 (synthetic): {x3_score} unification signals"
        if x2_score >= 1:
            return 2, f"X=2 (recursive): {x2_score} self-reference signals"

        # Framework domain counting (tools vs frameworks)
        framework_domains = set()
        fw_keywords = {
            'gravity': 'gravity', 'gravitational': 'gravity',
            'mechanics': 'mechanics', 'force': 'mechanics',
            'momentum': 'mechanics', 'acceleration': 'mechanics',
            'thermodynamics': 'thermo', 'entropy': 'thermo',
            'heat': 'thermo', 'temperature': 'thermo',
            'quantum': 'quantum', 'wave function': 'quantum',
            'planck': 'quantum', 'superposition': 'quantum',
            'electromagnetic': 'em', 'maxwell': 'em',
            'radiation': 'em', 'electric': 'em', 'magnetic': 'em',
            'geometry': 'geometry', 'curvature': 'geometry',
            'manifold': 'geometry', 'metric': 'geometry',
            'information': 'info', 'computation': 'info',
            'biology': 'bio', 'organism': 'bio',
            'conservation': 'conservation', 'conserved': 'conservation',
            'symmetry': 'symmetry',
            'algebra': 'algebra',
        }

        for kw, domain in fw_keywords.items():
            if kw in text_lower:
                framework_domains.add(domain)

        n = len(framework_domains)

        if n >= 3 or (n >= 2 and x3_score >= 1):
            return 3, f"X=3 (synthetic): {n} framework domains: {framework_domains}"
        if n == 2 and x2_score == 0:
            return 2, f"X=2: spans {n} frameworks: {framework_domains}"

        return 1, "X=1 (foundational): single framework, direct statement"

    # --------------------------------------------------------
    # §4. POLARITY (P)
    # --------------------------------------------------------

    def derive_polarity(self, text: str, synthesis: Dict[str, Any]) -> Tuple[str, str]:
        """§4: Derive polarity (+ expansion, - contraction).

        Priority:
        1. Explicit polarity hint in synthesis
        2. Signal-based detection (contraction keywords)
        3. Default P=+
        """
        # PRIORITY 1: Check synthesis for explicit polarity hint
        if synthesis and 'polarity' in synthesis:
            hint = synthesis['polarity']
            if isinstance(hint, str):
                hint_clean = hint.strip().lower()

                # Extract +/- from hint (e.g., "- (contraction ...)" or "+ (expansion ...)")
                if hint_clean.startswith('-') or 'contraction' in hint_clean[:30]:
                    return '-', f"P=- (contraction): explicit synthesis hint: {hint[:80]}"
                elif hint_clean.startswith('+') or 'expansion' in hint_clean[:30]:
                    return '+', f"P=+ (expansion): explicit synthesis hint: {hint[:80]}"

        # PRIORITY 2: Signal-based detection
        text_lower = text.lower() if text else ''

        contraction_signals = {
            'irreversible', 'entropy increase', 'decay', 'dissipation',
            'forbidden', 'impossible', 'restriction', 'loss', 'decoherence',
            'no-go', 'exclusion', 'decrease', 'collapse', 'never decreases',
            'eliminates', 'vieta', 'forbids', 'cannot',
        }

        contraction_score = sum(1 for s in contraction_signals if s in text_lower)

        if contraction_score >= 2:
            return '-', f"P=- (contraction): {contraction_score} restriction signals"

        # PRIORITY 3: Default
        return '+', "P=+ (expansion): default, constructive concept"

    # --------------------------------------------------------
    # §5. VALIDATION
    # --------------------------------------------------------

    def validate_proposal(self, proposal: MappingProposal) -> List[str]:
        """§5: Run consistency checks."""
        warnings = []

        if proposal.category != OntologicalCategory.NODE:
            return warnings

        coord = proposal.coordinate
        if not isinstance(coord, SigmaCoordinate):
            return warnings

        if coord.D not in (1, 2, 3, 4):
            warnings.append(f"D={coord.D} out of range [1,4]")
        if coord.A not in (1, 2, 3):
            warnings.append(f"A={coord.A} out of range [1,3]")
        if coord.X not in (1, 2, 3):
            warnings.append(f"X={coord.X} out of range [1,3]")

        # Cluster coherence with anchors
        concept_key = proposal.concept_name.lower().strip()
        for anchor_name, anchor_coord in self.anchors.items():
            if self._concepts_related(concept_key, anchor_name):
                distance = (abs(coord.D - anchor_coord.D) +
                           abs(coord.A - anchor_coord.A) +
                           abs(coord.X - anchor_coord.X))
                if distance > 4:
                    warnings.append(
                        f"Far from related anchor '{anchor_name}' "
                        f"({anchor_coord}): distance={distance}"
                    )

        return warnings

    def _concepts_related(self, a: str, b: str) -> bool:
        stop_words = {'the', 'of', 'a', 'an', 'in', 'on', 'for', 'and',
                      'theorem', 'law', 'principle', 'equation', 'theory',
                      'first', 'second', 'third', 'fundamental'}
        words_a = set(a.split()) - stop_words
        words_b = set(b.split()) - stop_words
        return bool(words_a & words_b)

    # --------------------------------------------------------
    # MAIN PIPELINE
    # --------------------------------------------------------

    def propose_mapping(self, concept_name: str, text: str = '',
                        synthesis: Optional[Dict[str, Any]] = None) -> MappingProposal:
        """Full mapping pipeline: §0 → §1-4 → §5."""
        synthesis = synthesis or {}
        reasoning = {}

        print(f"\n{'='*60}")
        print(f"MAPPER v2.1: Mapping '{concept_name}'")
        print(f"{'='*60}\n")

        # §0: NODE or CONSTRAINT?
        category, constraint_key = self.classify_category(
            concept_name, text, synthesis
        )

        if category == OntologicalCategory.CONSTRAINT:
            if constraint_key and constraint_key in KNOWN_CONSTRAINTS:
                ref = KNOWN_CONSTRAINTS[constraint_key]
                refs = [r.strip() for r in ref.split('+')]
            else:
                refs = self._derive_constraint_refs(text, synthesis)

            reasoning['§0'] = f"CONSTRAINT detected (key={constraint_key})"

            coordinate = ConstraintRef(
                references=refs,
                reason=f"Structural constraint, not a tesseract node",
                forced_sigma=SigmaCoordinate(4, 3, 3, '+')
            )

            proposal = MappingProposal(
                concept_name=concept_name,
                category=category,
                coordinate=coordinate,
                reasoning=reasoning,
                confidence=0.9 if constraint_key else 0.6,
            )

            print(f"  §0: CONSTRAINT → {coordinate}")

        else:
            # §1-4: Derive coordinates
            D, d_reason = self.derive_dimension(text, synthesis)
            reasoning['§1_dimension'] = d_reason
            print(f"  §1: {d_reason}")

            A, a_reason = self.derive_attribute(text, synthesis)
            reasoning['§2_attribute'] = a_reason
            print(f"  §2: {a_reason}")

            X, x_reason = self.derive_complexity(text, synthesis)
            reasoning['§3_complexity'] = x_reason
            print(f"  §3: {x_reason}")

            P, p_reason = self.derive_polarity(text, synthesis)
            reasoning['§4_polarity'] = p_reason
            print(f"  §4: {p_reason}")

            coordinate = SigmaCoordinate(D, A, X, P)
            confidence = self._calculate_confidence(reasoning)

            proposal = MappingProposal(
                concept_name=concept_name,
                category=category,
                coordinate=coordinate,
                reasoning=reasoning,
                confidence=confidence,
            )

            # §5: Validation
            warnings = self.validate_proposal(proposal)
            if warnings:
                reasoning['§5_warnings'] = '; '.join(warnings)
                proposal.confidence *= 0.7
                for w in warnings:
                    print(f"  ⚠️  {w}")

            print(f"\n  → RESULT: {coordinate} (confidence: {proposal.confidence:.2f})")

        self.history.append(proposal)
        return proposal

    def _derive_constraint_refs(self, text: str, synthesis: Dict) -> List[str]:
        """Derive constraint references when no known match exists."""
        text_lower = (text or '').lower()
        ont_status = str(synthesis.get('ontological_status', '')).lower()
        combined = f"{text_lower} {ont_status}"
        refs = []

        # Extract T/P references from ontological_status
        tp_match = re.findall(r'[tp]\d+(?:\.[cp]\d+(?:\.\d+)?)?', ont_status, re.IGNORECASE)
        if tp_match:
            refs.extend([m.upper() for m in tp_match])

        if not refs:
            if any(w in combined for w in ['barrier', 'limit', 'floor', 'bound']):
                refs.append('T7')
            if any(w in combined for w in ['observer', 'measurement', 'context']):
                refs.append('P8')
            if any(w in combined for w in ['inseparable', 'complementary', 'cannot separate']):
                refs.append('P6')
            if any(w in combined for w in ['threshold', 'phase transition', 'critical']):
                refs.append('P3')

        return refs if refs else ['UNKNOWN_CONSTRAINT']

    def _calculate_confidence(self, reasoning: Dict[str, str]) -> float:
        """Calculate confidence from reasoning quality."""
        confidence = 0.5

        for key, reason in reasoning.items():
            if key.startswith('§'):
                if 'explicit from synthesis' in reason.lower():
                    confidence += 0.15
                elif 'scores' in reason:
                    confidence += 0.08

        return min(confidence, 1.0)

    # --------------------------------------------------------
    # JUDGMENT PROCESSING
    # --------------------------------------------------------

    def process_judgment(self, judgment: Dict[str, Any]) -> Dict[str, Any]:
        status = judgment.get('judgment', 'UNCERTAIN')

        print(f"\n{'='*60}")
        print(f"MAPPER: Judgment received: {status}")
        print(f"{'='*60}\n")

        if status == 'VALID':
            print("[✓] Mapping validated!")
            return {'action': 'accept', 'mapping': judgment}
        elif status == 'INVALID':
            concerns = judgment.get('concerns', [])
            suggestions = judgment.get('suggestions', [])
            print(f"[✗] Invalid — concerns: {concerns}")
            return {'action': 'revise', 'concerns': concerns, 'suggestions': suggestions}
        else:
            return {'action': 'refine', 'judgment': judgment}

    # --------------------------------------------------------
    # BATCH PROCESSING
    # --------------------------------------------------------

    def map_batch(self, concepts: List[Dict[str, str]]) -> List[MappingProposal]:
        results = []
        for c in concepts:
            proposal = self.propose_mapping(
                concept_name=c['name'],
                text=c.get('text', ''),
                synthesis=c.get('synthesis', {}),
            )
            results.append(proposal)
        return results

    def summary_table(self) -> str:
        lines = [
            f"{'Concept':<35} {'Category':<12} {'Coordinate':<15} {'Confidence':<10}",
            '-' * 75,
        ]
        for p in self.history:
            lines.append(
                f"{p.concept_name:<35} {p.category.value:<12} "
                f"{str(p.coordinate):<15} {p.confidence:<10.2f}"
            )
        return '\n'.join(lines)


# ============================================================
# INTEGRATED TEST: Synthesizer + Mapper
# ============================================================

# Expected results table
EXPECTED = {
    'pythagorean theorem':              ('node', 'Σ1₁₁₊', 'Σ111₊'),
    'fundamental theorem of calculus':  ('node', 'Σ1₂₁₊', 'Σ121₊'),
    "noether's theorem":                ('node', 'Σ4₂₃₊', 'Σ423₊'),
    "maxwell's equations":              ('node', 'Σ4₃₁₊', 'Σ431₊'),
    'schrödinger equation':             ('node', 'Σ4₃₁₊', 'Σ431₊'),
    'second law of thermodynamics':     ('node', 'Σ4₃₁₋', 'Σ431₋'),
    'heisenberg uncertainty principle':  ('constraint', 'T7.C7.4', None),
    "newton's laws":                    ('node', 'Σ3₂₁₊', 'Σ321₊'),
    'special relativity':               ('node', 'Σ4₂₂₊', 'Σ422₊'),
    'general relativity':               ('node', 'Σ4₂₃₊', 'Σ423₊'),
    'conservation of energy':           ('node', 'Σ4₂₁₊', 'Σ421₊'),
    "gödel's incompleteness theorems":  ('constraint', 'P6 + P1', None),
}


def normalize_sigma(s):
    """Normalize Σ notation for comparison."""
    sub_map = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')
    return s.translate(sub_map)


def run_integrated_test():
    """Run Synthesizer → Mapper integrated test."""
    from pathlib import Path

    # Import synthesizer
    sys.path.insert(0, str(Path(__file__).parent))
    try:
        # Try importing from same directory
        from synthesizer_v2 import ConceptSynthesizerProtocol
    except ImportError:
        # Inline minimal synthesizer for standalone test
        print("[WARN] synthesizer_v2 not found, using mapper-only test")
        run_mapper_only_test()
        return

    synth = ConceptSynthesizerProtocol()
    mapper = MapperProtocol()

    print(f"\n{'='*70}")
    print(f"  INTEGRATED TEST: Synthesizer v2 → Mapper v2.1")
    print(f"{'='*70}")

    correct = 0
    total = len(EXPECTED)

    for concept_name, (exp_cat, exp_coord, exp_norm) in EXPECTED.items():
        # Synthesize
        result = synth.synthesize_concept(concept_name)
        synthesis = result.get('synthesis', {})

        # Build text from synthesis
        text = synthesis.get('formal_statement', '')
        elim = synthesis.get('elimination_test', '')
        text_full = f"{text}. {elim}"

        # Map
        proposal = mapper.propose_mapping(concept_name, text_full, synthesis)

        # Check
        actual_str = str(proposal.coordinate)
        actual_norm = normalize_sigma(actual_str)

        if exp_cat == 'constraint':
            match = isinstance(proposal.coordinate, ConstraintRef) and \
                    any(exp_coord in r or r in exp_coord
                        for r in proposal.coordinate.references)
        else:
            match = (exp_norm and actual_norm == normalize_sigma(exp_norm))

        status = '✅' if match else '❌'
        if match:
            correct += 1

        print(f"\n  {status} {concept_name}")
        print(f"     Expected: {exp_coord}")
        print(f"     Got:      {actual_str}")
        if not match:
            print(f"     Reasoning: {json.dumps(proposal.reasoning, indent=6, ensure_ascii=False)}")

    accuracy = correct / total * 100
    print(f"\n{'='*70}")
    print(f"  RESULTS: {correct}/{total} ({accuracy:.0f}%)")
    print(f"{'='*70}")
    print(f"\n{mapper.summary_table()}")


def run_mapper_only_test():
    """Run mapper-only test with handcrafted text (v2.0 compatible)."""
    TEST_CONCEPTS = [
        {'name': 'Pythagorean Theorem',
         'text': 'a² + b² = c². Defines the fundamental metric identity in Euclidean geometry. Pure axiomatic boundary.',
         'expected': 'Σ111₊'},
        {'name': 'Fundamental Theorem of Calculus',
         'text': 'Connects differentiation and integration as inverse operations. Bidirectional correspondence. Meta-principle of calculus.',
         'expected': 'Σ121₊'},
        {'name': "Noether's Theorem",
         'text': 'Every differentiable symmetry of the action corresponds to a conservation law. Unifies algebra, geometry, and physics across spacetime.',
         'expected': 'Σ423₊'},
        {'name': "Newton's Second Law",
         'text': 'Force equals mass times acceleration. Relates force to the rate of change of momentum in volumetric three-dimensional space.',
         'expected': 'Σ321₊'},
        {'name': 'Schrödinger Equation',
         'text': 'Describes the temporal evolution of the quantum state. Wave equation propagating the wavefunction through spacetime field.',
         'expected': 'Σ431₊'},
        {'name': 'Heisenberg Uncertainty Principle',
         'text': 'It is impossible to simultaneously know with arbitrary precision both position and momentum. Fundamental limit: ΔxΔp ≥ ℏ/2. Origin unreachable.',
         'expected': 'T7.C7.4'},
        {'name': 'Second Law of Thermodynamics',
         'text': 'Entropy of an isolated system never decreases. Irreversible process. Arrow of time. Dissipation and decay are universal field-level phenomena.',
         'expected': 'Σ431₋'},
        {'name': 'General Relativity',
         'text': 'Unifies geometry and gravity and matter. Spacetime curvature relates to energy-momentum. Combines differential geometry with gravitational physics into a covariant field theory.',
         'expected': 'Σ423₊'},
    ]

    mapper = MapperProtocol()
    correct = 0
    total = len(TEST_CONCEPTS)

    print(f"\n{'='*70}")
    print(f"  MAPPER v2.1 — MAPPER-ONLY TEST BATTERY ({total} concepts)")
    print(f"{'='*70}")

    for tc in TEST_CONCEPTS:
        proposal = mapper.propose_mapping(tc['name'], tc['text'])
        actual = normalize_sigma(str(proposal.coordinate))
        expected = normalize_sigma(tc['expected'])

        if isinstance(proposal.coordinate, ConstraintRef):
            match = any(tc['expected'] in r for r in proposal.coordinate.references)
        else:
            match = actual == expected

        status = '✅' if match else '❌'
        if match:
            correct += 1

        print(f"\n  {status} {tc['name']}")
        print(f"     Expected: {tc['expected']}")
        print(f"     Got:      {str(proposal.coordinate)}")
        if not match:
            print(f"     Reasoning: {proposal.reasoning}")

    accuracy = correct / total * 100
    print(f"\n{'='*70}")
    print(f"  RESULTS: {correct}/{total} ({accuracy:.0f}%)")
    print(f"{'='*70}")
    print(f"\n{mapper.summary_table()}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Mapper v2.1 — Ontological Sigma Proposer")
    parser.add_argument('--test', action='store_true', help="Run mapper-only test")
    parser.add_argument('--integrated', action='store_true', help="Run synthesizer+mapper test")
    parser.add_argument('--concept', type=str, help="Map a single concept")
    parser.add_argument('--text', type=str, default='', help="Concept description text")

    args = parser.parse_args()

    if args.integrated:
        run_integrated_test()
    elif args.test:
        run_mapper_only_test()
    elif args.concept:
        mapper = MapperProtocol()
        proposal = mapper.propose_mapping(args.concept, args.text)
        print(json.dumps(proposal.to_dict(), indent=2, ensure_ascii=False))
    else:
        print("Usage:")
        print("  python protocol_v2_1.py --test          # Mapper-only test")
        print("  python protocol_v2_1.py --integrated    # Full pipeline test")
        print("  python protocol_v2_1.py --concept 'X' --text '...'")
