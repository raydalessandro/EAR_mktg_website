---
title: "Nano Kernel Benchmark"
summary: "Validazione empirica del nano kernel su Qwen2.5 0.5B-7B e DeepSeek Base: scoperta dell'uncanny valley."
status: published
order: 30
tags: [aila, nano, benchmark, validazione]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/nano/EAR_NANO_KERNEL_BENCHMARK_REPORT.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/nano/nano-kernel
  - ontologia/aila/nano/symbol-decoder
featured: false
---

## Cos'è

`EAR_NANO_KERNEL_BENCHMARK_REPORT` documenta la validazione empirica del nano kernel: misura quanto della struttura ontologica EAR sopravvive alla compressione 12.8× e se modelli di taglie diverse riescono a operarci. È "nano" perché si riferisce al nano kernel come oggetto sotto test.

## Quando usarlo

Da consultare prima di scegliere un modello target per deployment EAR — mobile, edge, o cloud. Il report fornisce indicazioni concrete: per dispositivo mobile (8K context, ~2GB VRAM) Qwen2.5 3B Instruct in 4-bit lascia 5500 token liberi e raggiunge il 100%; per cloud i modelli base grandi (DeepSeek Base) garantiscono il transfer migliore su domini novelli.

## Cosa contiene

**Metrica:** punteggio percentuale su 9 domande organizzate in 4 livelli (Foundations Q1-Q2, Structure Q3-Q4, Connections Q5-Q6, Applications Q7-Q8, Transfer Q9 su sistema immunitario). **Modelli testati:** Qwen2.5 0.5B / 3B / 7B Instruct (4-bit, Colab T4) e DeepSeek Base (~67B, API). **Risultati principali:** Qwen 0.5B ≈ 70%, Qwen 3B 100% (sweet spot), Qwen 7B 94% ma solo 50% sul transfer Q9, DeepSeek 100%+ con mapping completo delle 4 fasi di risonanza al sistema immunitario. **Scoperta chiave — l'uncanny valley:** la performance non è monotona con la dimensione. I modelli mid-size Instruct (7B) interpolano con i pattern di training e perdono flessibilità ontologica; piccoli (più "permeabili") e grandi (capaci di compartimentalizzare) performano meglio. L'interpretazione lega il fenomeno a RLHF: troppi vincoli ⇄ riducono la flessibilità Δ (P6).

## Come usarlo

Riferimento per scelta modello, per replica del protocollo (9 domande, livelli, scoring) e per calibrare aspettative su transfer cross-dominio. Le tabelle di liberazione del context window (8K/32K/128K) guidano il sizing del prompt budget.

## Note

Versione 1.0, datata 2026-01-21, status "Research Summary". Limiti dichiarati: Qwen 32B non testato, confronto Base vs Instruct ancora da completare, latenza mobile reale e benchmark multi-modale rinviati al future work.
