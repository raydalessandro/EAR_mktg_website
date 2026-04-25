"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { SpiralLogo } from "./SpiralLogo";
import { PersonaSwitcher, usePersona, type Persona } from "./PersonaSwitcher";
import { TesseractTeaser } from "./TesseractTeaser";
import { TypeBadge } from "./TypeBadge";

type SectionLite = {
  slug: string;
  href: string;
  title: string;
  summary: string | null;
  status: string;
  docCount: number;
};

type DocLite = {
  slug: string;
  href: string;
  title: string;
  summary: string | null;
  parentSlug: string[];
  tags: string[];
  type: string | null;
};

type Props = {
  sections: SectionLite[];
  featured: DocLite[];
  recent: DocLite[];
};

const HERO: Record<Persona, { kicker: string; title: string; sub: string }> = {
  ai: {
    kicker: "Per AI agents",
    title: "Catalogo machine-readable",
    sub: "llms.txt, index.json, raw markdown, JSON-LD. Tutto fetchabile, tutto coerente. Una fetch e hai l'ontologia.",
  },
  vibecoder: {
    kicker: "Per Vibecoder",
    title: "Filosofia + tool",
    sub: "Trattato e teoria che giustificano la pratica, accanto a script e plugin pronti. La spirale che diventa pipeline.",
  },
  tecnico: {
    kicker: "Per Tecnico",
    title: "Codice pronto, prompt copia-incolla",
    sub: "Nano kernel per LLM piccoli, schede operative, automazioni e pipeline documentate. Niente sermoni.",
  },
  curioso: {
    kicker: "Per Curioso",
    title: "Sintesi prima del formalismo",
    sub: "Versioni in prosa del sistema, intro accessibili, glossario. Le derivazioni complete sono lì se le cerchi.",
  },
};

const PERSONA_PINS: Record<Persona, string[]> = {
  ai: ["/ai", "/llms.txt", "/index.json"],
  vibecoder: ["/ontologia/trattato", "/tesseract/paper", "/ontologia/aila/sistema-formale/kernel"],
  tecnico: ["/ontologia/aila/nano/nano-kernel", "/ontologia/aila/release-v1", "/tool"],
  curioso: ["/ontologia/aila/in-prosa/kernel-prosa", "/ontologia/aila/sogno-di-leibniz", "/ontologia/teoremi"],
};

const PERSONA_PIN_LABELS: Record<string, string> = {
  "/ai": "Guida AI",
  "/llms.txt": "llms.txt",
  "/index.json": "index.json",
};

