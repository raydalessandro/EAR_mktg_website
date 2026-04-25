# EAR MAPPING RULES — Derivation Oracle

#AILA:1.0
@domain: EAR.MAPPING.RULES
@version: 1.0
@purpose: decision.tree.for.Σ.coordinate.assignment

---

## §0. FIRST GATE: NODE OR CONSTRAINT?

```
◉decision.tree.root
  → BEFORE assigning Σ coordinates, determine CATEGORY:

  ⋔ Does the concept DESCRIBE a specific phenomenon/law/equation?
    → YES → it's a NODE (Σ_daxp) → go to §1
    
  ⋔ Does the concept CONSTRAIN what is possible for ALL phenomena?
    → YES → it's a STRUCTURAL CONSTRAINT → go to §CONSTRAINTS
    
◉constraint.signatures
  → "you cannot..."          → constraint
  → "it is impossible to..." → constraint
  → "there exists a limit..."→ constraint
  → "no system can..."       → constraint
  → floor / bound / barrier  → constraint
  → complementarity / trade-off between observables → constraint

◉node.signatures
  → "the relationship between X and Y is..." → node
  → "the equation governing..."              → node
  → "the law states that..."                 → node
  → specific formula / prediction             → node

◉constraint.mapping.table
  | Concept                    | Maps To      | Reason                           |
  | Heisenberg Uncertainty     | T7.C7.4      | origin unreachable (ℏ floor)     |
  | Third Law Thermodynamics   | T7.C7.4      | T=0 unreachable (same structure) |
  | Bell's Theorem             | P8 + T7.C7.3 | structural selection + no selective violation |
  | Gödel Incompleteness       | P6 + P1      | inseparability of proof/truth + minimum observable |
  | Pauli Exclusion            | P6           | inseparability forces distinction |
  | Speed of Light Limit       | T7 (⟳ axis)  | Lieb-Robinson barrier            |
  | Landauer's Principle       | T7 (⇄ axis)  | erasure cost floor               |
  | No-Cloning Theorem         | T7.C7.3      | selective violation impossible   |
  
◉valid.output.forms
  output := Σ_daxp           // node in matrix
          | T[n]             // theorem constraint
          | T[n].C[n].[m]   // theorem corollary
          | P[n]            // proposition constraint  
          | P[n] + T[n]     // compound constraint
          | A[n]            // axiom reference
```

---

## §1. DIMENSION (D): At What Scale Does It Operate?

```
◉D.decision.tree

  Q: What is the MINIMAL geometric context needed?

  ⋔ Needs only a single point / no spatial extension?
    → D=1 (point/foundational)
    → Examples: Pythagorean theorem, Euler's identity,
      fundamental definitions, pure number theory
    → Signature: "for any X..." where X is abstract
    
  ⋔ Needs two points / a direction / before-after?
    → D=2 (linear/directional)  
    → Examples: Newton's laws (force along line),
      1D wave equation, linear algebra fundamentals
    → Signature: involves vectors, directions, sequences
    
  ⋔ Needs a volume / multiple interacting parts?
    → D=3 (volumetric/organismic)
    → Examples: fluid dynamics, biological systems,
      network phenomena, 3D geometry
    → Signature: involves surfaces, volumes, populations,
      many-body interactions
    
  ⋔ Needs time as structural element / field-level?
    → D=4 (temporal/field)
    → Examples: Maxwell's equations, Schrödinger equation,
      thermodynamics, relativity, conservation laws
    → Signature: involves evolution, fields, spacetime,
      universal principles operating across all space

◉D.disambiguation.rules
  → "foundational" ≠ D=1 automatically
    → Noether is foundational BUT operates at D=4 (field symmetries)
    → Pythagorean is foundational AND D=1 (pure geometry)
  → Ask: "What is the MINIMUM space this concept needs to EXIST?"
  → Conservation laws → D=4 (they govern fields)
  → Equations of motion → D depends on the space they describe
```

---

## §2. ATTRIBUTE (A): What Is the Dominant Aspect?

