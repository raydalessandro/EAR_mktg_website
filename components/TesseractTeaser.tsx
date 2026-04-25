import Link from "next/link";

const STATS = [
  { value: "72", label: "nodi" },
  { value: "444", label: "archi" },
  { value: "4×3×3×2", label: "coordinate" },
  { value: "1/36", label: "asimmetria" },
];

export function TesseractTeaser() {
  return (
    <Link
      href="/tesseract"
      className="group block relative rounded-2xl border border-[color:var(--gray-200)] overflow-hidden bg-paper hover:border-accent hover:shadow-md transition-all"
    >
      <div className="absolute inset-0 opacity-[0.06] pointer-events-none">
        <svg
          viewBox="0 0 400 200"
          xmlns="http://www.w3.org/2000/svg"
          className="w-full h-full"
          aria-hidden="true"
        >
          <g stroke="currentColor" strokeWidth="0.5" fill="none">
            {Array.from({ length: 9 }).map((_, i) => (
              <g key={i}>
                <line
                  x1={50 + i * 35}
                  y1="40"
                  x2={70 + i * 35}
                  y2="80"
                />
                <line
                  x1={50 + i * 35}
                  y1="40"
                  x2={50 + i * 35}
                  y2="160"
                />
                <line
                  x1={70 + i * 35}
                  y1="80"
                  x2={70 + i * 35}
                  y2="170"
                />
              </g>
            ))}
            {Array.from({ length: 4 }).map((_, i) => (
              <line
                key={`h${i}`}
                x1="50"
                y1={40 + i * 40}
                x2="330"
                y2={40 + i * 40}
              />
            ))}
            {Array.from({ length: 4 }).map((_, i) => (
              <line
                key={`hb${i}`}
                x1="70"
                y1={80 + i * 30}
                x2="350"
                y2={80 + i * 30}
              />
            ))}
          </g>
        </svg>
      </div>

      <div className="relative px-6 py-7 sm:px-8 sm:py-9 grid gap-5 sm:grid-cols-[1fr_auto] sm:items-center">
        <div>
          <div className="text-xs uppercase tracking-wider text-accent font-mono mb-2">
            Centro ontologico
          </div>
          <h3 className="text-2xl sm:text-3xl font-bold tracking-tight text-ink group-hover:text-accent transition-colors">
            Il Tesseract
          </h3>
          <p className="mt-2 max-w-prose text-sm text-[color:var(--gray-500)] leading-relaxed">
            Reticolo a 72 nodi derivato da prima necessità. Quattro coordinate
            ortogonali, 444 archi, asimmetria 1/36. La struttura geometrica su
            cui poggia tutto il resto del sistema.
          </p>
        </div>

        <div className="grid grid-cols-4 sm:grid-cols-2 gap-x-6 gap-y-3 sm:gap-y-4 sm:min-w-[180px]">
          {STATS.map((s) => (
            <div key={s.label}>
              <div className="font-mono text-xl sm:text-2xl font-bold text-ink tabular-nums">
                {s.value}
              </div>
              <div className="text-[10px] uppercase tracking-wider text-[color:var(--gray-500)]">
                {s.label}
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="relative border-t border-[color:var(--gray-200)] px-6 sm:px-8 py-3 flex items-center justify-between text-sm">
        <span className="text-[color:var(--gray-500)]">
          paper · grafo · 9 test bridge-signature
        </span>
        <span className="text-accent group-hover:translate-x-0.5 transition-transform">
          esplora →
        </span>
      </div>
    </Link>
  );
}
