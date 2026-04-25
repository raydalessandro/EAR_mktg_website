#!/usr/bin/env node
/**
 * Bulk-rename a slug across the whole /content tree.
 *
 * Updates `related:` arrays in frontmatter and inline markdown links.
 * Does NOT move files — use `git mv` for that, then run this for refs.
 *
 * Usage: node scripts/migrate-slug.mjs <old-slug> <new-slug>
 *
 * Example:
 *   git mv content/ontologia/aila/foo.md content/ontologia/aila/bar/foo.md
 *   node scripts/migrate-slug.mjs ontologia/aila/foo ontologia/aila/bar/foo
 *
 * Slugs are matched without leading slash and without `.md` suffix.
 * Both `related:` entries and `(/foo/bar)` markdown links are updated.
 */

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CONTENT = path.resolve(__dirname, "..", "content");

const [, , oldSlug, newSlug] = process.argv;
if (!oldSlug || !newSlug) {
  console.error(
    "Usage: node scripts/migrate-slug.mjs <old-slug> <new-slug>\n" +
      "  Slugs without leading / and without .md, e.g. 'ontologia/aila/foo'"
  );
  process.exit(1);
}

const cleanOld = oldSlug.replace(/^\//, "").replace(/\.md$/, "");
const cleanNew = newSlug.replace(/^\//, "").replace(/\.md$/, "");

if (cleanOld === cleanNew) {
  console.log("No-op: old and new slug are identical.");
  process.exit(0);
}

// Patterns: match the old slug in
//   related: arrays:    "- ontologia/aila/foo"  or  "- /ontologia/aila/foo"
//   markdown links:     "(/ontologia/aila/foo)" or "(/ontologia/aila/foo/)"
//   plain refs in body: "/ontologia/aila/foo"
const patterns = [
  // related: with optional leading /
  { re: new RegExp(`(- )/?${escape(cleanOld)}(\\b|/)`, "g"), repl: `$1${cleanNew}$2` },
  // markdown link (/...)
  { re: new RegExp(`\\(/${escape(cleanOld)}(/?\\))`, "g"), repl: `(/${cleanNew}$1` },
  // bare path in href= or similar
  { re: new RegExp(`href=["']/${escape(cleanOld)}(/?)["']`, "g"), repl: `href="/${cleanNew}$1"` },
];

function escape(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function walk(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith(".")) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...walk(full));
    else if (entry.isFile() && entry.name.endsWith(".md")) out.push(full);
  }
  return out;
}

const files = walk(CONTENT);
let touched = 0;
let totalReplacements = 0;
for (const f of files) {
  const before = fs.readFileSync(f, "utf8");
  let after = before;
  let count = 0;
  for (const { re, repl } of patterns) {
    after = after.replace(re, (...m) => {
      count++;
      return typeof repl === "function" ? repl(...m) : m[0].replace(re, repl);
    });
  }
  if (after !== before) {
    fs.writeFileSync(f, after);
    touched++;
    totalReplacements += count;
    console.log(`  ${path.relative(CONTENT, f)} (${count} replacement${count === 1 ? "" : "s"})`);
  }
}

console.log("");
console.log(`Migrated ${cleanOld} -> ${cleanNew}`);
console.log(`  ${touched} files updated, ${totalReplacements} total replacements`);
