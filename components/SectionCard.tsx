import Link from "next/link";
import type { SectionNode } from "@/lib/content";
import { countDocumentsDeep } from "@/lib/content";

const STATUS_LABEL: Record<string, string> = {
  published: "Live",
  draft: "Draft",
  wip: "In costruzione",
  "coming-soon": "Coming soon",
};

const STATUS_COLOR: Record<string, string> = {
  published: "text-emerald-700 bg-emerald-50 border-emerald-100",
  draft: "text-amber-700 bg-amber-50 border-amber-100",
  wip: "text-amber-700 bg-amber-50 border-amber-100",
  "coming-soon": "text-[color:var(--gray-500)] bg-[color:var(--gray-50)] border-[color:var(--gray-200)]",
};

type Props = {
  node: SectionNode;
  variant?: "tile" | "row";
};

export function SectionCard({ node, variant = "tile" }: Props) {
  const count = countDocumentsDeep(node);
  const status = node.meta.status;
  const dimmed = status === "wip" || status === "coming-soon";

  if (variant === "row") {
    return (
      <Link
        href={node.href}
        className={`group flex items-start gap-4 border border-[color:var(--gray-200)] rounded-xl p-5 transition-all hover:border-accent hover:shadow-sm bg-paper ${
          dimmed ? "opacity-70" : ""
        }`}
      >
        <div className="flex-1">
          <div className="flex items-center gap-3 mb-1">
            <h3 className="text-lg font-semibold text-ink group-hover:text-accent transition-colors">
              {node.meta.title}
            </h3>
            <span
              className={`text-[10px] uppercase tracking-wider font-medium px-2 py-0.5 rounded border ${STATUS_COLOR[status]}`}
            >
              {STATUS_LABEL[status]}
            </span>
          </div>
          {node.meta.summary && (
            <p className="text-sm text-[color:var(--gray-500)]">{node.meta.summary}</p>
          )}
        </div>
        <div className="text-right text-sm text-[color:var(--gray-500)] tabular-nums shrink-0">
          {count} {count === 1 ? "doc" : "docs"}
        </div>
      </Link>
    );
  }

  return (
    <Link
      href={node.href}
      className={`group block border border-[color:var(--gray-200)] rounded-2xl p-6 transition-all hover:border-accent hover:shadow-md bg-paper relative overflow-hidden ${
        dimmed ? "opacity-70" : ""
      }`}
    >
      <div className="flex items-start justify-between gap-3 mb-3">
        <h3 className="text-xl font-bold text-ink group-hover:text-accent transition-colors">
          {node.meta.title}
        </h3>
        <span
          className={`text-[10px] uppercase tracking-wider font-medium px-2 py-0.5 rounded border ${STATUS_COLOR[status]} shrink-0`}
        >
          {STATUS_LABEL[status]}
        </span>
      </div>
      {node.meta.summary && (
        <p className="text-sm text-[color:var(--gray-500)] leading-relaxed mb-4">
          {node.meta.summary}
        </p>
      )}
      <div className="flex items-center justify-between text-sm text-[color:var(--gray-500)]">
        <span className="tabular-nums">
          {count} {count === 1 ? "documento" : "documenti"}
        </span>
        <span className="text-accent opacity-0 group-hover:opacity-100 transition-opacity">→</span>
      </div>
    </Link>
  );
}
