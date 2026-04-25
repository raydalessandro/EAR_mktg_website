import { describe, it, expect } from "vitest";
import { documentJsonLd, sectionJsonLd } from "@/lib/json-ld";

describe("documentJsonLd", () => {
  it("produces a TechArticle with absolute url and raw markdown encoding", () => {
    const ld = documentJsonLd({
      title: "Soglia Critica",
      summary: "Le transizioni locale→globale passano sempre per una soglia.",
      href: "/ontologia/teoremi/3-soglia-critica",
      meta: {},
    });
    expect(ld["@type"]).toBe("TechArticle");
    expect(ld["@context"]).toBe("https://schema.org");
    expect(ld.url).toBe("https://nodo432.com/ontologia/teoremi/3-soglia-critica");
    expect(ld.headline).toBe("Soglia Critica");

    const encoding = ld.encoding as Array<Record<string, unknown>>;
    expect(encoding).toHaveLength(1);
    expect(encoding[0].encodingFormat).toBe("text/markdown");
    expect(encoding[0].contentUrl).toBe(
      "https://nodo432.com/ontologia/teoremi/3-soglia-critica.md"
    );
  });

  it("adds a second encoding entry for canonical download (relative path)", () => {
    const ld = documentJsonLd({
      title: "Trattato",
      href: "/ontologia/trattato",
      meta: {
        download: { file: "/downloads/ontologia/trattato/x.pdf", format: "pdf" },
      },
    });
    const encoding = ld.encoding as Array<Record<string, unknown>>;
    expect(encoding).toHaveLength(2);
    expect(encoding[1].encodingFormat).toBe("application/pdf");
    expect(encoding[1].contentUrl).toBe(
      "https://nodo432.com/downloads/ontologia/trattato/x.pdf"
    );
  });

  it("preserves an absolute external download URL", () => {
    const ld = documentJsonLd({
      title: "External",
      href: "/x",
      meta: {
        download: { file: "https://cdn.example.com/file.zip", format: "zip" },
      },
    });
    const encoding = ld.encoding as Array<Record<string, unknown>>;
    expect(encoding[1].contentUrl).toBe("https://cdn.example.com/file.zip");
  });

  it("uses summary then description for description", () => {
    const ld1 = documentJsonLd({
      title: "T",
      summary: "summary text",
      href: "/x",
      meta: { description: "long desc" },
    });
    expect(ld1.description).toBe("summary text");

    const ld2 = documentJsonLd({
      title: "T",
      href: "/x",
      meta: { description: "long desc" },
    });
    expect(ld2.description).toBe("long desc");
  });

  it("emits joined keywords and author array", () => {
    const ld = documentJsonLd({
      title: "T",
      href: "/x",
      meta: { tags: ["alpha", "beta"], authors: ["Ray", "Claude"] },
    });
    expect(ld.keywords).toBe("alpha, beta");
    expect(ld.author).toEqual([
      { "@type": "Person", name: "Ray" },
      { "@type": "Person", name: "Claude" },
    ]);
  });

  it("emits ISO date strings only when dates are present", () => {
    const ld = documentJsonLd({
      title: "T",
      href: "/x",
      meta: {
        created: new Date("2026-04-25T00:00:00Z"),
        updated: new Date("2026-04-26T00:00:00Z"),
      },
    });
    expect(ld.datePublished).toBe("2026-04-25T00:00:00.000Z");
    expect(ld.dateModified).toBe("2026-04-26T00:00:00.000Z");
  });

  it("falls back dateModified to created when updated is missing", () => {
    const ld = documentJsonLd({
      title: "T",
      href: "/x",
      meta: { created: new Date("2026-04-25T00:00:00Z") },
    });
    expect(ld.dateModified).toBe("2026-04-25T00:00:00.000Z");
  });
});

describe("sectionJsonLd", () => {
  it("produces a CollectionPage with absolute url", () => {
    const ld = sectionJsonLd({
      title: "Ontologia",
      summary: "Sistema fondante",
      href: "/ontologia",
    });
    expect(ld["@type"]).toBe("CollectionPage");
    expect(ld.name).toBe("Ontologia");
    expect(ld.url).toBe("https://nodo432.com/ontologia");
    expect(ld.description).toBe("Sistema fondante");
    const isPartOf = ld.isPartOf as Record<string, unknown>;
    expect(isPartOf["@type"]).toBe("WebSite");
    expect(isPartOf.url).toBe("https://nodo432.com");
  });
});
