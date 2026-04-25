---
title: "Test 9 — Secondo organismo (incompleto)"
summary: "Package completo C. elegans + Drosophila + FlyWire per replica end-to-end. Connessioni FlyWire da scaricare separatamente."
status: published
type: study
version: "1.0"
order: 90
tags: [tesseract, bridge-signature, replica, flywire, incompleto]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-09-secondo-organismo/BRIDGE_SIGNATURE_COMPLETE.zip
  format: zip
  size: "8.0 MB"
related:
  - tesseract/paper
  - tesseract/bridge-signature/test-08-drosophila-elife
featured: false
---

## Cosa testa

Confezionamento finale del programma su due organismi: package end-to-end con
script, dati C. elegans completi, dati Drosophila Central Complex, e
**annotazioni FlyWire native** per riprodurre l'intero pipeline a scala di
cervello e di regione. Il test definisce il protocollo operativo per estendere
la validazione a un terzo organismo (umano, regionale).

## Risultato

Il package include:

- `bridge_signature_definitive.py` — pipeline unica per entrambi gli organismi
- `NeuronConnect.xls` — connettoma C. elegans (Varshney/WormAtlas)
- `elife-95402-supp2-v1.xlsx` — atlante neurotrasmettitori eLife 2024
- `flywire_neurons.tsv` — **32 MB** di annotazioni neuronali FlyWire
- `RESULTS.md`, `CENTRAL_COMPLEX_RESULTS.md`, `DROSOPHILA_REGIONAL_RESULTS.md`,
  `FLYWIRE_PARTIAL_RESULTS.md`, `BRIDGE_SIGNATURE_STATUS.md` — report
  dettagliati per ogni passo (globale, regionale, parziale)

Lo stato è **incompleto by design**: il file delle connessioni FlyWire
(`flywire_connections.feather`, ~812 MB) supera ogni budget di hosting
ragionevole e va scaricato separatamente da Zenodo, come indicato nel README
del package. Tutti i risultati statistici (p-value, sovra-rappresentazione,
direzioni) sono già pre-calcolati e disponibili nei report.

## Cosa significa

Il programma chiude qui come **proof-of-concept replicabile**. Chi vuole
verificare le statistiche del Test 8 con i dati FlyWire al loro livello nativo
trova script + annotazioni + report; chi vuole estendere a un terzo organismo
trova un protocollo già adattato per organismi grandi (analisi per regione,
non globale). L'estensione naturale (umano regionale, altre regioni di
Drosophila, formalizzazione del protocollo multi-scala) è lasciata aperta.

## Materiale

- [BRIDGE_SIGNATURE_COMPLETE.zip](/downloads/tesseract/bridge-signature/test-09-secondo-organismo/BRIDGE_SIGNATURE_COMPLETE.zip) — package completo (8 MB) con script, dati C. elegans, atlante eLife 2024, annotazioni FlyWire, e cinque report markdown

## Posizione nella sequenza

Nono e ultimo test. Chiude il programma con un package riproducibile che
include sia il successo C. elegans (Test 7) sia la replica Drosophila Central
Complex (Test 8). Il [report finale sintetico](/downloads/tesseract/bridge-signature/riassunto-finale/Breve-Bridge_Signature_Report.docx)
allegato all'overview riassume i risultati dei nove test in una pagina.
