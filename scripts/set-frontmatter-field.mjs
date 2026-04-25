#!/usr/bin/env node
/**
 * Bulk-set a frontmatter field on a list of markdown files. Idempotent
 * — if the field already exists the file is skipped (or replaced with
 * --force).
 *
 * Usage:
 *   node scripts/set-frontmatter-field.mjs <key> <value> --files <glob...>
 *   node scripts/set-frontmatter-field.mjs type teorema --files content/ontologia/teoremi/*.md
 *   node scripts/set-frontmatter-field.mjs version 1.1 --force --files content/...
 *
 * Inserted after `summary:` if present, else after `status:`, else at top.
 * Always quoted as a string. For other types, edit by hand.
 */

import fs from "node:fs";
import path from "node:path";

const args = process.argv.slice(2);
const filesIdx = args.indexOf("--files");
const force = args.includes("--force");

if (filesIdx === -1 || args.length < filesIdx + 2) {
  console.error(
    "Usage: node scripts/set-frontmatter-field.mjs <key> <value> [--force] --files <file1> [file2 ...]"
  );
  process.exit(1);
}

const positional = args.slice(0, filesIdx).filter((a) => !a.startsWith("--"));
const [key, value] = positional;
const files = args.slice(filesIdx + 1);

if (!key || value === undefined || files.length === 0) {
  console.error(
    "Need <key>, <value>, and at least one file after --files"
  );
  process.exit(1);
}

const formattedValue = /^[\d.]+$/.test(value)
  ? `"${value}"`
  : /^(true|false)$/.test(value)
    ? value
    : value;

let touched = 0;
let skipped = 0;
for (const f of files) {
  if (!fs.existsSync(f)) {
    console.warn(`  skip (not found): ${f}`);
    continue;
  }
  const text = fs.readFileSync(f, "utf8");
  const m = text.match(/^(---\n)([\s\S]*?)(\n---\n)/);
  if (!m) {
    console.warn(`  skip (no frontmatter): ${f}`);
    continue;
  }
  const fm = m[2];
  const existing = new RegExp(`^${escape(key)}:.*$`, "m").test(fm);
  if (existing && !force) {
    skipped++;
    continue;
  }

  let newFm;
  if (existing && force) {
    newFm = fm.replace(
      new RegExp(`^${escape(key)}:.*$`, "m"),
      `${key}: ${formattedValue}`
    );
  } else if (/^summary:/m.test(fm)) {
    newFm = fm.replace(/(^summary:.*$)/m, `$1\n${key}: ${formattedValue}`);
  } else if (/^status:/m.test(fm)) {
    newFm = fm.replace(/(^status:.*$)/m, `$1\n${key}: ${formattedValue}`);
  } else {
    newFm = `${key}: ${formattedValue}\n${fm}`;
  }

  const newText = m[1] + newFm + m[3] + text.slice(m[0].length);
  fs.writeFileSync(f, newText);
  touched++;
  console.log(`  ${f}`);
}

console.log("");
console.log(`Set ${key}=${formattedValue} on ${touched} file(s); skipped ${skipped}.`);

function escape(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
