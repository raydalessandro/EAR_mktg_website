---
title: "Diagnostica della rete"
summary: "Report 2026-02-08 sul network di 49 concetti / 17 nodi — hotspot, oscillazioni, occupancy, attribute dominance."
status: published
type: report
version: "1.0"
order: 30
tags: [mapping, diagnostica, hotspot, oscillazioni]
authors: [nodo432]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/mapping/diagnostica/network_diagnostic_report_20260208.txt
  format: txt
related:
  - ontologia/mapping/batches
  - tesseract/grafo
featured: false
---

## Cosa contiene

Il **report diagnostico** sul network attuale di mappatura,
generato dopo i 5 batch completati (math, physics, CS/logic, thermo,
quantum). 11 KB di analisi strutturale.

## Highlights

- **Network size**: 49 concetti su 5 domini → 17 nodi del Tesseract (23.6% coverage)
- **Hotspots**:
  - Σ₁₂₁₊ (9 concetti): tools relazionali-spaziali atomici (metriche, vincoli)
  - Σ₃₂₁₊ (8 concetti): dinamiche processuali-spaziali atomiche (flussi, evoluzione)
  - Σ₁₁₁₊ (5 concetti): fondamenti distintivi-temporali (esistenza, identità)
- **Oscillazioni** (6 concetti tensionali): documentate con `oscillation_notes`
- **Pattern per dominio**: math, physics, CS, thermo, quantum hanno firme diverse
- **Coordinate space occupancy**: 17/72 nodi popolati
- **Attribute dominance**: A=2 (relation) emerge come dominante, coerente con il [Bridge Signature finding](/tesseract/bridge-signature/test-04-killer-finding)

## Perché è utile

- Per capire **dove sta crescendo** il programma di mapping (e dove no)
- Per individuare **anomalie** (concetti tensionali da rivedere)
- Per pianificare i prossimi domini da mappare (riempiendo nodi vuoti)
- Come dato strutturale per studi sulla **distribuzione naturale del sapere** sul Tesseract

## Note

Il report è statico al **2026-02-08**. Verrà rigenerato a ogni nuovo
batch integrato. Lo script generatore è in
[`/sistema`](/ontologia/mapping/sistema) (`network_diagnostics.py`).
