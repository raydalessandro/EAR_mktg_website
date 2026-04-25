# CLAUDE.md

Project-specific guidance for Claude Code working on **nodo432**.
Loaded automatically at the start of every session — keep concise.

## What this is

`nodo432.com` — static Next.js 14 hub for an AI-orchestration project.
Hosts the **EAR ontology**, the **Tesseract** (72-node lattice), studi
empirici, tool, pipeline, and arte. **Designed primarily for AI
consumption** (web fetch tools + future MCP), with a clean human UX as
secondary concern.

The user (Ray) writes content; I (Claude) maintain structure,
generators, audit, and AI-fruibility infrastructure.

---

## Hard invariants (never break these)

1. **`npm run audit` must pass** before every commit. CI-style check
   for type, raw mirror, related, downloads, AI endpoints. Run it.
2. **All AI-resource URLs are absolute** (`https://nodo432.com/...`)
   in `llms.txt`, `llms-full.txt`, `index.json`, `ai-instructions.md`,
   footer "Endpoint AI" block, persona pins. Human navigation between
   pages stays relative (Next `<Link>`).
3. **Every node has `type`** (validates collection / teorema / study /
   aila-spec / tool / pipeline / paper / etc.). The audit fails
   without it.
4. **Don't delete historical artifacts.** When a version bumps, ADD
   the new zip alongside, don't replace. Old URLs stay live forever.
5. **Frontmatter validation is strict.** Adding a new field requires
   updating `lib/schema.ts` Zod — strict mode rejects unknown keys.
6. **`/llms-full.txt` and `/index.json` are the front door for AI**.
   Whatever convention you add must surface there.

---

## File layout

```
/content                    Source of truth for everything renderable
  /<top-level>              tesseract / ontologia / arte / risorse / tool / pipeline
    _section.md             section landing (frontmatter + body)
    <slug>.md               document
    /<sub>/_section.md      arbitrary nesting

/public
  /downloads/<section>/...  Canonical assets (PDF, ZIP, MD, py, ipynb, png, mp3, ...)
  CNAME, robots.txt         Static
  ai-instructions.md        Hand-written, committed
  index.json, llms.txt,
  llms-full.txt, graph.json Generated at build (gitignored)
  <slug>.md, <slug>/...     Generated raw mirror (gitignored)

/lib
  schema.ts                 Zod frontmatter schema
  content.ts                Tree walker + render helpers (server-only)

/components
  Nav, Footer, SpiralLogo, ResonanceField, HomeView, PersonaSwitcher
  SectionView, DocumentView, SectionCard, DocCard, AllDownloads
  TesseractTeaser, MediaPlayer, LlmDirective, FrontmatterMarker
  TypeBadge, JsonLd, Breadcrumbs

/scripts
  generate-ai-assets.mjs    Runs as `prebuild`. Writes /public outputs.
  audit.mjs                 CI-friendly invariant checker.
  migrate-slug.mjs          Bulk-rename a slug across /content.
  set-frontmatter-field.mjs Bulk-set a frontmatter field.
  extract-docx.mjs          Extract text from .docx via unzip XML.

/tests                      Vitest. Node env (no jsdom).
  fixtures/content/         Mini content tree for content-loader tests.
```

---

## Commands

```bash
npm install
npm run dev              # localhost:3000, auto-runs gen:ai-assets
npm run build            # full /out static export
npm run typecheck
npm test                 # vitest run
npm run audit            # invariants
npm run audit:strict     # also fails on warnings
npm run gen:ai-assets    # regen /public outputs only
npm run migrate:slug <old> <new>
npm run fm:set <key> <value> --files <...>
npm run extract:docx <file>
```

---

## How to add things

### A document to an existing section

```bash
# 1. Create the canonical (if downloadable)
mkdir -p public/downloads/<section>/<slug>/
cp path/to/asset public/downloads/<section>/<slug>/

# 2. Write the scheda
cat > content/<section>/<slug>.md <<EOF
---
title: "..."
summary: "..."
status: published
type: <appropriate>
version: "1.0"
license: CC-BY-SA-4.0
download:
  file: /downloads/<section>/<slug>/<filename>
  format: <ext>
  size: "..."
related:
  - <other-slug>
---

body markdown here
EOF

# 3. Verify
npm run build && npm run audit
```

