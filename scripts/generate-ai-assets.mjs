#!/usr/bin/env node
/**
 * AI-fruibility build assets generator.
 *
 * Runs as `prebuild`. Walks /content, then writes into /public:
 *   - index.json          full catalog of sections + documents with metadata
 *   - llms.txt            llmstxt.org-compliant site map for LLMs
 *   - llms-full.txt       concatenated bodies of all published documents
 *   - <slug>.md           raw markdown copy of every content file, at the
 *                         same URL path as the rendered HTML page
 *
 * The generated files are gitignored; they are produced fresh on every build.
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import matter from "gray-matter";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const CONTENT_DIR = path.join(ROOT, "content");
const PUBLIC_DIR = path.join(ROOT, "public");
const SITE_URL = process.env.SITE_URL ?? "https://nodo432.com";
const SECTION_FILE = "_section.md";

const STATUS_LIVE = new Set(["published"]);

function readFm(filePath) {
  const raw = fs.readFileSync(filePath, "utf8");
  const parsed = matter(raw);
  return { meta: parsed.data ?? {}, body: parsed.content ?? "" };
}

function defaultSectionMeta(name) {
  return { title: name, status: "wip", tags: [] };
}

function walk(dir, slug = []) {
  const out = { sections: [], documents: [] };
  if (!fs.existsSync(dir)) return out;

  const sectionFile = path.join(dir, SECTION_FILE);
  const sectionMeta = fs.existsSync(sectionFile)
    ? readFm(sectionFile).meta
    : defaultSectionMeta(slug[slug.length - 1] ?? "root");

  const sectionBody = fs.existsSync(sectionFile)
    ? readFm(sectionFile).body
    : "";

  if (slug.length > 0) {
    out.sections.push({
      slug,
      meta: sectionMeta,
      body: sectionBody,
      sectionFilePath: fs.existsSync(sectionFile) ? sectionFile : null,
    });
  }

  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith(".") || entry.name.startsWith("_")) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      const nested = walk(full, [...slug, entry.name]);
      out.sections.push(...nested.sections);
      out.documents.push(...nested.documents);
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      const docSlug = [...slug, entry.name.replace(/\.md$/, "")];
      const { meta, body } = readFm(full);
      out.documents.push({ slug: docSlug, meta, body, filePath: full });
    }
  }
  return out;
}

function urlFor(slugArr) {
  return `${SITE_URL}/${slugArr.join("/")}`;
}

function rawUrlFor(slugArr) {
  return `${SITE_URL}/${slugArr.join("/")}.md`;
}

function buildCatalog({ sections, documents }) {
  return {
    site: "nodo432",
    description:
      "Hub di orchestrazione AI. Sistema ontologico EAR, notazione AILA, teoremi strutturali, risorse e tool.",
    url: SITE_URL,
    generated_at: new Date().toISOString(),
    conventions: {
      raw_markdown:
        "Ogni pagina HTML ha un equivalente markdown aggiungendo .md all'URL. Esempio: /ontologia → /ontologia.md",
      catalog: "/index.json contiene tutto questo catalogo, machine-readable",
      llms_txt: "/llms.txt segue lo standard llmstxt.org",
      future_mcp:
        "Un server MCP è in roadmap (non ancora disponibile). Esporrà list_documents, read_document, get_section come tool MCP.",
    },
    sections: sections.map((s) => ({
      slug: "/" + s.slug.join("/"),
      title: s.meta.title,
      summary: s.meta.summary ?? null,
      status: s.meta.status ?? "published",
      url: urlFor(s.slug),
      raw_url: rawUrlFor(s.slug),
    })),
    documents: documents.map((d) => ({
      slug: "/" + d.slug.join("/"),
      title: d.meta.title,
      summary: d.meta.summary ?? null,
      description: d.meta.description ?? null,
      status: d.meta.status ?? "published",
      tags: d.meta.tags ?? [],
      authors: d.meta.authors ?? [],
      created: d.meta.created ?? null,
      updated: d.meta.updated ?? null,
      license: d.meta.license ?? null,
      url: urlFor(d.slug),
      raw_url: rawUrlFor(d.slug),
      download: d.meta.download
        ? {
            ...d.meta.download,
            url: d.meta.download.file?.startsWith("http")
              ? d.meta.download.file
              : `${SITE_URL}${d.meta.download.file ?? ""}`,
          }
        : null,
      related: d.meta.related ?? [],
      featured: !!d.meta.featured,
    })),
  };
}

function buildLlmsTxt({ sections, documents }) {
  const lines = [];
  lines.push("# nodo432");
  lines.push("");
  lines.push(
    "> Hub di orchestrazione AI. Sistema ontologico EAR (Essere/Agire/Risuonare), notazione AILA per LLM, teoremi strutturali, risorse e tool. Sito progettato per essere consultabile da agenti AI: ogni pagina ha equivalente markdown raw, catalogo completo machine-readable a /index.json."
  );
  lines.push("");
  lines.push(
    "Convenzioni: aggiungi `.md` a un URL pagina per ottenere il sorgente markdown. Es: `/ontologia/teoremi/3-soglia-critica` → `/ontologia/teoremi/3-soglia-critica.md`. Catalogo strutturato: `/index.json`."
  );
  lines.push("");

  const topSections = sections.filter((s) => s.slug.length === 1);

  for (const top of topSections) {
    const heading = top.meta.title ?? top.slug[0];
    lines.push(`## ${heading}`);
    lines.push("");
    if (top.meta.summary) {
      lines.push(top.meta.summary);
      lines.push("");
    }
    lines.push(
      `- [${top.meta.title}](${urlFor(top.slug)}): ${top.meta.summary ?? "sezione"}`
    );

    const subSections = sections.filter(
      (s) =>
        s.slug.length > 1 &&
        s.slug.slice(0, top.slug.length).join("/") === top.slug.join("/")
    );
    for (const sub of subSections) {
      lines.push(
        `  - [${sub.meta.title}](${urlFor(sub.slug)}): ${sub.meta.summary ?? "sotto-sezione"}`
      );
    }

    const inSection = documents.filter(
      (d) => d.slug[0] === top.slug[0] && STATUS_LIVE.has(d.meta.status ?? "published")
    );
    for (const doc of inSection) {
      const tail = doc.slug.slice(1).join("/");
      lines.push(
        `- [${doc.meta.title}](${urlFor(doc.slug)}): ${doc.meta.summary ?? tail}`
      );
    }
    lines.push("");
  }

  lines.push("## Optional");
  lines.push("");
  lines.push(`- [Catalogo JSON](${SITE_URL}/index.json): tutti i contenuti in formato strutturato, una sola fetch`);
  lines.push(`- [Sitemap](${SITE_URL}/sitemap.xml): sitemap XML standard`);
  lines.push(`- [llms-full.txt](${SITE_URL}/llms-full.txt): tutti i contenuti pubblicati concatenati`);
  lines.push(`- [Pagina /ai](${SITE_URL}/ai): guida human-readable alla navigazione AI del sito`);
  lines.push("");

  return lines.join("\n");
}

function readCanonicalIfMarkdown(meta) {
  const downloadFile = meta.download?.file;
  if (!downloadFile) return null;
  if (!downloadFile.endsWith(".md")) return null;
  if (downloadFile.startsWith("http")) return null;
  const rel = downloadFile.replace(/^\//, "");
  const local = path.join(PUBLIC_DIR, rel);
  if (!fs.existsSync(local)) return null;
  try {
    return fs.readFileSync(local, "utf8");
  } catch {
    return null;
  }
}

function buildLlmsFullTxt({ sections, documents }) {
  const lines = [];
  lines.push("# nodo432 — full content dump");
  lines.push("");
  lines.push(
    "Concatenazione completa dei contenuti pubblicati su nodo432. Per ogni documento è incluso il testo CANONICO completo (il file linkato nel campo download del frontmatter), quando il canonico è in formato markdown. Per documenti senza canonico markdown è incluso il body della scheda online."
  );
  lines.push("");
  lines.push(`Generato: ${new Date().toISOString()}`);
  lines.push(`Source: ${SITE_URL}/llms-full.txt`);
  lines.push(`Catalogo strutturato: ${SITE_URL}/index.json`);
  lines.push("");
  lines.push("=".repeat(72));
  lines.push("");

  function emitNodeBlock(node, kind) {
    if (!STATUS_LIVE.has(node.meta.status ?? "published")) return;

    lines.push("=".repeat(72));
    lines.push("");
    lines.push(`# ${node.meta.title}`);
    lines.push("");
    lines.push(`Kind: ${kind}`);
    lines.push(`Source page: ${urlFor(node.slug)}`);
    lines.push(`Raw markdown: ${rawUrlFor(node.slug)}`);
    if (node.meta.type) lines.push(`Type: ${node.meta.type}`);
    if (node.meta.version) lines.push(`Version: ${node.meta.version}`);
    if (node.meta.status) lines.push(`Status: ${node.meta.status}`);
    if (node.meta.summary) lines.push(`Summary: ${node.meta.summary}`);
    if (node.meta.tags?.length) lines.push(`Tags: ${node.meta.tags.join(", ")}`);
    if (node.meta.license) lines.push(`License: ${node.meta.license}`);

    const canonicalMd = readCanonicalIfMarkdown(node.meta);
    if (canonicalMd) {
      const canonicalUrl = node.meta.download.file.startsWith("http")
        ? node.meta.download.file
        : `${SITE_URL}${node.meta.download.file}`;
      lines.push(`Canonical download: ${canonicalUrl}`);
      lines.push("");
      lines.push("## Scheda (intro)");
      lines.push("");
      if (node.body?.trim()) lines.push(node.body.trim());
      lines.push("");
      lines.push("## Canonical content");
      lines.push("");
      lines.push(canonicalMd.trim());
      lines.push("");
    } else {
      if (node.meta.download) {
        const fmt = node.meta.download.format ?? "binary";
        const url = node.meta.download.file.startsWith("http")
          ? node.meta.download.file
          : `${SITE_URL}${node.meta.download.file}`;
        lines.push(`Canonical download (${fmt}, not inlined): ${url}`);
      }
      lines.push("");
      if (node.body?.trim()) {
        lines.push(node.body.trim());
        lines.push("");
      }
    }
  }

  for (const sec of sections) {
    if (sec.slug.length !== 1) continue;
    lines.push(`# ${sec.meta.title}`);
    if (sec.meta.summary) {
      lines.push("");
      lines.push(`> ${sec.meta.summary}`);
    }
    lines.push("");
    if (sec.body?.trim()) {
      lines.push(sec.body.trim());
      lines.push("");
    }
  }

  for (const sec of sections) {
    if (sec.slug.length === 1) continue;
    if (!sec.meta.download) continue;
    emitNodeBlock(sec, "section");
  }

  for (const doc of documents) {
    emitNodeBlock(doc, "document");
  }

  return lines.join("\n");
}

function copyRawMarkdown({ sections, documents }) {
  const written = [];
  for (const doc of documents) {
    const dest = path.join(PUBLIC_DIR, doc.slug.join("/") + ".md");
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(doc.filePath, dest);
    written.push(dest);
  }
  for (const sec of sections) {
    if (!sec.sectionFilePath) continue;
    const dest = path.join(PUBLIC_DIR, sec.slug.join("/") + ".md");
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(sec.sectionFilePath, dest);
    written.push(dest);
  }
  return written;
}

function cleanPreviousGeneration() {
  if (!fs.existsSync(CONTENT_DIR)) return;
  for (const entry of fs.readdirSync(CONTENT_DIR, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith(".") || entry.name.startsWith("_")) continue;
    const dir = path.join(PUBLIC_DIR, entry.name);
    const mdFile = path.join(PUBLIC_DIR, entry.name + ".md");
    if (fs.existsSync(dir)) fs.rmSync(dir, { recursive: true, force: true });
    if (fs.existsSync(mdFile)) fs.rmSync(mdFile);
  }
}

function main() {
  if (!fs.existsSync(PUBLIC_DIR)) fs.mkdirSync(PUBLIC_DIR, { recursive: true });

  cleanPreviousGeneration();

  const tree = walk(CONTENT_DIR);

  const catalog = buildCatalog(tree);
  fs.writeFileSync(
    path.join(PUBLIC_DIR, "index.json"),
    JSON.stringify(catalog, null, 2)
  );

  const llmsTxt = buildLlmsTxt(tree);
  fs.writeFileSync(path.join(PUBLIC_DIR, "llms.txt"), llmsTxt);

  const llmsFull = buildLlmsFullTxt(tree);
  fs.writeFileSync(path.join(PUBLIC_DIR, "llms-full.txt"), llmsFull);

  const rawFiles = copyRawMarkdown(tree);

  console.log(
    `[ai-assets] index.json (${catalog.sections.length} sections, ${catalog.documents.length} documents)`
  );
  console.log(`[ai-assets] llms.txt (${llmsTxt.length} bytes)`);
  console.log(`[ai-assets] llms-full.txt (${llmsFull.length} bytes)`);
  console.log(`[ai-assets] raw markdown copies: ${rawFiles.length}`);
}

main();
