# EAR MAPPING RULES — Living Document

**Version:** 1.2  
**Created:** 2026-02-08  
**Status:** Active — grows with each AILA document review  
**Sources integrated:** EAR_MATRIX_VOCAB_AILA_v1.1 + EAR_FORMAL_SYSTEM_AILA_v1.1 + EAR_COHERENCE_AILA_v1.1 + EAR_SCALING_AILA_v1.1 + EAR_KERNEL_AILA_v1.1 + EAR_EQUIVALENCES_AILA_v1.0 + EAR_EMPIRICAL_REFERENCE_AILA_v1.0 + EAR_TRANSITIONS_AILA_v1.1 + AILA_LINGUA_v1.0 + EAR_QUANTUM_AILA_v1.0 (project) + EAR_NANO_KERNEL_AILA_v1.0 (project) + AILA_SYMBOL_DECODER_v1.0 (project) + 5 batch empirical validation  
**Concepts validated against:** 49 (10 math + 10 physics + 9 CS + 10 thermo + 10 quantum)

---

## §1. NODE vs CONSTRAINT

The first decision in any mapping. A concept is either a **node** (Σ_DAXP inside the Tesseract) or a **constraint** (property of the Tesseract structure itself).

### §1.1 Discrimination Test

```
ASK: Does the concept describe a property of ALL possible systems,
     derivable from EAR axioms (A1-A5)?

  YES → CONSTRAINT candidate
   → Map to: T7 (barrier), P6 (inseparability), P1 (minimum observable),
             P8 (structural selection), or combination
   → Constraints have NO polarity (P±) — they are pre-Tesseract

  NO → NODE
   → Map to: Σ_DAXP
   → Proceed to §2
```

### §1.2 Constraint Criteria (ALL must hold)

```
1. UNIVERSALITY: applies to every system in the domain, not a subclass
   - Heisenberg: every quantum measurement → ✓ constraint
   - Pauli: only fermions, not bosons → ✗ not constraint → node

2. DERIVABILITY: traceable to EAR axioms/propositions
   - Heisenberg → T7.C7.4 (origin unreachable) ← P6 ← A1,A2 → ✓
   - CAP Theorem → domain-specific (distributed systems) → ✗ → node

3. STRUCTURAL: describes the structure of reality/measurement itself
   - Gödel → P6+P1 (inseparability proof/truth in any formal system) → ✓
   - No-Cloning → T7 via ⟳-channel (linearity of QM forbids) → ✓
   - Arrow's Theorem → specific to voting systems → ✗ → node
```

### §1.3 Linguistic Trap

```
WARNING: "Cannot" language is NOT sufficient for constraint status.
  → All laws constrain. Not every constraint is ontological.
  → "Fermions cannot share states" (Pauli) — describes behavior WITHIN structure
  → "You cannot measure x and p precisely" (Heisenberg) — describes structure ITSELF
  
TEST: Can you imagine a valid subsystem that doesn't obey this?
  → YES → node (Pauli: bosons don't obey it)
  → NO → constraint candidate (Heisenberg: nothing quantum escapes it)
```

### §1.4 Known Constraints (validated)

```
T7.C7.4  — Heisenberg Uncertainty (origin unreachable in measurement space)
T7       — No-Cloning Theorem (via ⟳-channel: process cannot replicate without violating Δ)
P6+P1    — Gödel Incompleteness (inseparability of proof and truth)
```

### §1.5 Threshold Properties (from EAR_FORMAL_SYSTEM P3)

