#!/usr/bin/env node
/**
 * Extracts plain text from a .docx file by reading word/document.xml
 * out of the zip and stripping XML tags. Useful for letting agents
 * (or quick inspection) read DOCX content without converting them.
 *
 * Usage: node scripts/extract-docx.mjs <file.docx> [--head=N]
 *
 * Stdout receives the extracted text. With --head=N only the first N
 * non-empty lines are printed, useful to identify a document quickly.
 */

import fs from "node:fs";
import { execSync } from "node:child_process";

const args = process.argv.slice(2);
const file = args.find((a) => !a.startsWith("--"));
const headArg = args.find((a) => a.startsWith("--head="));
const headN = headArg ? parseInt(headArg.split("=")[1], 10) : null;

if (!file) {
  console.error("Usage: node scripts/extract-docx.mjs <file.docx> [--head=N]");
  process.exit(1);
}

if (!fs.existsSync(file)) {
  console.error(`File not found: ${file}`);
  process.exit(1);
}

let xml;
try {
  xml = execSync(`unzip -p ${JSON.stringify(file)} word/document.xml`, {
    encoding: "utf8",
    maxBuffer: 50 * 1024 * 1024,
  });
} catch (e) {
  console.error(`Failed to unzip ${file}: ${e.message}`);
  process.exit(1);
}

let text = xml.replace(/<w:p[^>]*>/g, "\n").replace(/<[^>]+>/g, "");
text = text
  .replace(/&amp;/g, "&")
  .replace(/&lt;/g, "<")
  .replace(/&gt;/g, ">")
  .replace(/&quot;/g, '"')
  .replace(/&apos;/g, "'");

const lines = text
  .split("\n")
  .map((l) => l.trim())
  .filter(Boolean);

const slice = headN ? lines.slice(0, headN) : lines;
process.stdout.write(slice.join("\n") + "\n");
if (headN && lines.length > headN) {
  process.stdout.write(`... (${lines.length - headN} more lines)\n`);
}
