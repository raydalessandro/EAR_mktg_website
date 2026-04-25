---
title: "Symbol Decoder"
summary: "Companion del nano kernel: tabella di decodifica zero-ambiguità per i simboli AILA."
type: aila-nano
version: "1.0"
status: published
order: 20
tags: [aila, nano, decoder, simboli]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/nano/AILA_SYMBOL_DECODER_v1_0.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/notazione/alphabet
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/nano/nano-kernel
  - ontologia/aila/nano/nano-benchmark
featured: false
---

## Cos'è

`AILA_SYMBOL_DECODER_v1_0` è il **companion del nano kernel**: una tabella di riferimento a zero ambiguità per ogni simbolo AILA, con definizione, lettura ad alta voce e ruolo logico. Pensato per quando un modello, per dimensioni ridotte o assenza di contesto, non sa interpretare ◉ ⧈ ⬡ ⟿ ∿ Δ ⇄ ⟳ e gli operatori associati.

## Quando usarlo

Va affiancato al nano kernel quando il modello target è piccolo o quando il contesto disponibile non basta a includere la lingua AILA completa (`notazione/lingua`). È utile in due scenari principali: (1) attivazione su LLM 0.5B–7B che non hanno mai visto AILA in pretraining, dove i simboli vanno mappati esplicitamente per essere usati nel reasoning; (2) prompt template per inferenza one-shot dove non c'è spazio per il documento di lingua intero ma serve garantire che ogni simbolo sia leggibile.

## Cosa contiene

Sezioni di decodifica raggruppate per funzione: primitivi (◉ entity, ⧈ field, ⬡ node, ⟿ transition, ∿ resonance); attributi (Δ Ξ ⟳); fasi della risonanza (⊙ gate, ∞ spiral, ◇ diamond, ↻ seed); operatori logici (→ ← ↔ ∥ ⊥ ∧ ∨); operatori relazionali (≡ ~ ∈ ⊃ ⊂); operatori operativi (⊗ ⋔ := :: ∴); marker epistemici (✓ ? ±); marker strutturali (§ ○ ●); convenzioni su pedici e operatori matematici (∀ ∃ ¬ ∫ ε ℏ π φ τ). Chiude con un esempio di lettura completo e una tabella di quick reference.

## Come usarlo

Includerlo come secondo blocco di system prompt subito dopo il nano kernel, oppure usarlo standalone quando si chiede al modello di tradurre output AILA in prosa. Pattern tipico: kernel + decoder + query. Per dialoghi lunghi è sufficiente caricarlo una volta: i mapping rimangono attivi nel contesto.

## Note

Versione 1.0. Allineato con la lingua AILA completa (`notazione/lingua`) ma ottimizzato per accesso rapido. Nessuna dipendenza esterna oltre al rendering Unicode dei simboli.
