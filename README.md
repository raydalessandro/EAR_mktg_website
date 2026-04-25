# nodo432

Hub di orchestrazione AI. Antologia, risorse, tool e pipeline.

Sito statico costruito con Next.js 14 (App Router, static export), deployato
su GitHub Pages al dominio `nodo432.com`.

## Stack

- **Next.js 14** con `output: 'export'` → sito 100% statico
- **TypeScript** + **Tailwind CSS**
- **Markdown** come storage dei contenuti (file `.md` nel repo)
- **Zod** per validare il frontmatter
- Niente backend, niente database, niente CMS

## Struttura

```
/app                      # Next.js App Router
  layout.tsx              # nav + footer + canvas BG globale
  page.tsx                # home (router visivo)
  [...slug]/page.tsx      # route catch-all per qualsiasi profondità
  sitemap.ts
  not-found.tsx
/components               # SpiralLogo, ResonanceField, Nav, Footer, card, view
/lib
  content.ts              # tree walker + loader markdown
  schema.ts               # schema Zod del frontmatter
/content                  # il "database" del sito
  /antologia/_section.md
  /risorse/_section.md
  /tool/_section.md
  /pipeline/_section.md
/public/downloads/        # file scaricabili linkati dai documenti
/public/CNAME             # nodo432.com
```

## Aggiungere contenuti

Una **sezione** è una cartella con un `_section.md` che la descrive:

```yaml
---
title: Antologia
summary: Concetti, framework e metodologie.
status: published
order: 10
---
```

Un **documento** è un file `.md` con frontmatter:

```yaml
---
title: "Titolo"
summary: "Una riga di sintesi."
status: published
tags: [esempio]
download:                # opzionale
  file: /downloads/foo.md
  format: md
license: CC-BY-SA-4.0
---
```

Le sezioni si annidano a piacere. La route catch-all gestisce qualsiasi
profondità: nessuna route da aggiungere quando crei nuove cartelle.

Vedi `/risorse/template-frontmatter` sul sito (o
`/public/downloads/template-frontmatter.md`) per il template completo.

## Sviluppo locale

```bash
npm install
npm run dev          # http://localhost:3000
npm run build        # genera /out (sito statico)
npm run typecheck
```

## Deploy

Hosted su **Vercel** (Next.js framework preset). Ogni push su `main`
deploya in produzione, ogni push su altri branch o PR genera un URL di
preview automatico.

Dominio: `nodo432.com` configurato come custom domain in Vercel.

> Il file `public/CNAME` resta nel repo come backup: se in futuro si
> torna a GitHub Pages basta riabilitare la action e i DNS, niente
> altro da cambiare nel codice.

## Licenza

I contenuti pubblicati hanno la licenza dichiarata nel frontmatter di
ciascun documento (default suggerito: CC-BY-SA-4.0). Il codice del sito
è di proprietà degli autori.
