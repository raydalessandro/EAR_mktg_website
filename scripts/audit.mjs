#!/usr/bin/env node
/**
 * AI-fruibility audit. Runs after a build (or against /public after
 * `npm run gen:ai-assets`) and verifies invariants:
 *
 *   - every node in the catalog has a non-empty `type`
 *   - every node has a raw .md mirror at /<slug>.md
 *   - no `related:` cross-reference points to a missing slug
 *   - every `download.file` actually exists in /public/
 *   - llms.txt and llms-full.txt are present and non-empty
 *   - every section directory has _section.md
 *
 * Exit code 1 on any failure. Useful in CI.
 *
 * Usage: node scripts/audit.mjs [--strict] [--target=out|public]
 *   --strict   also fail on warnings (missing version, summary, etc.)
 *   --target   directory to audit (default: out, falls back to public)
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const CONTENT_DIR = path.join(ROOT, "content");

const args = new Set(process.argv.slice(2));
const STRICT = args.has("--strict");
const targetArg = [...args].find((a) => a.startsWith("--target="));
const TARGET = targetArg
  ? path.join(ROOT, targetArg.split("=")[1])
  : fs.existsSync(path.join(ROOT, "out"))
    ? path.join(ROOT, "out")
    : path.join(ROOT, "public");

const errors = [];
const warnings = [];

function fail(msg) {
  errors.push(msg);
}
function warn(msg) {
  warnings.push(msg);
}

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, "utf8"));
}

function checkContentTree() {
  const expected = [];
  const visit = (dir, slug = []) => {
    if (!fs.existsSync(dir)) return;
    const sectionFile = path.join(dir, "_section.md");
    if (slug.length > 0 && !fs.existsSync(sectionFile)) {
      warn(`section without _section.md: ${slug.join("/")}`);
    }
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      if (entry.name.startsWith(".") || entry.name.startsWith("_")) continue;
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        expected.push({ kind: "section", slug: [...slug, entry.name] });
        visit(full, [...slug, entry.name]);
      } else if (entry.isFile() && entry.name.endsWith(".md")) {
        expected.push({
          kind: "document",
          slug: [...slug, entry.name.replace(/\.md$/, "")],
        });
      }
    }
  };
  visit(CONTENT_DIR);
  return expected;
}

function checkCatalog() {
  const catalogPath = path.join(TARGET, "index.json");
  if (!fs.existsSync(catalogPath)) {
    fail(`/index.json missing at ${catalogPath}`);
    return null;
  }
  const catalog = readJson(catalogPath);
  return catalog;
}

function audit() {
  console.log(`Auditing ${TARGET}\n`);

  const catalog = checkCatalog();
  if (!catalog) return;

  const all = [...catalog.sections, ...catalog.documents];
  const slugSet = new Set(all.map((n) => n.slug.replace(/^\//, "")));

  // 1. type field
  const noType = all.filter((n) => !n.type);
  if (noType.length > 0) {
    fail(`${noType.length} nodes without type:`);
    for (const n of noType.slice(0, 10)) fail(`    ${n.slug}`);
  }

  // 2. raw .md mirror
  const noRaw = all.filter(
    (n) => !fs.existsSync(path.join(TARGET, n.slug + ".md"))
  );
  if (noRaw.length > 0) {
    fail(`${noRaw.length} nodes missing raw .md mirror:`);
    for (const n of noRaw.slice(0, 10)) fail(`    ${n.slug}.md`);
  }

  // 3. related: cross-refs
  const broken = [];
  for (const n of all) {
    for (const r of n.related ?? []) {
      const cleaned = r.replace(/^\//, "").replace(/\.md$/, "");
      if (!slugSet.has(cleaned)) broken.push({ from: n.slug, to: r });
    }
  }
  if (broken.length > 0) {
    fail(`${broken.length} broken related: cross-references:`);
    for (const b of broken.slice(0, 10)) fail(`    ${b.from}  ->  ${b.to}`);
  }

  // 4. download files exist
  const missingDownloads = [];
  for (const n of all) {
    if (!n.download?.file) continue;
    if (n.download.file.startsWith("http")) continue;
    const local = path.join(TARGET, n.download.file.replace(/^\//, ""));
    if (!fs.existsSync(local)) {
      missingDownloads.push({ from: n.slug, file: n.download.file });
    }
  }
  if (missingDownloads.length > 0) {
    fail(`${missingDownloads.length} missing download files:`);
    for (const m of missingDownloads.slice(0, 10))
      fail(`    ${m.from}  needs  ${m.file}`);
  }

  // 5. AI endpoints
  // gen-ai-assets writes llms.txt, llms-full.txt, robots.txt
  // Next.js writes sitemap.xml only during `next build`, into /out
  const isBuildOutput = path.basename(TARGET) === "out";
  const requiredAlways = ["llms.txt", "llms-full.txt", "robots.txt"];
  const requiredIfBuild = ["sitemap.xml"];
  for (const f of requiredAlways) {
    const p = path.join(TARGET, f);
    if (!fs.existsSync(p) || fs.statSync(p).size === 0) {
      fail(`/${f} missing or empty`);
    }
  }
  for (const f of requiredIfBuild) {
    const p = path.join(TARGET, f);
    if (!fs.existsSync(p) || fs.statSync(p).size === 0) {
      if (isBuildOutput) {
        fail(`/${f} missing or empty (build output expected here)`);
      } else {
        warn(`/${f} missing in ${path.basename(TARGET)}/ (only generated by next build into /out)`);
      }
    }
  }

  // Soft warnings (counted; don't fail unless --strict)
  const noSummary = all.filter((n) => !n.summary).length;
  const noVersion = all.filter(
    (n) => !n.version && n.type && !["collection"].includes(n.type)
  ).length;
  if (noSummary > 0) warn(`${noSummary} nodes without summary`);
  if (noVersion > 0) warn(`${noVersion} content nodes without version`);

  // 6. Featured nodes should have summary (otherwise the home card is empty)
  const featuredNoSummary = all.filter(
    (n) => n.featured && !n.summary
  );
  if (featuredNoSummary.length > 0) {
    warn(`${featuredNoSummary.length} featured nodes without summary:`);
    for (const n of featuredNoSummary.slice(0, 5))
      warn(`    ${n.slug}`);
  }

  // 7. download.file should not contain spaces or chars that need URL encoding
  const URL_UNSAFE = /[ #?&%]/;
  const unsafeUrls = [];
  for (const n of all) {
    if (!n.download?.file) continue;
    if (URL_UNSAFE.test(n.download.file)) {
      unsafeUrls.push({ from: n.slug, file: n.download.file });
    }
  }
  if (unsafeUrls.length > 0) {
    fail(`${unsafeUrls.length} download.file paths contain URL-unsafe chars (space/#/?/&/%):`);
    for (const u of unsafeUrls.slice(0, 10))
      fail(`    ${u.from}  →  ${u.file}`);
  }

  // 8. Version (when present) should look like dotted digits, optionally suffixed
  const VERSION_PATTERN = /^\d+(\.\d+){0,3}([-+][0-9A-Za-z.-]+)?$/;
  const oddVersions = all.filter(
    (n) => n.version && !VERSION_PATTERN.test(String(n.version))
  );
  if (oddVersions.length > 0) {
    warn(`${oddVersions.length} nodes with non-standard version strings:`);
    for (const n of oddVersions.slice(0, 5))
      warn(`    ${n.slug}  →  "${n.version}"`);
  }

  // 9. Every published node with a download should have a license declared
  const noLicenseWithDownload = all.filter(
    (n) =>
      n.download &&
      n.status === "published" &&
      !n.license
  );
  if (noLicenseWithDownload.length > 0) {
    warn(`${noLicenseWithDownload.length} published nodes with download but no license:`);
    for (const n of noLicenseWithDownload.slice(0, 5))
      warn(`    ${n.slug}`);
  }

  // Stats
  console.log(`Catalog: ${catalog.sections.length} sections, ${catalog.documents.length} documents`);
  console.log(`  with type:     ${all.filter((n) => n.type).length}/${all.length}`);
  console.log(`  with version:  ${all.filter((n) => n.version).length}/${all.length}`);
  console.log(`  with download: ${all.filter((n) => n.download).length}/${all.length}`);
  console.log(`  raw mirrors:   ${all.length - noRaw.length}/${all.length}`);
  console.log(`  broken refs:   ${broken.length}`);
  console.log("");

  // Type histogram
  const types = new Map();
  for (const n of all) {
    const t = n.type ?? "(none)";
    types.set(t, (types.get(t) ?? 0) + 1);
  }
  console.log(`Type distribution:`);
  for (const [t, c] of [...types.entries()].sort((a, b) => b[1] - a[1])) {
    console.log(`  ${t.padEnd(28)} ${c}`);
  }

  // Optional: verify content tree shape vs catalog
  const expected = checkContentTree();
  if (expected.length !== all.length) {
    warn(
      `content tree (${expected.length}) and catalog (${all.length}) differ — possibly stale build`
    );
  }
}

audit();

if (warnings.length > 0) {
  console.log("");
  console.log(`Warnings (${warnings.length}):`);
  for (const w of warnings) console.log(`  ⚠ ${w}`);
}

if (errors.length > 0) {
  console.log("");
  console.log(`FAIL (${errors.length} errors):`);
  for (const e of errors) console.log(`  ✗ ${e}`);
  process.exit(1);
}

if (STRICT && warnings.length > 0) {
  console.log("");
  console.log(`FAIL (--strict, ${warnings.length} warnings)`);
  process.exit(1);
}

console.log("");
console.log("✓ audit passed");
