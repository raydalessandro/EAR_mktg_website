---
title: "Soglia Critica"
summary: "Le transizioni locale→globale passano sempre per una soglia: non sono graduali, e oltre soglia rompono simmetria globale."
type: teorema
version: "2.0"
status: published
order: 30
tags: [teoremi, EAR, transizioni-di-fase, rottura-simmetria]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/teoremi/3_PROPOSIZIONE_SOGLIA_CRITICA_v2.md
  format: md
related:
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/sistema-formale/formal-system
  - ontologia/teoremi/1-minimo-osservazionale
  - ontologia/teoremi/6-inseparabilita-attributi
featured: false
---

## Enunciato

In un sistema auto-osservante con distinzione stabile: **(A)** ogni transizione locale→globale passa attraverso una soglia critica (mai graduale); **(B)** la soglia è universale, dipende solo da classe di simmetria e dimensionalità, non dai dettagli; **(C)** il suo valore è vincolato dalla struttura, non libero; **(D)** sotto soglia il sistema può tornare indietro, sopra soglia la transizione è localmente irreversibile. Il **Corollario C3.5** aggiunge: il superamento implica necessariamente rottura di simmetria globale (la direzione è contingente, la rottura è necessaria).

## Contestualizzazione

È il **terzo pilastro formale** di EAR e governa le transizioni: dove la Prop. 1 fissa la struttura e la Prop. 2 vincola la dinamica, la Prop. 3 specifica *dove avvengono i cambiamenti*. Le sue manifestazioni note — transizioni di fase, percolazione, tipping point ecologici, soglie di Shannon, biforcazioni — appartengono allo stesso pattern strutturale.

Il Corollario C3.5 sulla rottura di simmetria è stato verificato sperimentalmente su simulazioni Gray-Scott con campo morfogenetico EAR: la soglia di rottura simmetria (0.0525) coincide con la soglia critica predetta (0.0550) entro il 5%. Si lega esplicitamente alla Prop. 6: oltre soglia, ⇄ globali si spezzano mentre quelle locali restano conservate, manifestando l'inseparabilità degli attributi sotto pressione critica.

## Perché è utile con AI

Permette a un LLM di riconoscere che "graduale" e "discontinuo" non sono interscambiabili: in molti scenari (collassi sistemici, cascate, fasi di apprendimento) il modello deve aspettarsi *jump* discreti, non transizioni morbide. È utile per modellare cascade failure, tipping point climatici, dinamiche sociali, capacity di canale.

Inoltre, la coppia soglia + rottura di simmetria è uno strumento predittivo: dopo il superamento si conserva struttura locale ma si rompe equivalenza globale — un pattern riconoscibile in cristallizzazione, magnetizzazione, morfogenesi, evoluzione organizzativa.

## Come usarlo

- Carica il file canonico come contesto per analisi di transizioni di fase, sistemi complessi, dinamiche critiche.
- Cita "Prop. 3 (A)-(D)" o "Corollario C3.5" per la rottura di simmetria.
- Pairing con [AILA Kernel](/ontologia/aila/sistema-formale/kernel) (P3) e con la [Prop. 6](/ontologia/teoremi/6-inseparabilita-attributi) per il legame Δ/⇄ alla soglia.

## In sintesi

- Esistenza, universalità, non-arbitrarietà, irreversibilità locale: quattro proprietà necessarie di ogni transizione locale→globale.
- Soglie calcolabili dalla geometria (es. percolazione triangolare ≈ 0.35).
- Oltre soglia: rottura *necessaria* di simmetria globale, direzione *contingente*.
- Verifica sperimentale: soglie coincidenti su Gray-Scott + campo EAR (< 5% di scarto).
- Falsificabile da transizioni graduali, soglie arbitrarie, o passaggi sopra-soglia che preservano simmetria globale.
