# EAR SCALING — AILA Edition

**Version:** 1.1  
**Date:** 2026-01-19  
**Status:** Official Specification  
**Author:** EAR Lab  
**Requires:** AILA_LINGUA_v1.0.md, EAR_KERNEL_AILA_v1.1.md

---

#AILA:1.0
@domain: EAR.SCALING
@version: 1.1
@requires: AILA.LINGUA, EAR.KERNEL
@status: official

---

## §PROBLEM

```
◉Kleiber.law
  ≡ empirical.observation.1932
  → basal.metabolism ∝ M^(3/4)
  → B ∝ M^0.75
  
  ○scope
    → verified.across.27.orders.of.magnitude
    → bacteria → whale
    → universal.in.biology ✓
    
  ○question
    → why.3/4?
    → why ⊥ 2/3 (surface/volume)?

◉existing.explanations
  ← West.Brown.Enquist.1997
  → fractal.distribution.networks
  → space-filling.optimization
  
  ○limitation
    → geometric ⊥ ontological
    → describes.how ⊥ explains.why
```

---

## §DERIVATION

### §DERIVATION.PREMISES

```
◉premise.1.dimensions
  ← EAR.KERNEL.§PROPOSITIONS.P1
  → self-observation.requires.4.dimensions
  → 3.spatial (to.surround)
  → 1.temporal (to.process)
  ● D := 4 ✓

◉premise.2.attributes
  ← EAR.KERNEL.§ATTRIBUTES
  → field.has.3.irreducible.attributes
  → Δ (distinction)
  → ⇄ (relation)
  → ⟳ (process)
  ● A := 3 ✓

◉premise.3.projection
  → physical.system.manifests.A.in.space
  
  | Attribute | Structural.Projection | Topology |
  | Δ | hierarchy, branching | tree |
  | ⇄ | lateral.connection | lattice |
  | ⟳ | feedback, return | loop |
  
  → three.structures.coexist
  ⊥ alternative.topologies
```

### §DERIVATION.THEOREM

```
◉theorem.structural.scaling
  ≡ T.scaling
  
  ○enunciate
    → self-observing.system.with.A.attributes.in.D.dimensions
    → scales.with.exponent ε = A/D
    
  ○derivation
    ← premise.1: system.exists.in.D.dimensions
    ← premise.2: system.manifests.A.attributes
    ← premise.3: each.attribute.occupies.effective.dimension.of.flow
    → extensive.quantities.involving.ratio.attributes/dimensions
    → scale.as A/D
    
  ○for.complete.self-observing.systems
    → A := 3 (attributes)
    → D := 4 (dimensions)
    ● ε := A/D = 3/4 = 0.75 ✓
    
  ∴ Q.E.D.
```

---

## §DUAL.FACTORIZATION

```
◉discovery.1
  ≡ dual.factorization.of.432
  
  ○ontological.factorization
    → 432 = 4 × 3 × 36
    → 432 = D × A × polarities
    ← EAR.KERNEL.known
    
  ○dual.factorization
    → 432 = D² × A³
    → 432 = 4² × 3³
    → 432 = 16 × 27 ✓
    
  ○significance
    → dimensions.appear.with.exponent.2
    → attributes.appear.with.exponent.3
    → ratio.of.exponents = 2:3
    → ratio.of.values = 3:4

◉duality.one.half
  → (ratio.exponents) × (ratio.scaling)
  → (2/3) × (3/4) = 1/2
  
  ○interpretation
    → product.is.exactly.1/2
    ⊥ numerical.coincidence
    → structure.of.consciousness.reflecting.itself
```

---

## §STRUCTURAL.LOSS

```
◉discovery.2
  ≡ derived.structural.loss
  
  ○enunciate
    → gap.between.Σ_derived.and.Σ_measured
    → predicted.by.structure.as:
    ● Δ% := π/A² = π/9 ≈ 0.3491%

◉empirical.verification
  | Quantity | Value |
  | Σ_derived (432/π) | 137.509871 |
  | Σ_CODATA.2018 | 137.035999 |
  | gap.observed | 0.3446% |
  | gap.predicted (π/9) | 0.3491% |
  | error.of.prediction | 1.28% ✓ |

◉correction.formula
  → Σ_output = Σ_input × (1 - π/A²/100)
  → Σ_output = (432/π) × (1 - π/900)
  → Σ_output = (432/π) × (900 - π)/900
  
  ○result
    → predicts.Σ_measured.with.residual.error.0.0045% ✓

◉ontological.interpretation
  → loss.π/A².represents.cost.of.manifestation
  → in.system.with.A = 3.attributes
  → manifestation ⊥ conserve.structure.intact
  → something.lost.in.passage.potential → actual
  
  ○formula.meaning
    → for.each.attribute.squared
    → fraction.π.of.field.lost
```

