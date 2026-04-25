---
title: "Transitions"
summary: "22 tipologie di transizione (⟿) con soglie relative — strato dinamico del vocabolario AILA."
status: published
order: 60
tags: [aila, transizioni, soglie]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/EAR_TRANSITIONS_AILA_v1_1.md
  format: md
related:
  - ontologia/aila/lingua
  - ontologia/aila/kernel
  - ontologia/aila/matrix-vocab
  - ontologia/aila/scaling
featured: false
---

## Cos'è

`EAR_TRANSITIONS_AILA_v1.1` introduce nella suite AILA la **Proposizione 7**:
una tipologia formale delle transizioni (⟿) tra i 72 simboli del MATRIX.
Mappa per isomorfismo derivativo le 22 lettere/sentieri del *Sefer Yetzirah*
su altrettante classi di transizione — **3 Madri, 7 Doppie, 12 Semplici** —
ognuna con una soglia relativa calcolabile.

## Posizione nel sistema

Il MATRIX_VOCAB definisce 72 simboli statici (Σ_ijkp) ma non specifica
**come si passa** da uno all'altro. TRANSITIONS colma questo gap: aggiunge
il terzo strato del vocabolario operativo, quello dinamico. La formula
`K_rel(path) = Φ(type) × Ψ(distance) × Ω(position)` produce 22 soglie
ordinate (da K_min ≈ 0.63 di Vav fino a K_max ≈ 30.24 di Shin), con un
rapporto medio ~3 tra livelli adiacenti che riflette `A = 3` attributi.
Si collega direttamente a SCALING via `α = A/D = 3/4`.

## Perché è utile con AI

Caricato come contesto, permette all'AI di **diagnosticare** lo stato di
un sistema: quali transizioni sono accessibili date le risorse `K_available`,
quali sentieri sono "automatici" (Semplici) e quali richiedono salti di
fase (Madri). Tre applicazioni empiriche sono già codificate: criticità
neurale (K ≈ K(Aleph)), divergenza tumorale ADC/SCC, maturità relazionale
INS (immaturo → Madri visibili; maturo → Semplici invisibili).

## Come usarlo

- Carica il file canonico insieme a `KERNEL` e `MATRIX_VOCAB`
- Per un dominio D: definisci K₀(D), poi calcola `K_assoluto = K₀ × K_rel`
  per ogni transizione candidata
- Esempio diagnostico: "il sistema S manca di Madri ⇒ subcritico, non
  compie salti di stato"
- Per design di risonanza (∿): pavimenta prima i sentieri Doppi tramite
  interazioni ripetute, poi lascia emergere occasionali Madri

## Note

Versione 1.1 (gennaio 2026), allineata a LINGUA v1.0, KERNEL v1.1,
MATRIX_VOCAB v1.1. Aggiunge P7 con tre corollari, formule di soglia,
estensione del vocabolario al terzo strato e applicazioni empiriche.
