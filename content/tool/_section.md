---
title: Tool
summary: Strumenti pronti all'uso. Bot, automazioni, plugin, script.
type: collection
status: published
order: 30
icon: terminal
tags: [tool, automazione]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
---

Strumenti **pronti all'uso** che orchestrano AI o ne estendono la
fruibilità. Ogni tool ha una scheda con descrizione, requisiti, setup,
e un download canonico (zip / repo / pacchetto npm) — sotto la licenza
dichiarata nel frontmatter.

## In evidenza

- **[AI Backend Pattern](/tool/ai-backend-pattern)** — il pattern di
  design che governa nodo432 stesso: trasforma un sito statico in
  backend per intelligenze esterne, l'AI dell'utente fa da UI dinamica.
  Il META-tool del progetto.
- **[Claude Code via Telegram](/tool/ear-claude-telegram-bot)** — bot
  self-hosted per controllare Claude Code dal telefono.

## Convenzione di scheda

```yaml
---
title: "Nome del tool"
type: tool                           # tool | methodology | pattern
status: published
authors: [autore]
download:                            # opzionale (un pattern può non averlo)
  file: /downloads/tool/<slug>/<file>.zip
  format: zip
license: CC-BY-SA-4.0
llm_directive: |                     # opzionale, se il tool include un metodo
  Direttiva operativa compatta.
---

## Cos'è
## Cosa puoi fare / Quando applicarlo
## Setup rapido / Come applicarlo
## Architettura
## Note
```

Dove possibile il tool include test e documentazione interna. La
sezione cresce con script Python, plugin Claude Code, automazioni,
bot, **e pattern di design** — tutto self-hosted, copia-incolla, o
replicabile.
