import "server-only";

import fs from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { remark } from "remark";
import remarkGfm from "remark-gfm";
import remarkHtml from "remark-html";
import { frontmatterSchema, type Frontmatter } from "./schema";

const CONTENT_ROOT = path.join(process.cwd(), "content");
const SECTION_FILE = "_section.md";

export type DocumentNode = {
  kind: "document";
  slug: string[];
  href: string;
  filePath: string;
  meta: Frontmatter;
  parentSlug: string[];
};

export type SectionNode = {
  kind: "section";
  slug: string[];
  href: string;
  dirPath: string;
  meta: Frontmatter;
  children: SectionNode[];
  documents: DocumentNode[];
  parentSlug: string[] | null;
};

export type ContentNode = SectionNode | DocumentNode;

function readMarkdown(filePath: string) {
  const raw = fs.readFileSync(filePath, "utf8");
  const parsed = matter(raw);
  const result = frontmatterSchema.safeParse(parsed.data);
  if (!result.success) {
    const issues = result.error.issues
      .map((i) => `  - ${i.path.join(".")}: ${i.message}`)
      .join("\n");
    throw new Error(
      `Invalid frontmatter in ${path.relative(process.cwd(), filePath)}:\n${issues}`
    );
  }
  return { meta: result.data, body: parsed.content };
}

function buildHref(slug: string[]) {
  return "/" + slug.join("/");
}

function defaultSectionMeta(name: string): Frontmatter {
  return frontmatterSchema.parse({
    title: name,
    status: "wip",
  });
}

function walk(dir: string, slug: string[], parentSlug: string[] | null): SectionNode {
  const sectionFile = path.join(dir, SECTION_FILE);
  const sectionMeta = fs.existsSync(sectionFile)
    ? readMarkdown(sectionFile).meta
    : defaultSectionMeta(slug[slug.length - 1] ?? "root");

  const node: SectionNode = {
    kind: "section",
    slug,
    href: buildHref(slug),
    dirPath: dir,
    meta: sectionMeta,
    children: [],
    documents: [],
    parentSlug,
  };

  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    if (entry.name.startsWith(".") || entry.name.startsWith("_")) continue;
    const entryPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      node.children.push(walk(entryPath, [...slug, entry.name], slug));
      continue;
    }

    if (entry.isFile() && entry.name.endsWith(".md")) {
      const docSlug = [...slug, entry.name.replace(/\.md$/, "")];
      const { meta } = readMarkdown(entryPath);
      const doc: DocumentNode = {
        kind: "document",
        slug: docSlug,
        href: buildHref(docSlug),
        filePath: entryPath,
        meta,
        parentSlug: slug,
      };
      node.documents.push(doc);
    }
  }

  const orderFn = (a: { meta: Frontmatter }, b: { meta: Frontmatter }) => {
    const ao = a.meta.order ?? 999;
    const bo = b.meta.order ?? 999;
    if (ao !== bo) return ao - bo;
    return a.meta.title.localeCompare(b.meta.title);
  };
  node.children.sort(orderFn);
  node.documents.sort(orderFn);

  return node;
}

let cachedTree: SectionNode | null = null;

export function getContentTree(): SectionNode {
  if (cachedTree) return cachedTree;
  if (!fs.existsSync(CONTENT_ROOT)) {
    cachedTree = {
      kind: "section",
      slug: [],
      href: "/",
      dirPath: CONTENT_ROOT,
      meta: defaultSectionMeta("root"),
      children: [],
      documents: [],
      parentSlug: null,
    };
    return cachedTree;
  }
  cachedTree = walk(CONTENT_ROOT, [], null);
  return cachedTree;
}

export function findNode(slug: string[]): ContentNode | null {
  const root = getContentTree();
  if (slug.length === 0) return root;

  let current: SectionNode = root;
  for (let i = 0; i < slug.length; i++) {
    const part = slug[i];
    const isLast = i === slug.length - 1;

    const child = current.children.find((c) => c.slug[c.slug.length - 1] === part);
    if (child) {
      if (isLast) return child;
      current = child;
      continue;
    }

    if (isLast) {
      const doc = current.documents.find(
        (d) => d.slug[d.slug.length - 1] === part
      );
      if (doc) return doc;
    }
    return null;
  }
  return current;
}

export function listAllSlugs(): string[][] {
  const out: string[][] = [];
  const visit = (node: SectionNode) => {
    if (node.slug.length > 0) out.push(node.slug);
    for (const child of node.children) visit(child);
    for (const doc of node.documents) out.push(doc.slug);
  };
  visit(getContentTree());
  return out;
}

export function flattenDocuments(node: SectionNode = getContentTree()): DocumentNode[] {
  const docs: DocumentNode[] = [...node.documents];
  for (const child of node.children) {
    docs.push(...flattenDocuments(child));
  }
  return docs;
}

export function countDocumentsDeep(node: SectionNode): number {
  let n = node.documents.length;
  for (const c of node.children) n += countDocumentsDeep(c);
  return n;
}

export type DownloadEntry = {
  title: string;
  href: string;
  download: NonNullable<Frontmatter["download"]>;
  fromKind: "section" | "document";
};

export function collectDownloads(node: SectionNode): DownloadEntry[] {
  const out: DownloadEntry[] = [];
  if (node.meta.download) {
    out.push({
      title: node.meta.title,
      href: node.href,
      download: node.meta.download,
      fromKind: "section",
    });
  }
  for (const child of node.children) {
    out.push(...collectDownloads(child));
  }
  for (const doc of node.documents) {
    if (doc.meta.download) {
      out.push({
        title: doc.meta.title,
        href: doc.href,
        download: doc.meta.download,
        fromKind: "document",
      });
    }
  }
  return out;
}

export function topLevelSections(): SectionNode[] {
  return getContentTree().children;
}

export function readDocumentBody(doc: DocumentNode): string {
  const { body } = readMarkdown(doc.filePath);
  return body;
}

export async function renderMarkdown(md: string): Promise<string> {
  const file = await remark().use(remarkGfm).use(remarkHtml).process(md);
  return String(file);
}

export function breadcrumbs(slug: string[]): { href: string; label: string }[] {
  const crumbs: { href: string; label: string }[] = [{ href: "/", label: "Home" }];
  const acc: string[] = [];
  for (const part of slug) {
    acc.push(part);
    const node = findNode([...acc]);
    crumbs.push({
      href: "/" + acc.join("/"),
      label: node?.meta.title ?? part,
    });
  }
  return crumbs;
}
