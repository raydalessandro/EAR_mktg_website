---
title: Mapping
summary: Programma sistematico di mappatura dello scibile umano sulle 72 coordinate del Tesseract.
type: collection
status: published
order: 50
icon: branches
tags: [mapping, tesseract, scibile, coordinate, knowledge-mapping]
authors: [nodo432, Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
---

Programma sistematico per **mappare i concetti fondamentali della
scienza** (matematica, fisica, computer science, termodinamica,
quantistica, relatività, problemi del millennio…) sulle **72 coordinate
del [Tesseract](/tesseract)**: ogni concetto riceve una posizione
Σ_DAXP basata su Dimensione (D=1-4), Attributo (A=1-3), Complessità
(X=1-3) e Polarità (P=±).

## Stato attuale

- **49 concetti mappati** su **17 nodi** del Tesseract
- **Coverage**: 23.6% dei 72 nodi totali
- **Hotspots**: Σ₁₂₁₊ (9 concetti, tools relazionali-spaziali atomici), Σ₃₂₁₊ (8 concetti, dinamiche), Σ₁₁₁₊ (5 concetti, fondamenti distintivi)

## Struttura

| | Cosa contiene |
|---|---|
| **[Regole di derivazione](/ontologia/mapping/regole)** | Mapping rules + computational grounding — come si deriva la coordinata |
| **[Pipeline](/ontologia/mapping/pipeline)** | EAR Triangulation v2.0 — orchestrator + dashboard + run.py |
| **[Batches](/ontologia/mapping/batches)** | I 7 batch di mappatura: 5 completi (math, physics, CS, thermo, quantum), 2 in integrazione (relativity, millennium) |
| **[Diagnostica](/ontologia/mapping/diagnostica)** | Report di analisi rete: hotspot, oscillazioni, occupancy, attribute dominance |
| **[Sistema](/ontologia/mapping/sistema)** | Codice del knowledge_mapping system (mapper, synthesizer, scripts) |

## Workflow di mappatura

1. **Synthesis** — scrittura del JSON di sintesi (concept_name, ontological_content, polarity, elimination_test, examples)
2. **Mapping** — `mapper/protocol.py` v2.2 deriva D, A, X, P automaticamente
3. **Validation** — review umana (Opus come oracolo) per confermare/correggere coordinate
4. **Iterazione** — annotazioni di oscillazione per concetti tensionali fra nodi adiacenti

## Connessioni

- Il [Tesseract](/tesseract) è lo spazio di coordinate
- Il [Matrix Vocab AILA](/ontologia/aila/operazionale/matrix-vocab) è la notazione simbolica delle stesse coordinate
- I [teoremi](/ontologia/teoremi) sono mappati su nodi specifici (P1-P6 ↔ coordinate)

Il programma cresce con nuovi domini: prossimi candidati includono
relatività, problemi del millennio, biologia, neuroscienze.
