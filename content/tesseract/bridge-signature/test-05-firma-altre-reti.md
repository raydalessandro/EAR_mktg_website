---
title: "Test 5 — La firma su altre reti"
summary: "Karate Club, Florentine Families, Les Misérables: la firma trova i broker noti con precision 100% senza training."
status: published
type: study
version: "1.0"
order: 50
tags: [tesseract, bridge-signature, validazione, reti-sociali]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-05-firma-altre-reti/bridge_signature_package.zip
  format: zip
  size: "16 KB"
related:
  - tesseract/paper
  - tesseract/bridge-signature/test-04-killer-finding
featured: false
---

## Cosa testa

La firma trovata sul Tesseract è un'astrazione del Tesseract o cattura una
proprietà strutturale generale? Il test la applica a tre reti benchmark dove
i "ponti" sono noti dalla letteratura, senza adattamenti né soglie tarate sui
dati: solo la regola "> media" applicata a ciascuna rete.

## Risultato

Su tutte e tre le reti i broker conosciuti vengono identificati:

| Rete | Broker noti | Trovati |
|---|---|---|
| Zachary's Karate Club (34 nodi) | leader 0 e 33 | 2/2 (100%) |
| Florentine Families | i Medici | 1/1 (100%) |
| Les Misérables (77 personaggi) | Valjean, Myriel, Javert, Gavroche | 4/4 (100%) |

Su grafi Erdős-Rényi (random) la firma identifica nodi senza significato
strutturale, come atteso: in assenza di struttura reale, la firma non ha
potere predittivo. Nelle reti reali la frazione di ponti è **10-21%** dei
nodi — un range stabile compatibile con ~1/6.

## Cosa significa

La firma funziona **off-the-shelf** su reti che non hanno nulla a che vedere
con il Tesseract: una rete di amicizie del 1977, una rete di matrimoni del
Rinascimento, un grafo letterario di un romanzo del 1862. In tutti e tre i
casi i broker storicamente noti emergono come nodi che soddisfano le tre
disuguaglianze. Il controllo negativo (Erdős-Rényi) chiude la possibilità
banale che la firma "trovi sempre qualcosa".

A questo punto la firma è uno **strumento riusabile**. Ha applicazioni in
marketing/epidemiologia (broker sociali), drug discovery (proteine
adattatrici), neuroscienze (interneuroni), NLP (parole funzionali), risk
management (key person). I test successivi la portano dove conta davvero: i
connettomi reali.

## Materiale

- [BRIDGE_SIGNATURE_PAPER.md](/downloads/tesseract/bridge-signature/test-05-firma-altre-reti/) — paper standalone della firma con algoritmo, validazione e applicazioni
- [bridge_signature_package.zip](/downloads/tesseract/bridge-signature/test-05-firma-altre-reti/bridge_signature_package.zip) — script e dati per riprodurre i tre benchmark

## Posizione nella sequenza

Quinto test. Generalizza il killer finding del Test 4 a reti benchmark
classiche. Il Test 6 fa il salto al dominio dove la firma può davvero
mordere — la connettomica.
