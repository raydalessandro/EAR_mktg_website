import type { SectionNode } from "@/lib/content";
import { breadcrumbs } from "@/lib/content";
import { Breadcrumbs } from "./Breadcrumbs";
import { SectionCard } from "./SectionCard";
import { DocCard } from "./DocCard";

export function SectionView({ node }: { node: SectionNode }) {
  const crumbs = breadcrumbs(node.slug);
  const hasChildren = node.children.length > 0;
  const hasDocs = node.documents.length > 0;

  return (
    <div className="mx-auto max-w-canvas px-6 py-12">
      <Breadcrumbs items={crumbs} />

      <header className="mb-10 max-w-prose">
        <h1 className="text-4xl sm:text-5xl font-bold tracking-tight text-ink">
          {node.meta.title}
        </h1>
        {node.meta.summary && (
          <p className="mt-4 text-lg text-[color:var(--gray-500)] leading-relaxed">
            {node.meta.summary}
          </p>
        )}
        {node.meta.description && (
          <p className="mt-3 text-base text-[color:var(--gray-500)] leading-relaxed">
            {node.meta.description}
          </p>
        )}
      </header>

      {hasChildren && (
        <section className="mb-12">
          <h2 className="text-sm uppercase tracking-wider text-[color:var(--gray-500)] mb-4">
            Sotto-sezioni
          </h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {node.children.map((child) => (
              <SectionCard key={child.href} node={child} />
            ))}
          </div>
        </section>
      )}

      {hasDocs && (
        <section className="mb-12">
          <h2 className="text-sm uppercase tracking-wider text-[color:var(--gray-500)] mb-4">
            Documenti
          </h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {node.documents.map((doc) => (
              <DocCard key={doc.href} doc={doc} />
            ))}
          </div>
        </section>
      )}

      {!hasChildren && !hasDocs && (
        <div className="border border-dashed border-[color:var(--gray-200)] rounded-xl p-10 text-center text-[color:var(--gray-500)]">
          Sezione vuota. I contenuti arriveranno presto.
        </div>
      )}
    </div>
  );
}
