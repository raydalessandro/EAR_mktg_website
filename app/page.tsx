import { topLevelSections, flattenDocuments } from "@/lib/content";
import { HomeView } from "@/components/HomeView";

export default function HomePage() {
  const sections = topLevelSections();
  const allDocs = flattenDocuments().filter(
    (d) => d.meta.status === "published"
  );

  const recent = [...allDocs]
    .sort((a, b) => {
      const ad = (a.meta.updated ?? a.meta.created ?? new Date(0)).getTime();
      const bd = (b.meta.updated ?? b.meta.created ?? new Date(0)).getTime();
      return bd - ad;
    })
    .slice(0, 8)
    .map((d) => ({
      slug: d.slug.join("/"),
      href: d.href,
      title: d.meta.title,
      summary: d.meta.summary ?? null,
      parentSlug: d.parentSlug,
      tags: d.meta.tags,
      type: d.meta.type ?? null,
    }));

  const featured = allDocs
    .filter((d) => d.meta.featured)
    .slice(0, 6)
    .map((d) => ({
      slug: d.slug.join("/"),
      href: d.href,
      title: d.meta.title,
      summary: d.meta.summary ?? null,
      parentSlug: d.parentSlug,
      tags: d.meta.tags,
      type: d.meta.type ?? null,
    }));

  const sectionsLite = sections.map((s) => ({
    slug: s.slug.join("/"),
    href: s.href,
    title: s.meta.title,
    summary: s.meta.summary ?? null,
    status: s.meta.status,
    docCount: countDocsInSection(s),
  }));

  return (
    <HomeView sections={sectionsLite} featured={featured} recent={recent} />
  );
}

function countDocsInSection(node: import("@/lib/content").SectionNode): number {
  let n = node.documents.length;
  for (const c of node.children) n += countDocsInSection(c);
  return n;
}