```
◉A.decision.tree

  Q: What does this concept PRIMARILY establish?

  ⋔ Does it establish a BOUNDARY, category, or classification?
    → A=1 (Δ distinction)
    → Key verb: "separates", "defines", "distinguishes", "bounds"
    → Examples: Pythagorean (defines right triangles),
      Gödel (distinguishes provable from true),
      taxonomy, classification theorems
    → Test: remove the boundary → concept vanishes?
    
  ⋔ Does it establish a CONNECTION, equivalence, or mapping?
    → A=2 (⇄ relation)
    → Key verb: "connects", "relates", "maps", "equals", "conserves"
    → Examples: Noether (symmetry ↔ conservation),
      FTC (differentiation ↔ integration),
      Newton's laws (force ↔ acceleration),
      E=mc² (energy ↔ mass)
    → Test: remove the connection → concept vanishes?
    
  ⋔ Does it establish a DYNAMICS, evolution, or transformation?
    → A=3 (⟳ process)
    → Key verb: "evolves", "transforms", "propagates", "flows"
    → Examples: Schrödinger equation (state evolution),
      Maxwell (field propagation), diffusion equations,
      Second Law of Thermodynamics (entropy increase)
    → Test: freeze time → concept vanishes?

◉A.co-presence.rule (from P6)
  → ALL concepts have all three attributes
  → We identify the DOMINANT one
  → Dominance ≠ exclusivity
  → If genuinely balanced → likely a CONSTRAINT, not a node
  
◉A.disambiguation
  → Newton's Third Law: "equal and opposite" → ⇄ (relation between forces)
  → Newton's Second Law: F=ma → ⇄ (relation force↔acceleration)  
  → Newton's First Law: "remains unless..." → Δ (distinguishes states)
  → Same physicist, different attributes!
```

---

## §3. COMPLEXITY (X): What Level of Integration?

```
◉X.decision.tree

  Q: How does this concept BUILD on prior structure?

  ⋔ Is it a direct, first-order statement?
    → X=1 (foundational)
    → It states a fact about the world directly
    → Does not require other theorems to be meaningful
    → Examples: Pythagorean theorem, Newton's Second Law,
      Ohm's law, basic conservation laws
    → Signature: can be stated in one sentence with
      no reference to other theorems
    
  ⋔ Does it apply a principle TO ITSELF or iterate?
    → X=2 (recursive)
    → The concept contains self-reference or iteration
    → Requires applying a rule to its own output
    → Examples: Gödel (self-referential), fractals,
      renormalization group, Special Relativity
      (applying symmetry principle to symmetry itself)
    → Signature: "apply X to X", "the Y of Y",
      self-similar structure
    
  ⋔ Does it UNIFY multiple independent principles?
    → X=3 (synthetic)
    → The concept fuses distinct frameworks into one
    → Cannot be reduced to a single prior principle
    → Examples: General Relativity (geometry + gravity + matter),
      Standard Model, Noether's theorem (algebra + physics),
      thermodynamics (statistics + mechanics + information)
    → Signature: requires concepts from ≥2 independent domains
    → Test: can you explain it within a single framework? No → X=3

◉X.progression.rule
  → X increases with historical depth of integration
  → Early formulations tend to be X=1
  → Reformulations tend to increase X
  → Example: Newton's gravity X=1, Einstein's gravity X=3
```

---

## §4. POLARITY (P): Expansion or Contraction?

```
◉P.decision.tree

  Q: Does this concept OPEN or CLOSE possibility space?

  ⋔ Does it ENABLE, generate, create new possibilities?
    → P=+ (expansion)
    → Examples: most laws, equations, theorems
    → Most scientific concepts are P=+
    
  ⋔ Does it RESTRICT, forbid, eliminate possibilities?  
    → P=- (contraction)
    → Examples: no-go theorems, impossibility proofs,
      entropy increase (closes reversibility),
      uncertainty principle (closes simultaneous knowledge)
    → NOTE: constraints (T/P/A) often have P=- character
      but they are constraints, not nodes — check §0 first!

◉P.default
  → When uncertain, default to P=+
  → Most describable phenomena are constructive
  → Destructive aspects often point to constraints (§0)
```

