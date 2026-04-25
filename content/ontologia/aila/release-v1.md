---
title: "AILA v1.0 — Release Package"
summary: "Pacchetto completo AILA v1.0: docs, kernel, decoder, tokenizer di riferimento e LICENSE."
status: published
order: 999
tags: [aila, release, distribuzione, package]
authors: [nodo432]
created: 2026-01-24
updated: 2026-01-24
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/release/AILA-v1.0.zip
  format: zip
  size: "32 KB"
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/nano
featured: false
---

## Cos'è

Pacchetto di distribuzione completo dell'AILA v1.0. Una sola fetch contiene tutto il necessario per integrare AILA in un sistema esterno: documentazione concettuale, quick start operativo, specifiche di kernel, decoder e translator, oltre a un tokenizer di riferimento in TypeScript. Pensato come snapshot stabile e auto-contenuta, evita di ricomporre i singoli file canonici sparsi sul sito.

## Cosa contiene

| Path | Cosa è |
|---|---|
| `README.md` | Overview del pacchetto e indice dei contenuti |
| `LICENSE` | Licenza CC-BY-SA-4.0 |
| `.gitignore` | Esclusioni standard per integrazione in repo Git |
| `docs/INTRODUCTION.md` | Introduzione concettuale ad AILA |
| `docs/GETTING_STARTED.md` | Quick start operativo per integratori |
| `docs/BENCHMARK.md` | Risultati di benchmark e metriche di compressione |
| `docs/DECODER.md` | Documentazione del decoder simboli |
| `docs/KERNEL.md` | Specifica del kernel EAR |
| `specs/translator/README.md` | Specifica del translator (testo naturale ↔ AILA) |
| `proof/tokenizer.ts` | Tokenizer di riferimento in TypeScript |

## Quando usarlo

Per **integrazioni in sistemi esterni** quando serve una snapshot stabile e versionata invece di file dispersi sul sito. Adatto a distribuzioni offline, mirror, build riproducibili, audit di compliance e fork accademici. Se il tuo target è prototipare rapidamente, valuta in alternativa la versione **nano** o i singoli file canonici linkati dalle schede di /ontologia/aila/.

## Note

Il pacchetto è una **snapshot v1.0**. I file canonici aggiornati vivono comunque nel sito (sezioni di /ontologia/aila/) con eventuali aggiornamenti v1.1+. Per integrazioni che richiedono le ultime correzioni, fai riferimento alle schede online; per stabilità contrattuale, ancorati al .zip versionato.
