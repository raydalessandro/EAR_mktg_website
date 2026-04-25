/**
 * Minimal YAML serializer for our frontmatter shape. Not a general-purpose
 * YAML library — just enough to round-trip the values we actually emit.
 *
 * Conservative quoting rules: any string that could be misinterpreted as
 * something else (a number, a boolean, a date, contains YAML-special chars,
 * starts/ends with whitespace) is JSON.stringify'd. Everything else is bare.
 */

const BOOLEAN_LIKE = /^(true|false|yes|no|null|~)$/i;
// Anything that starts with a digit is risky in YAML 1.1/1.2 (numbers,
// versions like "1.0.1", dates "2026-04-25", measurements "12 KB"…).
// Always quote.
const STARTS_WITH_DIGIT = /^[-+]?\d/;
const SPECIAL_CHARS = /[#:'"\\&*!|>%@`]/;
const LEADING_TRAILING_WS = /^\s|\s$/;

function escape(value: string): string {
  if (value === "") return '""';
  if (STARTS_WITH_DIGIT.test(value)) return JSON.stringify(value);
  if (BOOLEAN_LIKE.test(value)) return JSON.stringify(value);
  if (SPECIAL_CHARS.test(value)) return JSON.stringify(value);
  if (LEADING_TRAILING_WS.test(value)) return JSON.stringify(value);
  if (value.startsWith("- ") || value.startsWith("? ") || value.startsWith(": "))
    return JSON.stringify(value);
  return value;
}

function formatValue(v: unknown): string {
  if (v instanceof Date) return v.toISOString().slice(0, 10);
  if (typeof v === "string") return escape(v);
  if (typeof v === "boolean" || typeof v === "number") return String(v);
  return JSON.stringify(v);
}

export function serializeFrontmatter(
  meta: Record<string, unknown>
): string {
  const lines: string[] = [];
  for (const [key, value] of Object.entries(meta)) {
    if (value === undefined || value === null) continue;

    if (Array.isArray(value)) {
      if (value.length === 0) continue;
      lines.push(`${key}:`);
      for (const item of value) lines.push(`  - ${formatValue(item)}`);
      continue;
    }

    if (value instanceof Date) {
      lines.push(`${key}: ${formatValue(value)}`);
      continue;
    }

    if (typeof value === "object") {
      lines.push(`${key}:`);
      for (const [k2, v2] of Object.entries(
        value as Record<string, unknown>
      )) {
        if (v2 === undefined || v2 === null) continue;
        lines.push(`  ${k2}: ${formatValue(v2)}`);
      }
      continue;
    }

    lines.push(`${key}: ${formatValue(value)}`);
  }
  return lines.join("\n");
}
