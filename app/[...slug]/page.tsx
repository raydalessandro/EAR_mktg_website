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

export function generateMetadata({ params }: { params: Params }): Metadata {
  const node = findNode(params.slug);
  if (!node) return {};
  return {
    title: node.meta.title,
    description: node.meta.summary ?? node.meta.description,
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
