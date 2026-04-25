---
title: "Batches"
summary: I 7 batch di mappatura — 5 completi, 2 in integrazione. 49 concetti su 17 nodi del Tesseract.
type: collection
status: published
order: 50
icon: branches
tags: [mapping, batches, scibile]
authors: [nodo432]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
---

I **batch** sono il prodotto del programma di mapping: ogni batch è un
dominio scientifico con N concetti mappati su coordinate Σ_DAXP del
Tesseract. Ogni voce ha un JSON di sintesi (input) e un JSON di
risultati (output coordinate).

## Status

| # | Dominio | Concetti | Stato |
|---|---|---|---|
| 1 | [Mathematics](/ontologia/mapping/batches/1-mathematics) | 10 | ✓ completo |
| 2 | [Classical Physics](/ontologia/mapping/batches/2-classical-physics) | 10 | ✓ completo |
| 3 | [CS / Logic](/ontologia/mapping/batches/3-cs-logic) | 9 | ✓ completo |
| 4 | [Thermodynamics](/ontologia/mapping/batches/4-thermodynamics) | 10 | ✓ completo (introduce P=−) |
| 5 | [Quantum Mechanics](/ontologia/mapping/batches/5-quantum) | 10 | ✓ completo (10/10 P± predictions) |
| 6 | [Relativity & Cosmology](/ontologia/mapping/batches/6-relativity) | — | ⏳ da integrare |
| 7 | [Millennium Problems](/ontologia/mapping/batches/7-millennium) | — | ⏳ da integrare |

**Totale finora:** 49 concetti, 17 nodi del Tesseract popolati (23.6%).

## Come leggere ogni batch

Ogni scheda batch ha:
- Lista dei concetti mappati con le loro coordinate Σ_DAXP
- Hotspots e pattern del dominio
- Link al **synthesis JSON** (input) e al **results JSON** (output)
- Note su oscillazioni e casi limite

I file JSON si possono caricare in `pandas` / `networkx` per analisi
quantitative o in un LLM come contesto strutturato.
