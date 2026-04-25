---
title: AILA Nano
summary: AILA in formato compatto. Per LLM piccoli o contesti limitati.
type: collection
status: published
order: 70
icon: zap
tags: [aila, nano, compact, llm-light]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
---

Versione **compatta** dell'AILA — pensata per quando lavori con modelli
linguistici piccoli o contesti limitati (token budget stretto, edge
inference, modelli specializzati). È la stessa ontologia, ridotta
all'essenziale operativo: il kernel più stringato, un decoder dei
simboli per il bootstrap rapido, e un benchmark che misura la fedeltà
rispetto alla versione completa.

## Quando usarla

- LLM con < 100K tokens di context window
- Modelli piccoli (1-7B parametri) dove il prompt grande satura attenzione
- Onboarding rapido prima di passare al kernel completo
- Embedding in prompt template / system message dove ogni token conta
