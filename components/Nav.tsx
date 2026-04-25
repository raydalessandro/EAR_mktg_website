import Link from "next/link";
import { SpiralLogo } from "./SpiralLogo";

export function Nav() {
  return (
    <nav className="fixed top-0 inset-x-0 z-40 backdrop-blur bg-paper/80 border-b border-[color:var(--gray-200)]">
      <div className="mx-auto max-w-canvas px-6 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 text-ink no-underline">
          <span className="text-accent">
            <SpiralLogo size={28} />
          </span>
          <span className="font-bold tracking-tight text-lg">nodo432</span>
        </Link>
        <ul className="hidden sm:flex items-center gap-6 text-sm text-[color:var(--gray-500)]">
          <li>
            <Link href="/antologia" className="hover:text-ink transition-colors">
              Antologia
            </Link>
          </li>
          <li>
            <Link href="/risorse" className="hover:text-ink transition-colors">
              Risorse
            </Link>
          </li>
          <li>
            <Link href="/tool" className="hover:text-ink transition-colors">
              Tool
            </Link>
          </li>
          <li>
            <Link href="/pipeline" className="hover:text-ink transition-colors">
              Pipeline
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}
