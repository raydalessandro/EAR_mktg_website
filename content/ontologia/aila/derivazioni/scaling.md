---
title: "Scaling"
summary: "Derivazione da primi principi dell'esponente ε = A/D = 3/4 — Kleiber, Hurst, 432 = D²×A³."
type: aila-derivation
version: "1.1"
status: published
order: 70
tags: [aila, scaling, kleiber]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/EAR_SCALING_AILA_v1_1.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/teoremi/4-scaling-dimensionale
  - ontologia/aila/operazionale/transitions
featured: false
---

## Cos'è

`EAR_SCALING_AILA_v1.1` deriva da primi principi il **teorema di scaling
strutturale** `ε = A/D = 3/4`: ogni sistema auto-osservante con A attributi
in D dimensioni scala con esponente A/D. Da qui discendono Kleiber (1932),
l'esponente di Hurst, la fattorizzazione duale `432 = D² × A³` e la perdita
strutturale `Δ% = π/A² ≈ 0.349%`.

## Posizione nel sistema

È la trasposizione in AILA del Teorema 4 (vedi
[teorema scaling dimensionale](/ontologia/teoremi/4-scaling-dimensionale)).
Mentre il KERNEL afferma `A := 3` (Δ, ⇄, ⟳) e `D := 4` (3 spazio + 1 tempo),
SCALING li combina in quattro formule fondamentali — F1 struttura
(`432 = D²×A³`), F2 resistenza (`Σ = 432/π ≈ 137.51`), F3 scaling
(`ε = 3/4`), F4 perdita (`Δ = π/9`) — senza parametri liberi. La derivazione
canonica della costante di struttura fine è documentata nel Trattato §RESISTANCE.

## Perché è utile con AI

Avere SCALING in contesto permette all'AI di **predire quantitativamente**
gli esponenti allometrici di qualsiasi sistema noti A e D, distinguere
sistemi completi (ε = 3/4) da degeneri (`ε = 2/4`, `1/4` se mancano
attributi), e verificare se una deviazione osservata segnala patologia
(es. tumori con `Δ_scaling = |β̄ - θ| ≠ 0`). Fornisce inoltre il legame
diretto tra struttura ontologica e costanti fisiche misurate.

## Come usarlo

- Carica il file insieme a [Kernel](/ontologia/aila/sistema-formale/kernel) per le premesse A, D
- Applicazioni dirette: metabolismo (ε = 3/4), frequenza cardiaca (-1/4),
  vita media (1/4), serie temporali (Hurst ~0.75)
- Test di falsificazione: cercare sistemi con esponente 3/4 ma <3 attributi,
  oppure `Σ_output > Σ_input` (vietato dalla teoria)
- Pairing utile con [Coherence](/ontologia/aila/empirico/coherence) per leggere
  `+1/12` cerebrale come surplus di integrazione

## Note

Versione 1.1 (gennaio 2026). Cita Kleiber 1932, West-Brown-Enquist 1997,
Hurst 1951, CODATA 2018. Estende v1.0 con derivazione dettagliata,
fattorizzazione duale e condizioni di falsificazione esplicite.
