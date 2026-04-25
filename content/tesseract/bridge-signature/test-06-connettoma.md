---
title: "Test 6 — Il connettoma"
summary: "Teoria strutturale del connettoma: 72 tipi neuronali, regole 9:3:1, gli interneuroni sono ponti, non background."
status: published
type: study
version: "1.0"
order: 60
tags: [tesseract, bridge-signature, connettoma, neuroscienze]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-06-connettoma/connectome_package.zip
  format: zip
  size: "16 KB"
related:
  - tesseract/paper
  - tesseract/bridge-signature/test-05-firma-altre-reti
featured: false
---

## Cosa testa

Il salto dal benchmark generale al dominio neurale. Il test traduce il
Tesseract in linguaggio neuroscientifico: D = ruolo funzionale (input,
processing, output, modulation), A = tipo cellulare (eccitatorio, connettivo,
inibitorio), X = scala (locale, regionale, globale), P = stato (attivo,
quiescente). Le tre regole 9:3:1 diventano complementarità funzionale,
polarità di stato, adiacenza spaziale.

## Risultato

Applicate al grafo dei 72 tipi neuronali, le regole producono la firma ponte
sui nodi A=2 (connettivi):

| Metrica | A=1 (Eccit.) | A=2 (Connect.) | A=3 (Inib.) |
|---|---|---|---|
| Grado | 12.0 | **13.0** | 12.0 |
| Clustering | 0.470 | **0.397** | 0.470 |

Differenze: **+8% di grado**, **−16% di clustering** per i connettivi. Sul
**connettoma di C. elegans** (302 neuroni completi) il "rich club" di 14 hub
identificato da Towlson et al. 2013 ha esattamente la firma — grado 3.4×,
betweenness 11×, clustering 0.64× rispetto alla media. I neuroni
neuromodulatori (dopaminergici, serotoninergici) sono il **2.3×**
sovra-rappresentati nel rich club.

## Cosa significa

Gli interneuroni non sono **background** ma **bridge**: tengono insieme il
connettoma. Questo riformula tre osservazioni cliniche note: perché la
disfunzione interneuronale ha effetti pervasivi (schizofrenia, autismo);
perché i sistemi neuromodulatori (dopamina, serotonina) hanno effetti su
funzioni eterogenee; perché i farmaci che li target hanno spettro ampio e
richiedono titolazione fine. La predizione operativa per la connettomica:
in qualsiasi connettoma completo, gli interneuroni avranno la firma e
saranno circa 1/3 del totale.

## Materiale

- [CONNECTOME_BRIDGE_PAPER.md](/downloads/tesseract/bridge-signature/test-06-connettoma/) — paper completo: 4 coordinate, 3 regole, validazione, implicazioni cliniche e AI
- [connectome_package.zip](/downloads/tesseract/bridge-signature/test-06-connettoma/connectome_package.zip) — script e dati di analisi

## Posizione nella sequenza

Sesto test. Costruisce la teoria strutturale che i Test 7-9 sottoporranno a
verifica statistica su connettomi reali. Il Test 7 esegue la prima verifica
end-to-end su C. elegans usando l'atlante eLife 2024 dei neurotrasmettitori.
