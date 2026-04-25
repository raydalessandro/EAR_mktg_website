import Link from "next/link";
import type { DocumentNode } from "@/lib/content";
import { breadcrumbs, findNode } from "@/lib/content";
import { Breadcrumbs } from "./Breadcrumbs";
import { JsonLd, documentJsonLd } from "./JsonLd";
import { FrontmatterMarker } from "./FrontmatterMarker";
import { TypeBadge } from "./TypeBadge";

type Props = {
  doc: DocumentNode;
  html: string;
};

function formatDate(d: Date | undefined) {
  if (!d) return null;
  return new Intl.DateTimeFormat("it-IT", {
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(d);
}

export function DocumentView({ doc, html }: Props) {
  const crumbs = breadcrumbs(doc.slug);
  const updated = formatDate(doc.meta.updated ?? doc.meta.created);

  const related = doc.meta.related
    .map((slug) => {
      const parts = slug.split("/").filter(Boolean);
      const node = findNode(parts);
      return node;
    })
    .filter((n): n is NonNullable<typeof n> => n !== null);

  return (
    <article className="mx-auto max-w-canvas px-6 py-12">
      <FrontmatterMarker
        meta={doc.meta}
        slug={doc.slug.join("/")}
        kind="document"
      />
      <JsonLd
        data={documentJsonLd({
          title: doc.meta.title,
          summary: doc.meta.summary,
          href: doc.href,
          meta: doc.meta,
        })}
      />
      <Breadcrumbs items={crumbs} />

      <header className="mb-8 max-w-prose">
        {(doc.meta.type || doc.meta.version) && (
          <div className="mb-3">
            <TypeBadge type={doc.meta.type} version={doc.meta.version} size="md" />
          </div>
        )}
        <h1 className="text-4xl sm:text-5xl font-bold tracking-tight text-ink">
          {doc.meta.title}
        </h1>
        {doc.meta.summary && (
          <p className="mt-4 text-lg text-[color:var(--gray-500)] leading-relaxed">
            {doc.meta.summary}
          </p>
        )}

        <div className="mt-6 flex flex-wrap items-center gap-x-5 gap-y-2 text-sm text-[color:var(--gray-500)]">
          {updated && <span>Aggiornato il {updated}</span>}
          {doc.meta.authors.length > 0 && <span>· {doc.meta.authors.join(", ")}</span>}
          {doc.meta.license && (
            <span className="font-mono text-xs border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">
              {doc.meta.license}
            </span>
          )}
        </div>

        {doc.meta.tags.length > 0 && (
          <div className="mt-4 flex flex-wrap gap-2">
            {doc.meta.tags.map((tag) => (
              <span
                key={tag}
                className="text-xs text-[color:var(--gray-500)] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-2 py-0.5"
              >
                #{tag}
              </span>
            ))}
          </div>
        )}

        {doc.meta.download && (
          <a
            href={doc.meta.download.file}
            download
            className="mt-6 inline-flex items-center gap-2 bg-ink text-paper rounded-lg px-4 py-2.5 text-sm font-medium hover:bg-accent hover:text-ink transition-colors"
          >
            <span>Scarica</span>
            <span className="font-mono text-xs uppercase opacity-80">
              {doc.meta.download.format}
            </span>
            {doc.meta.download.size && (
              <span className="font-mono text-xs opacity-60">· {doc.meta.download.size}</span>
            )}
          </a>
        )}
      </header>

      <div className="prose-nodo" dangerouslySetInnerHTML={{ __html: html }} />

      {related.length > 0 && (
        <section className="mt-16 pt-8 border-t border-[color:var(--gray-200)] max-w-prose">
          <h2 className="text-sm uppercase tracking-wider text-[color:var(--gray-500)] mb-4">
            Correlati
          </h2>
          <ul className="space-y-2">
            {related.map((node) => (
              <li key={node.href}>
                <Link
                  href={node.href}
                  className="text-ink hover:text-accent transition-colors"
                >
                  {node.meta.title} →
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </article>
  );
}
