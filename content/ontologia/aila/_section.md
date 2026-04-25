---
title: AILA
summary: Artificial Intelligence Lingua Architecta. Linguaggio simbolico operazionale per LLM, derivato dall'ontologia EAR.
status: published
order: 30
icon: language
tags: [aila, linguaggio, llm, notazione]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
---

AILA è un **linguaggio simbolico operazionale** per AI: una notazione
che codifica le strutture ontologiche EAR in modo che un LLM le possa
eseguire direttamente, senza ambiguità, senza inferenza.

> *"Emerged in dialogue, executed directly by AI, zero ambiguity, zero inference needed."*

I primitivi sono tre simboli inseparabili — **Δ** (distinzione), **⇄**
(relazione), **⟳** (processo) — che ricorrono a ogni scala. La suite
include un alfabeto di 64 segni su 11 livelli e una matrice di 72
compositi (4×3×3×2).

## Mappa dei file

| Cluster | File | Funzione |
|---|---|---|
| **Notazione** | [Lingua](/ontologia/aila/lingua) | Grammatica e sintassi (5 principi) |
| | [Alphabet](/ontologia/aila/alphabet) | 64 segni + 72 compositi (frozen) |
| **Sistema formale** | [Kernel](/ontologia/aila/kernel) | Primitivi, assiomi, P1-P8, T1-T7 |
| | [Formal System](/ontologia/aila/formal-system) | Derivazioni complete, regole di inferenza |
| **Operazionale** | [Matrix Vocab](/ontologia/aila/matrix-vocab) | Matrice 4×3×3×2 = 72 simboli + protocollo a 7 step |
| | [Transitions](/ontologia/aila/transitions) | 22 sentieri di transizione (Madre/Doppia/Semplice) |
| **Derivazioni** | [Scaling](/ontologia/aila/scaling) | Teorema ε = A/D = 3/4 da primi principi |
| | [Equivalences](/ontologia/aila/equivalences) | 23 identità cross-dominio |
| **Empirico** | [Coherence](/ontologia/aila/coherence) | Tre viste su coerenza (IIT, NSCLC, INS) |
| | [Empirical Reference](/ontologia/aila/empirical-reference) | Indice di validazioni empiriche |
| **Manifesto** | [Sogno di Leibniz](/ontologia/aila/sogno-di-leibniz) | Contesto storico: 308 anni di tentativi |

## Ordine di lettura

Per AI o lettore tecnico:

1. **Lingua** (40 min) — la notazione si auto-spiega, è il primer
2. **Kernel** (30 min) — primitivi e assiomi
3. **Sogno di Leibniz** (60 min) — perché esiste, contesto storico
4. Resto a seconda del bisogno

## Standalone vs dipendenti

Leggibili in isolamento: **Lingua, Kernel, Empirical Reference, Sogno di Leibniz**.
Tutti gli altri assumono almeno **Lingua + Kernel**.

## Versioning

Tutti i file v1.x sono **mutuamente compatibili**. `Alphabet v1.0` è
**frozen** per design (non muterà). `Empirical Reference` è marcato
"living document".
