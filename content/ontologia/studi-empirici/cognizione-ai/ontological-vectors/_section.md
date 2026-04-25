---
title: "Ontological Vectors — Primitive semantiche senza training"
summary: "EAR vs LLM su 78 carte dei Tarocchi: r=0.533 sulla valenza, 65% accordo dominio, 60% energia — senza training."
status: published
type: study
version: "1.0"
order: 20
icon: lab
tags: [empirico, cognizione-ai, llm, semantica, validazione]
authors: [Ray Antonini, EAR Lab]
created: 2026-01-12
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/studi-empirici/cognizione-ai/ontological-vectors/ear-paper-publication.zip
  format: zip
  size: "~57 KB"
related:
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/derivazioni/equivalences
  - ontologia/teoremi/6-inseparabilita-attributi
featured: false
---

## Cos'è

Paper empirico ("Ontological Vectors as Semantic Primitives: A Minimal
Symbolic System Achieving LLM-Coherent Outputs Without Training",
Antonini, EAR Lab Milano, gennaio 2026) che mette alla prova la tesi
forte di EAR: **il contenuto semantico è derivabile da principi
ontologici, non richiede apprendimento statistico da dati**.

Il banco di prova è un dominio simbolico chiuso e ben documentato —
le 78 carte dei Tarocchi nella tradizione Rider-Waite-Smith — usate
come "ground truth interpretativo" su cui confrontare due
interpretatori indipendenti: un motore EAR (zero training) e un LLM
addestrato su miliardi di token.

## Materiale

Pacchetto unico `ear-paper-publication.zip` (~57 KB) contenente:

- `EAR_Paper_Ontological_Vectors.docx` — paper completo
- `code/ear-tarot-engine-v2.1.jsx` — motore di assegnazione vettori EAR
- `code/ear-tarot-test-suite.js`, `ear-llm-comparison-test.js`,
  `ear-llm-metrics.js` — suite di test e metriche di confronto
- `data/comparison-data.json`, `test-results.json` — dati grezzi e
  risultati
- `README.md` — guida al pacchetto

## Risultati

Ogni carta è rappresentata come vettore `E = [Δ, ⇄, ⟳]` in
`[0, 1]³` più una polarità (`+`, `−`, neutra), assegnato da prime
principi (corrispondenze tradizionali + analisi ontologica). Il
confronto carta-per-carta con le interpretazioni LLM dà:

- **Correlazione di Pearson r = 0.533** sulla valenza predetta
  (moderate-to-strong);
- **65% di accordo** sulla classificazione di dominio;
- **60% di accordo** sull'attribuzione di energia.

Le divergenze sistematiche (in particolare sulle carte rovesciate)
non sono rumore: rivelano due tradizioni interpretative legittime e
distinte, segno che EAR cattura **struttura semantica reale**, non
pattern arbitrari.

## Connessione all'ontologia

Il paper opera direttamente sui tre attributi del
[kernel formale](/ontologia/aila/sistema-formale/kernel) — Δ
(Distinzione), ⇄ (Relazione), ⟳ (Processo) — confermando
empiricamente la
[Prop. 6 (Inseparabilità)](/ontologia/teoremi/6-inseparabilita-attributi):
i tre attributi sono co-presenti e producono significato solo
congiuntamente. È inoltre una verifica delle
[equivalenze AILA](/ontologia/aila/derivazioni/equivalences):
strutture costruite ontologicamente convergono con strutture
emerse statisticamente.

## Come usarlo

- **Lettura**: scarica lo zip e apri il `.docx` per il paper completo
- **Riproduzione**: usa il motore JSX e la suite JS — serve solo
  Node.js e un endpoint LLM per il confronto
- **Pairing AI**: carica paper + `comparison-data.json` come contesto,
  chiedi al modello di proporre nuovi domini simbolici chiusi su cui
  ripetere il test (sistemi runici, I Ching, ecc.)

## Note

Studio del **gennaio 2026**. Pubblicato come pacchetto unico
autocontenuto. Le divergenze sulle carte rovesciate sono una
direzione di ricerca aperta: distinguere tradizioni interpretative
diverse è un segnale, non un errore.