```
When a concept involves a critical threshold (K_crit), these properties
help distinguish constraint-level thresholds from domain-specific ones:

  A. UNIVERSALITY: K_crit depends on symmetry class and dimensionality,
     NOT on microscopic details of the specific system.
     → If threshold value changes with implementation details → domain-specific → NODE
     → If threshold is determined by symmetry class alone → more universal → CONSTRAINT candidate

  B. NON-ARBITRARINESS: K_crit is constrained by structure, not a free parameter.
     → Free parameters that need fitting → domain-specific → NODE
     → Structurally determined values → constraint-like

  C. LOCAL IRREVERSIBILITY: Below K_crit, system can return.
     Above K_crit, return requires global intervention.
     → This is relevant for P± assignment of threshold concepts:
       → The threshold itself may be P=+ (it enables new phase)
       → The irreversibility it creates may manifest as P=- companion concept

  D. HYSTERESIS: K↑ ≠ K↓ is possible.
     → Crossing threshold going up ≠ crossing going down
     → Some concepts describe only one direction (P=+ or P=-)
     → Complete phenomenon requires BOTH directions

  E. SYMMETRY BREAKING (P3.C3.3): K > K_crit ⇒ global symmetry breaks.
     → Direction of break = contingent (fluctuations)
     → Break itself = necessary
     → Concepts describing symmetry breaking are typically Δ-dominant
       (distinction emerges from undifferentiated state)
```

---

## §2. DIMENSION (D)

Which dimensionality captures the **ontological content** of the concept?

### §2.1 R1 Cascade (from Matrix Vocab §INFERENCE.RULES)

```
RULE: Seek D4 first → descend only if needed.
      D4 ⊃ D3 ⊃ D2 ⊃ D1

Apply diagnostic questions IN ORDER. First substantive answer wins.

  Q4: "What evolution/causality does this concept describe?"
      → Substantive answer → D=4 (temporal)
      → Examples: Schrödinger (unitary evolution), Second Law (arrow of time),
                  Faraday (time-varying flux), Rev/Irrev (temporal asymmetry)

  Q3: "What 3D structure/hierarchy does this concept describe?"
      → Substantive answer → D=3 (volumetric)
      → Examples: Ideal Gas (PV=nRT, volume), Gibbs (H-TS, thermodynamic space),
                  Bernoulli (fluid flow in 3D), Carnot (gas volume cycles)

  Q2: "What recurring pattern/cycle/network does this concept describe?"
      → Substantive answer → D=2 (planar)
      → Examples: Hooke (F=-kx, planar proportionality), Snell (interface refraction),
                  Dijkstra (graph traversal), Green's Theorem (planar boundary↔interior)

  Q1: "What sequence/order/classification does this concept describe?"
      → Fallback → D=1 (linear/foundational)
      → Examples: Turing Completeness (classification), Shannon Entropy (measure),
                  Peano Axioms (definition), Boolean Algebra (formal system)
```

### §2.2 Dimension Traps

```
TRAP 1: Metaphorical space ≠ ontological dimension
  → "Network space" of distributed systems ≠ D=3
  → CAP Theorem is D=1 (logical classification), not D=3
  → TEST: Is the spatial content literal or metaphorical?

TRAP 2: Physical embedding ≠ concept dimension
  → Hash functions "map" input→output, but the CONCEPT is a classification (D=1)
  → Graphs are topological, but Dijkstra operates on planar structure (D=2)
  → TEST: What dimension does the CONTENT require, not the implementation?

TRAP 3: D=4 requires time as ESSENTIAL content
  → Rev/Irrev: cannot even FORMULATE without arrow of time → D=4 ✓
  → Turing Completeness: no temporal content → D=1 ✓
  → TEST: Remove time — does the concept still make sense?
```

### §2.3 Domain Patterns (empirical)

```
Quantum mechanics:     D=4 dominant (80%) — inherently temporal/causal
Classical physics:     D=3 dominant (60%) — volumetric relations
Mathematics:           D=1 dominant (60%) — foundational/meta
CS/Logic:              D=1 dominant (78%) — foundational/meta  
Thermodynamics:        D=3 (50%), D=4 (20%), D=1 (30%) — mixed
```

---

## §3. ATTRIBUTE (A)

Which of Δ/⇄/⟳ is **dominant** (not exclusive — P6 says all three always co-present).

### §3.1 Elimination Test