export function HomeView({ sections, featured, recent }: Props) {
  const [persona] = usePersona();
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  const hero = HERO[persona];
  const pins = PERSONA_PINS[persona];

  const tesseractSection = sections.find((s) => s.slug === "tesseract");
  const otherSections = sections.filter((s) => s.slug !== "tesseract");

  return (
    <div className="mx-auto max-w-canvas px-6">
      <section className="pt-16 pb-8 sm:pt-24">
        <div className="text-accent inline-flex">
          <SpiralLogo size={56} />
        </div>
        <h1 className="mt-6 text-5xl sm:text-7xl font-bold tracking-tight text-ink">
          nodo<span className="text-accent">432</span>
        </h1>
        <p className="mt-5 max-w-prose text-lg sm:text-xl text-[color:var(--gray-500)] leading-relaxed">
          Hub di orchestrazione AI. Sistema ontologico EAR, Tesseract a 72 nodi,
          notazione AILA, studi empirici e tool.
        </p>

        {mounted && (
          <div className="mt-8">
            <PersonaSwitcher />
          </div>
        )}
      </section>

      {mounted && (
        <section className="pb-12">
          <p className="text-xs uppercase tracking-wider text-accent font-mono mb-2">
            {hero.kicker}
          </p>
          <h2 className="text-3xl sm:text-4xl font-bold tracking-tight max-w-prose">
            {hero.title}
          </h2>
          <p className="mt-3 max-w-prose text-[color:var(--gray-500)] leading-relaxed">
            {hero.sub}
          </p>
          <div className="mt-5 flex flex-wrap gap-3">
            {pins.map((href) => {
              const isExt = href.endsWith(".txt") || href.endsWith(".json");
              const label =
                PERSONA_PIN_LABELS[href] ??
                href.replace(/^\/ontologia\//, "").replace(/-/g, " ").replace(/\//g, " · ");
              const className =
                "inline-flex items-center gap-1 text-sm px-3 py-1.5 rounded-full border border-[color:var(--gray-200)] hover:border-accent hover:text-accent transition-colors";
              return isExt ? (
                <a key={href} href={href} className={className}>
                  {label} <span className="opacity-60">↗</span>
                </a>
              ) : (
                <Link key={href} href={href} className={className}>
                  {label} <span className="opacity-60">→</span>
                </Link>
              );
            })}
          </div>
        </section>
      )}

      {tesseractSection && (
        <section className="pb-12">
          <TesseractTeaser />
        </section>
      )}

      <section className="pb-12">
        <div className="flex items-baseline justify-between mb-4">
          <h2 className="text-2xl font-bold tracking-tight">Altre sezioni</h2>
        </div>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-2">
          {otherSections.map((s) => {
            const dimmed = s.status === "wip" || s.status === "coming-soon";
            return (
              <Link
                key={s.href}
                href={s.href}
                className={`group block border border-[color:var(--gray-200)] rounded-xl p-5 hover:border-accent hover:shadow-sm transition-all bg-paper ${
                  dimmed ? "opacity-70" : ""
                }`}
              >
                <h3 className="text-lg font-semibold text-ink group-hover:text-accent transition-colors mb-1">
                  {s.title}
                </h3>
                {s.summary && (
                  <p className="text-sm text-[color:var(--gray-500)] leading-relaxed mb-3">
                    {s.summary}
                  </p>
                )}
                <div className="text-xs text-[color:var(--gray-500)] tabular-nums">
                  {s.docCount} {s.docCount === 1 ? "documento" : "documenti"}
                </div>
              </Link>
            );
          })}
        </div>
      </section>

      {featured.length > 0 && (
        <section className="pb-12">
          <h2 className="text-2xl font-bold tracking-tight mb-4">In evidenza</h2>
          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {featured.map((doc) => (
              <Link
                key={doc.href}
                href={doc.href}
                className="group block border border-[color:var(--gray-200)] rounded-xl p-4 hover:border-accent hover:shadow-sm transition-all bg-paper"
              >
                <div className="flex items-center gap-2 mb-2">
                  {doc.type ? (
                    <TypeBadge type={doc.type} />
                  ) : (
                    <span className="text-[10px] uppercase tracking-wider text-[color:var(--gray-500)] font-mono truncate">
                      {doc.parentSlug.join(" / ")}
                    </span>
                  )}
                </div>
                <h3 className="font-semibold text-ink group-hover:text-accent transition-colors mb-1">
                  {doc.title}
                </h3>
                {doc.summary && (
                  <p className="text-xs text-[color:var(--gray-500)] line-clamp-2">
                    {doc.summary}
                  </p>
                )}
              </Link>
            ))}
          </div>
        </section>
      )}

      {recent.length > 0 && (
        <section className="pb-16">
          <h2 className="text-2xl font-bold tracking-tight mb-4">Recenti</h2>
          <ul className="divide-y divide-[color:var(--gray-200)] border-y border-[color:var(--gray-200)]">
            {recent.map((doc) => (
              <li key={doc.href}>
                <Link
                  href={doc.href}
                  className="flex items-center justify-between gap-6 py-3 group"
                >
                  <div className="min-w-0">
                    <div className="text-xs uppercase tracking-wider text-[color:var(--gray-500)] font-mono">
                      {doc.parentSlug.join(" / ")}
                    </div>
                    <div className="font-medium text-ink group-hover:text-accent transition-colors truncate">
                      {doc.title}
                    </div>
                  </div>
                  <span className="text-accent opacity-0 group-hover:opacity-100 transition-opacity shrink-0">
                    →
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
