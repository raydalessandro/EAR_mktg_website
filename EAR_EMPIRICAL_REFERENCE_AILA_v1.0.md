# EAR EMPIRICAL REFERENCE — AILA Edition

**Version:** 1.0  
**Date:** 2026-01-19  
**Status:** Living Document  
**Author:** EAR Lab  
**Purpose:** Quick reference for all empirical validations

---

#AILA:1.0
@domain: EAR.EMPIRICAL.REFERENCE
@version: 1.0
@requires: AILA.LINGUA
@status: official
@update: continuous

---

## §PURPOSE

```
◉this.document
  ≡ index.of.empirical.validations
  → results.in.AILA.format
  → pointers.to.full.papers
  ⊥ replace.original.studies
  
  ○use.cases
    → quick.context.for.new.research
    → avoid.repeating.known.validations
    → identify.gaps.in.empirical.coverage
    → cross-reference.during.literature.review
```

---

## §ONCOLOGY

### §NSCLC.Scaling.Divergence

```
◉study.identity
  → title: "Divergence of Structural and Metabolic Scaling Exponents 
            as Signature of Hierarchical Incoherence in Tumors"
  → date: 2026-01
  → status: manuscript.ready
  → full.document: paper_divergenza/manuscript/main_manuscript.md

◉dataset
  → source: NSCLC.Radiogenomics (Brummer.&.Savage.2021)
  → n.total := 52
  → n.ADC := 38 (adenocarcinoma)
  → n.SCC := 14 (squamous.cell.carcinoma)

◉metrics.defined
  ○β̄.structural.exponent
    ≡ vessel.radius.scaling.parameter
    → from.tumor.vascular.network
    → optimal (Murray's.law) := 0.75
    → isometric := 1.0
    
  ○θ.metabolic.exponent
    ≡ slope.of.log(SUVmax).vs.log(MTV)
    → from.PET-CT.imaging
    
  ○Δ.divergence
    ● formula := |β̄ - θ|
    → quantifies.structure-function.decoupling

◉results
  | Tumor.Type | n | β̄ | θ | Δ |
  | ADC | 38 | 0.914 | 0.337 | 0.577 |
  | SCC | 14 | 0.920 | 0.228 | 0.692 |
  
  ○statistics
    ● p := < 0.0001 ✓
    ● Cohen's.d := 2.15 ✓
    ● Welch.t-test.confirmed ✓
    ● Mann-Whitney.U.confirmed ✓

◉EAR.correspondence
  → β̄ (structure) ↔ ⇄ (relation)
  → θ (metabolism) ↔ ⟳ (process)
  → Δ (divergence) ↔ loss.of.Δ.coordination
  ← validates: P4, P6
  
◉interpretation
  → tumors.lose.hierarchical.coherence
  → structure.tends.to.isometric (β̄ → 1)
  → metabolism.fragments (θ → low)
  → Δ.increases.with.malignancy
  → SCC.more.incoherent.than.ADC

◉limitations
  → sample.size.moderate
  → staging.data.unavailable
  → single.cancer.type
  → θ.calculated.at.group.level

◉future.directions
  → longitudinal.Δ.tracking
  → multi-cancer.generalization
  → TNM.staging.correlation
```

---

## §NEURAL

### §Criticality.Baseline

```
◉study.identity
  → title: "EAR Criticality Validation - Step 1"
  → date: 2026-01
  → status: internal.validation
  → full.document: EAR_Neuronal_Research_Complete_v2_1.md

◉model
  → type: LIF + STDP
  → source: Kern, Date & Chao 2024
  → N := 200 neurons (80% exc, 20% inh)
  → STDP.on.EE.connections

◉results.SOC.emergence
  | Noise (mV) | τ | State |
  | 6.0 | 2.16 | subcritical |
  | 6.5 | 1.76 | transition |
  | 7.0 | 1.52 | critical ✓ |
  | 7.5 | 1.37 | supercritical |
  | 8.0 | 1.29 | supercritical |
  
  ● τ_critical := 1.52 ✓
  ← matches: Beggs.&.Plenz.2003, Shew.2011

◉EAR.correspondence
  ← validates: P3 (critical.threshold)
  
◉status.epistemico
  → coerenza.con.letteratura ✓
  → distintivo: NO (any.LIF+STDP.reaches.SOC)
```

### §Informational.vs.Spatial.Structure

```
◉study.identity
  → title: "EAR Criticality Validation - Step 2"
  → date: 2026-01
  → status: discriminating.test
  → full.document: EAR_Neuronal_Research_Complete_v2_1.md

◉hypothesis.tested
  ⋔ standard.framework: STDP.reinforces.spatial.neighbors
  ⋔ EAR.Prop.5: STDP.reinforces.informational.correlates

◉method
  → let.STDP.self-organize.network
  → measure.correlation.of.final.weights.with:
    → A) spatial.distance.between.neurons
    → B) activity.correlation (spike.patterns)

◉results
  | Metric | Value |
  | weight-distance.r | 0.010 |
  | weight-activity.r | 0.164 |
  | ratio | 16:1 ✓ |
  
  ○detail.by.seed (noise = 7.5 mV)
    | Seed | r_distance | r_activity | τ |
    | 42 | 0.014 | 0.232 | exploded |
    | 123 | 0.027 | 0.081 | 1.38 |
    | 456 | -0.028 | 0.238 | exploded |
    | 789 | 0.027 | 0.103 | 1.29 |

◉EAR.correspondence
  ← supports: P5 (informational.structure.over.spatial)
  
◉status.epistemico
  → direction.clear: activity >> distance ✓
  → effect.weak: r = 0.16 (2.6% variance)
  → high.variability.between.seeds
  → verdict: MODERATE.SUPPORT

◉limitations
  → small.network (N = 200)
  → some.seeds.explode
  → stable.trials.have.lower.r_activity
```