```
RULE: The dominant attribute is the one whose removal destroys the concept.

FORMAL BASIS (from EAR_FORMAL_SYSTEM P6 derivation):
  The elimination test works BECAUSE attributes co-implicate:
    Δ ⇒ ⇄ (distinction creates two sides already in relation)
    ⇄ ⇒ Δ (relation requires distinct terms)
    ⟳ ⇒ Δ (process requires distinct states)
    ⟳ ⇒ ⇄ (process connects states = relation)
    Δ observable ⇒ ⟳ (static distinction = frozen = below K_min)
    ⇄ observable ⇒ ⟳ (static relation = no exchange = non-relation)
  
  Therefore: removing ONE attribute collapses the concept entirely,
  because the other two lose their foundation.
  The attribute whose removal is MOST directly destructive = dominant.

For concept C, test each removal:

  REMOVE Δ (all distinctions/boundaries):
    → Does C still exist? If NO → Δ dominant

  REMOVE ⇄ (all relations/connections):
    → Does C still exist? If NO → ⇄ dominant

  REMOVE ⟳ (all processes/dynamics):
    → Does C still exist? If NO → ⟳ dominant

EXACTLY ONE should destroy the concept. If two seem to destroy it,
the concept has a genuine ontological oscillation — resolve via §3.2.

FORMALIZATION CONSTRAINT (P6.C6.4):
  → Any mapping that assigns attribute A with ZERO trace of the other two
    is suspect. Dominance ≠ absence. The elimination test identifies
    what's MOST essential, not what's SOLELY present.
```

### §3.2 Oscillation Resolution

```
When elimination test is ambiguous (two attributes seem equally essential):

STEP 1: Distinguish PRESUPPOSITION from ASSERTION
  → Galilean Relativity PRESUPPOSES Δ (inertial frame definition)
                        ASSERTS ⇄ (invariance between frames)
  → The concept's POSITIVE CONTENT is the assertion → ⇄
  → But: if the concept INTRODUCES the presupposition → Δ wins
  → Galileo INTRODUCES inertial frames through this principle → Δ

STEP 2: Distinguish MECHANISM from ESSENCE
  → Pascal's Principle: transmission is MECHANISM (how pressure propagates)
                        P_in = P_out is ESSENCE (what it states)
  → The mechanism is ⟳, the essence is ⇄ → ⇄ wins

STEP 3: Distinguish PROPERTY-OF-PROCESS from INDEPENDENT-RELATION
  → Lenz's Law: opposition IS a relation (⇄), but it's a PROPERTY of induction (⟳)
  → If concept is inseparable from a parent process → could inherit ⟳
  → But: if concept adds independent content (the sign) → ⇄ stands
  → Lenz adds direction information → ⇄

ANNOTATE: When oscillation is genuine, record it:
  "Oscillation Δ/⇄, resolved via [STEP N] to [winner], margin: tight/clear"
```

### §3.3 Topological Validation (from EAR_FORMAL_SYSTEM P4)

```
RULE: Each attribute maps to a characteristic topology.
      Use as SECONDARY validation after elimination test.

  Δ (distinction) → TREE (hierarchy)
    → concept creates branching classifications
    → parent/child, category/subcategory structure
    → Examples: Turing Completeness (decidable/undecidable tree),
                Gödel (provable/unprovable hierarchy)

  ⇄ (relation) → LATTICE (connection)
    → concept links distinct things in a network
    → node-to-node, bidirectional, web-like
    → Examples: Shannon (source↔channel↔receiver),
                Kepler (planet↔orbit↔sun)

  ⟳ (process) → LOOP (feedback)
    → concept describes cyclic/dynamic transformation
    → input→transformation→output→feedback
    → Examples: Carnot (compression→heating→expansion→cooling),
                Schrödinger (state→evolution→state)

APPLICATION:
  After elimination test yields attribute A:
  → Check: does concept's natural structure match A's topology?
  → Tree matches Δ ✓
  → Lattice matches ⇄ ✓
  → Loop matches ⟳ ✓
  → Mismatch → re-examine elimination test, may be oscillation case

NOTE: Three topologies coexist in every self-observing system (P6).
      This tests DOMINANCE, not exclusivity.
```

