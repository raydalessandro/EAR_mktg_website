"use client";

import { useEffect, useState } from "react";

export const PERSONAS = ["ai", "vibecoder", "tecnico", "curioso"] as const;
export type Persona = (typeof PERSONAS)[number];

const STORAGE_KEY = "nodo432:persona";

export function getPersonaFromUrl(): Persona | null {
  if (typeof window === "undefined") return null;
  const params = new URLSearchParams(window.location.search);
  const p = params.get("as");
  if (p && (PERSONAS as readonly string[]).includes(p)) return p as Persona;
  return null;
}

export function usePersona(): [Persona, (p: Persona) => void] {
  const [persona, setPersona] = useState<Persona>("vibecoder");

  useEffect(() => {
    const fromUrl = getPersonaFromUrl();
    if (fromUrl) {
      setPersona(fromUrl);
      localStorage.setItem(STORAGE_KEY, fromUrl);
      return;
    }
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored && (PERSONAS as readonly string[]).includes(stored)) {
      setPersona(stored as Persona);
    }
  }, []);

  const update = (p: Persona) => {
    setPersona(p);
    localStorage.setItem(STORAGE_KEY, p);
    const url = new URL(window.location.href);
    url.searchParams.set("as", p);
    window.history.replaceState({}, "", url);
  };

  return [persona, update];
}

const LABEL: Record<Persona, string> = {
  ai: "AI",
  vibecoder: "Vibecoder",
  tecnico: "Tecnico",
  curioso: "Curioso",
};

const TAGLINE: Record<Persona, string> = {
  ai: "raw data, llms.txt, JSON catalogo, raw markdown",
  vibecoder: "filosofia + tool, teoria che giustifica la pratica",
  tecnico: "prompt copia-incolla, pipeline documentate, automazioni",
  curioso: "sintesi, intro accessibili, glossario",
};

type Props = {
  onChange?: (p: Persona) => void;
};

export function PersonaSwitcher({ onChange }: Props) {
  const [persona, setPersona] = usePersona();

  const handleSet = (p: Persona) => {
    setPersona(p);
    onChange?.(p);
  };

  return (
    <div className="inline-flex flex-col gap-2 mb-8">
      <div className="flex flex-wrap gap-2">
        {PERSONAS.map((p) => {
          const active = persona === p;
          return (
            <button
              key={p}
              type="button"
              onClick={() => handleSet(p)}
              className={`px-4 py-2 rounded-full border text-sm transition-all ${
                active
                  ? "bg-ink text-paper border-ink"
                  : "border-[color:var(--gray-200)] text-[color:var(--gray-500)] hover:border-accent hover:text-ink"
              }`}
              aria-pressed={active}
            >
              {LABEL[p]}
            </button>
          );
        })}
      </div>
      <p className="text-xs text-[color:var(--gray-500)]">
        {TAGLINE[persona]}
      </p>
    </div>
  );
}
