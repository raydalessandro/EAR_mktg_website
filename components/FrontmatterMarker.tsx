import type { Frontmatter } from "@/lib/schema";

function escape(value: string): string {
  if (/^[\s'"`]|[\s]$|[#:'"\\]|^[\d-]/.test(value)) return JSON.stringify(value);
  return value;
}

function formatValue(v: unknown): string {
  if (v instanceof Date) return v.toISOString().slice(0, 10);
  if (typeof v === "string") return escape(v);
  if (typeof v === "boolean" || typeof v === "number") return String(v);
  return JSON.stringify(v);
}

export function serializeFrontmatter(meta: Frontmatter & { slug?: string }): string {
  const lines: string[] = [];
  const skip = new Set<string>();
  for (const [key, value] of Object.entries(meta)) {
    if (skip.has(key)) continue;
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
      for (const [k2, v2] of Object.entries(value as Record<string, unknown>)) {
        if (v2 === undefined || v2 === null) continue;
        lines.push(`  ${k2}: ${formatValue(v2)}`);
      }
      continue;
    }
    lines.push(`${key}: ${formatValue(value)}`);
  }
  return lines.join("\n");
}

type Props = {
  meta: Frontmatter;
  slug: string;
  kind: "section" | "document";
};

export function FrontmatterMarker({ meta, slug, kind }: Props) {
  const enriched = { ...meta, slug, kind };
  const yaml = serializeFrontmatter(enriched as Frontmatter & { slug: string });
  return (
    <script
      type="application/yaml"
      data-purpose="frontmatter"
      data-kind={kind}
      data-slug={slug}
      dangerouslySetInnerHTML={{ __html: yaml }}
    />
  );
}
