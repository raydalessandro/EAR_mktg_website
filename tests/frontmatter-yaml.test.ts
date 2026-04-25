import { describe, it, expect } from "vitest";
import { serializeFrontmatter } from "@/lib/frontmatter-yaml";

describe("serializeFrontmatter", () => {
  it("emits scalar fields as plain bare values when safe", () => {
    const yaml = serializeFrontmatter({
      title: "Plain Title",
      status: "published",
      order: 10,
      featured: true,
    });
    expect(yaml).toContain("title: Plain Title");
    expect(yaml).toContain("status: published");
    expect(yaml).toContain("order: 10");
    expect(yaml).toContain("featured: true");
  });

  it("quotes strings that contain colons", () => {
    const yaml = serializeFrontmatter({
      summary: "Foo: bar baz",
    });
    expect(yaml).toContain('summary: "Foo: bar baz"');
  });

  it("quotes strings that look like numbers", () => {
    const yaml = serializeFrontmatter({ version: "1.0" });
    expect(yaml).toContain('version: "1.0"');
  });

  it("quotes strings that look like booleans or null", () => {
    const yaml = serializeFrontmatter({
      a: "true",
      b: "false",
      c: "yes",
      d: "null",
    });
    expect(yaml).toContain('a: "true"');
    expect(yaml).toContain('b: "false"');
    expect(yaml).toContain('c: "yes"');
    expect(yaml).toContain('d: "null"');
  });

  it("quotes strings that look like dates", () => {
    const yaml = serializeFrontmatter({ ref: "2026-04-25" });
    expect(yaml).toContain('ref: "2026-04-25"');
  });

  it("formats Date instances as YYYY-MM-DD bare strings", () => {
    const yaml = serializeFrontmatter({
      created: new Date("2026-04-25T00:00:00Z"),
    });
    expect(yaml).toContain("created: 2026-04-25");
  });

  it("emits arrays as block sequences", () => {
    const yaml = serializeFrontmatter({
      tags: ["alpha", "beta"],
      authors: ["nodo432"],
    });
    expect(yaml).toContain("tags:\n  - alpha\n  - beta");
    expect(yaml).toContain("authors:\n  - nodo432");
  });

  it("skips empty arrays", () => {
    const yaml = serializeFrontmatter({ tags: [], title: "T" });
    expect(yaml).not.toContain("tags:");
    expect(yaml).toContain("title: T");
  });

  it("emits nested objects with two-space indentation", () => {
    const yaml = serializeFrontmatter({
      download: { file: "/downloads/foo.md", format: "md", size: "12 KB" },
    });
    expect(yaml).toContain("download:");
    expect(yaml).toContain("  file: /downloads/foo.md");
    expect(yaml).toContain("  format: md");
    expect(yaml).toContain('  size: "12 KB"');
  });

  it("skips undefined and null values", () => {
    const yaml = serializeFrontmatter({
      title: "T",
      missing: null,
      alsoMissing: undefined,
    });
    expect(yaml).toContain("title: T");
    expect(yaml).not.toContain("missing");
    expect(yaml).not.toContain("alsoMissing");
  });

  it("quotes strings with special YAML chars", () => {
    const yaml = serializeFrontmatter({
      hash: "#hashtag",
      amp: "a & b",
      pipe: "a | b",
    });
    expect(yaml).toContain('hash: "#hashtag"');
    expect(yaml).toContain('amp: "a & b"');
    expect(yaml).toContain('pipe: "a | b"');
  });

  it("quotes strings with leading/trailing whitespace", () => {
    const yaml = serializeFrontmatter({ x: "  padded  " });
    expect(yaml).toContain('x: "  padded  "');
  });

  it("handles empty strings explicitly", () => {
    const yaml = serializeFrontmatter({ x: "" });
    expect(yaml).toContain('x: ""');
  });

  it("preserves real-world saga-engine-like frontmatter shape", () => {
    const yaml = serializeFrontmatter({
      title: "Saga Engine",
      summary: "Pipeline per saghe.",
      type: "pipeline",
      version: "1.0.1",
      tags: ["pipeline", "saga"],
      created: new Date("2026-04-25T00:00:00Z"),
      download: {
        file: "/downloads/pipeline/saga-engine/saga-engine-v1.0.1.zip",
        format: "zip",
        size: "232 KB",
      },
      featured: true,
    });
    expect(yaml).toMatch(/^title: Saga Engine$/m);
    expect(yaml).toMatch(/^version: "1\.0\.1"$/m);
    expect(yaml).toMatch(/^featured: true$/m);
    expect(yaml).toContain("download:");
    expect(yaml).toContain(
      "  file: /downloads/pipeline/saga-engine/saga-engine-v1.0.1.zip"
    );
  });
});
