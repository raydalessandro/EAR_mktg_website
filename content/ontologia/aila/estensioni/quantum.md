---
title: "Quantum"
summary: "Estensione quantistica AILA: introduce P8 (Selezione Strutturale) e T7 (Unità di Barriera) per le anomalie empiriche."
status: published
order: 10
tags: [aila, estensioni, quantum, P8, T7]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/estensioni/EAR_QUANTUM_AILA_v1.0.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/sistema-formale/formal-system
featured: true
---

## Cos'è

Estensione quantistica dell'AILA core. Aggiunge la **Proposizione 8 (Selezione Strutturale)** e il **Teorema 7 (Unità di Barriera)**, formalizzando la correlazione fra struttura dell'osservatore Σ(O) ed esiti misurati. Connette gli assiomi EAR alle anomalie quantistiche empiriche più discusse degli ultimi vent'anni, fornendo un calcolo esplicito dove le interpretazioni classiche restano descrittive.

## Posizione nel sistema

L'estensione **estende** il core (KERNEL + FORMAL_SYSTEM) — non lo sostituisce. Mantiene piena compatibilità con A1-A5 e con le proposizioni P1-P7 e i teoremi T1-T6 del sistema formale di base. Sopra questo strato aggiunge P8 e T7, con relativi corollari (C8.1-C8.3, C7.1-C7.4) e predizioni discriminanti (Pred.6-Pred.8). Richiede come dipendenze AILA_LINGUA_v1.0, EAR_KERNEL_AILA_v1.0 e EAR_FORMAL_SYSTEM_AILA_v1.0.

## Cosa risolve

- **Wigner's Friend** (Proietti 2019, Bong 2020): fatti osservatore-dipendenti spiegati come Σ(O₁) ≠ Σ(O₂).
- **Quantum eraser** (Kim 2000, Kastner 2019): la struttura del rivelatore determina la distribuzione, senza retrocausalità.
- **Contestualità Kochen-Specker** (Cabello 2022): contesto di misura come Σ(apparato), P8 dimostrata sperimentalmente.
- **Quantum Darwinism** (Zhu 2025): einselection come selezione strutturale dell'ambiente.
- **Bell senza entanglement** (Guo 2024): la variabile nascosta è nell'osservatore/setup, non nella particella.

## Perché è utile con AI

Permette al modello di applicare il framework EAR a problemi quantistici mantenendo coerenza formale: invece di scegliere fra interpretazioni concorrenti (Copenhagen, MWI, QBism, RQM), l'AI dispone di un calcolo unificato basato su Σ(O) e K(O). Genera predizioni testabili — ad esempio variance(outcomes) ∝ 1/K(O) — e disambigua interpretazioni di esperimenti classici riducendoli a istanze di P8.

## Come usarlo

- Caricare come contesto **aggiuntivo** al kernel/formal-system, mai isolato.
- **Pairing obbligatorio** con KERNEL_AILA_v1.x e FORMAL_SYSTEM_AILA_v1.x.
- Citare P8 e T7 con riferimento ai rispettivi corollari per derivazioni.
- Per predizioni quantitative usare le formule di C8.3 e C7.2 (ε ~ ℏ).

## Note

v1.0 official spec, frozen al 2026-01-19. Dipendenze: KERNEL_AILA_v1.x, FORMAL_SYSTEM_AILA_v1.x, MATRIX_VOCAB_AILA_v1.x. Eventuali revisioni saranno emesse come v1.1+ mantenendo retrocompatibilità con i riferimenti P8/T7.