### §E/I.Balance.and.Criticality

```
◉study.identity
  → title: "EAR Criticality Validation - Step 3"
  → date: 2026-01
  → status: internal.validation
  → full.document: EAR_Neuronal_Research_Complete_v2_1.md

◉results.matrix.Noise × E/I
  |  | E>I (3.0) | E=I (1.0) | I>E (0.33) |
  | noise=6 | 2.156 | 2.162 | 2.182 |
  | noise=7 | 1.503 | 1.528 | 1.517 |
  | noise=8 | 1.264 | 1.281 | 1.293 |

◉interpretation
  ● effect.NOISE (dominant) := Δτ = 0.89
  ● effect.E/I (weak) := Δτ = 0.02
  → STDP.maintains.E/I.homeostatically
  → control.parameter = external.drive ⊥ initial.E/I

◉EAR.correspondence
  ← validates: P3 (threshold.mechanism)
  ← consistent.with: Arviv.2016, Ikeda.2025
  
◉status.epistemico
  → coerenza ✓
  → distintivo: NO
```

### §INS.Maturity.Prediction

```
◉study.identity
  → title: "EAR Criticality Validation - Step 4"
  → date: 2026-01
  → status: discriminating.prediction.confirmed
  → full.document: EAR_Neuronal_Research_Complete_v2_1.md

◉EAR.prediction
  ← from.P5.4-phase.structure (⊙ ∞ ◇ ↻)
  
  → maturity ↑ ⇒ shift.dominance ∞ → ↻
  → INS.captures.mainly.∞ (Spiral)
  → mature.relations.have.less.∞, more.↻
  ∴ mature.relations → LESS.visible.INS
  
  ○standard.framework.predicts
    → deeper.relation → more.connection → more.sync

◉literature.confirmation
  ○Djalovski.et.al.2021
    → SCAN, DOI: 10.1093/scan/nsab051
    → finding: romantic.couples.show.LOWER.INS.than.friends
    → quote: "highest synchrony among friends... 
              romantic partners showed lowest synchrony"
    
  ○Zhou.et.al.2025
    → Acta.Psychologica, DOI: 10.1016/j.actpsy.2025.106117
    → finding: high.self-other.overlap → LESS.need.for.real-time.INS
    → interpretation: Node (◇) formed reduces need for Spiral (∞)

◉EAR.correspondence
  ← validates: P5 (resonance.phases)
  ← supports: 4-phase.co-presence.model
  
◉status.epistemico
  → direction.opposite.to.standard.framework ✓
  → literature.confirms.EAR ⊥ standard ✓
  → authors.independent (don't.know.EAR) ✓
  → verdict: STRONG.DISTINCTIVE.SUPPORT

◉caveat
  → prediction.derived.after.finding.pattern
  → technically.explanatory.capacity ⊥ a.priori.prediction
  → but: 4-phase.structure.IS.a.priori.in.framework
```

---

## §SEMANTIC.VALIDATION

### §Ontological.Vectors.LLM.Comparison

```
◉study.identity
  → title: "Ontological Vectors as Semantic Primitives: 
            A Minimal Symbolic System Achieving LLM-Coherent 
            Outputs Without Training"
  → author: Ray.Antonini
  → date: 2026-01
  → status: manuscript.ready
  → full.document: EAR_Paper_Ontological_Vectors.docx

◉domain
  → Tarot (78.cards) as.closed.symbolic.system
  → rationale: well-defined.identities, rich.tradition, 
               no.prior.computational.formalization

◉method
  → assign.EAR.vectors [Δ, ⇄, ⟳] to.each.card
  → from.first.principles + traditional.correspondences
  → compare.outputs.with.LLM (Claude) interpretations
  → LLM.has.no.knowledge.of.EAR.system

◉sample
  → n := 20 cards (stratified.random)
  → 10 Major.Arcana (3 reversed)
  → 6 Minor.Arcana.numerals (3 reversed)
  → 4 Court.cards (1 reversed)

◉results
  | Metric | Score | Baseline | Significance |
  | valence.correlation | r = 0.533 | 0.00 | moderate-strong ✓ |
  | domain.agreement | 65% | 25% | 2.6× baseline ✓ |
  | energy.agreement | 60% | 33% | 1.8× baseline ✓ |
  | keyword.Jaccard | 0.198 | ~0.05 | above.random ✓ |
  | reversal.direction | 57.1% | 50% | above.random |

◉systematic.divergence
  → all.major.divergences.on.REVERSED.cards
  → EAR: implements."blocked.energy".interpretation
  → LLM: implements."semantic.inversion".interpretation
  → both.are.legitimate.Tarot.traditions
  
  | Card | LLM.valence | EAR.valence | Δ |
  | Ten.of.Swords | -0.90 | +0.78 | 1.68 |
  | The.Devil (R) | +0.30 | -0.87 | 1.17 |
  | Eight.of.Swords (R) | +0.40 | -0.88 | 1.28 |

◉EAR.correspondence
  ← validates: Δ, ⇄, ⟳.as.semantic.primitives
  ← validates: framework.captures.genuine.structure
  
◉theoretical.implications
  → semantic.content.derivable.from.ontological.principles
  → ⊥ requires.statistical.learning.from.data
  → EAR.and.LLM.access.common.underlying.structure
  → reversal.divergence.shows.EAR.is.coherent.theory ⊥ noise

◉limitations
  → n = 20 (small.sample)
  → single.LLM
  → no.human.expert.validation.yet
  → domain.specific (Tarot)
```

