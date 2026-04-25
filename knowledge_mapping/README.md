# Knowledge Mapping System — EAR Tesseract

**Sistema per mappare scibile umano (matematica, fisica, CS, etc.) su Matrix 72 (Tesseract EAR)**

---

## 🎯 Obiettivo

Mappare concetti scientifici/matematici fondamentali su coordinate Σ del Tesseract:
- **D** (Dimension): 1-4 (Δ distinction, ⇄ relation, ⟳ process, Σ composite)
- **A** (Attribute): 1-3 (temporality, spatiality, causality)
- **X** (Complexity): 1-3 (atomic, systemic, emergent)
- **P** (Polarity): +/- (expansion/contraction)

**Esempio:** Second Law of Thermodynamics → Σ₄₃₃₋ (composite, causal, emergent, contraction)

---

## 📊 Status

**49 concetti mappati** → **17 nodi Tesseract** (23.6% coverage)

### Batches completati:
1. **Mathematics** (10 concepts) — batch_1_mathematics.json
2. **Classical Physics** (10 concepts) — batch_2_classical_physics.json
3. **CS/Logic** (9 concepts) — batch_3_cs_logic.json
4. **Thermodynamics** (10 concepts) — batch_4_thermodynamics.json ⚡ introduce P=-
5. **Quantum Mechanics** (10 concepts) — batch_5_quantum.json ⚡ 10/10 P± predictions

### Hotspots (nodi più popolati):
- **Σ₁₂₁₊** (9 concepts) — Relational-spatial-atomic tools (metrics, constraints)
- **Σ₃₂₁₊** (8 concepts) — Process-spatial-atomic evolution (dynamics, flows)
- **Σ₁₁₁₊** (5 concepts) — Distinction-temporal-atomic foundations (existence, identity)

---

## 🔄 Workflow

### 1. SYNTHESIS (manuale)
Io (Claude) scrivo synthesis JSON con:
- `concept_name`: Nome concetto
- `ontological_content`: Descrizione ontologica ricca
- `polarity`: P=+ (expansion/classifica) o P=- (contraction/vieta)
- `elimination_test`: Test rimozione attributo dominante
- `examples`: Istanze concrete

**Guideline:** `docs/SYNTHESIS_GUIDELINES.md` v2.0

### 2. MAPPING (automatico)
`mapper/protocol.py` v2.2 deriva coordinate Σ:
- Legge synthesis JSON
- Deriva D, A, X, P (con priority system per polarity)
- Output: `results/batch_X_domain_results.json`

**Comando:**
```bash
python scripts/map_concepts.py batch_X_domain.json
```

### 3. VALIDATION (umana)
Ray invia synthesis + mapping a **Opus** (LLM oracolo):
- Valida D, A, X, P
- Conferma/corregge coordinate
- Io aggiorno JSON con `oscillation_notes`

**Doc review:** `docs/new_syntheses_for_opus_review.md`

---

## 📁 Struttura

```
knowledge_mapping/
├── batches/              Synthesis files (input)
│   ├── batch_1_mathematics.json
│   ├── batch_2_classical_physics.json
│   └── ...
├── results/              Mapping results (output)
│   ├── batch_1_mathematics_results.json
│   └── ...
├── diagnostics/          Network analysis
│   ├── network_diagnostics.py
│   └── network_diagnostic_report_batch1-5_20260208.txt
├── docs/                 Guidelines & reviews
│   ├── SYNTHESIS_GUIDELINES.md (v2.0 — P± system codificato)
│   ├── new_syntheses_for_opus_review.md
│   └── REVISED_MAPPINGS.md
├── scripts/              Automation utilities
│   ├── batch_map.py
│   ├── map_concepts.py
│   ├── test_euler.py
│   └── ...
├── backups/              Batch backups pre-revision
├── mapper/               Mapper v2.2 (derive Σ from synthesis)
└── concept_synthesizer/  Synthesizer (manual + LLM-backed option)
```

---

## 🔧 Comandi Utili

### Mappare nuovo batch
```bash
cd knowledge_mapping/scripts
python map_concepts.py ../batches/batch_6_biology.json
```

### Diagnostics rete
```bash
cd knowledge_mapping/diagnostics
python network_diagnostics.py
```

### Test synthesis automatica (LLM-backed)
```bash
cd knowledge_mapping/scripts
python test_auto_synthesis.py
```

---

## 💡 Insights Chiave

### Sistema P± (Polarity)
**Codificato in batch 4 (Thermodynamics), validato 10/10 in batch 5 (Quantum)**

**P=+ (expansion):** Concetto **classifica/apre** regioni di spazio delle possibilità
- Esempio: CAP Theorem — classifica 3 regioni valide (CA, CP, AP)

**P=- (contraction):** Concetto **vieta/elimina** regioni di spazio delle possibilità
- Esempio: Second Law — vieta regione ΔS<0 (impossibile in natura)

**Discriminatore:** "Vieta vs classifica"

**Constraints (T7, P6, C7.x) non hanno polarity** — sono pre-Tesseract, descrivono struttura non contenuti.

### Elimination Test
**Metodo primario per determinare attributo dominante (A):**
1. Rimuovi temporality → concetto sopravvive? Se collassa → A=1 (temporal)
2. Rimuovi spatiality → concetto sopravvive? Se collassa → A=2 (spatial)
3. Rimuovi causality → concetto sopravvive? Se collassa → A=3 (causal)

**Attributo distrutto = attributo PRIMARY.**

---

## 📈 Prossimi Passi

**Pending (domani):** Aggiungere **regole di derivazione**
- Inferenze tra nodi vicini (Σ_DAXP → Σ_D'A'X'P')
- Pattern transizioni dimensionali (D→D)
- Shift attributi (A→A)

**Futuri batches:**
- Biology/Evolution (⟳-heavy organisms)
- General Relativity (D=4 spacetime curvature)
- Statistical Mechanics (bridge micro↔macro)
- Set Theory/Logic (Δ-heavy foundations)

---

## 🧠 Design Philosophy

**Questo è mapping ONTOLOGICO, non categorizzazione.**

Non chiediamo "in quale categoria sta X?" ma "**quale struttura ontologica realizza X?**"

**Tesseract = spazio delle strutture possibili dell'esistenza.**

Ogni concetto scientifico è una **realizzazione** di una struttura Σ — mappare significa **riconoscere la forma ontologica sottostante**.

---

**Ultimo update:** 2026-02-08
**Version:** v1.0 (post-riorganizzazione progetti)
