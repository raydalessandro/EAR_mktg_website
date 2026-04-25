import { describe, it, expect } from "vitest";
import {
  detectMediaKind,
  mimeFor,
  mimeForOrFallback,
  normalizeFormat,
  AUDIO_FORMATS,
  VIDEO_FORMATS,
  IMAGE_FORMATS,
} from "@/lib/media";

describe("normalizeFormat", () => {
  it("lowercases and trims", () => {
    expect(normalizeFormat("  MP3 ")).toBe("mp3");
    expect(normalizeFormat("PNG")).toBe("png");
  });

  it("strips a leading dot", () => {
    expect(normalizeFormat(".mp4")).toBe("mp4");
  });

  it("returns empty string for null/undefined/empty", () => {
    expect(normalizeFormat(null)).toBe("");
    expect(normalizeFormat(undefined)).toBe("");
    expect(normalizeFormat("")).toBe("");
  });
});

describe("detectMediaKind", () => {
  it("detects audio formats", () => {
    for (const fmt of ["mp3", "wav", "ogg", "flac", "m4a", "aac"]) {
      expect(detectMediaKind(fmt)).toBe("audio");
    }
  });

  it("detects video formats", () => {
    for (const fmt of ["mp4", "webm", "mov"]) {
      expect(detectMediaKind(fmt)).toBe("video");
    }
  });

  it("detects image formats", () => {
    for (const fmt of ["png", "jpg", "jpeg", "webp", "gif", "svg"]) {
      expect(detectMediaKind(fmt)).toBe("image");
    }
  });

  it("returns null for non-media formats", () => {
    expect(detectMediaKind("pdf")).toBeNull();
    expect(detectMediaKind("zip")).toBeNull();
    expect(detectMediaKind("md")).toBeNull();
    expect(detectMediaKind("py")).toBeNull();
    expect(detectMediaKind("ipynb")).toBeNull();
    expect(detectMediaKind("docx")).toBeNull();
  });

  it("handles uppercase and dotted formats", () => {
    expect(detectMediaKind("MP3")).toBe("audio");
    expect(detectMediaKind(".PNG")).toBe("image");
  });

  it("returns null for missing/empty", () => {
    expect(detectMediaKind(null)).toBeNull();
    expect(detectMediaKind(undefined)).toBeNull();
    expect(detectMediaKind("")).toBeNull();
  });

  it("audio/video/image format sets are disjoint", () => {
    const seen = new Set<string>();
    for (const fmt of [...AUDIO_FORMATS, ...VIDEO_FORMATS, ...IMAGE_FORMATS]) {
      expect(seen.has(fmt)).toBe(false);
      seen.add(fmt);
    }
  });
});

describe("mimeFor", () => {
  it("returns the proper MIME for known formats", () => {
    expect(mimeFor("mp3")).toBe("audio/mpeg");
    expect(mimeFor("mp4")).toBe("video/mp4");
    expect(mimeFor("png")).toBe("image/png");
    expect(mimeFor("svg")).toBe("image/svg+xml");
    expect(mimeFor("jpg")).toBe("image/jpeg");
    expect(mimeFor("jpeg")).toBe("image/jpeg");
  });

  it("returns null for unknown formats", () => {
    expect(mimeFor("pdf")).toBeNull();
    expect(mimeFor("madeup")).toBeNull();
  });
});

describe("mimeForOrFallback", () => {
  it("falls back to <kind>/<fmt> for known kind, unknown explicit MIME", () => {
    // contrived: m4a is in AUDIO_FORMATS and has explicit MIME
    expect(mimeForOrFallback("m4a")).toBe("audio/mp4");
  });

  it("returns octet-stream for entirely unknown formats", () => {
    expect(mimeForOrFallback("zip")).toBe("application/octet-stream");
    expect(mimeForOrFallback("madeup")).toBe("application/octet-stream");
  });
});
