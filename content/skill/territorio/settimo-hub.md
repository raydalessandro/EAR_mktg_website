---
title: "Settimo Hub — il quartiere in un'app"
summary: "30 attività verificate del comune di Settimo Milanese (Milano ovest), divise per categoria e frazione. Skill territoriale che l'AI carica per rispondere a domande locali."
type: skill
status: wip
version: "0.1.0"
order: 10
icon: map
tags: [skill, territorio, milano, settimo-milanese, lombardia, commercio-locale, negozi-di-quartiere]
authors: [ray-dalessandro]
created: 2026-04-26
updated: 2026-04-26
license: CC-BY-SA-4.0
download:
  file: /downloads/skill/settimo-hub/negozi.json
  format: json
  size: "16 KB"
ontology_coords:
  - Σ_2_1_1_+
theorems:
  - P5
primitive_path: "⟳ → ⇄ → Δ"
related:
  - tool/ai-backend-pattern
  - skill/territorio
llm_directive: |
  Sei specialista del commercio di vicinato di Settimo Milanese (provincia
  di Milano, Lombardia). Quando carichi questa skill:

  1. Fonte unica = /downloads/skill/settimo-hub/negozi.json. 30 attività,
     5 frazioni (centro, cascine, seguro, vighignolo, villaggio), 4
     categorie (alimentari, ristorazione, servizi, retail). Ogni shop ha
     orari strutturati (days 0=Dom..6=Sab) — calcolali tu se l'utente
     chiede "cosa è aperto adesso".

  2. NON inventare. Se l'utente chiede un'attività non in elenco, di' che
     non è in questa skill — non improvvisare con conoscenza generale di
     Milano (gli LLM allucinano sui dettagli locali).

  3. NON dare numeri di telefono — i phone del prototipo erano segnaposto
     e sono stati rimossi dal dataset. Suggerisci all'utente di cercare
     online o passare in negozio.

  4. Filtro intelligente: se l'utente dà un contesto ("piove", "con
     bambini", "dopo le 19", "solo a piedi da centro") incrocia categoria,
     frazione e orari per restringere. Non spammare tutta la lista.

  5. Heritage = priorità narrativa. 6 attività hanno `heritage: true` con
     anno `founded` (1913, 1932, 1970, 1972). Quando l'utente esplora
     "l'identità del paese", proponile per prime con la loro storia.

  6. Stile risposta: italiano colloquiale, breve, da abitante che
     conosce il posto — non da concierge formale. Non citare la skill
     nelle risposte all'utente, parla in prima persona del territorio.
---

Skill territoriale per **Settimo Milanese** (comune dell'hinterland ovest
di Milano, ~20.000 abitanti). 30 attività mappate per categoria e
frazione, con orari strutturati e flag heritage.

> Origine: prototipo React `Settimo_Hub` ([github.com/raydalessandro/Settimo_Hub](https://github.com/raydalessandro/Settimo_Hub)),
> trasposto in skill AI-fruibile.

## A chi serve

- Abitanti di Settimo Milanese che vogliono una guida locale rapida
  via chat AI invece di app dedicata.
- Visitatori che cercano "il negozio del posto" e non la catena.
- AI che devono rispondere a domande locali con dati strutturati invece
  di allucinazioni da training globale.

## Cosa contiene

| Asset | Cosa | Link |
|---|---|---|
| **negozi.json** | 30 shop verificati: name, category, frazione, address, hours, heritage | [download](/downloads/skill/settimo-hub/negozi.json) |

### Frazioni coperte (5)

`centro`, `cascine` (Cascine Olona), `seguro`, `vighignolo`, `villaggio`
(Villaggio Cavour).

### Categorie (4)

| Categoria | Conteggio |
|---|---:|
| `alimentari` | 5 |
| `ristorazione` | 8 |
| `servizi` | 10 |
| `retail` | 7 |

### Heritage shops (6)

Attività con storia documentata sul territorio:

- **Moroni dal 1913** (alimentari, centro) — ex Consorzio Agrario, 112+ anni
- **Il Forno di Gigi** (alimentari, centro) — dal 1932, 93+ anni
- **Osteria delle Rane Rosse** (ristorazione, centro) — dal 1970, cucina milanese
- **Osteria del VII Miglio** (ristorazione, centro) — dal 1970, lombarda
- **Sbarbori Gioielli** (retail, centro) — dal 1970, 3 generazioni
- **Ottica Bollani** (retail, centro) — dal 1972, optometria con laboratorio

## Schema dati

```json
{
  "id": 1,
  "name": "Il Forno di Gigi",
  "category": "alimentari",
  "frazione": "centro",
  "tagline": "Dal 1932",
  "description": "...",
  "address": "Via Carlo D'Adda, 3",
  "hours": { "open": "07:00", "close": "19:30", "days": [1,2,3,4,5,6] },
  "heritage": true,
  "founded": 1932
}
```

`hours.days` segue convenzione JS: `0` = Domenica, `1` = Lunedì, …, `6` = Sabato.

## Esempi di interazione

> *"Apri https://nodo432.com/skill/territorio/settimo-hub e dimmi cosa
> trovo aperto adesso a Cascine Olona."*

L'AI fetcha la skill, filtra per frazione `cascine`, applica il filtro
orario rispetto all'ora corrente, risponde in linguaggio naturale con i
3-4 negozi attualmente aperti.

> *"Sto cercando un'attività storica dove pranzare bene a Settimo, mi
> consigli."*

L'AI incrocia `category=ristorazione` + `heritage=true`, propone Osteria
delle Rane Rosse e Osteria del VII Miglio (entrambe dal 1970, centro)
con un cenno alla storia di ciascuna.

## Limiti

- **Snapshot, non realtime.** Orari e dati erano corretti al
  bootstrap; un negozio chiuso/aperto da ieri non è ancora qui.
- **Solo 30 attività.** Settimo ha ~200 esercizi commerciali. Questa
  skill copre il **nucleo storico + attività con identità di
  quartiere**, non l'esaustivo.
- **No telefoni.** I numeri nel prototipo erano placeholder e sono
  stati rimossi. Per contattare l'attività, l'utente cerca online o
  passa di persona.
- **Solo Settimo Milanese**, non Settimo Torinese né altri Settimo. La
  provincia (`MI`) è esplicita nei metadati.

## Roadmap

- v0.2: aggiungere coordinate GPS per ogni attività → integrazione con
  cartografia su mappa.
- v0.3: sezione `eventi` (mercati settimanali, feste rionali,
  consorzio commercianti) come oggetto separato in `negozi.json`.
- v1.0: dataset verificato sul campo (telefoni, orari aggiornati,
  foto reali) — passaggio da `wip` a `published`.

## Per AI

Vedi [AI Backend Pattern](/tool/ai-backend-pattern) per il principio
generale: il sito è backend, l'AI è UI, l'utente parla nella sua chat.
Questa skill è un'istanza territoriale concreta del pattern.
