import { execFileSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { beforeAll, describe, expect, it } from "vitest";

const ROOT = path.resolve(__dirname, "..");
const PUBLIC_DIR = path.join(ROOT, "public");
const SCRIPT = path.join(ROOT, "scripts", "generate-ai-assets.mjs");

beforeAll(() => {
  // Run the generator against the real /content. Safe: it only writes /public.
  execFileSync("node", [SCRIPT], { cwd: ROOT, stdio: "pipe" });
}, 60_000);

describe("generate-ai-assets.mjs → public/index.json", () => {
  let catalog: any;

  beforeAll(() => {
    const p = path.join(PUBLIC_DIR, "index.json");
    expect(fs.existsSync(p)).toBe(true);
    catalog = JSON.parse(fs.readFileSync(p, "utf8"));
  });

  it("has non-empty sections and documents arrays", () => {
    expect(Array.isArray(catalog.sections)).toBe(true);
    expect(Array.isArray(catalog.documents)).toBe(true);
    expect(catalog.sections.length).toBeGreaterThan(0);
    expect(catalog.documents.length).toBeGreaterThan(0);
  });

  it("every entry has kind, slug, title, url, raw_url", () => {
    const all = [...catalog.sections, ...catalog.documents];
    for (const n of all) {
      expect(typeof n.kind).toBe("string");
      expect(["section", "document"]).toContain(n.kind);
      expect(typeof n.slug).toBe("string");
      expect(n.slug.length).toBeGreaterThan(0);
      expect(typeof n.title).toBe("string");
      expect(n.title.length).toBeGreaterThan(0);
      expect(typeof n.url).toBe("string");
      expect(n.url).toMatch(/^https?:\/\//);
      expect(typeof n.raw_url).toBe("string");
      expect(n.raw_url).toMatch(/\.md$/);
    }
  });

  it("at least one entry has download.url", () => {
    const all = [...catalog.sections, ...catalog.documents];
    const withDownload = all.filter((n) => n.download && n.download.url);
    expect(withDownload.length).toBeGreaterThan(0);
    for (const n of withDownload) {
      expect(typeof n.download.url).toBe("string");
      expect(n.download.url.length).toBeGreaterThan(0);
    }
  });

  it("conventions.future_mcp mentions MCP (roadmap note)", () => {
    expect(catalog.conventions).toBeDefined();
    expect(typeof catalog.conventions.future_mcp).toBe("string");
    expect(catalog.conventions.future_mcp).toMatch(/MCP/i);
  });
});

describe("generate-ai-assets.mjs → llms.txt", () => {
  it("exists, starts with '# nodo432', contains '## Ontologia'", () => {
    const p = path.join(PUBLIC_DIR, "llms.txt");
    expect(fs.existsSync(p)).toBe(true);
    const content = fs.readFileSync(p, "utf8");
    expect(content.startsWith("# nodo432")).toBe(true);
    expect(content).toContain("## Ontologia");
  });
});

describe("generate-ai-assets.mjs → llms-full.txt", () => {
  it("exists and is larger than 100 KB", () => {
    const p = path.join(PUBLIC_DIR, "llms-full.txt");
    expect(fs.existsSync(p)).toBe(true);
    const stat = fs.statSync(p);
    expect(stat.size).toBeGreaterThan(100 * 1024);
  });
});

describe("generate-ai-assets.mjs → raw .md mirrors", () => {
  it("writes a sample raw markdown mirror", () => {
    const sample = path.join(
      PUBLIC_DIR,
      "ontologia",
      "teoremi",
      "3-soglia-critica.md"
    );
    expect(fs.existsSync(sample)).toBe(true);
    expect(fs.statSync(sample).size).toBeGreaterThan(0);
  });
});
