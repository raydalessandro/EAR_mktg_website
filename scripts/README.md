# scripts

Strumenti riusabili per la gestione del repo. Tutti pensati per essere
chiamati direttamente con `node` (ESM, niente build step) o via npm script.

## generate-ai-assets.mjs

Generato a build time da `npm run prebuild`. Cammina `/content`, scrive
in `/public`:

- `index.json` — catalogo machine-readable (sezioni + documenti, schema
  uniforme con `type`, `version`, `download`, `related`, ecc.)
- `llms.txt` — mappa testuale standard [llmstxt.org](https://llmstxt.org/)
- `llms-full.txt` — concatenazione completa: per ogni nodo con `download.file`
  in markdown viene inlineato il contenuto canonico
- `<slug>.md` per ogni nodo — mirror raw del sorgente

Si invoca anche da solo: `npm run gen:ai-assets`.

## audit.mjs

Verifica gli invarianti di AI-fruibility sul build. Si invoca con:

```bash
node scripts/audit.mjs                  # default: audit /out se esiste, altrimenti /public
node scripts/audit.mjs --target=public   # esplicito
node scripts/audit.mjs --strict          # fail anche sui warning
```

**Errori che fanno fallire** (exit 1):
- nodi senza `type`
- raw `.md` mirror mancante
- `related:` rotti (slug non esistente)
- `download.file` che non esiste sul filesystem
- `llms.txt`, `llms-full.txt`, `sitemap.xml`, `robots.txt` mancanti o vuoti

**Warning** (non bloccanti senza `--strict`):
- nodi senza `summary`
- nodi-contenuto senza `version`
- sezioni senza `_section.md` (verranno renderizzate con title = nome cartella)

Output include la distribuzione dei `type` e i conteggi.

Adatto a CI: `node scripts/audit.mjs --strict` post-build.

## migrate-slug.mjs

Rinomina uno slug ovunque sia citato in `/content`. Aggiorna campi
`related:` e link markdown nel corpo. **Non sposta i file** — usa
`git mv` separatamente.

```bash
git mv content/ontologia/aila/foo.md content/ontologia/aila/bar/foo.md
node scripts/migrate-slug.mjs ontologia/aila/foo ontologia/aila/bar/foo
```

Pattern coperti:
- `- ontologia/aila/foo` o `- /ontologia/aila/foo` (related)
- `(/ontologia/aila/foo)` o `(/ontologia/aila/foo/)` (markdown link)
- `href="/ontologia/aila/foo"` (link HTML)

## extract-docx.mjs

Estrae testo da `.docx` leggendo `word/document.xml` dello zip. Utile per
agenti o ispezione veloce senza convertire i file.

```bash
node scripts/extract-docx.mjs path/to/file.docx              # tutto il testo
node scripts/extract-docx.mjs path/to/file.docx --head=10    # solo prime 10 righe
```

Richiede `unzip` nel `$PATH`.

## set-frontmatter-field.mjs

Imposta in batch un campo nel frontmatter di una lista di file `.md`.
Idempotente: se il campo esiste già lo skippa, salvo `--force` che lo
sovrascrive.

```bash
# Aggiungi type=teorema a tutti i teoremi (skip se già presente)
node scripts/set-frontmatter-field.mjs type teorema --files content/ontologia/teoremi/*.md

# Sovrascrivi version=1.1 su una lista
node scripts/set-frontmatter-field.mjs version 1.1 --force --files content/ontologia/aila/sistema-formale/*.md
```

Inserito dopo `summary:` se presente, altrimenti dopo `status:`,
altrimenti in cima al frontmatter.

---

## Convenzioni

- Tutti gli script sono ESM (`.mjs`), Node ≥ 18
- Niente dipendenze esterne fuori da quelle già in `package.json`
- Idempotenza preferita: poter rieseguire senza danni
- Output umano-leggibile su stdout, exit code 1 su errore
