import { z } from "zod";

export const STATUSES = ["published", "draft", "wip", "coming-soon"] as const;
export type Status = (typeof STATUSES)[number];

export const downloadSchema = z.object({
  file: z.string(),
  format: z.string().default("md"),
  size: z.string().optional(),
});

export const frontmatterSchema = z
  .object({
    title: z.string().min(1, "title required"),
    summary: z.string().optional(),
    description: z.string().optional(),
    llm_directive: z.string().optional(),

    // Ontological grounding (scaffolding for AI reasoning, NOT for human display).
    // ontology_coords: Σ_DAXP codes from the Tesseract this document lives on.
    // theorems: which EAR theorems this document instantiates / proves / tests.
    //   Accepts forms like "P3", "T7", "C3.5" or longer "P3-Soglia".
    // primitive_path: short human-readable primitive flow, e.g. "Δ → ⇄ → ⟳".
    ontology_coords: z.array(z.string()).default([]),
    theorems: z.array(z.string()).default([]),
    primitive_path: z.string().optional(),

    status: z.enum(STATUSES).default("published"),
    type: z.string().optional(),
    version: z.string().optional(),
    order: z.number().int().optional(),
    icon: z.string().optional(),
    tags: z.array(z.string()).default([]),
    authors: z.array(z.string()).default([]),
    created: z.coerce.date().optional(),
    updated: z.coerce.date().optional(),
    download: downloadSchema.optional(),
    license: z.string().optional(),
    related: z.array(z.string()).default([]),
    featured: z.boolean().default(false),
  })
  .strict();

export type Frontmatter = z.infer<typeof frontmatterSchema>;
