---
title: Come organizziamo i contenuti
summary: Convenzioni dell'antologia. Cartelle, frontmatter, slug, stati.
status: published
order: 1
tags: [meta, convenzioni]
authors: [ray]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
---

Questa scheda è un **placeholder funzionale** — serve a verificare che il
flusso di pubblicazione funzioni end-to-end. Sostituiscila quando inizi a
pubblicare contenuti reali.

## Convenzioni

Ogni cartella sotto `/content` è una sezione. Ogni file `.md` è un
documento foglia. Il file speciale `_section.md` descrive la cartella che
lo contiene (titolo, riassunto, stato).

La gerarchia è arbitraria: puoi annidare sotto-sezioni a piacere.
Aggiungere una nuova area significa creare una cartella e un `_section.md`
— niente registri da aggiornare.

## Frontmatter minimo

```yaml
---
title: "Titolo del documento"
summary: "Una riga che apparirà nelle card."
status: published   # published | draft | wip | coming-soon
tags: [esempio]
---
```

## Stati

- **published** — visibile a piena opacità
- **draft** — visibile, badge "Draft"
- **wip** — dimmed, badge "In costruzione"
- **coming-soon** — dimmed, badge "Coming soon" (per teaser)

Tutti i conteggi nelle card sezione sono calcolati a build time
attraversando l'albero — non c'è nulla da aggiornare a mano.
