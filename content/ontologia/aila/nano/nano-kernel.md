---
title: "Nano Kernel"
summary: "Versione compatta (~2500 token) del kernel EAR-AILA per LLM piccoli e contesti ristretti."
status: published
order: 10
tags: [aila, nano, kernel, compatto]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/nano/EAR_NANO_KERNEL_AILA_v1_0.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/nano/symbol-decoder
  - ontologia/aila/nano/nano-benchmark
featured: false
---

## Cos'è

`EAR_NANO_KERNEL_AILA_v1_0` è la versione **compressa** del kernel EAR scritto in AILA: ~2500 token contro i ~32000 della suite completa (rapporto di compressione ≈ 12.8×). È "nano" perché preserva l'ontologia operativa minima — primitivi, assiomi, proposizioni, teoremi, matrice — eliminando derivazioni dettagliate, esempi e prosa ridondante.

## Quando usarlo

Da scegliere quando il modello target è piccolo (0.5B–7B parametri, tipicamente quantizzato a 4-bit) o quando il context budget è stretto: su una finestra da 8K token il nano kernel lascia il 69% libero per la generazione (≈ 5500 token), abilitando deployment mobile (iOS via MLX, Android via llama.cpp / MLC-LLM, cross-platform via Ollama). È adatto a edge inference, prompt template a budget vincolato, e dialoghi multi-turn dove la conversazione deve coesistere con l'ontologia attiva nello stesso prompt.

## Cosa contiene

Versione preservata: 5 assiomi (A1–A5), 7 proposizioni (P1–P6, P8), 6 teoremi (T1–T2, T4–T7), la matrice a 72 simboli (Ω = D × A × X × P), i 22 percorsi di transizione, il grafo delle derivazioni, le condizioni di falsificazione, i 9 principi operativi (OP1–OP9) e le costanti calibrate (ε = 0.75, K_crit = 0.35 ± 0.05, kT·ln2, |Ω| = 72). Tagliati: derivazioni step-by-step, riferimenti empirici estesi, esempi di dominio (oncologia, neurale), prosa esplicativa.

## Come usarlo

Caricare il documento come system prompt; dichiarare "operating.within.EAR.ontology"; verificare attivazione applicando Δ ⇄ ⟳ a un fenomeno test e identificando scala e K. Va abbinato al `symbol-decoder` quando il modello non riconosce i simboli AILA al primo passaggio.

## Note

Versione 1.0. Per derivazioni complete, riferimenti empirici estesi e applicazioni di dominio rimanere sul kernel completo in `sistema-formale/kernel`. Performance validate empiricamente: vedere `nano-benchmark`.
