import { notFound } from "next/navigation";
import type { Metadata } from "next";
import {
  findNode,
  listAllSlugs,
  readDocumentBody,
  renderMarkdown,
} from "@/lib/content";
import { SectionView } from "@/components/SectionView";
import { DocumentView } from "@/components/DocumentView";

type Params = { slug: string[] };

export function generateStaticParams(): Params[] {
  return listAllSlugs().map((slug) => ({ slug }));
}

const SITE_URL = "https://nodo432.com";

export function generateMetadata({ params }: { params: Params }): Metadata {
  const node = findNode(params.slug);
  if (!node) return {};
  const url = `${SITE_URL}${node.href}`;
  const description =
    node.meta.summary ??
    node.meta.description ??
    `${node.meta.title} su nodo432`;
  const keywords = [
    ...(node.meta.tags ?? []),
    node.meta.type,
    "nodo432",
    "EAR",
    "ontologia",
  ].filter(Boolean) as string[];
  return {
    title: node.meta.title,
    description,
    keywords,
    alternates: { canonical: url },
    openGraph: {
      title: node.meta.title,
      description,
      url,
      type: "article",
      siteName: "nodo432",
      locale: "it_IT",
    },
    twitter: {
      card: "summary",
      title: node.meta.title,
      description,
    },
  };
}

export default async function CatchAllPage({ params }: { params: Params }) {
  const node = findNode(params.slug);
  if (!node) notFound();

  if (node.kind === "section") {
    return <SectionView node={node} />;
  }

  const body = readDocumentBody(node);
  const html = await renderMarkdown(body);
  return <DocumentView doc={node} html={html} />;
}
