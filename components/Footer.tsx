import Link from "next/link";

export function Footer() {
  return (
    <footer className="mt-24 border-t border-[color:var(--gray-200)]">
      <div className="mx-auto max-w-canvas px-6 py-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 text-sm text-[color:var(--gray-500)]">
        <div>
          <span className="text-ink font-semibold">nodo432</span>
          <span className="mx-2">·</span>
          <span>Hub di orchestrazione AI</span>
        </div>
        <div className="flex flex-wrap gap-5">
          <Link href="/ontologia" className="hover:text-ink">
            Ontologia
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
          <Link href="/ai" className="hover:text-ink">
            Per AI
          </Link>
          <a href="/llms.txt" className="hover:text-ink font-mono text-xs">
            llms.txt
          </a>
        </div>
      </div>
    </footer>
  );
}