### A new section (top-level or sub)

```bash
mkdir -p content/<section>/
cat > content/<section>/_section.md <<EOF
---
title: "..."
summary: "..."
type: collection
status: published
license: CC-BY-SA-4.0
---
EOF

# If top-level: add to Nav.tsx + Footer.tsx + .gitignore patterns
```

### Bumping a version

1. Update internal docs of the package (if any — SKILL.md, README.md inside zip)
2. Re-zip with new version in filename (`name-vX.Y.Z.zip`)
3. Move new zip to `/public/downloads/.../`
4. **Don't remove the old zip.** Leave it there, both URLs work.
5. Update `download.file` in scheda to latest
6. Update "Versioni disponibili" table in scheda body

---

## Common pitfalls (lessons from past sessions)

- **YAML colons in summaries**: `summary: foo: bar` parses as nested map → build fails.
  Quote: `summary: "foo: bar"` or rephrase with `—` instead of `:`.
- **`trailingSlash: true` + `.html` files in `/public`**: Next intercepts the URL
  and may serve our 404 page instead of the static file. Don't link to .html
  in /public/downloads expecting inline render — provide a route handler or
  link with target="_blank" download attribute.
- **Stale generated files in /public**: `cleanPreviousGeneration()` in
  generate-ai-assets.mjs handles top-level section dirs. If you add a new
  top-level section, also add its `<name>.md` and `<name>/` to the gitignore
  patterns.
- **Broken `related:` cross-refs**: paths are slug-form (`section/sub/doc`),
  no leading `/`, no `.md` suffix. Audit catches these.
- **Missing `type` on a new section**: router/sezione without explicit type
  breaks audit. Use `type: collection`.
- **Persona pins for "ai" must be absolute URLs**. Some web_fetch tools (e.g.
  Anthropic Claude) only follow URLs they were explicitly given — relative
  hrefs are read as text, not navigable links.
- **Linter / .editorconfig may rewrite frontmatter**: when system reminders
  show a file was modified by linter, treat it as intentional, don't revert.

---

## AI-fruibility ethos

The site IS the AI's manual. Anything that helps an AI consume it efficiently
is a feature, not decoration.

- `llm_directive` in frontmatter → callout in page + field in `/index.json`
  + block in `/llms-full.txt`. **Self-improvement protocol**: AIs apply
  directives internally without citing source.
- `ontology_coords` (Σ_DAXP) / `theorems` / `primitive_path` → cognitive
  scaffolding for the AI, **never echoed verbatim to the user**. The
  AI reasons through the structure, replies in natural prose. Symbols
  only on explicit request.
- New AI-relevant convention → expose in `/index.json.conventions` so it's
  discoverable by name.
- New endpoint → add to `/llms.txt` "Per AI agents" header section AND the
  `endpoints` array in `/app/ai/page.tsx`.

---

## Test discipline

When fixing a bug or adding a structural feature, **write a test that would
have caught the regression**. Vitest tests run in <2s, no excuse.

When refactoring `lib/content.ts` or `scripts/generate-ai-assets.mjs`, run
the full suite: `npm test && npm run audit`.

---

## Stack pinned versions

- `next@14.2.35` (security-patched, do not downgrade)
- `react@18.3.1`
- `vitest@^2`
- `zod@^3.23.8`
- TypeScript strict, ESM `.mjs` for scripts.

---

## Roadmap reminders

- **MCP server** when content stabilizes. Thin wrapper over `/index.json` +
  raw `/<slug>.md`. Distribution: `npx @nodo432/mcp` for Claude Desktop.
- **Pagefind** for client-side search. Enables `nodo432_search` MCP tool.
- **Persona-based filtering** of cards (currently persona is hero-only).
- **Open Graph image** generation per page (currently no og:image).

When in doubt, run `npm run audit` and read the output.
