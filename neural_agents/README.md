# Neural Mapping Agents — EAR Ontology Automation

**3-Agent System per mappare fenomeni neurali a coordinate Σ (Matrix 72)**

Versione **locale** del sistema training agents — tutto in filesystem, niente Drive/Colab.

---

## 🎯 Obiettivo

Automatizzare il processo di mapping che facevamo manualmente (es. burst criticality):

1. **Network Builder** — Costruisce e simula reti neurali (LIF, STDP, Brian2)
2. **Ontology Judge** — Ha AILA completa, valida proposte ontologicamente
3. **Mapper** — Ha EAR base + docs fenomeni, propone coordinate Σ

Gli agenti **ciclano autonomamente** fino a trovare mapping valido.

---

## 🔄 Workflow

```
MAPPER
  ↓ genera test code (es. LIF+STDP)
  ↓ invia a Builder

NETWORK BUILDER
  ↓ esegue simulazione
  ↓ raccoglie metrics (tau, spikes, weights)
  ↓ invia results a Mapper

MAPPER
  ↓ analizza results
  ↓ propone Σ coordinates
  ↓ invia proposal a Judge

ONTOLOGY JUDGE
  ↓ valida con AILA docs
  ↓ emette judgment (VALID/INVALID/UNCERTAIN)
  ↓ invia a Mapper

MAPPER
  ↓ processa judgment
  ↓ se VALID → accept
  ↓ se INVALID → revise
  ↓ se UNCERTAIN → refine
  ↓ LOOP ↑
```

---

## 📁 Struttura

```
neural_mapping_agents/
├── README.md                  ← Questo file
├── test_flow.py               ← Test suite
│
├── shared/
│   └── file_sync.py           ← Communication layer (locale)
│
├── network_builder/
│   ├── protocol.py            ← Executor reti neurali
│   ├── context/               ← [Templates Brian2]
│   └── output/                ← Simulation results
│
├── ontology_judge/
│   ├── protocol.py            ← Validator ontologico
│   ├── context/               ← [AILA docs completi - Ray]
│   └── output/                ← Judgments history
│
└── mapper/
    ├── protocol.py            ← Proposer Σ coordinates
    ├── context/               ← [EAR base + fenomeni - Ray]
    └── output/                ← Mappings history
```

---

## 🚀 Quick Start

### Test Sistema (Local)

```bash
cd neural_mapping_agents

# Test comunicazione
python test_flow.py --test comm

# Test ciclo completo (placeholder logic)
python test_flow.py --test cycle

# Tutti i test
python test_flow.py --test all
```

**Output atteso:**
- Mapper propone test burst_criticality
- Builder esegue simulazione → tau=1.52
- Mapper analizza → propone Σ₄₂₂₊
- Judge valida → VALID
- Mapper accetta mapping ✅

---

## 🛠️ Setup Context (Ray's Part)

### 1. Ontology Judge Context

Aggiungi **tutti i documenti AILA** in:
```
ontology_judge/context/
├── EAR_NANO_KERNEL_AILA_v1_0.md
├── AILA_MINI (tutte le sezioni)
├── Matrix72_derivation.md
└── ... altri docs ontologici
```

Questi docs saranno caricati in memory del Judge per validazione.

### 2. Mapper Context

Aggiungi **EAR base + fenomeni da mappare**:
```
mapper/context/
├── EAR_base.md                    ← Principi base Matrix 72
├── phenomena_to_map.md            ← Lista fenomeni (burst, STDP, E/I balance, etc.)
├── burst_criticality.md           ← Dettagli fenomeno specifico
└── ... altri fenomeni neurali
```

### 3. Network Builder Templates

Aggiungi **template Brian2** per simulazioni:
```
network_builder/context/
├── LIF_STDP_template.py           ← Template rete LIF con STDP
├── burst_detection.py             ← Codice per analisi avalanche
└── ... altri templates
```

---

## 🔧 Come Funziona (Dettagli)

### Communication Layer (FileSync)

Stessa logica di DriveSync ma locale:

```python
from shared.file_sync import FileSync
sync = FileSync()

# Builder scrive results
sync.write_network_result({'tau': 1.52, 'spikes': 368})

# Mapper legge
results = sync.read_network_result()

# Judge scrive judgment
sync.write_judgment({'judgment': 'VALID', 'reasoning': '...'})

# Mapper legge
judgment = sync.read_judgment()
```

**Markers `.ready`** prevengono race conditions (come DriveSync).

### Network Builder

```python
from network_builder.protocol import NetworkBuilderProtocol

builder = NetworkBuilderProtocol()

# Opzione 1: Test con codice diretto
code = """
import brian2 as b2
# ... simulazione LIF
results = {'tau': 1.52}
"""
builder.execute_and_report(code)

# Opzione 2: Loop automatico (aspetta mapping proposals)
builder.run_loop()
```

### Ontology Judge

```python
from ontology_judge.protocol import OntologyJudgeProtocol

judge = OntologyJudgeProtocol()

# Carica AILA docs da context/
# (Ray popola la cartella)

# Loop: aspetta mapping proposals, valida, emette judgment
judge.run_loop()
```