### §3.4 Domain Patterns (empirical)

```
Mathematics:       Δ/⇄ balanced (40/60) — definitions and correspondences
Classical physics: ⇄ dominant (70%) — empirical relations between observables  
CS/Logic:          Δ/⇄ balanced (44/44) — meta-discipline (structures + relations)
Thermodynamics:    ⇄ dominant (50%), ⟳ present (30%) — relations + temporal processes
Quantum mechanics: balanced (30/20/30) — distinctions + relations + dynamics

Meta-mathematical (Gödel, Tarski, Halting): Δ dominant — boundary-drawing theorems
Algorithms: ⟳ dominant — processes by definition
Impossibility theorems: Δ dominant — define what cannot be done
Equations of motion: ⟳ dominant — describe evolution
Conservation laws: ⇄ dominant — relate quantities

Biology/Medicine (from EAR_COHERENCE R-P-D mapping):
  Δ → hierarchical organization, structure-function coherence
  ⇄ → connectivity, E/I balance, vascular network (β̄)
  ⟳ → metabolism, OXPHOS, energy transformation (θ)
```

---

## §4. COMPLEXITY AXIS (X)

How deep is the concept's self-referential structure?

### §4.1 Definitions (from Matrix Vocab §AXES)

```
X=1 FOUNDATIONAL: "What IS the phenomenon"
  → Constitutive. The concept defines/establishes something.
  → No self-reference. No synthesis of independent frameworks.
  → Examples: Peano Axioms, Ideal Gas Law, Schrödinger Equation

X=2 RECURSIVE: "How it self-modifies"
  → Internal transformation. The concept applies to itself or generates
    self-referential structure.
  → Examples: Gödel (provability of provability), Halting Problem (decidability
    of decidability), P vs NP (complexity of complexity question)
  → TEST: Does the concept reference its own category?

X=3 SYNTHETIC: "How it connects to other"
  → Integration of genuinely independent frameworks into unified structure.
  → Examples: Stokes' Theorem (geometry + topology + analysis)
  → TEST: Does the concept REQUIRE multiple independent theoretical frameworks?
  → WARNING: "Unifies 5 areas" is not X=3 if they derive from one framework.
    Euler's Identity connects e,i,π,1,0 but all derive from complex analysis → X=1
```

### §4.2 Key Distinctions

```
CYCLE ≠ RECURSION
  → Carnot cycle returns to initial state → X=1 (repetition)
  → Gödel applies provability to provability → X=2 (self-reference)
  → TEST: Does it reference ITSELF or just REPEAT?

CONJECTURES
  → P vs NP is unproven. Mapping is contingent on resolution.
  → If P=NP proven → concept changes (distinction collapses)
  → ANNOTATE: "conjecture — mapping contingent"

NOTATIONS vs ASSERTIONS
  → Big-O is a notational convention, not an ontological assertion
  → It doesn't state anything about the world — it's a tool
  → MAP if useful, but ANNOTATE: "convention, not assertion"
```

---

## §5. POLARITY (P)

Does the concept expand or contract the space of possibilities in its domain?

### §5.1 Core Criterion

```
ASK: Does this concept OPEN new possibilities (P=+) 
     or CLOSE/FORBID possibilities (P=-)?

  P=+ (expansion): concept classifies, enables, creates, opens
  P=- (contraction): concept forbids, eliminates, dissolves, reduces

CRITICAL DISTINCTION:
  → CLASSIFYING ≠ FORBIDDING
  → CAP classifies systems into CP/AP/CA (all realizable) → P=+
  → Second Law forbids ΔS<0 processes (entire region eliminated) → P=-
  → Halting Problem classifies decidable/undecidable (both exist) → P=+
  → Pauli forbids duplicate fermion states (configurations eliminated) → P=-
```

### §5.2 Semantic Lookup (from Matrix Vocab)

