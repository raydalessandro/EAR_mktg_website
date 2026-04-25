---
title: "Grafo del Tesseract — Matrix 72"
summary: Dati JSON del reticolo a 72 nodi e 444 archi. Versione base + espansa.
status: published
type: dataset
version: "1.0"
order: 20
tags: [tesseract, grafo, dataset, json, matrix-72]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/grafo/GRAFO_MATRIX_72.json
  format: json
  size: "16 KB"
related:
  - tesseract/paper
  - tesseract/visualizzazione
  - tesseract/bridge-signature/test-04-killer-finding
  - ontologia/aila/operazionale/matrix-vocab
featured: false
---

## Cosa è

Il **grafo completo del Tesseract** in formato JSON: 72 nodi (uno per
ogni coordinata Σ_DAXP) con metadati di posizione (D, A, X, P), 444
archi con classificazione tipo cabalistico (Mother / Double / Simple)
e pesi/distanze.

## Due versioni

| File | Contenuto | Uso |
|---|---|---|
| **GRAFO_MATRIX_72.json** ([download](/downloads/tesseract/grafo/GRAFO_MATRIX_72.json)) | Grafo base: 72 nodi + 444 archi con metadati | Analisi strutturale, viz, computazioni |
| **GRAFO_MATRIX_72_EXPANDED.json** ([download](/downloads/tesseract/grafo/GRAFO_MATRIX_72_EXPANDED.json)) | Versione arricchita con etichette estese, descrizioni semantiche, mapping verso AILA | Dataset di lavoro per mapping concetti, didattica |

## Struttura dei dati

Ogni nodo include:
- `id` — coordinate canoniche (es. `Σ123-`)
- `D, A, X, P` — i 4 valori
- `label`, `description` — testi (nella versione expanded)
- `neighbors` — lista degli archi uscenti

Ogni arco include:
- `from`, `to`
- `kind` — `mother | double | simple`
- `weight` — distanza/forza dell'arco

## Perché è utile con AI

Carica il JSON in pandas / NetworkX / un altro grafo library e:

- Fai analisi topologica (centralità, comunità, percorsi)
- Calcola la **Bridge Signature** (vedi [test-04](/tesseract/bridge-signature/test-04-killer-finding)) per identificare i nodi A=2
- Mappa concetti reali su coordinate Σ_DAXP per il programma di [mapping](/ontologia/mapping)
- Verifica predizioni del paper (degree mean = 12.33, asimmetria 1/36)

## Come usarlo

```python
import json, networkx as nx
G = nx.node_link_graph(json.load(open("GRAFO_MATRIX_72.json")))
print(G.number_of_nodes(), G.number_of_edges())  # 72, 444
```

## Note

I file `.json` sono la **fonte canonica machine-readable** del Tesseract.
La versione expanded è "living document" (può ricevere arricchimenti
semantici); la versione base è stabile (riflette la struttura geometrica
necessaria, non muterà).
