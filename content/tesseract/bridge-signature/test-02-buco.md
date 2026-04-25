---
title: "Test 2 — Cercare il buco"
summary: "Cinque test adversarial cercano lacune nel framework: il pattern resiste a noise 20%, regole alternative e regole casuali."
status: published
type: study
version: "1.0"
order: 20
tags: [tesseract, bridge-signature, adversarial, falsificazione]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-02-buco/researcher_tests_complete.zip
  format: zip
  size: "20 KB"
related:
  - tesseract/paper
  - tesseract/bridge-signature/test-01-12-archi
featured: false
---

## Cosa testa

Una volta accettato che i 12 archi extra sono ontologici, restano altre vie di
attacco. Questo test simula in anticipo la second-order critique: cross-domain
(il pattern vale solo nel Tesseract?), regole alternative (Hamming ≤ 1
basterebbe?), regole casuali (è un artefatto?), robustezza al rumore (struttura
fragile?), dati linguistici reali (predizione confermata fuori?).

## Risultato

Il pattern A=2 → grado maggiore **emerge** in grafi sociali simulati e in
grafi linguistici, e nel corpus italiano reale le parole funzionali sono
**20× più frequenti** delle parole di contenuto. Il pattern **non emerge** con
regole Hamming né con regole casuali. La struttura **resiste al noise fino al
20%**. Il Tesseract con i suoi +8% di grado per A=2 risulta quindi
**conservativo** rispetto alla realtà empirica.

## Cosa significa

Il programma non sta misurando un artefatto delle regole kabbalistiche: sta
misurando una proprietà ontologica reale che le regole 9:3:1 catturano e altre
regole no. La predizione è falsificabile in modo concreto — qualsiasi corpus
in cui i nomi siano più frequenti delle preposizioni rompe il framework.

Restano due "buchi" non chiusi: come si connettono i cluster a livello 2 (la
ricorsione olografica), e perché proprio le regole kabbalistiche e non altre.
Il Test 3 li affronta direttamente.

## Materiale

- [researcher_tests_summary.md](/downloads/tesseract/bridge-signature/test-02-buco/) — sintesi dei cinque test
- [researcher_tests_complete.zip](/downloads/tesseract/bridge-signature/test-02-buco/researcher_tests_complete.zip) — script completi: cross-domain, find-the-hole, dati reali

## Posizione nella sequenza

Secondo test. Porta avanti il lavoro adversarial del Test 1 estendendolo dal
Tesseract puro a domini esterni. Lascia in piedi due dubbi residui che il
Test 3 dissolve trasformandoli in derivazioni esplicite.
