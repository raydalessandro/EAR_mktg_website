"use client";

import { useState } from "react";

const VIZ_URL = "/tesseract/viz";
const FULLSCREEN_URL = "/tesseract/viz";

export function TesseractEmbed() {
  const [loaded, setLoaded] = useState(false);

  return (
    <div className="relative rounded-2xl border border-[color:var(--gray-200)] overflow-hidden bg-paper">
      <div className="px-5 py-3 border-b border-[color:var(--gray-200)] flex items-center justify-between">
        <div>
          <span className="font-semibold text-ink">Tesseract</span>
          <span className="ml-3 text-xs text-[color:var(--gray-500)]">
            72 nodi · 444 archi · interattivo
          </span>
        </div>
        <a
          href={FULLSCREEN_URL}
          target="_blank"
          rel="noopener noreferrer"
          className="text-xs text-accent hover:text-ink transition-colors"
        >
          apri full-screen ↗
        </a>
      </div>
      <div className="relative aspect-[16/10] bg-[color:var(--gray-50)]">
        {!loaded && (
          <div className="absolute inset-0 flex items-center justify-center text-sm text-[color:var(--gray-500)]">
            <span className="animate-pulse">caricamento del reticolo…</span>
          </div>
        )}
        <iframe
          src={VIZ_URL}
          title="Tesseract — visualizzazione 3D interattiva"
          className="absolute inset-0 w-full h-full"
          loading="lazy"
          onLoad={() => setLoaded(true)}
          sandbox="allow-scripts allow-same-origin"
        />
      </div>
    </div>
  );
}
