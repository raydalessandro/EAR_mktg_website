// Stub for the `server-only` package used by lib/content.ts.
// The real package throws if imported in a client bundle; in our
// vitest (node env) we just want it to be a no-op.
export {};