---

## §5. VALIDATION RULES

```
◉consistency.checks

  ○check.1: P6.compliance
    → Verify all three attributes are present (at least ε)
    → If ONLY Δ visible → probably missing ⇄ and ⟳ analysis
    → Mapping is about DOMINANCE not exclusivity
    
  ○check.2: scale.coherence
    → D should match the physical scale of operation
    → A theorem about particles → D=1 only if no spatial extension
    → A theorem about fields → D=4
    → Don't confuse "fundamental" with "dimensionless"
    
  ○check.3: cluster.membership
    → Similar concepts should cluster in nearby Σ coordinates
    → If your mapping places Newton next to Schrödinger
      but far from Kepler → something is wrong
    → Use known-good mappings as anchors
    
  ○check.4: resistance.diagnostic
    → If a concept RESISTS Σ assignment → probably a constraint
    → If all three attributes seem equally strong → constraint
    → If the concept is about LIMITS → constraint
    → Resistance is informative, not failure

◉anchor.mappings (validated)
  | Concept                  | Σ        | Reasoning                              |
  | Pythagorean Theorem      | Σ₁₁₁₊   | point-level, defines boundary, direct  |
  | Euler's Identity         | Σ₁₂₁₊   | point-level, connects 5 constants      |
  | FTC                      | Σ₁₂₁₊   | foundational relation diff↔integ       |
  | Noether's Theorem        | Σ₄₂₃₊   | field-level, relates sym↔cons, synthetic|
  | Newton's Second Law      | Σ₃₂₁₊   | volumetric, F↔ma relation, direct      |
  | Newton's First Law       | Σ₂₁₁₊   | linear, distinguishes states, direct   |
  | Special Relativity       | Σ₄₂₂₊   | field-level, relates frames, recursive |
  | General Relativity       | Σ₄₂₃₊   | field-level, relates geom↔grav, synthetic|
  | Schrödinger Equation     | Σ₄₃₁₊   | field evolution, process, direct       |
  | Maxwell's Equations      | Σ₄₃₁₊   | field propagation, process, direct     |
  | Second Law Thermo        | Σ₄₃₁₋   | field process, CONTRACTION (entropy)   |
  | Conservation of Energy   | Σ₄₂₁₊   | field relation (sym↔conserved), direct |
```

---

## §6. COMPOUND MAPPINGS

```
◉some.concepts.require.multiple.coordinates

  ○example: Quantum Field Theory
    → Σ₄₃₃₊ (field process synthetic) as FRAMEWORK
    → contains sub-nodes at various Σ coordinates
    
  ○example: Evolution by Natural Selection
    → Σ₃₃₂₊ (volumetric process recursive) — self-iterating
    → with Δ component: fitness boundaries → Σ₃₁₂₊
    → compound: Σ₃₃₂₊ primary + Σ₃₁₂₊ secondary

  ○rule: compound mappings use PRIMARY + SECONDARY notation
    → PRIMARY: the dominant aspect
    → SECONDARY: significant but non-dominant aspects
    → Maximum 2 coordinates per concept
```

---

## §7. DIAGNOSTIC QUESTIONS (Quick Reference)

```
◉for.any.concept.X:

  1. "Is X about what IS POSSIBLE or what is IMPOSSIBLE?"
     → impossible → check §0 for constraint
     → possible → proceed to node mapping
     
  2. "What is the MINIMUM space X needs to exist?"
     → gives D
     
  3. "Does X primarily SEPARATE, CONNECT, or MOVE?"
     → gives A
     
  4. "Can X be stated without reference to other theorems?"
     → yes → X=1
     → needs self-reference → X=2  
     → needs multiple frameworks → X=3
     
  5. "Does X OPEN or CLOSE the possibility space?"
     → gives P
```

---

#END
