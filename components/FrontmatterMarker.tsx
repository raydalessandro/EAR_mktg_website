import type { Frontmatter } from "@/lib/schema";
import { serializeFrontmatter } from "@/lib/frontmatter-yaml";

export { serializeFrontmatter };

type Props = {
  meta: Frontmatter;
  slug: string;
  kind: "section" | "document";
};

export function FrontmatterMarker({ meta, slug, kind }: Props) {
  const enriched = { ...meta, slug, kind };
  const yaml = serializeFrontmatter(enriched as unknown as Record<string, unknown>);
  return (
    <script
      type="application/yaml"
      data-purpose="frontmatter"
      data-kind={kind}
      data-slug={slug}
      dangerouslySetInnerHTML={{ __html: yaml }}
    />
  );
}