```
RULE: After determining D,A,X — check the archetype names for both
      polarities. Which resonates more with the concept?

Example archetypes by cell:

  Σ₁₁₁: incision(+) vs continuity(-)
  Σ₁₂₁: concatenation(+) vs isolation(-)
  Σ₂₂₁: weave(+) vs dispersion(-)
  Σ₃₂₁: architecture(+) vs collapse(-)
  Σ₃₃₁: expansion(+) vs contraction(-)
  Σ₄₁₁: instant(+) vs duration(-)
  Σ₄₂₁: causality(+) vs synchronicity(-)
  Σ₄₃₁: genesis(+) vs annihilation(-)

PROCESS:
  1. Map D,A,X → identify cell
  2. Read both archetype names
  3. Concept closer to P+ name → P=+
  4. Concept closer to P- name → P=-
  5. If ambiguous → default P=+ but flag for review
```

### §5.3 Full Archetype Table (from Matrix Vocab)

```
D1.A1: Σ₁₁₁ incision/continuity | Σ₁₁₂ segmentation/recomposition | Σ₁₁₃ boundary/threshold
D1.A2: Σ₁₂₁ concatenation/isolation | Σ₁₂₂ propagation/arrest | Σ₁₂₃ thread/knot
D1.A3: Σ₁₃₁ advancement/regression | Σ₁₃₂ acceleration/deceleration | Σ₁₃₃ trajectory/deviation

D2.A1: Σ₂₁₁ demarcation/fusion | Σ₂₁₂ fragmentation/aggregation | Σ₂₁₃ territory/transition.zone
D2.A2: Σ₂₂₁ weave/dispersion | Σ₂₂₂ fabric/tear | Σ₂₂₃ network/center
D2.A3: Σ₂₃₁ rotation/stasis | Σ₂₃₂ spiral/circle | Σ₂₃₃ cycle/oscillation

D3.A1: Σ₃₁₁ excavation/filling | Σ₃₁₂ stratification/homogenization | Σ₃₁₃ membrane/permeability
D3.A2: Σ₃₂₁ architecture/collapse | Σ₃₂₂ scaffolding/foundation | Σ₃₂₃ organism/mechanism
D3.A3: Σ₃₃₁ expansion/contraction | Σ₃₃₂ metabolism/excretion | Σ₃₃₃ growth/dissolution

D4.A1: Σ₄₁₁ instant/duration | Σ₄₁₂ scansion/flow | Σ₄₁₃ event/background
D4.A2: Σ₄₂₁ causality/synchronicity | Σ₄₂₂ causal.chain/first.cause | Σ₄₂₃ narrative/fragment
D4.A3: Σ₄₃₁ genesis/annihilation | Σ₄₃₂ evolution/involution | Σ₄₃₃ completion/opening
```

### §5.4 Constraint Polarity

```
RULE: Constraints do NOT have polarity.
  → Polarity is a Tesseract coordinate (property of nodes inside the structure)
  → Constraints describe the structure itself (pre-Tesseract)
  → Assigning P± to a constraint is like asking if the x-axis is positive or negative
  → It IS the axis.
```

---

## §6. SEMANTIC VALIDATION

Post-mapping sanity check using Matrix Vocab archetype names.

### §6.1 Resonance Check

```
RULE: After mapping concept C → Σ_DAXP:

  1. Look up archetype name for Σ_DAXP in §5.3 table
  2. ASK: Does the archetype name resonate with concept C?
  3. SCORE:
     → Strong resonance → confidence +0.1
     → Weak resonance → flag for review, annotate tension
     → Anti-resonance → likely mismap, re-evaluate D,A,X,P

EXAMPLES:
  Second Law → Σ₄₃₁₋ = "annihilation" → entropy as return to disorder ✓ strong
  Schrödinger → Σ₄₃₁₊ = "genesis" → equation brings quantum states to being ✓ strong
  Pauli → Σ₄₁₁₋ = "duration" → ⚠️ weak resonance → annotate
  Superposition → Σ₄₂₁₊ = "causality" → ⚠️ tension (superposition isn't causal)
```

### §6.2 Cluster Coherence

