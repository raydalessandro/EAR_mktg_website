# nodo432

Hub di orchestrazione AI. Ontologia, risorse, tool e pipeline.

Sito statico costruito con Next.js 14 (App Router, static export), deployato
su Vercel al dominio `nodo432.com`.

> **Sito progettato per essere consumato da agenti AI.** I siti ormai sono
> sempre più territorio di scraping LLM. Qui l'AI-fruibility è dimensione
> strutturale, non aggiunta cosmetica. Vedi sezione **AI-fruibility**.

## Stack

- **Next.js 14** con `output: 'export'` → sito 100% statico
- **TypeScript** + **Tailwind CSS**
- **Markdown** come storage dei contenuti (file `.md` nel repo)
- **Zod** per validare il frontmatter
- Niente backend, niente database, niente CMS

## AI-fruibility

Ogni build genera automaticamente, dal tree `/content`, una serie di
endpoint pensati per LLM e agenti AI:

| URL | Cosa | Standard |
|---|---|---|
| `/llms.txt` | Mappa testuale del sito ottimizzata per LLM | [llmstxt.org](https://llmstxt.org/) |
| `/llms-full.txt` | Concatenazione di tutti i documenti pubblicati | — |
| `/index.json` | Catalogo strutturato: sezioni, documenti, slug, summary, tag, download, related | — |
| `/<slug>.md` | Sorgente markdown di ogni pagina (aggiungi `.md` a un URL pagina) | — |
| `/sitemap.xml` | Sitemap XML standard | sitemaps.org |
| `/robots.txt` | Allow esplicito a GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, ecc. | — |
| `/ai` | Pagina human-readable che spiega come consumare il sito da AI | — |

Inoltre, ogni pagina documento ha JSON-LD (`TechArticle` schema.org)
inline nell'HTML, con autore, data, licenza, link al raw markdown e al
download canonico.

Generazione: lo script `scripts/generate-ai-assets.mjs` viene eseguito
come `prebuild` di npm, leggendo `/content` e scrivendo i file in
`/public`. I file generati sono gitignorati (rigenerati a ogni build).

### Server MCP (roadmap — priorità alta)

Un server [Model Context Protocol](https://modelcontextprotocol.io)
dedicato a nodo432 è in roadmap. Esporrà come tool MCP:

- `list_documents(filter?)` — elenco completo o filtrato per tag / sezione / stato
- `read_document(slug)` — corpo markdown di un documento
- `get_section(slug)` — sotto-albero di una sezione con metadata
- `search(query)` — ricerca full-text (Pagefind)

Distribuzione prevista: pacchetto npm avviabile via `npx` per Claude
Desktop e altri client MCP, oppure endpoint HTTP/SSE (Vercel function)
per integrazione web. Il data layer attuale (`/index.json` + raw `.md`)
è già la base completa: il server MCP sarà un wrapper sottile.

## Struttura

```
/app                        # Next.js App Router
  layout.tsx                # nav + footer + canvas BG globale
  page.tsx                  # home (router visivo)
  [...slug]/page.tsx        # route catch-all per qualsiasi profondità
  ai/page.tsx               # guida per agenti AI
  sitemap.ts
  not-found.tsx
/components                 # SpiralLogo, ResonanceField, Nav, Footer, card, view, JsonLd
/lib
  content.ts                # tree walker + loader markdown (server-side)
  schema.ts                 # schema Zod del frontmatter
/scripts
  generate-ai-assets.mjs    # genera llms.txt, index.json, raw .md (eseguito in prebuild)
/content                    # il "database" del sito
  /ontologia/_section.md
  /risorse/_section.md
  /tool/_section.md
  /pipeline/_section.md
/public
  downloads/                # file canonici scaricabili (PDF, MD originali)
  CNAME                     # nodo432.com
  robots.txt
  # generati a build time:
  llms.txt, llms-full.txt, index.json
  <slug>.md mirror del tree /content
```

## Aggiungere contenuti

Una **sezione** è una cartella con un `_section.md` che la descrive:

```yaml
---
title: Ontologia
summary: Il sistema concettuale fondante.
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
related:
  - ontologia/teoremi/3-soglia-critica
---
```

Le sezioni si annidano a piacere. La route catch-all gestisce qualsiasi
profondità: nessuna route da aggiungere quando crei nuove cartelle. Ogni
nuovo `.md` viene automaticamente:

1. Renderizzato come pagina HTML
2. Esposto come raw markdown all'URL `<slug>.md`
3. Incluso nel catalogo `/index.json`
4. Indicizzato in `/llms.txt` e `/llms-full.txt`

## Sviluppo locale

```bash
npm install
npm run dev          # http://localhost:3000 (auto-genera assets AI)
npm run build        # /out completo (statico)
npm run typecheck
npm run gen:ai-assets  # rigenera solo gli asset AI
```

## Testing

Suite Vitest che protegge gli invariant del progetto: schema Zod del
frontmatter, content loader (`lib/content.ts`), generatore di asset AI
(`scripts/generate-ai-assets.mjs`) e script di audit
(`scripts/audit.mjs`). Ambiente Node, niente jsdom.

```bash
npm test             # vitest run (one-shot, exit code per CI)
npm run test:watch   # vitest in modalità watch
npm run test:ui      # UI Vitest (richiede @vitest/ui installato)
```

I test del content loader usano fixture sotto `tests/fixtures/content/`;
`lib/content.ts` espone `_setRootForTesting(path)` (e rispetta la env
`CONTENT_ROOT`) per puntare a una root alternativa. I test di
generazione e audit lavorano contro `/content` reale e scrivono in
`/public` (che è già un output di build).

## Deploy

Hosted su **Vercel** (Next.js framework preset). Ogni push su `main`
deploya in produzione, ogni push su altri branch o PR genera un URL di
preview automatico. Dominio: `nodo432.com`.

> Il file `public/CNAME` resta nel repo come backup: se in futuro si
> torna a GitHub Pages basta riabilitare una action e i DNS.

## Licenza

I contenuti pubblicati hanno la licenza dichiarata nel frontmatter di
ciascun documento (default suggerito: CC-BY-SA-4.0). Il codice del sito
è di proprietà degli autori.
