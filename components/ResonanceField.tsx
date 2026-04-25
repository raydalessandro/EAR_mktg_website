"use client";

import { useEffect, useRef } from "react";

const PHI = 1.618033988749;
const BASE_FREQUENCY = 432 / 1000;

function harmonic(x: number, y: number, t: number, n: number) {
  const frequency = BASE_FREQUENCY * n;
  const amplitude = 1 / n;
  const phase = t * frequency + (x * PHI + y) * Math.PI;
  return Math.sin(phase) * amplitude;
}

export function ResonanceField() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let time = 0;
    let mouseX = 0;
    let mouseY = 0;
    let scrollY = 0;
    let raf = 0;

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resize();

    const onMouse = (e: MouseEvent) => {
      mouseX = e.clientX / window.innerWidth;
      mouseY = e.clientY / window.innerHeight;
    };
    const onScroll = () => {
      const max = document.body.scrollHeight - window.innerHeight;
      scrollY = max > 0 ? window.scrollY / max : 0;
    };

    window.addEventListener("resize", resize);
    document.addEventListener("mousemove", onMouse);
    document.addEventListener("scroll", onScroll);

    const compose = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const resolution = 50;
      const cellSize = Math.max(canvas.width, canvas.height) / resolution;

      ctx.strokeStyle = "#d4af37";
      ctx.lineWidth = 0.5;

      for (let i = 0; i < resolution; i++) {
        for (let j = 0; j < resolution; j++) {
          const x = i / resolution;
          const y = j / resolution;

          let resonance = 0;
          resonance += harmonic(x, y, time, 1);
          resonance += harmonic(x, y, time, 2);
          resonance += harmonic(x, y, time, 3);
          resonance += harmonic(x, y, time, 5);
          resonance += harmonic(x, y, time, 8);

          const dx = x - mouseX;
          const dy = y - mouseY;
          const distance = Math.sqrt(dx * dx + dy * dy);
          const scrollInfluence = Math.sin(scrollY * Math.PI * 2);

          resonance *= (1 + distance) * (1 + scrollInfluence * 0.2);

          if (Math.abs(resonance) > 0.5) {
            const px = i * cellSize;
            const py = j * cellSize;
            const size = Math.abs(resonance) * cellSize * 0.3;
            const angle = resonance * Math.PI;

            ctx.beginPath();
            ctx.moveTo(px + Math.cos(angle) * size, py + Math.sin(angle) * size);
            for (let k = 0; k < 3; k++) {
              const a = angle + (k * Math.PI * 2) / 3;
              ctx.lineTo(
                px + Math.cos(a) * size * (1 - k * 0.2),
                py + Math.sin(a) * size * (1 - k * 0.2)
              );
            }
            ctx.stroke();
          }
        }
      }

      const breath = Math.sin((time * Math.PI) / 4);
      canvas.style.opacity = String(0.08 + breath * 0.02);

      time += 0.016;
      raf = requestAnimationFrame(compose);
    };

    raf = requestAnimationFrame(compose);

    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener("resize", resize);
      document.removeEventListener("mousemove", onMouse);
      document.removeEventListener("scroll", onScroll);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      aria-hidden="true"
      className="fixed inset-0 -z-10 pointer-events-none"
    />
  );
}
