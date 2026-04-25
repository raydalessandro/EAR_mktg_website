# Context Documents — Loaded ✅

**Date:** 2026-02-08
**Status:** All documents loaded successfully

---

## Ontology Judge Context

**Path:** `ontology_judge/context/`

**AILA Extended (v1.1 - latest):**
- [x] EAR_FORMAL_SYSTEM_AILA_v1_1.md
- [x] EAR_KERNEL_AILA_v1_1.md
- [x] EAR_COHERENCE_AILA_v1_1.md
- [x] EAR_MATRIX_VOCAB_AILA_v1_1.md
- [x] EAR_SCALING_AILA_v1_1.md
- [x] EAR_TRANSITIONS_AILA_v1_1.md

**AILA Base (v1.0):**
- [x] EAR_EMPIRICAL_REFERENCE_AILA_v1.0.md
- [x] EAR_EQUIVALENCES_AILA_v1_0.md
- [x] AILA_LINGUA_v1.0.md

**Total:** 9 documents

**Loading test:**
```bash
cd ontology_judge
python -c "from protocol import OntologyJudgeProtocol; j = OntologyJudgeProtocol()"

Output:
[OK] Loaded AILA_LINGUA_v1.0.md
[OK] Loaded EAR_COHERENCE_AILA_v1_1.md
[OK] Loaded EAR_EMPIRICAL_REFERENCE_AILA_v1.0.md
[OK] Loaded EAR_EQUIVALENCES_AILA_v1_0.md
[OK] Loaded EAR_FORMAL_SYSTEM_AILA_v1_1.md
[OK] Loaded EAR_KERNEL_AILA_v1_1.md
[OK] Loaded EAR_MATRIX_VOCAB_AILA_v1_1.md
[OK] Loaded EAR_SCALING_AILA_v1_1.md
[OK] Loaded EAR_TRANSITIONS_AILA_v1_1.md
```

✅ **All AILA extended docs loaded**

---

## Mapper Context

**Path:** `mapper/context/`

**EAR Base:**
- [x] EAR_NANO_KERNEL_AILA_v1_0.md (ontologia essenziale)

**Neural Phenomena:**
- [x] EAR_Neuronal_Research_Complete_v2.1.md (burst mapping research)

**GRAFO Tesseract (Matrix 72):**
- [x] GRAFO_MATRIX_72.json (72 nodes)
- [x] GRAFO_MATRIX_72_EXPANDED.json (72 nodes expanded)

**Path:** `mapper/context/grafo/`

**Total:** 2 markdown + 2 JSON files

**Loading test:**
```bash
cd mapper
python -c "from protocol import MapperProtocol; m = MapperProtocol()"

Output:
[OK] Loaded EAR_NANO_KERNEL_AILA_v1_0.md
[OK] Loaded EAR_Neuronal_Research_Complete_v2.1.md
[OK] Loaded GRAFO_MATRIX_72.json (72 nodes)
[OK] Loaded GRAFO_MATRIX_72_EXPANDED.json (72 nodes)
```

✅ **Nano Kernel + Neural research + GRAFO loaded**

---

## Network Builder Context

**Path:** `network_builder/context/`

**Status:** Empty (waiting for Brian2 templates)

**TODO (Ray):**
- [ ] Add Brian2 LIF+STDP template
- [ ] Add burst detection code (avalanche analysis)
- [ ] Add STDP convergence code
- [ ] Other neural simulation templates

---

## Document Assignment Rationale

### Ontology Judge = Deep Knowledge
- **9 AILA docs** (FORMAL_SYSTEM, KERNEL, COHERENCE, MATRIX_VOCAB, SCALING, TRANSITIONS, EMPIRICAL_REFERENCE, EQUIVALENCES, LINGUA)
- **Full ontological authority** — can validate deeply against all EAR principles
- **Role:** Final validator, catches subtle errors, ensures coherence

### Mapper = Agile Reasoning
- **Nano Kernel** — essential ontology (axioms, propositions, Δ⇄⟳)
- **GRAFO Tesseract** — can navigate Matrix 72, see existing mappings
- **Neuronal Research** — domain context (burst, STDP, criticality)
- **Role:** Fast proposer, iterates quickly, learns from Judge feedback

### Separation Benefits
1. **Lightweight Mapper** → proposes fast without overthinking
2. **Rigorous Judge** → validates with full ontological depth
3. **Clear feedback loop** → Mapper learns from INVALID judgments
4. **Scalable** → Mapper can handle many phenomena, Judge ensures quality

---

## How Agents Use Context

### Ontology Judge

When validating mapping:
1. Reads proposed Σ coordinate
2. Checks against Matrix 72 structure (MATRIX_VOCAB)
3. Validates dimension/attribute/complexity/polarity (KERNEL)
4. Checks coherence rules (COHERENCE)
5. Verifies transitions if applicable (TRANSITIONS)
6. Emits VALID/INVALID/UNCERTAIN with reasoning from AILA

### Mapper

When proposing mapping:
1. Analyzes network results (tau, spikes, weights)
2. Consults Nano Kernel for Σ structure
3. Looks at GRAFO for similar phenomena patterns
4. Reads neuronal research for domain context
5. Proposes Σ with reasoning
6. Sends to Judge for validation

When processing INVALID judgment:
1. Reads Judge's concerns
2. Adjusts reasoning based on feedback
3. Re-proposes refined Σ
4. Iterates until VALID

---

## Next Steps

### 1. Test with Real Phenomena ✅ Ready

Now that context is loaded, test full cycle:

```bash
cd neural_mapping_agents
python test_flow.py --test cycle
```

Should now use **real AILA docs** for validation instead of placeholder logic.

### 2. Refine Validation Logic

**Ontology Judge:**
- Currently: checks Sigma format + EAR keywords
- **Next:** Use loaded AILA docs to validate dimension/attribute/polarity rules
- **Example:** If phenomenon is Σ₄₂₂₊, verify dimension 4 is correct for criticality

**Mapper:**
- Currently: hardcoded Sigma proposals
- **Next:** Use GRAFO to find similar phenomena, reason analogically
- **Example:** Query GRAFO for nodes with similar metrics, propose Σ based on matches

### 3. Add Brian2 Templates

**Network Builder:**
- Add real simulation code (not dummy numpy)
- LIF network with STDP
- Burst detection (avalanche exponents)
- STDP convergence analysis

---

## Verification Checklist

- [x] AILA extended docs in Judge context
- [x] Nano Kernel in Mapper context
- [x] GRAFO Tesseract JSON in Mapper context
- [x] Neuronal research in Mapper context
- [x] Judge loads 9 AILA docs correctly
- [x] Mapper loads Nano + GRAFO + research correctly
- [x] Protocols updated to load new docs
- [ ] Test cycle with real validation (next step)
- [ ] Refine Judge validation logic (after testing)
- [ ] Refine Mapper proposal logic (after testing)
- [ ] Add Brian2 templates to Builder (Ray)

---

**Status:** Context loading complete ✅
**Ready for:** Real phenomena testing with full AILA validation