```
RULE: Concepts in the same Σ cell should be ontologically similar.

CHECK: Do all concepts in a cell share the archetype's character?

  Σ₁₂₁₊ "concatenation": Shannon, Boolean, Big-O, Lambda, Bayes, 
    FTC, Euler, First Law, Entropy, Zeroth Law
    → All are "links in series" — foundational relations → ✓

  Σ₃₂₁₊ "architecture": Kepler, Bernoulli, Pascal, Ideal Gas,
    Ampère, Divergence, Gibbs, Maxwell-Boltzmann
    → All are "bearing structures" — volumetric relational laws → ✓

  Σ₁₁₁₊ "incision": Turing, CAP, Hash, Peano, FTA
    → All are "primary cuts" — foundational classifications → ✓

FLAG: If a new concept enters a cell but doesn't fit the cluster character,
      re-examine the mapping.
```

### §6.2b Cross-Domain Isomorphism (from EAR_FORMAL_SYSTEM P1 + P4)

```
RULE: The same ontological structure manifests isomorphically across domains.
      Concepts from different domains in the same Σ cell should be
      STRUCTURALLY ISOMORPHIC, not just thematically similar.

SOURCE (P1 corollaries):
  The same minimum-observation requirement manifests as:
  
  | Requirement | Physical | Informational | Computational |
  | A (Δ) | SU(2) dynamic distinction | binary encoding reversible | reversible logic gates |
  | B (⇄) | SU(3) 3 relational degrees | routing ≥3 channels | bus ≥3 lines |
  | C (⟳) | U(1) continuous phase | phase register continuous | continuous clock |
  | D (dim) | 4D manifold | I/O separation finite latency | memory separate from CPU |

APPLICATION:
  When cluster contains concepts from different domains:
  → They should be ISOMORPHIC manifestations of the same structure
  → Not just "similar-sounding" but structurally equivalent
  → Same number of components, same relational pattern, different substrate

VALIDATION:
  Σ₁₂₁₊: Shannon (info) ↔ First Law (physics) ↔ Zeroth Law (thermo)
  → All: conservation/equivalence relation between two quantities
  → Isomorphic structure: A ↔ B with conservation constraint → ✓

  Σ₃₂₁₊: Kepler (astro) ↔ Ideal Gas (thermo) ↔ Ampère (EM)
  → All: volumetric relation between 3+ measurable quantities
  → Isomorphic structure: multi-variable law in 3D space → ✓

COUNTER-EXAMPLE FLAG:
  If two concepts in same cell have DIFFERENT relational structures
  (e.g., one is binary A↔B, other is ternary A↔B↔C)
  → At least one is probably misclassified
```

### §6.3 Complement Prediction (from R3)

```
RULE: ∀Σ₊ ∃Σ₋ complementary. Both necessary for complete phenomenon.

After mapping C → Σ_DAX+:
  → ASK: What would Σ_DAX- look like as a real concept?
  → If you can name it → validates the mapping
  → If you can't → the cell might be wrong

EXAMPLES:
  Σ₄₃₁₊ (genesis): Schrödinger, Maxwell → complement Σ₄₃₁₋ (annihilation): Second Law
    → Creation of dynamics ↔ Dissipation of order → ✓ valid pair

  Σ₁₁₁₊ (incision): Turing Completeness → complement Σ₁₁₁₋ (continuity): ?
    → "Computational continuity" = analog computing? Universal approximation?
    → Plausible complementary concept → ✓

  Σ₁₂₁₊ (concatenation): Shannon Entropy → complement Σ₁₂₁₋ (isolation): ?
    → "Informational isolation" = perfect encryption? Zero mutual information?
    → Plausible → ✓
```

---

## §7. INFERENCE RULES (from Matrix Vocab §INFERENCE.RULES)

