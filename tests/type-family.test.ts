import { describe, it, expect } from "vitest";
import { getTypeFamily, knownTypes } from "@/lib/type-family";

describe("getTypeFamily", () => {
  it("returns 'philosophy' for trattato", () => {
    expect(getTypeFamily("trattato")).toBe("philosophy");
  });

  it("returns 'theory' for teorema and papers", () => {
    expect(getTypeFamily("teorema")).toBe("theory");
    expect(getTypeFamily("paper")).toBe("theory");
    expect(getTypeFamily("paper-appendix")).toBe("theory");
  });

  it("returns 'aila' for all aila-* types", () => {
    const ailaTypes = [
      "aila-spec",
      "aila-notation",
      "aila-operational",
      "aila-derivation",
      "aila-empirical",
      "aila-extension",
      "aila-nano",
      "aila-prose-companion",
      "aila-manifesto",
      "aila-release",
    ];
    for (const t of ailaTypes) {
      expect(getTypeFamily(t)).toBe("aila");
    }
  });

  it("returns 'study' for studies and datasets", () => {
    expect(getTypeFamily("study")).toBe("study");
    expect(getTypeFamily("dataset")).toBe("study");
    expect(getTypeFamily("visualization")).toBe("study");
    expect(getTypeFamily("batch")).toBe("study");
    expect(getTypeFamily("report")).toBe("study");
  });

  it("returns 'tool' for tools and pipelines", () => {
    expect(getTypeFamily("tool")).toBe("tool");
    expect(getTypeFamily("pipeline")).toBe("tool");
    expect(getTypeFamily("methodology")).toBe("tool");
    expect(getTypeFamily("template")).toBe("tool");
  });

  it("returns 'neutral' for collection (router)", () => {
    expect(getTypeFamily("collection")).toBe("neutral");
  });

  it("returns 'neutral' for unknown types", () => {
    expect(getTypeFamily("madeup")).toBe("neutral");
    expect(getTypeFamily("future-type")).toBe("neutral");
  });

  it("returns 'neutral' for null/undefined", () => {
    expect(getTypeFamily(null)).toBe("neutral");
    expect(getTypeFamily(undefined)).toBe("neutral");
    expect(getTypeFamily("")).toBe("neutral");
  });
});

describe("knownTypes", () => {
  it("returns a non-empty list", () => {
    expect(knownTypes().length).toBeGreaterThan(10);
  });

  it("includes the canonical types we use across the site", () => {
    const types = knownTypes();
    for (const expected of [
      "trattato",
      "teorema",
      "aila-spec",
      "study",
      "tool",
      "pipeline",
      "collection",
    ]) {
      expect(types).toContain(expected);
    }
  });
});
