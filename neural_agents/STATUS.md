# Status — Neural Mapping Agents

**Created:** 2026-02-08
**Status:** Infrastructure Complete ✅
**Tested:** Local flow working ✅

---

## ✅ What Works

### Infrastructure
- [x] FileSync communication layer (tested)
- [x] Network Builder protocol (executes code, reports results)
- [x] Ontology Judge protocol (validates mappings)
- [x] Mapper protocol (analyzes, proposes Σ, iterates)
- [x] Full cycle test (all 3 agents communicating)
- [x] Error handling (timeouts, exceptions)

### Test Results
```
Communication layer: PASSED ✅
Full cycle test: PASSED ✅

Output:
  Phenomenon: burst_criticality
  Proposed Σ: Σ₄₂₂₊
  Judgment: VALID
  Action: accept
```

---

## 🚧 What's Placeholder

### Logic (Needs Refinement)

**Ontology Judge:**
- Currently checks: Sigma format, EAR keywords in reasoning
- Needs: Deep validation against AILA principles, Matrix 72 rules

**Mapper:**
- Currently: Hardcoded Sigma proposals for known phenomena
- Needs: Automatic reasoning from network results to Σ coordinates

**Network Builder:**
- Currently: Dummy numpy simulations
- Needs: Real Brian2 templates (LIF, STDP, burst detection)

### Context (Empty — Ray Populates)

**Ontology Judge:**
- `ontology_judge/context/` — Add ALL AILA docs

**Mapper:**
- `mapper/context/` — Add EAR base + phenomena to map

**Network Builder:**
- `network_builder/context/` — Add Brian2 simulation templates

---

## 🎯 Next Steps

### Phase 1: Context Population (Ray) ⏳

1. **Ontology Judge context:**
   - Copy AILA_MINI (all sections)
   - Copy EAR_NANO_KERNEL
   - Copy Matrix 72 derivation
   - Any other ontology docs

2. **Mapper context:**
   - Write EAR_base.md (Σ system, dimensions, attributes)
   - Write phenomena_to_map.md (burst, STDP, E/I balance, etc.)
   - Write detailed docs for each phenomenon

3. **Network Builder context:**
   - Write Brian2 template for LIF+STDP
   - Write burst detection code (avalanche analysis)
   - Write STDP convergence code

### Phase 2: Logic Refinement (Together) ⏳

1. **Test with real phenomena:**
   - Run cycle on burst_criticality with real data
   - Observe Mapper reasoning
   - Observe Judge validation

2. **Iterate on logic:**
   - Refine Mapper's Σ proposal algorithm
   - Refine Judge's validation criteria
   - Add more phenomena patterns

3. **Build knowledge base:**
   - Store validated mappings
   - Use as reference for future mappings

### Phase 3: Production (When Ready)

1. Run 3 agents in separate terminals
2. Let them cycle autonomously
3. Monitor mappings until VALID
4. Build comprehensive Σ catalog for neural phenomena

---

## 🔧 How to Run Now

### Test Infrastructure

```bash
cd neural_mapping_agents

# Test communication
python test_flow.py --test comm

# Test full cycle (placeholder logic)
python test_flow.py --test cycle
```

### Test Individual Agents

```bash
# Network Builder
cd network_builder
python protocol.py --test

# Ontology Judge
cd ontology_judge
python protocol.py --test

# Mapper
cd mapper
python protocol.py --test
```

---

## 📊 Comparison: Training vs Mapping Agents

| Aspect | Training Agents | Neural Mapping Agents |
|--------|-----------------|------------------------|
| **Goal** | Train LLM ontology-guided | Map phenomena → Σ |
| **Environment** | Drive + Colab (GPU) | Local filesystem |
| **Agents** | Custode, Architetto, Esecutore | Judge, Mapper, Builder |
| **Communication** | DriveSync (remote) | FileSync (local) |
| **Status** | Infrastructure ready | Infrastructure ready ✅ |
| **Next** | Context + Colab test | Context + logic refine |

**Same pattern, different applications.** 🎯

---

## 🐛 Known Issues

### None So Far

All tests passing, communication working, no errors detected.

### Potential Future Issues

- **Brian2 import** — Builder will need Brian2 installed
- **Context loading** — Large AILA docs may need chunking
- **Validation depth** — Judge may need DeepSeek for complex reasoning

---

## 💡 Design Decisions

### Why Local (vs Drive/Colab)?

1. **Simpler for neural work** — no GPU needed for small simulations
2. **Faster iteration** — no cloud latency
3. **Easier debugging** — direct file access
4. **Standalone** — works offline

### Why Same Pattern as Training Agents?

1. **Proven architecture** — file-based communication works
2. **Reusable code** — FileSync ~= DriveSync
3. **Familiar workflow** — Ray knows the pattern
4. **Easy to understand** — same mental model

### Why 3 Agents?

1. **Separation of concerns:**
   - Builder = execution (no interpretation)
   - Judge = ontology (no execution)
   - Mapper = reasoning (no validation)

2. **Clean interfaces:**
   - Each agent has single responsibility
   - Communication via simple JSON files

3. **Debuggable:**
   - Can inspect each agent's output independently
   - Can run agents separately for testing

---

## 📁 File Structure

```
neural_mapping_agents/
├── README.md              ← Overview, usage guide
├── STATUS.md              ← This file (current state)
├── test_flow.py           ← Test suite ✅
│
├── shared/
│   └── file_sync.py       ← Communication layer ✅
│
├── network_builder/
│   ├── protocol.py        ← Executor ✅
│   ├── context/           ← [Empty — Ray adds templates]
│   │   └── README.md
│   ├── output/            ← Simulation results
│   └── logs/              ← Agent logs
│
├── ontology_judge/
│   ├── protocol.py        ← Validator ✅
│   ├── context/           ← [Empty — Ray adds AILA]
│   │   └── README.md
│   ├── output/            ← Judgments
│   └── logs/              ← Agent logs
│
└── mapper/
    ├── protocol.py        ← Proposer ✅
    ├── context/           ← [Empty — Ray adds EAR base]
    │   └── README.md
    ├── output/            ← Mappings
    └── logs/              ← Agent logs
```

---

**Ready for:** Context population → real phenomena testing → logic iteration

**Contact:** Ray when ready to add context docs and refine logic

**Estimated time to production:** 1-2 days after context added


## ✅ UPDATE 2026-02-08: Context Documents Loaded

### Ontology Judge
- 9 AILA extended docs loaded (v1.1 latest)
- FORMAL_SYSTEM, KERNEL, COHERENCE, MATRIX_VOCAB, SCALING, TRANSITIONS
- EMPIRICAL_REFERENCE, EQUIVALENCES, LINGUA

### Mapper  
- EAR_NANO_KERNEL_AILA_v1_0.md
- EAR_Neuronal_Research_Complete_v2.1.md
- GRAFO_MATRIX_72.json + GRAFO_MATRIX_72_EXPANDED.json (72 nodes each)

**See CONTEXT_LOADED.md for details.**

**Status:** Ready for real phenomena testing with full AILA validation! ✅