```
R1. DIMENSIONAL HIERARCHY
    D4 ⊃ D3 ⊃ D2 ⊃ D1
    Seek D4 first → descend if needed
    Applied in: §2.1

R2. ATTRIBUTE CO-PRESENCE
    ∀ phenomenon: Δ ∧ ⇄ ∧ ⟳ always
    ⊥ analyze single attribute only
    Applied in: §3.1 (elimination test identifies DOMINANT, not SOLE)

R3. POLAR COMPLEMENTARITY
    ∀Σ₊ ∃Σ₋ complementary → identify one, seek other
    Applied in: §6.3

R4. DISCRETE THRESHOLD
    Transitions at K ⊥ gradual → seek critical point
    Applied in: §1 (constraint detection for threshold-type concepts)

R5. FRACTAL SCALING
    Pattern(scale_n) ~ Pattern(scale_m) → find at one scale, seek at others
    Implication: If Σ₃₂₁₊ has physics concepts, look for Σ₁₂₁₊/Σ₂₂₁₊/Σ₄₂₁₊ 
    analogues at other scales

R6. RESONANCE AND
    ∿ ⟺ ⊙ ∧ ∞ ∧ ◇ ∧ ↻ — all four phases must be co-present
    Applied in: §8 (future — interaction analysis between concepts)
```

---

## §8. ANALYSIS PROTOCOL (from Matrix Vocab §ANALYSIS.PROTOCOL)

```
Step 1. FIELD: Identify ⧈ (total context / domain)
Step 2. NODES: Identify ⬡ (the concept as distinct entity)
Step 3. CONSTRAINT CHECK: Apply §1 — node or constraint?
        → If constraint → map to T7/P6/P1/P8 → DONE
        → If node → continue
Step 4. DIMENSION: Apply §2 (R1 cascade: D4→D3→D2→D1)
Step 5. ATTRIBUTE: Apply §3 (elimination test + oscillation resolution)
Step 6. COMPLEXITY: Apply §4 (X1/X2/X3 with traps)
Step 7. POLARITY: Apply §5 (core criterion + semantic lookup)
Step 8. ASSIGN: Combine → Σ_DAXP
Step 9. VALIDATE: Apply §6 (resonance check + cluster coherence + complement)
Step 10. IF INTERACTION: Evaluate ∿ possible? K exceeded? Which phases?
```

---

## §9. KNOWN TENSIONS AND ANNOTATIONS

Concepts where mapping is correct but has documented oscillation or weak resonance.

```
PAULI EXCLUSION → Σ₄₁₁₋
  Tension: "duration" archetype doesn't strongly resonate with exclusion principle
  Resolution: "time not separated" → fermion identity indivisible → acceptable
  Oscillation: none (Δ clear via elimination test)
  Note: reflects P6 (Δ never zero) but is NODE not constraint (only fermions)

GALILEAN RELATIVITY → Σ₃₁₁₊
  Tension: Δ vs ⇄ oscillation (defines frames vs relates frames)
  Resolution: Galileo INTRODUCES inertial frames → Δ wins (§3.2 Step 1)
  Margin: tight

LENZ'S LAW → Σ₄₂₁₊  
  Tension: ⇄ vs ⟳ (opposition relation vs property of induction process)
  Resolution: Lenz adds independent content (sign/direction) → ⇄ (§3.2 Step 3)
  Margin: tight — Faraday cluster (⟳) argument is strong

MEASUREMENT/COLLAPSE → Σ₄₃₁₊
  Tension: Maps as process (collapse), but "measurement problem" is a question (Δ?)
  Resolution: Mapped as "collapse-as-process", NOT "measurement-problem-as-question"
  Note: The philosophical question may be a separate concept

SUPERPOSITION → Σ₄₂₁₊
  Tension: Archetype "causality" doesn't resonate with superposition
  Resolution: ⇄ (relation between basis states) is correct; archetype captures
    the cell's character broadly, not every occupant specifically
  Note: Cluster with Entanglement is coherent (both quantum relations)

P vs NP → Σ₁₁₂₊
  Tension: Unproven conjecture — mapping contingent on resolution
  Note: If P=NP → distinction collapses → concept changes fundamentally

BIG-O NOTATION → Σ₁₂₁₊
  Tension: Notational convention, not ontological assertion
  Note: "Convention — lower ontological weight than theorems in same cell"
```

