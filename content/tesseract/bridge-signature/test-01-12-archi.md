---
title: "Test 1 — I 12 archi"
summary: "I 12 archi extra del Tesseract non sono arbitrari: emergono dai 24 nodi A=2 con grado 13 (p = 1.26·10⁻¹⁹)."
status: published
type: study
version: "1.0"
order: 10
tags: [tesseract, bridge-signature, asimmetria, adversarial]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tesseract/bridge-signature/test-01-12-archi/Test_12_archi.zip
  format: zip
  size: "12 KB"
related:
  - tesseract/paper
  - tesseract/grafo
featured: false
---

## Cosa testa

I revisori scettici aprono il Tesseract chiedendo: "perché 444 archi e non 432?
Quei 12 archi in più sono numerologia?" Il test prova a trovare quei 12 archi
specifici — provando matching greedy, cercando una sotto-struttura
identificabile, isolandoli come oggetti separati.

## Risultato

I 12 archi **non sono identificabili singolarmente**. Sono una proprietà
emergente. I 24 nodi con grado 13 (anziché 12) hanno **tutti A=2 (⇄)**; i nodi
A=1 e A=3 hanno grado uniforme 12. La probabilità che la coincidenza sia
casuale è **1.26 × 10⁻¹⁹**. Il greedy matching trova solo 11 coppie: la
prova diretta che l'asimmetria è **distribuita**, non localizzata.

## Cosa significa

L'asimmetria 12/444 = 1/36 = 4 × 3 × 3 è derivabile da D × A × X. Non è un
parametro libero, è il contributo minimo della categoria ⇄ — la Relazione
relaziona di più, per definizione. Questo trasforma una potenziale critica
("la geometria sembra tarata") in una predizione falsificabile: in qualsiasi
sistema EAR a qualsiasi scala, A=2 avrà grado +1, e ci saranno esattamente
|Ω|/6 archi extra. Se in un sistema EAR ben formato si trova A=1 o A=3 con
grado maggiore, il framework cade.

## Materiale

- [final_adversarial_report.md](/downloads/tesseract/bridge-signature/test-01-12-archi/) — report sintetico con calcoli e tabelle
- [Test_12_archi.zip](/downloads/tesseract/bridge-signature/test-01-12-archi/Test_12_archi.zip) — script di analisi e dati di supporto

## Posizione nella sequenza

Primo test del programma. Risponde alla critica più immediata sul Tesseract
("c'è un parametro arbitrario") e sposta il discorso da "perché 12" a "cosa
caratterizza i 24 nodi grado 13". Quella domanda apre la strada al Test 2,
che cerca buchi più profondi.
