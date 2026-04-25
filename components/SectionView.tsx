import fs from "node:fs";
import type { SectionNode } from "@/lib/content";
import { breadcrumbs, collectDownloads, renderMarkdown } from "@/lib/content";
import { Breadcrumbs } from "./Breadcrumbs";
import { SectionCard } from "./SectionCard";
import { DocCard } from "./DocCard";
import { JsonLd, sectionJsonLd } from "./JsonLd";
import { FrontmatterMarker } from "./FrontmatterMarker";
import { AllDownloads } from "./AllDownloads";
import { LlmDirective } from "./LlmDirective";

function readSectionBody(node: SectionNode): string {
  const file = `${node.dirPath}/_section.md`;
  if (!fs.existsSync(file)) return "";
  const raw = fs.readFileSync(file, "utf8");
  const match = raw.match(/^---\n[\s\S]*?\n---\n?/);
  return match ? raw.slice(match[0].length).trim() : raw.trim();
}

export async function SectionView({ node }: { node: SectionNode }) {
  const crumbs = breadcrumbs(node.slug);
  const hasChildren = node.children.length > 0;
  const hasDocs = node.documents.length > 0;
  const body = readSectionBody(node);
  const html = body ? await renderMarkdown(body) : "";
  const download = node.meta.download;
  const allDownloads = collectDownloads(node);

  return (
    <div className="mx-auto max-w-canvas px-6 py-12">
      <FrontmatterMarker
        meta={node.meta}
        slug={node.slug.join("/")}
        kind="section"
      />
      <JsonLd
        data={sectionJsonLd({
          title: node.meta.title,
          summary: node.meta.summary,
          href: node.href,
        })}
      />
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

        {download && (
          <a
            href={download.file}
            download
            className="mt-6 inline-flex items-center gap-2 bg-ink text-paper rounded-lg px-4 py-2.5 text-sm font-medium hover:bg-accent hover:text-ink transition-colors"
          >
            <span>Scarica</span>
            <span className="font-mono text-xs uppercase opacity-80">
              {download.format}
            </span>
            {download.size && (
              <span className="font-mono text-xs opacity-60">· {download.size}</span>
            )}
          </a>
        )}
      </header>

      {node.meta.llm_directive && (
        <LlmDirective directive={node.meta.llm_directive} />
      )}

      {html && (
        <div className="prose-nodo mb-12" dangerouslySetInnerHTML={{ __html: html }} />
      )}

      {allDownloads.length > 1 && <AllDownloads entries={allDownloads} />}

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

      {!hasChildren && !hasDocs && !html && (
        <div className="border border-dashed border-[color:var(--gray-200)] rounded-xl p-10 text-center text-[color:var(--gray-500)]">
          Sezione vuota. I contenuti arriveranno presto.
        </div>
      )}
    </div>
  );
}
