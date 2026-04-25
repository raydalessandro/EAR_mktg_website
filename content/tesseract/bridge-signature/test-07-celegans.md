---
title: "Test 7 — C. elegans"
summary: "281 neuroni, 2291 sinapsi: i modulatori sono sovra-rappresentati 2.91× tra i ponti (χ² p = 0.0004)."
status: published
type: study
version: "1.0"
order: 70
tags: [tesseract, bridge-signature, c-elegans, validazione-empirica]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-07-celegans/celegans_final_package.zip
  format: zip
  size: "112 KB"
related:
  - tesseract/paper
  - tesseract/bridge-signature/test-06-connettoma
featured: false
---

## Cosa testa

La predizione del Test 6 in cifre, su dati reali e con test statistici.
Dataset: il connettoma di Varshney et al. (NeuronConnect.xls) — 281 neuroni
connessi, 2.291 sinapsi — incrociato con la classificazione neurotrasmettitoriale
**eLife 2024 "A neurotransmitter atlas of C. elegans"** (Hobert et al.). I
neuroni sono partizionati in eccitatori (glutammato/acetilcolina), modulatori
(dopamina/serotonina/tiramina) e inibitori (GABA).

## Risultato

| Tipo | N | Grado | Clustering | Betweenness |
|---|---|---|---|---|
| Eccitatori | 238 | 16.19 | 0.345 | 0.0052 |
| **Modulatori** | 15 | **22.07** | **0.241** | **0.0071** |
| Inibitori | 28 | 14.18 | 0.301 | 0.0027 |

Delta modulatori vs eccitatori: **grado +36%**, **clustering −30%**,
**betweenness +37%**. Tutte e tre le metriche vanno nella direzione predetta,
con magnitudine **amplificata** rispetto al Tesseract teorico (+8%, −16%).

Sui 58 nodi che soddisfano la firma ponte (20.6% del totale), i modulatori
sono **sovra-rappresentati 2.91×**: χ² = 12.555, **p = 0.000395**. T-test sul
clustering: t = −2.057, p = 0.041.

## Cosa significa

La predizione strutturale derivata da principi primi resta **statisticamente
verificata** su un connettoma biologico reale. La direzione degli effetti è
identica a quella del Tesseract; la magnitudine è maggiore, coerentemente con
il principio che il modello geometrico cattura una struttura conservativa
mentre i sistemi reali la amplificano. I neuroni neuromodulatori non sono
"accessori" del sistema nervoso: sono ponti che integrano stati
comportamentali, modulano la risposta globale e coordinano sistemi neurali
diversi. La struttura del connettoma non è casuale — segue regole derivabili
**a priori**.

## Materiale

- [C_ELEGANS_FINAL_RESULTS.md](/downloads/tesseract/bridge-signature/test-07-celegans/) — risultati con tabelle e p-value
- [NeuronConnect.xls](/downloads/tesseract/bridge-signature/test-07-celegans/NeuronConnect.xls) — connettoma originale Varshney/WormAtlas
- [celegans_final_package.zip](/downloads/tesseract/bridge-signature/test-07-celegans/celegans_final_package.zip) — script di analisi e dati derivati

## Posizione nella sequenza

Settimo test. Prima validazione su un sistema biologico completo. Apre la
domanda di replicazione: il risultato vale anche su un connettoma
**dieci volte più grande**, costruito con altre tecnologie? Il Test 8 prova
con il Central Complex di Drosophila.
