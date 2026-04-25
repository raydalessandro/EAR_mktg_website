const SITE_URL = "https://nodo432.com";

type DocumentMeta = {
  description?: string;
  authors?: string[];
  created?: Date;
  updated?: Date;
  license?: string;
  tags?: string[];
  download?: { file?: string; format?: string };
};

export type DocumentInput = {
  title: string;
  summary?: string;
  href: string;
  meta: DocumentMeta;
};

export function documentJsonLd(doc: DocumentInput): Record<string, unknown> {
  const url = SITE_URL + doc.href;
  const rawUrl = url.replace(/\/$/, "") + ".md";
  const datePublished = doc.meta.created?.toISOString?.();
  const dateModified =
    doc.meta.updated?.toISOString?.() ?? datePublished ?? undefined;
  return {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    headline: doc.title,
    description: doc.summary ?? doc.meta.description,
    url,
    mainEntityOfPage: { "@type": "WebPage", "@id": url },
    inLanguage: "it-IT",
    author: (doc.meta.authors ?? []).map((name) => ({
      "@type": "Person",
      name,
    })),
    datePublished,
    dateModified,
    license: doc.meta.license,
    keywords: (doc.meta.tags ?? []).join(", "),
    isPartOf: {
      "@type": "WebSite",
      name: "nodo432",
      url: SITE_URL,
    },
    encoding: [
      {
        "@type": "MediaObject",
        encodingFormat: "text/markdown",
        contentUrl: rawUrl,
        description: "Raw markdown source of this page",
      },
      ...(doc.meta.download?.file
        ? [
            {
              "@type": "MediaObject",
              encodingFormat:
                doc.meta.download.format === "pdf"
                  ? "application/pdf"
                  : "text/markdown",
              contentUrl: doc.meta.download.file.startsWith("http")
                ? doc.meta.download.file
                : SITE_URL + doc.meta.download.file,
              description: "Canonical downloadable version",
            },
          ]
        : []),
    ],
  };
}

export type SectionInput = {
  title: string;
  summary?: string;
  href: string;
};

export function sectionJsonLd(section: SectionInput): Record<string, unknown> {
  const url = SITE_URL + section.href;
  return {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: section.title,
    description: section.summary,
    url,
    inLanguage: "it-IT",
    isPartOf: {
      "@type": "WebSite",
      name: "nodo432",
      url: SITE_URL,
    },
  };
}
