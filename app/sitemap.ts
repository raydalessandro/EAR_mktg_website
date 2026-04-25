import type { MetadataRoute } from "next";
import { listAllSlugs } from "@/lib/content";

const BASE_URL = "https://nodo432.com";

export default function sitemap(): MetadataRoute.Sitemap {
  const now = new Date();
  const entries: MetadataRoute.Sitemap = [
    { url: `${BASE_URL}/`, lastModified: now, changeFrequency: "weekly", priority: 1 },
  ];
  for (const slug of listAllSlugs()) {
    entries.push({
      url: `${BASE_URL}/${slug.join("/")}`,
      lastModified: now,
      changeFrequency: "monthly",
      priority: 0.7,
    });
  }
  return entries;
}
