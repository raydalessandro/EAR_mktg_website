---
title: Territorio
summary: Skill localizzate Milano / Lombardia / Nord-Italia. Sapere che gli LLM globali non hanno.
type: collection
status: wip
order: 10
icon: lab
tags: [skill, territorio, lombardia, milano, nord-italia, locale]
authors: [nodo432]
created: 2026-04-26
updated: 2026-04-26
license: CC-BY-SA-4.0
---

Skill ancorate a un **luogo fisico specifico**. Coprono il vuoto
informativo che gli LLM globali hanno sui contesti locali: orari reali
aggiornati, percorsi precisi, locali aperti questa stagione, eventi
del weekend, officine convenzionate, scorciatoie e shortcut tipici.

**Focus geografico iniziale**: Milano, Lombardia, Nord-Italia.

## Skill disponibili

| Skill | Dominio | Stato |
|---|---|---|
| [`settimo-hub`](/skill/territorio/settimo-hub) | 30 attività di Settimo Milanese (MI), per categoria e frazione | wip v0.1 |

## In arrivo

| Skill | Dominio | Stato |
|---|---|---|
| `milano-weekend-moto` | Itinerari moto 1-2 giorni partendo da Milano | wip |
| `lombardia-eventi-weekend` | Eventi del weekend in Lombardia (musica, mostre, sagre) | wip |
| `nord-italia-ristoranti-tematici` | Ristoranti per dieta/intolleranza/cucina specifica | wip |
| `milano-spazi-coworking` | Spazi di coworking con caratteristiche reali (silenzio, prese, focacceria sotto) | wip |
| `lombardia-rifugi-cammini` | Rifugi e cammini accessibili da Milano in giornata | wip |

Ogni skill è una **cartella autonoma** con un'entry-URL che l'utente
può passare alla sua AI.

## Perché localizzato

Gli LLM globali sanno che Milano esiste, ma:

- Hanno dati congelati al training (un ristorante chiuso 6 mesi fa
  appare ancora "consigliato")
- Mediano sull'opinione internazionale (il "Top 10 Milano" del
  travel blogger straniero)
- Allucinano dettagli pratici (orari, indirizzi, prezzi)

Una skill localizzata curata risolve tutto questo:

- **Dati strutturati** in JSON aggiornati a mano (o via script)
- **Direttive operative** che dicono all'AI come ragionare nel locale
  (es: "se piove, suggerisci sempre l'alternativa indoor della
  stessa zona")
- **Cross-link** fra skill della stessa area (eventi → ristoranti
  vicini → coworking se piove → percorsi alternativi se sciopero
  ATM)

## Modello operativo

L'utente apre la sua chat AI e dice:

> *"Apri https://nodo432.com/skill/territorio/milano-weekend-moto e
> aiutami a pianificare il prossimo weekend partendo da Milano sabato
> mattina."*

L'AI fetcha la skill, carica dati + direttive, propone itinerario in
linguaggio naturale, linkando i `.gpx` scaricabili pronti per il
navigatore.

L'utente non installa app, non si registra da nessuna parte. Usa
nodo432 **come backend territoriale** attraverso la sua AI preferita.