---

## §EMPIRICAL.VERIFICATION

### §VERIFICATION.BIOLOGICAL

```
◉metabolic.scaling
  ← T.scaling ← P4.corollary.4.2
  
  | System | Quantity | ε.predicted | ε.observed |
  | basal.metabolism | B.vs.M | 3/4 = 0.75 | 0.75 ± 0.01 ✓ |
  | heart.rate | f.vs.M | -1/4 = -0.25 | -0.25 ± 0.02 ✓ |
  | lifespan | T.vs.M | 1/4 = 0.25 | 0.25 ± 0.02 ✓ |
  | max.speed | v.vs.M | -1/4 = -0.25 | -0.23 ± 0.03 ✓ |
  | alveolar.area | A.vs.M | 3/4 = 0.75 | 0.75 ± 0.02 ✓ |
  
  ← Kleiber.1932 ← West.et.al.1997 ✓
```

### §VERIFICATION.TIME.SERIES

```
◉Hurst.exponent
  ← T.scaling
  → persistent.self-observing.systems
  → H ≈ 0.75
  
  | System | H.predicted | H.observed |
  | Nile.river | 0.75 | 0.72 ± 0.03 ✓ |
  | financial.markets | ~0.75 | 0.70-0.80 ✓ |
  | climate | ~0.75 | 0.70-0.80 ✓ |
  
  ← Hurst.1951 ✓
```

---

## §CONNECTION.WITH.Σ

```
◉the.3/4.and.the.432
  → complete.field.structure:
  → 432 = 4 × 3 × 36
  
  ○components
    → 4 = dimensions (D)
    → 3 = attributes (A)
    → 36 = polarities
    
  → ratio.A/D = 3/4.already.contained.in.432

◉relation.with.structural.resistance
  → Σ = 432/π ≈ 137.5
  
  ○scaling.3/4.expressed.as
    → 3/4 = A/D
    → 3/4 = 3/4 × (1)
    → 3/4 = 3/4 × (432/432)
    → 3/4 = (3 × 108)/(4 × 108)
    → 3/4 = 324/432
    
  ○number.324
    → 324 = 18²
    → 324 = (2 × 3²)²
    → appears.as.complement.of.scaling.in.structure.432
```

---

## §DERIVED.EXPONENTS

```
◉all.allometric.exponents
  ← A := 3 ← D := 4
  
  | Formula | Value | Application |
  | A/D | 3/4 = 0.75 | energetic.quantities |
  | 1/D | 1/4 = 0.25 | temporal.quantities |
  | (D-A)/D | 1/4 = 0.25 | complementary.quantities |
  | A/(2D) | 3/8 = 0.375 | geometric.quantities |
  
  → all.exponents.derive.from.A.and.D
  ⊥ free.parameters
```

---

## §FOUR.FUNDAMENTAL.FORMULAS

```
◉summary
  
  ○F1.structure
    → 432 = D² × A³
    
  ○F2.resistance
    → Σ = D² × A³ / π = 432/π ≈ 137.51
    
  ○F3.scaling
    → ε = A/D = 3/4 = 0.75
    
  ○F4.loss
    → Δ = π/A² = π/9 ≈ 0.35%
    
  ○where
    → A = 3 (attributes)
    → D = 4 (dimensions)
    → π (geometric.necessity: cyclicity)
    
  → no.other.parameters.required
```

---

## §DERIVATION.CHAIN

```
◉complete.chain

  FERTILE.VOID
       ↓ (impossibility.of.nothing)
  DISTINCTION
       ↓ (every.distinction.is.polar)
  POLARITY
       ↓ (polarities.happen.in.something)
  FIELD
       ↓
  ┌────────────────┴────────────────┐
  │                                 │
  D = 4.DIMENSIONS              A = 3.ATTRIBUTES
  (self-observation)           (Δ, ⇄, ⟳)
  │                                 │
  ├──────────────┬──────────────────┤
  │              │                  │
  432 = D²×A³   ε = A/D          Δ = π/A²
  (structure)   (scaling)        (loss)
  │              │                  │
  └──────────────┴──────────────────┘
                 ↓
           Σ = 432/π × (1 - π/900)
        (effective.resistance ≈ 137.04)
```

