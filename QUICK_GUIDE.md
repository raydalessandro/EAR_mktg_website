# Quick Guide — Neural Mapping Projects

**Guida veloce per orientarsi nella nuova struttura (post-riorganizzazione 2026-02-08)**

---

## 📂 Struttura (Ultra-Semplificata)

```
neural_mapping_agents/
├── README.md                    ← Leggi questo per overview completa
├── knowledge_mapping/           ← LAVORO ATTIVO (49 concepts mappati)
├── neural_agents/               ← SPERIMENTALE (infrastructure ready)
└── _OLD_ROOT/                   ← BACKUP SICUREZZA (non toccare)
```

---

## 🎯 Quale Progetto Usare?

### **knowledge_mapping/** — Usa Questo
- **Cosa fa:** Mappa scibile umano (matematica, fisica, CS, etc.) su Matrix 72
- **Status:** ✅ In produzione, 49 concepts → 17 nodi (23.6% Tesseract)
- **Come:** Semi-manuale (Claude synthesis + Opus validation)
- **Prossimo:** Derivation rules (domani)

### **neural_agents/** — Non Usare (per ora)
- **Cosa fa:** Multi-agent automation per fenomeni neurali
- **Status:** ⚠️ Sperimentale, mai testato in produzione
- **Quando:** Futuro, quando metodologia knowledge_mapping sarà consolidata

---

## 🚀 Comandi Rapidi

### Dove Trovo I Batch Mappati?
```bash
cd knowledge_mapping/batches
ls -lh
# batch_1_mathematics.json
# batch_2_classical_physics.json
# batch_3_cs_logic.json
# batch_4_thermodynamics.json
# batch_5_quantum.json
```

### Dove Trovo I Risultati?
```bash
cd knowledge_mapping/results
ls -lh
# batch_1_mathematics_results.json
# batch_2_classical_physics_results.json
# ...
```

### Dove Trovo La Diagnostica Rete?
```bash
cd knowledge_mapping/diagnostics
cat network_diagnostic_report_batch1-5_20260208.txt
# Report completo 49 concepts → 17 nodi
```

### Dove Trovo Le Guidelines?
```bash
cd knowledge_mapping/docs
cat SYNTHESIS_GUIDELINES.md
# P± system codificato, elimination test, esempi
```

---

## 📊 Status Veloce

**knowledge_mapping:**
- ✅ 49 concepts mappati
- ✅ 17 nodi Tesseract occupati (23.6%)
- ✅ P± system validato (10/10 predictions batch 5)
- ✅ Hotspots: Σ₁₂₁₊ (9), Σ₃₂₁₊ (8), Σ₁₁₁₊ (5)
- 📋 Pending: Derivation rules (domani)

**neural_agents:**
- ⚠️ Infrastructure ready
- ⚠️ Mai usato in produzione
- ⚠️ Da completare: Network Builder, Orchestrator

---

## ✅ I Due Progetti Sono Separati?

**SÌ. Totalmente indipendenti:**

- **Nessun file condiviso** — ogni progetto ha copie proprie di `mapper/` e `concept_synthesizer/`
- **Modifiche a knowledge_mapping/** → NON impattano neural_agents/
- **Modifiche a neural_agents/** → NON impattano knowledge_mapping/

**Prova:**
```bash
# Questi sono FILE DIVERSI (copie indipendenti)
ls -i knowledge_mapping/mapper/protocol.py
ls -i neural_agents/mapper/protocol.py
# Inode diversi = file fisici separati
```

---

## 🔄 Dove È Finito Tutto Il Vecchio?

**`_OLD_ROOT/` — Archivio completo root originale**

Contiene:
- Tutti i file originali della vecchia root
- Mapper/synthesizer/judge originali
- Batch files originali
- Script originali
- Doc originali

**Se qualcosa non funziona → tutto è recuperabile da lì.**

---

## 📝 Documenti Utili

**Root:**
- `README.md` — Overview completa due progetti
- `REORGANIZATION_SUMMARY.md` — Dettagli riorganizzazione completa
- `QUICK_GUIDE.md` — Questo file

**knowledge_mapping/:**
- `README.md` — Documentazione Progetto B (sistema in uso)
- `docs/SYNTHESIS_GUIDELINES.md` — PPU v2.0 (P± system)
- `docs/new_syntheses_for_opus_review.md` — Workflow review Opus
- `docs/REVISED_MAPPINGS.md` — Storia correzioni

**neural_agents/:**
- `README.md` — Documentazione Progetto A (sperimentale)
- `STATUS.md` — Stato implementazione agents
- `CONTEXT_LOADED.md` — Context caricato agents

---

## ❓ Domande Frequenti

### "Posso modificare knowledge_mapping/ senza rompere neural_agents/?"
**SÌ.** I due progetti sono totalmente indipendenti.

### "I batch files sono duplicati?"
**NO.** Sono stati COPIATI da root a `knowledge_mapping/batches/`. Root originale archiviata in `_OLD_ROOT/`.

### "Gli script funzionano con i nuovi path?"
**SÌ.** Path relativi verificati, import funzionano correttamente.

### "E se qualcosa non funziona?"
**Rollback completo possibile da `_OLD_ROOT/`.** Niente è stato cancellato.

### "Devo aggiornare la copia Desktop?"
**SÌ, probabilmente.** Desktop ha ancora vecchia struttura. Decidi tu se aggiornare o tenere snapshot old.

---

## 🎯 Prossimi Passi (Domani)

1. **Derivation Rules** — Come avevi chiesto ieri
2. **Test knowledge_mapping/** — Verifica mapping nuovo batch funziona con nuova struttura
3. **Update Desktop copy** (opzionale) — Se vuoi riflettere nuova organizzazione

---

**Ultimo update:** 2026-02-08 21:00
**Riorganizzazione:** Completata ✅
**Safety backup:** `_OLD_ROOT/` preservato ✅
