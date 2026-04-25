import { getTypeFamily } from "@/lib/type-family";

type Props = {
  type?: string | null;
  version?: string | null;
  size?: "sm" | "md";
  className?: string;
};

const FAMILY_STYLE: Record<string, string> = {
  philosophy: "bg-amber-50 text-amber-800 border-amber-200",
  theory: "bg-violet-50 text-violet-800 border-violet-200",
  aila: "bg-emerald-50 text-emerald-800 border-emerald-200",
  study: "bg-sky-50 text-sky-800 border-sky-200",
  tool: "bg-slate-100 text-slate-700 border-slate-200",
  neutral:
    "bg-[color:var(--gray-50)] text-[color:var(--gray-500)] border-[color:var(--gray-200)]",
};

export function TypeBadge({ type, version, size = "sm", className = "" }: Props) {
  if (!type && !version) return null;
  const family = getTypeFamily(type);
  const style = FAMILY_STYLE[family];
  const sizing =
    size === "md" ? "text-xs px-2 py-0.5" : "text-[10px] px-1.5 py-0.5";

  return (
    <span
      className={`inline-flex items-center gap-1 rounded-md border font-mono uppercase tracking-wider ${sizing} ${style} ${className}`}
    >
      {type && <span>{type}</span>}
      {version && <span className="opacity-75">v{version}</span>}
    </span>
  );
}
