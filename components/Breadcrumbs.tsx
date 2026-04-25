import Link from "next/link";

type Crumb = { href: string; label: string };

export function Breadcrumbs({ items }: { items: Crumb[] }) {
  if (items.length <= 1) return null;
  return (
    <nav aria-label="Breadcrumbs" className="text-sm text-[color:var(--gray-500)] mb-6">
      <ol className="flex flex-wrap items-center gap-1.5">
        {items.map((item, i) => {
          const isLast = i === items.length - 1;
          return (
            <li key={item.href} className="flex items-center gap-1.5">
              {isLast ? (
                <span className="text-ink">{item.label}</span>
              ) : (
                <Link href={item.href} className="hover:text-ink transition-colors">
                  {item.label}
                </Link>
              )}
              {!isLast && <span className="opacity-50">/</span>}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}
