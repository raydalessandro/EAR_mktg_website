import { execFileSync, spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { beforeAll, describe, expect, it } from "vitest";

const ROOT = path.resolve(__dirname, "..");
const GEN_SCRIPT = path.join(ROOT, "scripts", "generate-ai-assets.mjs");
const AUDIT_SCRIPT = path.join(ROOT, "scripts", "audit.mjs");

// The audit checks for sitemap.xml + robots.txt in TARGET. Sitemap is
// emitted by Next during `next build` (app/sitemap.ts), so it only
// exists under /out. We prefer auditing /out when present (the real
// post-build state); otherwise we fall back to /public, which only
// passes if a sitemap.xml has been pre-placed.
const OUT_DIR = path.join(ROOT, "out");
const PREFERRED_TARGET = fs.existsSync(path.join(OUT_DIR, "sitemap.xml"))
  ? "out"
  : "public";

beforeAll(() => {
  // Ensure freshly generated AI assets exist in /public (and copied into
  // /out by Next's static export, if /out exists from a prior build).
  execFileSync("node", [GEN_SCRIPT], { cwd: ROOT, stdio: "pipe" });
}, 60_000);

describe(`audit.mjs --target=${PREFERRED_TARGET}`, () => {
  it("exits 0 on the current generated state", () => {
    const result = spawnSync(
      "node",
      [AUDIT_SCRIPT, `--target=${PREFERRED_TARGET}`],
      { cwd: ROOT, encoding: "utf8" }
    );
    if (result.status !== 0) {
      // Surface output to make CI failures debuggable.
      console.error("audit stdout:\n" + result.stdout);
      console.error("audit stderr:\n" + result.stderr);
    }
    expect(result.status).toBe(0);
  }, 60_000);
});