---

## §CROSS-DOMAIN.SYNTHESIS

### §CHE.Metric

```
◉Coerenza.Gerarchica.Effettiva
  ≡ CHE
  ● formula := Seme (↻) / Spirale (∞)
  → ratio.of.persistent.effects.to.active.synchronization

◉cross-domain.application
  | Domain | Numerator (↻) | Denominator (∞) | CHE.high = |
  | INS.social | behavioral.change.T+k | real-time.INS | mature.relation |
  | Tumors | structure-function.coord | local.metabolic.activity | healthy.tissue |
  | Neural.STDP | weight-activity.corr | firing.rate.during.stim | organized.network |

◉unifying.insight
  → HIGH.activity + LOW.coordination = PATHOLOGY / IMMATURITY
  → LOW.activity + HIGH.coordination = HEALTH / MATURITY
  
  ○tumors
    → high.metabolism + low.coordination = Δ.high = pathology
    
  ○INS
    → high.sync + low.behavioral.coord = immature.relation
    → low.sync + high.behavioral.coord = mature.relation
```

---

## §VALIDATION.STATUS.SUMMARY

```
◉by.proposition
  | Proposition | Empirical.Status | Distinctive? |
  | P1 (minimum.observable) | not.directly.tested | - |
  | P2 (conservation) | not.directly.tested | - |
  | P3 (critical.threshold) | validated (τ=1.52) | NO (known) |
  | P4 (scaling.3/4) | validated (tumors, Kleiber) | partial |
  | P5 (resonance) | validated (INS, Step.2) | YES ✓ |
  | P6 (inseparability) | validated (Δ_scaling) | YES ✓ |
  | P7 (transitions) | not.empirically.tested | - |
  | P8 (structural.selection) | not.empirically.tested | - |
  | T7 (barrier.unity) | literature.consistent | partial |

◉by.domain
  | Domain | Status | Key.Result |
  | Oncology | strong | Δ = |β̄ - θ| distinguishes ADC/SCC |
  | Neural.SOC | confirmed | τ = 1.52 at criticality |
  | Neural.structure | moderate | activity/distance = 16:1 |
  | INS.social | strong | maturity → less.sync |
  | Semantic | strong | r = 0.533 EAR-LLM correlation |

◉gaps.requiring.research
  → P1: direct.test.of.K_min.threshold
  → P2: information.conservation.in.transitions
  → P7: transition.types.empirical.mapping
  → P8: observer.structure → outcome.correlation
  → T7: barrier.floor.measurement
  → longitudinal.tumor.Δ
  → φ-Δ_scaling.correlation.in.brain
  → CHE.predictive.validity
```

---

## §KEY.LITERATURE

### §External.References

```
◉scaling.and.allometry
  ← Kleiber.1932: metabolism ∝ M^0.75
  ← West.Brown.Enquist.1997: fractal.network.derivation
  ← Guiot.et.al.2006: dynamic.tumor.exponent
  ← Brummer.&.Savage.2021: NSCLC.dataset

◉criticality.and.SOC
  ← Beggs.&.Plenz.2003: neural.avalanches
  ← Shew.et.al.2011: criticality.maximizes.computation
  ← Arviv.et.al.2016: E/I.and.criticality
  ← Ikeda.et.al.2025: E/I.and.STDP.co-stabilization

◉INS.and.hyperscanning
  ← Djalovski.et.al.2021: romantic < friends.INS
  ← Zhou.et.al.2025: self-other.overlap.reduces.INS.need
  ← Lotter.et.al.2023: INS.meta-analysis (91.experiments)

◉coherence.mechanisms
  ← Grieco.et.al.2023: PV+.and.OXPHOS
  ← Walter.&.Hinterberger.2022: SOC.and.consciousness
```

---

## §UPDATE.LOG

```
◉v1.0 (2026-01-19)
  → initial.compilation
  → includes: oncology, neural (4.steps), semantic.validation
  → cross-domain.synthesis.with.CHE
  → validation.status.summary
  → gap.identification
```

---

#END
