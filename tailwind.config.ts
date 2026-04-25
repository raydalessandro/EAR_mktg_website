import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx,md,mdx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#0a0a0a",
        paper: "#fafafa",
        accent: "#d4af37",
        "gray-50": "#f9f9f9",
        "gray-200": "#e5e5e5",
        "gray-500": "#737373",
        "gray-900": "#171717",
      },
      fontFamily: {
        sans: [
          "Inter",
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "sans-serif",
        ],
        mono: ["ui-monospace", "SFMono-Regular", "Menlo", "monospace"],
      },
      maxWidth: {
        prose: "72ch",
        canvas: "1200px",
      },
      animation: {
        "spiral-breathe": "spiral-breathe 4s ease-in-out infinite",
      },
      keyframes: {
        "spiral-breathe": {
          "0%, 100%": { transform: "rotate(0deg) scale(1)" },
          "50%": { transform: "rotate(5deg) scale(1.05)" },
        },
      },
    },
  },
  plugins: [],
};

export default config;
