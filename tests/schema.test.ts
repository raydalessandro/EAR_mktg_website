import { describe, expect, it } from "vitest";
import { frontmatterSchema, downloadSchema, STATUSES } from "@/lib/schema";

describe("frontmatterSchema", () => {
  it("accepts a minimal valid object (just title)", () => {
    const result = frontmatterSchema.safeParse({ title: "Hello" });
    expect(result.success).toBe(true);
    if (result.success) {
      expect(result.data.title).toBe("Hello");
      // defaults applied
      expect(result.data.status).toBe("published");
      expect(result.data.tags).toEqual([]);
      expect(result.data.authors).toEqual([]);
      expect(result.data.related).toEqual([]);
      expect(result.data.featured).toBe(false);
    }
  });

  it("rejects missing title", () => {
    const result = frontmatterSchema.safeParse({ summary: "no title" });
    expect(result.success).toBe(false);
    if (!result.success) {
      const titleIssue = result.error.issues.find((i) =>
        i.path.includes("title")
      );
      expect(titleIssue).toBeDefined();
    }
  });

  it("rejects an empty title string", () => {
    const result = frontmatterSchema.safeParse({ title: "" });
    expect(result.success).toBe(false);
  });

  it("validates the status enum (published / draft / wip / coming-soon)", () => {
    for (const s of STATUSES) {
      const r = frontmatterSchema.safeParse({ title: "T", status: s });
      expect(r.success).toBe(true);
    }
    const bad = frontmatterSchema.safeParse({
      title: "T",
      status: "archived",
    });
    expect(bad.success).toBe(false);
  });

  it("download.format accepts arbitrary strings", () => {
    for (const fmt of ["md", "pdf", "zip", "py", "ipynb", "png", "weird-fmt"]) {
      const r = downloadSchema.safeParse({ file: "/x.bin", format: fmt });
      expect(r.success).toBe(true);
    }
  });

  it("download.format defaults to 'md' when omitted", () => {
    const r = downloadSchema.safeParse({ file: "/x" });
    expect(r.success).toBe(true);
    if (r.success) expect(r.data.format).toBe("md");
  });

  it("tags / authors / related default to empty arrays when omitted", () => {
    const r = frontmatterSchema.safeParse({ title: "T" });
    expect(r.success).toBe(true);
    if (r.success) {
      expect(r.data.tags).toEqual([]);
      expect(r.data.authors).toEqual([]);
      expect(r.data.related).toEqual([]);
    }
  });

  it("coerces created and updated from ISO date strings", () => {
    const r = frontmatterSchema.safeParse({
      title: "T",
      created: "2026-04-25",
      updated: "2026-04-25T10:00:00Z",
    });
    expect(r.success).toBe(true);
    if (r.success) {
      expect(r.data.created).toBeInstanceOf(Date);
      expect(r.data.updated).toBeInstanceOf(Date);
      expect(r.data.created?.getUTCFullYear()).toBe(2026);
    }
  });

  it("strict mode rejects unknown keys", () => {
    const r = frontmatterSchema.safeParse({
      title: "T",
      randomExtra: "boom",
    });
    expect(r.success).toBe(false);
    if (!r.success) {
      const unknown = r.error.issues.find((i) =>
        i.message.toLowerCase().includes("unrecognized")
      );
      expect(unknown).toBeDefined();
    }
  });
});
