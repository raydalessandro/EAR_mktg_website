---
title: "Visualizzazione interattiva"
summary: HTML standalone con la viz 3D del Tesseract — 72 nodi, 444 archi, navigabile.
status: published
type: visualization
version: "1.0"
order: 30
tags: [tesseract, visualizzazione, interattiva, html]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/visualizzazione/ear_tesseract_visualization.html
  format: html
  size: "20 KB"
related:
  - tesseract/grafo
  - tesseract/paper
featured: true
---

## Cosa è

Un singolo file HTML che, aperto in un browser, mostra il **Tesseract
navigabile in 3D**: tutti i 72 nodi con etichette delle coordinate
Σ_DAXP, i 444 archi colorati per tipo (Mother / Double / Simple),
controlli di rotazione e zoom, evidenziazione per attributo (A=1, A=2,
A=3) e per polarità (P+/P-).

[**Apri la visualizzazione →**](/tesseract/viz)

## Perché vale la pena aprirla

La visualizzazione rende **intuitivo** ciò che il paper rende formale:

- I 24 nodi A=2 (i "ponti") emergono visivamente come hub
- L'asimmetria di 1/36 si vede come 12 archi "extra" oltre il cristallo perfetto
- Le tre dimensioni di complessità (atomic / systemic / emergent) si dispongono in strati
- I cluster naturali del grafo corrispondono a domini concettuali

## Come usarla

- **Browser**: scarica e apri (zero dipendenze, JS inline)
- **Embed**: il file è autosufficiente, può essere iframe-d in un'altra pagina
- **Modifica**: il sorgente è leggibile — puoi adattare colori, etichette, layout

## Note

Versione 1.0. Stile minimale, focalizzato su comprensione strutturale
più che estetica. La pagina home del sito embed-da una versione di
questa viz come centerpiece.
