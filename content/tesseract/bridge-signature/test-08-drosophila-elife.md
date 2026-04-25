---
title: "Test 8 — Drosophila Central Complex"
summary: "2864 neuroni del Central Complex: la firma si replica con sovra-rappresentazione 1.40× e p = 0.011."
status: published
type: study
version: "1.0"
order: 80
tags: [tesseract, bridge-signature, drosophila, replica, scaling]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-08-drosophila-elife/DEFINITIVE_BRIDGE_SIGNATURE.zip
  format: zip
  size: "172 KB"
related:
  - tesseract/paper
  - tesseract/bridge-signature/test-07-celegans
featured: false
---

## Cosa testa

Replica del risultato C. elegans su un secondo organismo, con un connettoma
**10× più grande** e ottenuto con tecnologia diversa. Dataset di partenza:
**FlyWire** (Dorkenwald et al., Nature 2024) — 139.000 neuroni, 16.8M
connessioni nel cervello completo di Drosophila. La classificazione
neurotrasmettitoriale è ricavata dalle annotazioni FlyWire.

## Risultato

Sull'intero cervello di Drosophila il test **fallisce**: grado modulatori
−39%, sovra-rappresentazione 0.21×, direzione opposta alla predizione. La
diagnosi non è "teoria sbagliata" ma "scala sbagliata". Applicando la
proposizione **P4 (Scaling)** di EAR, l'analisi si restringe al **Central
Complex** — una singola regione (centro di navigazione/controllo motorio),
2.864 neuroni connessi, 118.083 sinapsi (soglia ≥ 3), 206 modulatori (7.2%).

A questa scala la firma si replica:

| Metrica | Predizione | Osservato |
|---|---|---|
| Grado M vs E | + | +3.3% |
| Clustering M vs E | − | −0.7% |
| Betweenness M vs E | + | **+47.9%** |

Tutte e tre le direzioni confermate. χ² = 6.460, **p = 0.011**.
Sovra-rappresentazione modulatori tra i ponti: **1.40×**. T-test betweenness:
t = 2.28, p = 0.023.

## Cosa significa

Il risultato è una **doppia validazione**: la firma si replica su un secondo
organismo, e la sua "scala operativa" è chiarita. La firma ponte agisce
**dentro** un sistema (⬡), non **attraverso** un meta-sistema (⧈). Il cervello
di Drosophila è un campo di sistemi specializzati (Central Complex, Mushroom
Body, Optic Lobe, …) — non un singolo sistema da analizzare globalmente.
Questo conferma operativamente P4 di EAR: **la struttura è invariante tra
scale, i parametri variano**. Le direzioni si conservano (C. elegans e CX
identiche), la magnitudine cambia (3.24× vs 1.40×).

Insight metodologico applicabile altrove: nei connettomi grandi, l'analisi
deve corrispondere al livello ontologico appropriato (modulo/regione), non
proiettare il sistema-di-sistemi su un singolo grafo piatto.

## Materiale

- [elife-95402-supp2-v1.xlsx](/downloads/tesseract/bridge-signature/test-08-drosophila-elife/elife-95402-supp2-v1.xlsx) — atlante eLife 2024 dei neurotrasmettitori
- [DEFINITIVE_BRIDGE_SIGNATURE.zip](/downloads/tesseract/bridge-signature/test-08-drosophila-elife/DEFINITIVE_BRIDGE_SIGNATURE.zip) — package con script `bridge_signature_definitive.py`, dati C. elegans e Drosophila, README e RESULTS

## Posizione nella sequenza

Ottavo test. Replica del risultato C. elegans (Test 7) su un secondo
organismo e validazione operativa di P4 (Scaling). Il Test 9 estende il
package per riprodurre tutto end-to-end con i file FlyWire al loro livello
nativo — è la chiusura del programma e resta marcato come *incompleto* per i
dati che richiedono download separato.
