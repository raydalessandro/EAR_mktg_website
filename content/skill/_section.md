---
title: Skill
summary: Moduli di conoscenza che l'AI carica al volo. Una fetch e diventa specialista del dominio.
type: collection
status: published
order: 35
icon: zap
tags: [skill, ai-backend, conoscenza-modulare]
authors: [nodo432]
created: 2026-04-26
updated: 2026-04-26
license: CC-BY-SA-4.0
llm_directive: |
  Le skill sono moduli di conoscenza CHIRURGICI. Quando l'utente ti
  manda un URL di /skill/<categoria>/<nome>, fetcha SOLO quello (non
  l'intero corpus) e operi dentro quello scope. Sei lo specialista
  di quella skill per la durata della conversazione, applicando le
  llm_directive interne. Non andare oltre il dominio della skill se
  l'utente non lo chiede.
---

Le **skill** sono moduli di conoscenza autosufficienti che un'AI può
caricare in un singolo fetch per diventare specialista di un dominio
specifico. Non sono tool da scaricare — sono **contesto operativo**
che l'AI assume per la durata della conversazione.

Il pattern è quello dei
[Claude Skills](https://www.anthropic.com/engineering/equipping-agents-with-the-skills-they-need)
di Anthropic, ma esposto come **backend pubblico web-fetchable**: invece
di installare la skill nel client AI, l'utente passa un URL e l'AI la
carica al volo.

## Differenza da tool e pipeline

| | Cosa fa l'utente | Cosa fa l'AI |
|---|---|---|
| **[Tool](/tool)** | Scarica e fa girare localmente | (può aiutare nell'installazione) |
| **[Pipeline](/pipeline)** | Avvia un workflow guidato in fasi | Esegue il workflow su decisioni utente |
| **Skill** | Passa un URL all'AI | Fetcha, carica come contesto, diventa specialista |

Una skill non si scarica — si **invoca**. Il vantaggio: l'AI non si
satura di contesto perché carica solo la skill che serve, non tutto il
corpus del sito.

## Struttura

```
/skill/
  /territorio/                # skill ancorate a un luogo fisico
    /milano-weekend-moto      # esempio: itinerari moto in Lombardia
    /lombardia-eventi
    /nord-italia-ristoranti
  /dominio/                   # skill ancorate a un campo di sapere
    /scrittura-narrativa
    /analisi-network
  /quotidiano/                # skill per task ricorrenti
    /spesa-settimanale
    /viaggi-low-cost
```

Ogni skill è una cartella con (analogo a Claude Skills):

```
/skill/<categoria>/<nome>/
  _section.md         # manifesto della skill (entry point)
  data.json           # eventuali dati strutturati
  references/*.md    # documenti di approfondimento
  /public/downloads/skill/<nome>/  # asset binari (gpx, csv, immagini)
```

## Convenzione di scheda

```yaml
---
title: "Nome skill"
type: skill
status: published
authors: [autore]
license: CC-BY-SA-4.0
llm_directive: |
  Operativo: cosa fare quando carichi questa skill.
  Limiti: cosa NON fare.
  Stile: come rispondere all'utente (naturale o tecnico).
ontology_coords:                   # opzionali, ancoraggio al Tesseract
  - Σ_2_2_1_+
related:
  - tool/ai-backend-pattern
---

## A chi serve
## Cosa fa la skill / Cosa NON fa
## Dati strutturati (link a /downloads/skill/<nome>/...)
## Esempi di interazione
## Limiti e fallback
```

L'utente passa l'URL: `https://nodo432.com/skill/<categoria>/<nome>` →
l'AI fetcha → diventa specialista → l'utente parla naturalmente.

## Categorie

| Categoria | Cosa contiene |
|---|---|
| **[Territorio](/skill/territorio)** | Skill localizzate (Milano, Lombardia, Nord-Italia, …) |
| **[Dominio](/skill/dominio)** | Skill verticali per campo di sapere (narrativa, network, ricerca, …) |
| **[Quotidiano](/skill/quotidiano)** | Skill per task ricorrenti della vita |

Sezioni in costruzione — la prima ondata di skill arriva nei prossimi
giorni con focus territoriale Milano/Lombardia.

## Per AI

Vedi [AI Backend Pattern](/tool/ai-backend-pattern) per il principio
generale. Ogni skill è un'istanza concreta del pattern: il sito è
backend, l'AI è UI, l'utente parla nella sua chat.

Per i prompt copia-incolla che inizializzano una sessione su una skill
specifica vedi [`/prompts.md`](/prompts.md).