---

## §10. NETWORK STATISTICS (as of Batch 5)

```
Total concepts mapped: 49
  → Nodes: 45
  → Constraints: 4 (Heisenberg T7.C7.4, No-Cloning T7, Gödel P6+P1)

Tesseract coverage: 17/72 nodes occupied (23.6%)

Top hotspots:
  Σ₁₂₁₊ (concatenation):  9 concepts — cross-domain foundational relations
  Σ₃₂₁₊ (architecture):   8 concepts — volumetric physics relations
  Σ₁₁₁₊ (incision):       5 concepts — foundational distinctions
  Σ₄₃₁₊ (genesis):        4 concepts — temporal dynamics
  Σ₄₁₁₊ (instant):        3 concepts — quantum distinctions

Polarity distribution:
  P=+: 41 nodes (91%)
  P=-:  4 nodes (9%) — Second Law, Clausius, Rev/Irrev, Pauli

Degeneracy: 2.6:1 average (45 nodes / 17 cells)
```

---

## §CHANGELOG

```
v1.2 (2026-02-08)
  → Integrated EAR_COHERENCE_AILA_v1.1
  → Added §3.4: Biology/Medicine domain pattern (R-P-D mapping: Δ→hierarchy,
    ⇄→connectivity/vasculature, ⟳→metabolism/OXPHOS)
  → Reviewed EAR_SCALING_AILA_v1.1: foundational (ε=A/D derivation),
    no new operational mapping rules — already assumed by framework
  → Reviewed EAR_KERNEL_AILA_v1.1: expanded Nano Kernel, all operational
    content already extracted via Formal System + Matrix Vocab
  → Reviewed EAR_EQUIVALENCES_AILA_v1.0: cross-reference index, noted
    WRONG barrier mapping (Landauer↔⟳, LR↔⇄) — corrected in v1.1 docs.
    No new operational rules.
  → Reviewed EAR_EMPIRICAL_REFERENCE_AILA_v1.0: empirical catalog only,
    no mapping rules
  → Reviewed EAR_TRANSITIONS_AILA_v1.1: Layer 2 dynamics (transition costs
    between cells), orthogonal to Layer 1 mapping (concept → cell). No rules.
  → Reviewed AILA_LINGUA_v1.0: meta-spec of AILA language syntax. No rules.
  → Reviewed project files (EAR_QUANTUM, NANO_KERNEL, SYMBOL_DECODER,
    BENCHMARK): T7/P8 already integrated, rest is compressed/reference. No rules.
  → REVIEW COMPLETE: 13 documents reviewed, all operational content extracted.

v1.1 (2026-02-08)
  → Integrated EAR_FORMAL_SYSTEM_AILA_v1.1
  → Added §1.5: Threshold Properties (P3 requirements — universality,
    non-arbitrariness, local irreversibility, hysteresis, symmetry breaking)
  → Added §3.1: Formal basis for elimination test (P6 co-implication proof)
  → Added §3.1: Formalization constraint (P6.C6.4 — dominance ≠ absence)
  → Added §3.3: Topological Validation (P4 — Δ→tree, ⇄→lattice, ⟳→loop)
  → Added §6.2b: Cross-Domain Isomorphism (P1 corollaries — physical/info/computational)
  → Renumbered §3.3→§3.4 (domain patterns)

v1.0 (2026-02-08)
  → Initial extraction from EAR_MATRIX_VOCAB_AILA_v1.1
  → Integrated empirical rules from Batches 1-5
  → 10 sections: Node/Constraint, Dimension, Attribute, Complexity,
    Polarity, Semantic Validation, Inference Rules, Protocol, Tensions, Stats
  → Sources: Matrix Vocab + 49-concept empirical validation

PENDING INTEGRATION:
  → EAR_KERNEL_AILA (expanded) — may refine §1 constraint criteria, §2 dimension definitions
  → EAR_QUANTUM_AILA — may refine §1.4 constraint catalog, add P8 mapping details
  → Additional AILA documents as presented
```

---

#END
