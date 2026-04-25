import Link from "next/link";
import type { DocumentNode } from "@/lib/content";

const STATUS_LABEL: Record<string, string> = {
  published: "Live",
  draft: "Draft",
  wip: "In costruzione",
  "coming-soon": "Coming soon",
};

export function DocCard({ doc }: { doc: DocumentNode }) {
  const dimmed = doc.meta.status === "wip" || doc.meta.status === "coming-soon";
  return (
    <Link
      href={doc.href}
      className={`group block border border-[color:var(--gray-200)] rounded-xl p-5 hover:border-accent hover:shadow-sm transition-all bg-paper ${
        dimmed ? "opacity-70" : ""
      }`}
    >
      <div className="flex items-start justify-between gap-3 mb-2">
        <h4 className="font-semibold text-ink group-hover:text-accent transition-colors">
          {doc.meta.title}
        </h4>
        {doc.meta.download && (
          <span className="text-[10px] uppercase tracking-wider text-accent border border-accent/40 rounded px-1.5 py-0.5 shrink-0">
            {doc.meta.download.format}
          </span>
        )}
      </div>
      {doc.meta.summary && (
        <p className="text-sm text-[color:var(--gray-500)] leading-relaxed mb-3">
          {doc.meta.summary}
        </p>
      )}
      {doc.meta.tags.length > 0 && (
        <div className="flex flex-wrap gap-1.5">
          {doc.meta.tags.slice(0, 4).map((tag) => (
            <span
              key={tag}
              className="text-[11px] text-[color:var(--gray-500)] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5"
            >
              #{tag}
            </span>
          ))}
        </div>
      )}
      {(doc.meta.status === "wip" || doc.meta.status === "coming-soon") && (
        <div className="mt-3 text-[10px] uppercase tracking-wider text-[color:var(--gray-500)]">
          {STATUS_LABEL[doc.meta.status]}
        </div>
      )}
    </Link>
  );
}
