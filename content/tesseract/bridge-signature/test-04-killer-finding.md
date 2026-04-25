---
title: "Test 4 — Killer Finding: la firma ⇄"
summary: "Tre disuguaglianze identificano i 24 nodi A=2 del Tesseract: precision 100%, recall 100%, F1 100%."
status: published
type: study
version: "1.0"
order: 40
tags: [tesseract, bridge-signature, scoperta, firma-topologica]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-04-killer-finding/signature_verification.py
  format: py
  size: "8 KB"
related:
  - tesseract/paper
  - tesseract/grafo
  - tesseract/bridge-signature/test-03-buchi-dissolti
featured: true
---

## Cosa testa

Esiste una caratterizzazione **diretta** dei 24 nodi A=2, espressa solo in
metriche di rete standard, senza riferimento al modello generativo del
Tesseract? Il test prova combinazioni di tre metriche classiche — grado,
betweenness, clustering — confrontandole con la media globale.

## Risultato

La congiunzione

> grado > media ∧ betweenness > media ∧ clustering < media

identifica **esattamente i 24 nodi A=2 su 72**, e nessun altro:

- **Precision: 100%**
- **Recall: 100%**
- **F1: 100%**

Nessun falso positivo, nessun falso negativo. La firma non era un input del
modello: emerge spontaneamente dalla struttura.

## Cosa significa

È il punto di svolta del programma. Da qui in poi non serve più sapere cosa sia
EAR, il Tesseract o la Kabbalah per usare il risultato. La firma è un
**algoritmo di tre righe**: prendi una rete, calcola le tre metriche, applica
la disuguaglianza. I nodi che la soddisfano sono i ponti — i broker, gli
adattatori, gli interneuroni.

L'errore iniziale (la previsione era "A=2 ha **più** clustering") si è
rivelato necessario: ha portato alla scoperta corretta, ovvero che ⇄ ha
**meno** clustering perché connette diversi, non simili. La predizione
falsificabile è netta: in qualsiasi rete naturale dove esista una distinzione
Δ/⇄/⟳, i nodi connettori avranno grado e betweenness alti e clustering basso.
Se i broker noti hanno clustering alto, EAR è falsificato.

## Materiale

- [KILLER_FINDING.md](/downloads/tesseract/bridge-signature/test-04-killer-finding/) — testo della scoperta con metriche e implicazioni
- [signature_verification.py](/downloads/tesseract/bridge-signature/test-04-killer-finding/signature_verification.py) — script di verifica riproducibile sui 72 nodi

## Posizione nella sequenza

Quarto test. È il **killer finding** del programma: sposta l'oggetto da
"validare il Tesseract" a "validare uno strumento universale". I cinque test
successivi rispondono a una sola domanda: la firma vale fuori dal Tesseract?
Il Test 5 inizia a verificarlo su reti benchmark classiche.
