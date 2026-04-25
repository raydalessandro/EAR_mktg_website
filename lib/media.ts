export type MediaKind = "audio" | "video" | "image";

export const AUDIO_FORMATS = new Set([
  "mp3",
  "wav",
  "ogg",
  "flac",
  "m4a",
  "aac",
]);

export const VIDEO_FORMATS = new Set(["mp4", "webm", "mov"]);

export const IMAGE_FORMATS = new Set([
  "png",
  "jpg",
  "jpeg",
  "webp",
  "gif",
  "svg",
]);

const MIME: Record<string, string> = {
  mp3: "audio/mpeg",
  wav: "audio/wav",
  ogg: "audio/ogg",
  flac: "audio/flac",
  m4a: "audio/mp4",
  aac: "audio/aac",
  mp4: "video/mp4",
  webm: "video/webm",
  mov: "video/quicktime",
  png: "image/png",
  jpg: "image/jpeg",
  jpeg: "image/jpeg",
  webp: "image/webp",
  gif: "image/gif",
  svg: "image/svg+xml",
};

export function normalizeFormat(fmt: string | undefined | null): string {
  return (fmt ?? "").trim().toLowerCase().replace(/^\./, "");
}

export function detectMediaKind(fmt: string | undefined | null): MediaKind | null {
  const f = normalizeFormat(fmt);
  if (!f) return null;
  if (AUDIO_FORMATS.has(f)) return "audio";
  if (VIDEO_FORMATS.has(f)) return "video";
  if (IMAGE_FORMATS.has(f)) return "image";
  return null;
}

export function mimeFor(fmt: string | undefined | null): string | null {
  const f = normalizeFormat(fmt);
  if (!f) return null;
  return MIME[f] ?? null;
}

export function mimeForOrFallback(fmt: string | undefined | null): string {
  const explicit = mimeFor(fmt);
  if (explicit) return explicit;
  const kind = detectMediaKind(fmt);
  if (!kind) return "application/octet-stream";
  return `${kind}/${normalizeFormat(fmt)}`;
}
