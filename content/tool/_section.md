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

## Convenzione di scheda

```yaml
---
title: "Nome del tool"
type: tool
status: published
authors: [autore]
download:
  file: /downloads/tool/<slug>/<file>.zip
  format: zip
license: CC-BY-SA-4.0
---

## Cos'è
## Cosa puoi fare
## Setup rapido
## Architettura
## Note
```

Dove possibile il tool include test e documentazione interna. La
sezione cresce con script Python, plugin Claude Code, automazioni,
bot — tutto self-hosted o copia-incolla.