### Mapper

```python
from mapper.protocol import MapperProtocol

mapper = MapperProtocol()

# Ciclo completo autonomo
mapper.run_cycle(initial_phenomenon='burst_criticality')

# Output:
# - Genera test code
# - Aspetta network results
# - Analizza
# - Propone Σ
# - Aspetta judgment
# - Processa feedback
```

---

## 🧪 Testing

### Test Singoli Protocolli

```bash
# Network Builder
cd network_builder
python protocol.py --test

# Ontology Judge
cd ontology_judge
python protocol.py --test

# Mapper
cd mapper
python protocol.py --test --phenomenon burst_criticality
```

### Test Integrazione

```bash
# Test ciclo completo
python test_flow.py --test cycle
```

---

## 🎛️ Production Usage

### 3 Terminali Separati

**Terminal 1 — Network Builder:**
```bash
cd network_builder
python protocol.py --loop
# Aspetta mapping proposals, esegue simulazioni
```

**Terminal 2 — Ontology Judge:**
```bash
cd ontology_judge
python protocol.py --loop
# Aspetta mapping proposals, valida ontologicamente
```

**Terminal 3 — Mapper:**
```python
cd mapper
python
>>> from protocol import MapperProtocol
>>> mapper = MapperProtocol()
>>> mapper.run_cycle('burst_criticality')
# Ciclo autonomo: propone test, analizza, mappa, valida
```

### O: Singolo Script Orchestrator

**TODO:** Creare `orchestrator.py` che gestisce i 3 agenti in threads/async.

---

## 📊 Example Output

```
MAPPER: Proposing Sigma coordinates
====================================

Phenomenon: burst_criticality
Analysis:
  - Avalanche exponent τ = 1.52
  - Total spikes: 368
  - Near critical value 1.5

Proposed Σ: Σ₄₂₂₊
Reasoning: Criticality (dimension 4) shows temporal process (⟳=2)
           with intermediate complexity, constructive emergence
Confidence: 0.8

====================================
ONTOLOGY JUDGE: Validating mapping
====================================

Phenomenon: burst_criticality
Proposed Σ: Σ₄₂₂₊

Validation:
  ✓ Reasoning uses EAR concepts (Δ, ⇄, ⟳)
  ✓ Sigma format correct
  ✓ Coherent with Matrix 72 structure

JUDGMENT: VALID
Reasoning: Mapping coherent with EAR principles

====================================
MAPPER: Processing judgment
====================================

Judgment: VALID
Next Action: accept

✅ Mapping validated and accepted!
```

---

## 🔍 Cosa È Placeholder vs Production-Ready

### ✅ Production-Ready

- **FileSync communication** — testato, funziona
- **File-based protocol** — markers, timeout, error handling
- **Agent loops** — wait/execute/report cycles
- **Basic validation logic** — checks Sigma format, EAR keywords

### 🚧 Placeholder (Ray Refines)

- **Ontology validation logic** — usa keyword detection, serve logic profonda AILA
- **Network analysis** — guarda solo tau e spikes, serve analisi completa
- **Sigma proposals** — mapping hardcoded, serve reasoning automatico
- **Test code generation** — templates dummy, servono Brian2 reali

---

## 🎯 Next Steps

### 1. Context Population (Ray)

- [ ] Aggiungi AILA docs a `ontology_judge/context/`
- [ ] Aggiungi EAR base + fenomeni a `mapper/context/`
- [ ] Aggiungi template Brian2 a `network_builder/context/`

### 2. Logic Refinement (Insieme)

- [ ] Refine ontology validation (Judge)
- [ ] Refine network analysis (Mapper)
- [ ] Refine Sigma proposals (Mapper)
- [ ] Add real Brian2 simulations (Builder)

### 3. Production Testing

- [ ] Test con fenomeni reali (burst, STDP, E/I balance)
- [ ] Iterate su mappings fino a VALID
- [ ] Build knowledge base di mappings validati

---

## 🆚 vs Training Agents System

| Feature | Training Agents | Neural Mapping |
|---------|-----------------|----------------|
| **Obiettivo** | LLM training ontology-guided | Neural phenomena → Σ mapping |
| **Environment** | Google Drive + Colab (GPU) | Local filesystem only |
| **Agents** | Custode, Architetto, Esecutore | Judge, Mapper, Builder |
| **Output** | Trained model | Validated Σ coordinates |
| **Communication** | DriveSync (Drive files) | FileSync (local files) |

**Pattern identico**, obiettivi diversi.

---

## 📝 Notes

- Sistema **completamente locale** — no cloud, no API, no Drive
- **Autonomo** — cicla senza intervento umano (dopo setup context)
- **Debuggabile** — ogni step scrive file JSON leggibili
- **Estendibile** — facile aggiungere nuovi fenomeni/test

---

**Status:** Infrastructure ready ✅
**Tested:** Communication + full cycle ✅
**Next:** Ray popola context → test con fenomeni reali → iterate logic

**Created:** 2026-02-08
