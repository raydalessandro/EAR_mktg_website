import type { Metadata, Viewport } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Nav } from "@/components/Nav";
import { Footer } from "@/components/Footer";
import { ResonanceField } from "@/components/ResonanceField";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  metadataBase: new URL("https://nodo432.com"),
  title: {
    default: "nodo432 — Hub di orchestrazione AI",
    template: "%s · nodo432",
  },
  description:
    "Antologia, risorse, tool e pipeline per orchestrare l'AI. Documenti scaricabili, plugin Claude Code, script e metodologie.",
  openGraph: {
    type: "website",
    locale: "it_IT",
    url: "https://nodo432.com",
    siteName: "nodo432",
  },
  robots: { index: true, follow: true },
};

export const viewport: Viewport = {
  themeColor: "#fafafa",
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="it" className={inter.variable}>
      <body className="font-sans bg-paper text-ink min-h-screen flex flex-col">
        <ResonanceField />
        <Nav />
        <main className="flex-1 pt-16">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
