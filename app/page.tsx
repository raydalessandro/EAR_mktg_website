import Link from "next/link";
import { SpiralLogo } from "@/components/SpiralLogo";
import { SectionCard } from "@/components/SectionCard";
import { topLevelSections, flattenDocuments } from "@/lib/content";

export default function HomePage() {
  const sections = topLevelSections();
  const allDocs = flattenDocuments().filter(
    (d) => d.meta.status === "published"
  );

  const recent = [...allDocs]
    .sort((a, b) => {
      const ad = (a.meta.updated ?? a.meta.created ?? new Date(0)).getTime();
      const bd = (b.meta.updated ?? b.meta.created ?? new Date(0)).getTime();
      return bd - ad;
    })
    .slice(0, 6);

  const featured = allDocs.filter((d) => d.meta.featured).slice(0, 3);

  return (
    <div className="mx-auto max-w-canvas px-6">
      <section className="pt-20 pb-16 sm:pt-32 sm:pb-24">
        <div className="text-accent inline-flex">
          <SpiralLogo size={64} />
        </div>
        <h1 className="mt-8 text-5xl sm:text-7xl font-bold tracking-tight text-ink">
          nodo<span className="text-accent">432</span>
        </h1>
        <p className="mt-6 max-w-prose text-xl sm:text-2xl text-[color:var(--gray-500)] leading-relaxed">
          Hub di orchestrazione AI. Antologia, risorse scaricabili, tool e
          pipeline — un punto nodale da cui si dipartono i nostri strumenti.
        </p>
        <p className="mt-3 max-w-prose text-sm text-[color:var(--gray-500)]">
          In costruzione: i contenuti vengono aggiunti progressivamente.
        </p>
      </section>

      <section className="pb-16">
        <div className="flex items-baseline justify-between mb-6">
          <h2 className="text-2xl font-bold tracking-tight">Sezioni</h2>
          <span className="text-sm text-[color:var(--gray-500)]">
            {sections.length} {sections.length === 1 ? "ramo" : "rami"}
          </span>
        </div>
        {sections.length > 0 ? (
          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-2">
            {sections.map((s) => (
              <SectionCard key={s.href} node={s} />
            ))}
          </div>
        ) : (
          <p className="text-[color:var(--gray-500)]">Nessuna sezione ancora.</p>
        )}
      </section>

      {featured.length > 0 && (
        <section className="pb-16">
          <h2 className="text-2xl font-bold tracking-tight mb-6">In evidenza</h2>
          <div className="grid gap-4 sm:grid-cols-3">
            {featured.map((doc) => (
              <Link
                key={doc.href}
                href={doc.href}
                className="group block border border-[color:var(--gray-200)] rounded-xl p-5 hover:border-accent hover:shadow-sm transition-all bg-paper"
              >
                <div className="text-xs uppercase tracking-wider text-accent mb-2">
                  {doc.parentSlug.join(" / ")}
                </div>
                <h3 className="font-semibold text-ink group-hover:text-accent transition-colors mb-1">
                  {doc.meta.title}
                </h3>
                {doc.meta.summary && (
                  <p className="text-sm text-[color:var(--gray-500)]">
                    {doc.meta.summary}
                  </p>
                )}
              </Link>
            ))}
          </div>
        </section>
      )}

      {recent.length > 0 && (
        <section className="pb-16">
          <h2 className="text-2xl font-bold tracking-tight mb-6">Recenti</h2>
          <ul className="divide-y divide-[color:var(--gray-200)] border-y border-[color:var(--gray-200)]">
            {recent.map((doc) => (
              <li key={doc.href}>
                <Link
                  href={doc.href}
                  className="flex items-center justify-between gap-6 py-4 group"
                >
                  <div className="min-w-0">
                    <div className="text-xs uppercase tracking-wider text-[color:var(--gray-500)]">
                      {doc.parentSlug.join(" / ")}
                    </div>
                    <div className="font-medium text-ink group-hover:text-accent transition-colors truncate">
                      {doc.meta.title}
                    </div>
                  </div>
                  <span className="text-accent opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                    →
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