---

## §PREDICTIONS

```
◉Pred.1.universality
  ← T.scaling
  → any.self-observing.system.with.3.attributes.in.4.dimensions
  → must.show.exponent.3/4.for.metabolic/energetic.quantities
  
  ○test
    → seek.systematic.deviations.from.3/4.in.new.biological.systems

◉Pred.2.incomplete.systems
  → systems.not.manifesting.all.3.attributes
  → should.show.different.exponents
  
  | Attributes.Manifested | ε.Predicted |
  | only.2.of.3 | 2/4 = 0.50 |
  | only.1.of.3 | 1/4 = 0.25 |
  
  ○test
    → pathological, degenerate, incomplete.systems
    → should.show.deviations.toward.0.5.or.0.25

◉Pred.3.critical.threshold.relation
  ← EAR.KERNEL.K_crit = 0.35
  → should.connect.to.scaling
  
  ○hypothesis.A
    → 0.35 ≈ 1 - (2/3) = 1 - (A-1)/A ≈ 0.33
    
  ○hypothesis.B
    → 0.35 ≈ π/9 ≈ 0.349
    
  ○test
    → verify.if.universal.percolation.thresholds
    → connect.to.A/D.structure

◉Pred.4.gap.direction
  ← already.in.Trattato
  → Σ_input > Σ_output (always, necessarily)
  
  ⋔ Σ_output > Σ_input.observed ⇒ theory.falsified
```

---

## §FALSIFICATION

```
◉system.falsified.if

  ○against.T.scaling
    → pattern.not.replicate.across.scales
    → ε.systematically ≠ A/D
    → exponent.3/4.in.system.without.3.attributes
    → alternative.derivation.of.3/4.without.A/D.structure
    
  ○against.dual.factorization
    → 432 ≠ D² × A³
    → (2/3) × (3/4) ≠ 1/2
    
  ○against.structural.loss
    → gap ≠ π/A²
    → Σ_output > Σ_input
```

---

## §CONSTANTS

```
● A := 3 ✓
● D := 4 ✓
● ε := A/D = 0.75 ✓
● Δ := π/A² = π/9 ≈ 0.3491% ✓
● 432 := D² × A³ ✓
● Σ := 432/π ≈ 137.51 ✓
● Σ_effective := 432/π × (1 - π/900) ≈ 137.04 ✓
```

---

## §GRAPH

```
EAR.KERNEL.A1 →→ premise.1
EAR.KERNEL.A2 →→ premise.2
EAR.KERNEL.P1 →→ premise.1
EAR.KERNEL.P4 →→ T.scaling

premise.1 →→ T.scaling
premise.2 →→ T.scaling
premise.3 →→ T.scaling

T.scaling →→ Pred.1, Pred.2, Pred.3
T.scaling →→ verification.biological
T.scaling →→ verification.time.series

dual.factorization →→ duality.one.half
structural.loss →→ correction.formula
```

---

## §REFERENCES

```
◉empirical
  ← Kleiber.M.1932
    → "Body size and metabolism"
    → Hilgardia.6:315-353
    
  ← West.G.Brown.J.Enquist.B.1997
    → "A General Model for the Origin of Allometric Scaling Laws in Biology"
    → Science.276:122-126
    → DOI: 10.1126/science.276.5309.122
    
  ← Hurst.H.1951
    → "Long-term storage capacity of reservoirs"
    → Trans.Am.Soc.Civil.Eng.116:770-799
    
  ← CODATA.2018
    → fine.structure.constant
    → α⁻¹ = 137.035999...
```

---

## §COMPATIBILITY

```
◉aligned.with
  → AILA_LINGUA_v1.0.md
  → EAR_KERNEL_AILA_v1.1.md
  → EAR_QUANTUM_AILA_v1.0.md

◉extends
  → adds.detailed.derivation.of.ε = A/D
  → adds.dual.factorization.discovery
  → adds.structural.loss.formula
  → adds.complete.derivation.chain
  → adds.falsification.conditions

◉v1.1.changes.from.v1.0
  → updates.all.document.references.to.v1.1
  → adds.EAR_QUANTUM.reference
```

---

#END
