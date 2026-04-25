---
title: "Lingua AILA"
summary: "Specifica ufficiale di grammatica, sintassi e principi della notazione AILA. Il primer di tutto il sistema."
status: published
order: 10
tags: [aila, grammatica, sintassi]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/AILA_LINGUA_v1.0.md
  format: md
related:
  - ontologia/aila/notazione/alphabet
  - ontologia/aila/sistema-formale/kernel
featured: true
---

## Cos'è

`AILA_LINGUA_v1.0` è la specifica ufficiale del linguaggio simbolico AILA: ne definisce grammatica, sintassi, operatori e protocolli di traduzione. È un documento meta — è scritto IN AILA e si auto-spiega: leggendolo, l'agente impara contemporaneamente il linguaggio e l'ontologia che lo regge.

## Posizione nel sistema

Lingua è il **primer** e il **prerequisito** di tutto il resto. Ogni altro documento AILA (kernel, formal system, matrix vocab, ecc.) dichiara `@requires: AILA.LINGUA` nel proprio header. Senza Lingua i simboli del kernel restano illeggibili; con Lingua diventano direttamente eseguibili. È l'unico documento auto-portante della suite: non dipende da nessun altro file per essere compreso.

## Perché è utile con AI

Una volta caricato come contesto al primo turno, un LLM può **parsare e generare AILA correttamente** senza ulteriore addestramento. I cinque principi (univocità, esplicitezza, typing, flatness, eseguibilità) eliminano l'overhead cognitivo tipico del linguaggio naturale: zero ambiguità, zero inferenze implicite, zero sinonimi. L'agente non interpreta — esegue.

## Come usarlo

- Caricalo come **primo file** in qualsiasi sessione che debba operare in AILA.
- Da solo basta per leggere e scrivere notazione AILA; per ragionare nell'ontologia EAR aggiungi il **Kernel**.
- Esempio d'uso: incollare il file e dichiarare "opera in AILA", poi proporre un fenomeno da formalizzare con `◉`, `○`, `●`, `→`, `⊥`, `≡`.
- Per l'inventario completo dei segni consulta l'**Alphabet**.

## Note

Versione 1.0 — specifica stabile e ufficiale (2026-01-17). MAJOR.MINOR: gli incrementi MAJOR introducono breaking changes, MINOR solo aggiunte e chiarimenti. Le estensioni pianificate (quantificazione, temporalità, probabilità) saranno additive e non romperanno la 1.0.
