import path from "node:path";
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";

import {
  _setRootForTesting,
  breadcrumbs,
  collectDownloads,
  countDocumentsDeep,
  findNode,
  flattenDocuments,
  getContentTree,
  topLevelSections,
} from "@/lib/content";

const FIXTURE_ROOT = path.resolve(__dirname, "fixtures/content");
const INVALID_ROOT = path.resolve(__dirname, "fixtures/content-invalid");

beforeAll(() => {
  _setRootForTesting(FIXTURE_ROOT);
});

afterAll(() => {
  _setRootForTesting(null);
});

beforeEach(() => {
  // Reset the cached tree before each test so changes to the root take effect.
  _setRootForTesting(FIXTURE_ROOT);
});

describe("getContentTree()", () => {
  it("returns the expected fixture tree shape", () => {
    const tree = getContentTree();
    expect(tree.kind).toBe("section");
    expect(tree.slug).toEqual([]);
    // Two top-level sections: alpha (order 1) and beta (order 2)
    expect(tree.children.map((c) => c.slug[0])).toEqual(["alpha", "beta"]);

    const alpha = tree.children[0];
    expect(alpha.meta.title).toBe("Alpha");
    // alpha has 1 sub-section and 2 documents
    expect(alpha.children.map((c) => c.slug.join("/"))).toEqual(["alpha/sub"]);
    expect(alpha.documents.map((d) => d.slug.join("/"))).toEqual([
      "alpha/doc-a",
      "alpha/doc-b",
    ]);

    const sub = alpha.children[0];
    expect(sub.documents[0].slug).toEqual(["alpha", "sub", "nested-doc"]);
  });
});

describe("findNode()", () => {
  it("finds a top-level section by slug", () => {
    const node = findNode(["alpha"]);
    expect(node).not.toBeNull();
    expect(node?.kind).toBe("section");
    expect(node?.meta.title).toBe("Alpha");
  });

  it("finds a nested document by slug", () => {
    const node = findNode(["alpha", "sub", "nested-doc"]);
    expect(node).not.toBeNull();
    expect(node?.kind).toBe("document");
    expect(node?.meta.title).toBe("Nested Doc");
  });

  it("finds a direct document under a section", () => {
    const node = findNode(["alpha", "doc-a"]);
    expect(node?.kind).toBe("document");
    expect(node?.meta.title).toBe("Doc A");
  });

  it("returns null for an invalid slug", () => {
    expect(findNode(["nope"])).toBeNull();
    expect(findNode(["alpha", "ghost"])).toBeNull();
    expect(findNode(["alpha", "sub", "missing"])).toBeNull();
  });
});

describe("flattenDocuments()", () => {
  it("returns every document in the tree", () => {
    const docs = flattenDocuments();
    const slugs = docs.map((d) => d.slug.join("/")).sort();
    expect(slugs).toEqual(
      ["alpha/doc-a", "alpha/doc-b", "alpha/sub/nested-doc", "beta/lonely"].sort()
    );
  });
});

describe("countDocumentsDeep()", () => {
  it("counts every document recursively", () => {
    const tree = getContentTree();
    expect(countDocumentsDeep(tree)).toBe(4);
    const alpha = tree.children.find((c) => c.slug[0] === "alpha")!;
    expect(countDocumentsDeep(alpha)).toBe(3);
    const beta = tree.children.find((c) => c.slug[0] === "beta")!;
    expect(countDocumentsDeep(beta)).toBe(1);
  });
});

describe("collectDownloads()", () => {
  it("returns downloads from both sections and documents", () => {
    const tree = getContentTree();
    const downloads = collectDownloads(tree);

    const fromSection = downloads.filter((d) => d.fromKind === "section");
    const fromDoc = downloads.filter((d) => d.fromKind === "document");

    expect(fromSection.length).toBeGreaterThanOrEqual(1);
    expect(fromDoc.length).toBeGreaterThanOrEqual(2);

    const titles = downloads.map((d) => d.title).sort();
    expect(titles).toContain("Alpha");
    expect(titles).toContain("Doc A");
    expect(titles).toContain("Nested Doc");

    // Format passthrough
    const docA = downloads.find((d) => d.title === "Doc A");
    expect(docA?.download.format).toBe("pdf");
    const nested = downloads.find((d) => d.title === "Nested Doc");
    expect(nested?.download.format).toBe("zip");
  });
});

describe("topLevelSections()", () => {
  it("returns the children of the root", () => {
    const top = topLevelSections();
    expect(top.map((s) => s.slug[0])).toEqual(["alpha", "beta"]);
  });
});

describe("breadcrumbs()", () => {
  it("produces home + ancestors for a deep slug", () => {
    const crumbs = breadcrumbs(["alpha", "sub", "nested-doc"]);
    expect(crumbs[0]).toEqual({ href: "/", label: "Home" });
    expect(crumbs.map((c) => c.label)).toEqual([
      "Home",
      "Alpha",
      "Alpha Sub",
      "Nested Doc",
    ]);
    expect(crumbs.map((c) => c.href)).toEqual([
      "/",
      "/alpha",
      "/alpha/sub",
      "/alpha/sub/nested-doc",
    ]);
  });

  it("returns just home for an empty slug", () => {
    expect(breadcrumbs([])).toEqual([{ href: "/", label: "Home" }]);
  });
});

describe("invalid frontmatter", () => {
  it("throws a clear error when a document has missing title", () => {
    _setRootForTesting(INVALID_ROOT);
    expect(() => getContentTree()).toThrow(/Invalid frontmatter/i);
    expect(() => getContentTree()).toThrow(/title/i);
  });
});
