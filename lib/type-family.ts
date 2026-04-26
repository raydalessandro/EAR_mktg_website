export type TypeFamily =
  | "philosophy"
  | "theory"
  | "aila"
  | "study"
  | "tool"
  | "neutral";

const TYPE_FAMILY: Record<string, TypeFamily> = {
  trattato: "philosophy",
  teorema: "theory",
  paper: "theory",
  "paper-appendix": "theory",
  "aila-spec": "aila",
  "aila-notation": "aila",
  "aila-operational": "aila",
  "aila-derivation": "aila",
  "aila-empirical": "aila",
  "aila-extension": "aila",
  "aila-nano": "aila",
  "aila-prose-companion": "aila",
  "aila-manifesto": "aila",
  "aila-release": "aila",
  study: "study",
  dataset: "study",
  visualization: "study",
  batch: "study",
  report: "study",
  methodology: "tool",
  pipeline: "tool",
  tool: "tool",
  template: "tool",
  skill: "tool",
  collection: "neutral",
};

export function getTypeFamily(type: string | null | undefined): TypeFamily {
  if (!type) return "neutral";
  return TYPE_FAMILY[type] ?? "neutral";
}

export function knownTypes(): string[] {
  return Object.keys(TYPE_FAMILY);
}
