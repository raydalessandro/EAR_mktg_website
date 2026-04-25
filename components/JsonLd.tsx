type Props = {
  data: Record<string, unknown>;
};

export function JsonLd({ data }: Props) {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
    />
  );
}

const SITE_URL = "https://nodo432.com";

export function documentJsonLd(doc: {
  title: string;
  summary?: string;
  href: string;
  meta: {
    description?: string;
    authors?: string[];
    created?: Date;
    updated?: Date;
    license?: string;
    tags?: string[];
    download?: { file?: string; format?: string };
  };
}) {
  const url = SITE_URL + doc.href;
  const rawUrl = url.replace(/\/$/, "") + ".md";
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
    datePublished: doc.meta.created?.toISOString?.() ?? undefined,
    dateModified: doc.meta.updated?.toISOString?.() ?? doc.meta.created?.toISOString?.() ?? undefined,
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

export function sectionJsonLd(section: {
  title: string;
  summary?: string;
  href: string;
}) {
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
