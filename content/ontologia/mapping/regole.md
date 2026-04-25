---
title: "Regole di derivazione"
summary: Mapping rules v1.1 + computational grounding v0.1 — come una sintesi diventa coordinata Σ_DAXP.
status: published
type: methodology
version: "1.1"
order: 10
tags: [mapping, regole, derivazione, metodologia]
authors: [nodo432, Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/mapping/regole/EAR_MAPPING_RULES_v1-1.md
  format: md
related:
  - tesseract/paper
  - ontologia/mapping/pipeline
  - ontologia/aila/operazionale/matrix-vocab
featured: false
---

## Cosa sono

Le **regole formali** per mappare un concetto (descritto in JSON di
sintesi) su una coordinata Σ_DAXP del [Tesseract](/tesseract).
Definiscono come decidere D, A, X, P a partire dalle proprietà
ontologiche del concetto, in modo replicabile e auditabile.

## Due documenti

| File | Cosa | Download |
|---|---|---|
| **EAR_MAPPING_RULES_v1-1.md** | Le regole di derivazione (cosa fa il mapper) | [scarica](/downloads/ontologia/mapping/regole/EAR_MAPPING_RULES_v1-1.md) |
| **EAR_COMPUTATIONAL_GROUNDING_v0.1.md** | Il "grounding" computazionale: come una proprietà ontologica corrisponde a una proprietà calcolabile | [scarica](/downloads/ontologia/mapping/regole/EAR_COMPUTATIONAL_GROUNDING_v0.1.md) |

## Perché contano

Senza regole esplicite, la mappatura sarebbe arbitraria. Con queste
regole, è **falsificabile**: due reviewer indipendenti dovrebbero
arrivare alla stessa coordinata se le regole sono ben formate. Le
oscillazioni residue (quando un concetto vive "fra due nodi") sono
documentate come eccezioni note.

## Connessioni

- Il [paper Tesseract](/tesseract/paper) definisce lo spazio
- Queste regole definiscono la **funzione di mappatura** verso quello spazio
- La [pipeline](/ontologia/mapping/pipeline) è l'implementazione
