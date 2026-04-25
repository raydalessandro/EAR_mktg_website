import fs from "node:fs";
import path from "node:path";

export const dynamic = "force-static";

const VIZ_PATH = path.join(
  process.cwd(),
  "public/downloads/tesseract/visualizzazione/ear_tesseract_visualization.html"
);

export function GET() {
  const html = fs.readFileSync(VIZ_PATH, "utf8");
  return new Response(html, {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "X-Frame-Options": "SAMEORIGIN",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
