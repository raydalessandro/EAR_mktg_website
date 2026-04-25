# Neural Mapping Projects — EAR Tesseract

**Due progetti indipendenti per mappare conoscenza su Matrix 72 (Tesseract EAR)**

---

## 📂 Struttura

Questa directory contiene **DUE PROGETTI SEPARATI**:

### 1️⃣ **knowledge_mapping/** — Sistema in Produzione ✅
**Mappa scibile umano (matematica, fisica, CS, etc.) su coordinate Σ**

- **Status:** Attivo, 49 concepts mappati → 17 nodi Tesseract (23.6% coverage)
- **Workflow:** Semi-manuale (Claude synthesis + Mapper automatico + Opus validation)
- **Batches:** Mathematics, Classical Physics, CS/Logic, Thermodynamics, Quantum Mechanics
- **Breakthrough:** Sistema P± (polarity) codificato e validato (10/10 predictions)

📖 **[Vai al README →](knowledge_mapping/README.md)**

---

### 2️⃣ **neural_agents/** — Sistema Sperimentale ⚠️
**Multi-agent automation per mappare fenomeni neurali su coordinate Σ**

- **Status:** Infrastruttura pronta, non ancora in produzione
- **Workflow:** Completamente automatizzato (3 agents loop autonomo)
- **Agents:** Network Builder + Mapper + Ontology Judge
- **Focus:** Neuroscienze computazionali (burst, STDP, LTP, criticality)

📖 **[Vai al README →](neural_agents/README.md)**

---

## 🎯 Differenze Chiave

| Aspetto | knowledge_mapping | neural_agents |
|---------|------------------|---------------|
| **Input** | Concetti scientifici fondamentali | Fenomeni neurali computazionali |
| **Processo** | Semi-manuale (Claude + Opus) | Automatizzato (3 agents autonomi) |
| **Status** | ✅ Produzione (49 concepts) | ⚠️ Sperimentale (infrastructure ready) |
| **Validation** | Opus (LLM oracolo umano-guidato) | Judge agent (AILA-backed autonomo) |
| **Output** | Mapping Σ validati batch-by-batch | Mapping Σ validati in loop autonomo |

---

## 🧠 Design Philosophy

**knowledge_mapping:**
- Focus su **qualità reasoning ontologico**
- Perfezionamento manuale metodologia
- Costruzione knowledge base curato (scibile umano)
- P± system, elimination test, constraint vs node distinction

**neural_agents:**
- Focus su **scala e automazione**
- Applicazione metodologia consolidata
- Mapping massivo fenomeni neurali
- Infrastructure per future expansion

---

## 📋 File Condivisione

**Nessun file condiviso tra i due progetti.**

Ogni progetto ha:
- Propria copia di `mapper/` (versioni possono divergere)
- Propria copia di `concept_synthesizer/` (versioni possono divergere)
- Propri test scripts
- Propri output/results

**Modifica a knowledge_mapping/ NON impatta neural_agents/ e viceversa.**

---

## 🚀 Quick Start

### Lavorare su Knowledge Mapping
```bash
cd knowledge_mapping
cat README.md  # leggi documentazione completa
cd scripts
python map_concepts.py ../batches/batch_6_biology.json
```

### Testare Neural Agents
```bash
cd neural_agents
cat README.md  # leggi documentazione completa
cd tests
python test_flow.py
```

---

## 📊 Stato Globale

**Knowledge Mapping:**
- 49 concepts → 17 nodi (23.6% Tesseract)
- P± system validato (100% accuracy batch 5)
- Prossimo: Derivation rules (domani)

**Neural Agents:**
- Infrastructure completa
- Da implementare: Network Builder, Orchestrator
- In attesa di: Metodologia consolidata da knowledge_mapping

---

**Ultimo update:** 2026-02-08 (riorganizzazione progetti)
**Maintainer:** Claude + Ray (Alessio)
