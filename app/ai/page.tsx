import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Per AI agents",
  description:
    "Come consumare nodo432 da agenti AI: llms.txt, raw markdown, catalogo JSON, MCP server (roadmap).",
};

const SITE = "https://nodo432.com";

const endpoints = [
  {
    path: "/llms.txt",
    title: "Mappa per LLM",
    description:
      "Standard llmstxt.org. Mappa testuale del sito ottimizzata per LLM, con descrizioni e link.",
  },
  {
    path: "/llms-full.txt",
    title: "Tutti i contenuti pubblicati",
    description:
      "Concatenazione di tutti i documenti in stato published. Una sola fetch per avere tutto in contesto.",
  },
  {
    path: "/index.json",
    title: "Catalogo strutturato",
    description:
      "JSON con sezioni, documenti, slug, summary, tag, link al raw markdown e ai download canonici.",
  },
  {
    path: "/sitemap.xml",
    title: "Sitemap",
    description: "Sitemap XML standard.",
  },
  {
    path: "/robots.txt",
    title: "Politica per bot",
    description:
      "GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot e altri sono esplicitamente autorizzati.",
  },
];

export default function AiPage() {
  return (
    <div className="mx-auto max-w-canvas px-6 py-16">
      <header className="max-w-prose">
        <p className="text-sm uppercase tracking-wider text-[color:var(--gray-500)]">
          Per AI agents
        </p>
        <h1 className="mt-3 text-4xl sm:text-5xl font-bold tracking-tight">
          Questo sito è progettato per essere consumato da AI
        </h1>
        <p className="mt-5 text-lg text-[color:var(--gray-500)] leading-relaxed">
          Ogni pagina HTML ha un equivalente markdown raw, il catalogo è
          machine-readable, i bot AI sono autorizzati, e un server MCP è in
          roadmap.
        </p>
      </header>

      <section className="mt-12 max-w-prose">
        <h2 className="text-2xl font-bold mb-4">Convenzioni di accesso</h2>
        <ul className="space-y-4 text-[17px] leading-relaxed">
          <li>
            <strong>Raw markdown.</strong> Aggiungi <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">.md</code> a un URL pagina per ottenere il sorgente markdown.{" "}
            Es: <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">/ontologia/teoremi/3-soglia-critica</code> →{" "}
            <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">/ontologia/teoremi/3-soglia-critica.md</code>
          </li>
          <li>
            <strong>Download canonici.</strong> I documenti più estesi
            (trattato, file AILA originali) sono linkati come download canonici
            in <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">/downloads/...</code> — il path è esposto nel campo{" "}
            <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">download.file</code> del catalogo JSON.
          </li>
          <li>
            <strong>JSON-LD.</strong> Ogni pagina documento contiene
            structured data <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">TechArticle</code> con autore, data,
            licenza, link al raw markdown e al download.
          </li>
          <li>
            <strong>Cross-references.</strong> Il campo{" "}
            <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">related</code> nel JSON e nel frontmatter dei
            singoli documenti dichiara collegamenti semantici (es. una
            proposizione e la sua versione AILA).
          </li>
        </ul>
      </section>

      <section className="mt-12">
        <h2 className="text-2xl font-bold mb-4">Endpoint</h2>
        <div className="grid gap-3 sm:grid-cols-2">
          {endpoints.map((e) => (
            <a
              key={e.path}
              href={e.path}
              className="block border border-[color:var(--gray-200)] rounded-xl p-5 hover:border-accent hover:shadow-sm transition-all bg-paper"
            >
              <div className="font-mono text-sm text-accent mb-1">
                {SITE}
                {e.path}
              </div>
              <div className="font-semibold text-ink mb-1">{e.title}</div>
              <p className="text-sm text-[color:var(--gray-500)] leading-relaxed">
                {e.description}
              </p>
            </a>
          ))}
        </div>
      </section>

      <section className="mt-12 max-w-prose">
        <h2 className="text-2xl font-bold mb-4">Workflow tipico</h2>
        <ol className="list-decimal pl-5 space-y-2 text-[17px] leading-relaxed">
          <li>
            Fetch <Link href="/llms.txt" className="text-accent underline underline-offset-4">/llms.txt</Link> per la mappa.
          </li>
          <li>
            Fetch <Link href="/index.json" className="text-accent underline underline-offset-4">/index.json</Link> per il catalogo machine-readable.
          </li>
          <li>
            Fetch del raw markdown della pagina target (URL pagina + .md).
          </li>
          <li>
            Se serve la versione canonica integrale, fetch del download
            indicato nel campo <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">download.file</code>.
          </li>
        </ol>
      </section>

      <section className="mt-12 max-w-prose">
        <h2 className="text-2xl font-bold mb-4">MCP server <span className="text-sm font-normal text-[color:var(--gray-500)] uppercase tracking-wider ml-2">roadmap</span></h2>
        <p className="text-[17px] leading-relaxed text-[color:var(--gray-500)]">
          Un server <a href="https://modelcontextprotocol.io" className="text-accent underline underline-offset-4">Model Context Protocol</a> dedicato a nodo432 è in
          progettazione. Esporrà come tool MCP:
        </p>
        <ul className="mt-4 space-y-2 text-[17px] leading-relaxed">
          <li>
            <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">list_documents</code> — elenco completo o filtrato per tag/sezione/stato
          </li>
          <li>
            <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">read_document(slug)</code> — corpo markdown di un documento
          </li>
          <li>
            <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">get_section(slug)</code> — sotto-albero di una sezione con metadata
          </li>
          <li>
            <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">search(query)</code> — ricerca full-text
          </li>
        </ul>
        <p className="mt-4 text-[17px] leading-relaxed text-[color:var(--gray-500)]">
          Distribuzione prevista: pacchetto npm avviabile via{" "}
          <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">npx</code> per Claude Desktop / client MCP, oppure
          endpoint HTTP/SSE per integrazione web.
        </p>
      </section>

      <section className="mt-12 max-w-prose">
        <h2 className="text-2xl font-bold mb-4">Licenze</h2>
        <p className="text-[17px] leading-relaxed text-[color:var(--gray-500)]">
          Ogni documento dichiara la propria licenza nel frontmatter (campo{" "}
          <code className="font-mono text-[0.9em] bg-[color:var(--gray-50)] border border-[color:var(--gray-200)] rounded px-1.5 py-0.5">license</code>) e nel JSON-LD della pagina. La
          maggior parte dei contenuti è CC-BY-SA-4.0; in caso di omissione,
          assumere "tutti i diritti riservati" e verificare con gli autori.
        </p>
      </section>
    </div>
  );
}
