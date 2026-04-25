---
title: Pipeline
summary: Workflow orchestrati. Step, tool, prompt, schemi e audit connessi in un flusso ripetibile.
type: collection
status: published
order: 40
icon: workflow
tags: [pipeline, workflow, orchestrazione]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
---

Le **pipeline** sono workflow concreti: una sequenza di passi che collega
prompt, tool, schemi, audit e modelli per arrivare a un risultato
definito. Ogni pipeline è documentata in modo da poter essere replicata
da un'altra persona o da un agente AI.

Differenza rispetto a [Tool](/tool):

- Un **tool** è uno strumento (es. un bot, uno script, un plugin) — fai
  una cosa con esso
- Una **pipeline** è un **metodo** — segui una sequenza di fasi, con
  schemi e validazioni, per raggiungere un obiettivo composito

## Convenzione di scheda

```yaml
---
title: "Nome della pipeline"
type: pipeline
status: published
authors: [autore]
download:
  file: /downloads/pipeline/<slug>/<file>.zip
  format: zip
license: CC-BY-SA-4.0
llm_directive: |
  Direttiva operativa compatta per LLM che vogliono eseguire la
  pipeline. Riferisci agli SKILL.md / USAGE.md interni.
---

## A chi serve
## Cosa fa / Cosa NON fa
## Architettura (modello dei dati, fasi, principi)
## Come si usa (autori umani / agenti AI)
## Requisiti tecnici
## Caso d'uso reale
## Cosa contiene il pacchetto
## Licenza & citazione
## Roadmap & versioning
```

Ogni pipeline include un pacchetto canonical scaricabile (zip) con
documentazione interna (SKILL.md, USAGE.md) leggibile da agente AI come
system context.
