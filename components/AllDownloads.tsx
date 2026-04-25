import Link from "next/link";
import type { DownloadEntry } from "@/lib/content";

type Props = {
  entries: DownloadEntry[];
};

export function AllDownloads({ entries }: Props) {
  if (entries.length === 0) return null;

  return (
    <details className="mb-12 border border-[color:var(--gray-200)] rounded-xl bg-paper group">
      <summary className="cursor-pointer select-none px-5 py-4 flex items-center justify-between gap-3 list-none [&::-webkit-details-marker]:hidden">
        <div className="flex items-center gap-3">
          <span className="text-sm font-semibold text-ink">
            Tutti i download di questa sezione
          </span>
          <span className="text-xs text-[color:var(--gray-500)] tabular-nums">
            {entries.length} {entries.length === 1 ? "file" : "file"}
          </span>
        </div>
        <span className="text-accent text-sm transition-transform group-open:rotate-90">
          ›
        </span>
      </summary>
      <div className="border-t border-[color:var(--gray-200)] px-5 py-4">
        <ul className="divide-y divide-[color:var(--gray-200)]">
          {entries.map((e, i) => (
            <li
              key={`${e.href}-${i}`}
              className="py-3 flex items-center justify-between gap-4"
            >
              <div className="min-w-0">
                <Link
                  href={e.href}
                  className="font-medium text-ink hover:text-accent transition-colors"
                >
                  {e.title}
                </Link>
                <div className="text-xs text-[color:var(--gray-500)] font-mono truncate">
                  {e.download.file}
                </div>
              </div>
              <a
                href={e.download.file}
                download
                className="shrink-0 inline-flex items-center gap-2 text-sm text-ink hover:text-accent transition-colors"
              >
                <span className="font-mono text-xs uppercase border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">
                  {e.download.format}
                </span>
                {e.download.size && (
                  <span className="font-mono text-xs text-[color:var(--gray-500)]">
                    {e.download.size}
                  </span>
                )}
                <span className="text-accent">↓</span>
              </a>
            </li>
          ))}
        </ul>
      </div>
    </details>
  );
}
