import Link from "next/link";

const SITE = "https://nodo432.com";

export function Footer() {
  return (
    <footer className="mt-24 border-t border-[color:var(--gray-200)]">
      <div className="mx-auto max-w-canvas px-6 py-10 flex flex-col gap-6 text-sm text-[color:var(--gray-500)]">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div>
            <span className="text-ink font-semibold">nodo432</span>
            <span className="mx-2">·</span>
            <span>Hub di orchestrazione AI</span>
          </div>
          <div className="flex flex-wrap gap-5">
            <Link href="/tesseract" className="hover:text-ink">
              Tesseract
            </Link>
            <Link href="/ontologia" className="hover:text-ink">
              Ontologia
            </Link>
            <Link href="/arte" className="hover:text-ink">
              Arte
            </Link>
            <Link href="/risorse" className="hover:text-ink">
              Risorse
            </Link>
            <Link href="/tool" className="hover:text-ink">
              Tool
            </Link>
            <Link href="/pipeline" className="hover:text-ink">
              Pipeline
            </Link>
            <a href={`${SITE}/ai`} className="hover:text-ink">
              Per AI
            </a>
          </div>
        </div>

        <div className="border-t border-[color:var(--gray-200)] pt-4">
          <span className="block sm:inline text-[10px] uppercase tracking-wider mr-3 mb-2 sm:mb-0">
            Endpoint AI
          </span>
          <span className="flex flex-wrap gap-x-4 gap-y-2 font-mono text-xs">
            <a
              href={`${SITE}/ai-instructions.md`}
              className="hover:text-ink"
              data-ai-endpoint="ai-instructions"
            >
              {SITE}/ai-instructions.md
            </a>
            <a
              href={`${SITE}/llms.txt`}
              className="hover:text-ink"
              data-ai-endpoint="llms-txt"
            >
              {SITE}/llms.txt
            </a>
            <a
              href={`${SITE}/llms-full.txt`}
              className="hover:text-ink"
              data-ai-endpoint="llms-full"
            >
              {SITE}/llms-full.txt
            </a>
            <a
              href={`${SITE}/index.json`}
              className="hover:text-ink"
              data-ai-endpoint="index"
            >
              {SITE}/index.json
            </a>
            <a
              href={`${SITE}/graph.json`}
              className="hover:text-ink"
              data-ai-endpoint="graph"
            >
              {SITE}/graph.json
            </a>
          </span>
        </div>
      </div>
    </footer>
  );
}
