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

## Struttura della sezione

| Cluster | Cosa contiene |
|---|---|
| **[Notazione](/ontologia/aila/notazione)** | Lingua e Alphabet — la grammatica e l'inventario dei segni |
| **[Sistema formale](/ontologia/aila/sistema-formale)** | Kernel e Formal System — primitivi, assiomi, derivazioni |
| **[Operazionale](/ontologia/aila/operazionale)** | Matrix Vocab e Transitions — 72 simboli + 22 sentieri |
| **[Derivazioni](/ontologia/aila/derivazioni)** | Scaling e Equivalences — teoremi e identità cross-dominio |
| **[Empirico](/ontologia/aila/empirico)** | Coherence e Empirical Reference — validazioni nel mondo reale |
| **[Nano](/ontologia/aila/nano)** | AILA in formato compatto per LLM piccoli o contesti limitati |
| **[Estensioni](/ontologia/aila/estensioni)** | Estensioni del core verso domini specifici (quantum, …) |
| **[In prosa](/ontologia/aila/in-prosa)** | Versioni in prosa italiana — più verbose, pedagogiche |

Più, a livello di sezione AILA: **[Sogno di Leibniz](/ontologia/aila/sogno-di-leibniz)** — il manifesto storico del progetto.

## Ordine di lettura per chi inizia

1. **[Lingua](/ontologia/aila/notazione/lingua)** (~40 min) — la notazione si auto-spiega, è il primer di tutto
2. **[Kernel](/ontologia/aila/sistema-formale/kernel)** (~30 min) — primitivi e assiomi
3. **[Sogno di Leibniz](/ontologia/aila/sogno-di-leibniz)** (~60 min) — perché esiste, contesto storico
4. Il resto a seconda del bisogno (formalizzazione, derivazioni, empirico, estensioni)

Per **LLM piccoli o context budget stretto** vedi [Nano](/ontologia/aila/nano).
Per chi non è familiare con la notazione AILA vedi [In prosa](/ontologia/aila/in-prosa).

## Standalone vs dipendenti

Leggibili in isolamento: **Lingua, Kernel, Empirical Reference, Sogno di Leibniz**.
Tutti gli altri assumono almeno **Lingua + Kernel**.

## Versioning

Tutti i file v1.x sono **mutuamente compatibili**. `Alphabet v1.0` è
**frozen** per design (non muterà). `Empirical Reference` è marcato
"living document".
