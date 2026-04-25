import Link from "next/link";

export default function NotFound() {
  return (
    <div className="mx-auto max-w-canvas px-6 py-24 text-center">
      <p className="text-sm uppercase tracking-wider text-[color:var(--gray-500)]">
        404
      </p>
      <h1 className="mt-4 text-4xl sm:text-5xl font-bold tracking-tight">
        Nodo non trovato
      </h1>
      <p className="mt-4 text-[color:var(--gray-500)]">
        La pagina richiesta non esiste o è stata spostata.
      </p>
      <Link
        href="/"
        className="mt-8 inline-block bg-ink text-paper rounded-lg px-4 py-2.5 text-sm font-medium hover:bg-accent hover:text-ink transition-colors"
      >
        Torna alla home
      </Link>
    </div>
  );
}
