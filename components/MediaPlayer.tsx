import { detectMediaKind, mimeForOrFallback } from "@/lib/media";

type Download = {
  file?: string;
  format?: string;
};

type Props = {
  download: Download;
  title?: string;
};

export function MediaPlayer({ download, title }: Props) {
  const file = download.file;
  if (!file) return null;
  const kind = detectMediaKind(download.format);
  if (!kind) return null;
  const mime = mimeForOrFallback(download.format);

  if (kind === "audio") {
    return (
      <div className="my-6 p-4 rounded-xl border border-[color:var(--gray-200)] bg-[color:var(--gray-50)]">
        <audio
          controls
          preload="metadata"
          className="w-full"
          aria-label={title ? `Player audio: ${title}` : "Player audio"}
        >
          <source src={file} type={mime} />
          Il tuo browser non supporta l&apos;audio HTML5.{" "}
          <a href={file} download className="text-accent underline">
            Scarica il file
          </a>
          .
        </audio>
      </div>
    );
  }

  if (kind === "video") {
    return (
      <div className="my-6 rounded-xl border border-[color:var(--gray-200)] overflow-hidden bg-black">
        <video
          controls
          preload="metadata"
          className="w-full block"
          aria-label={title ? `Player video: ${title}` : "Player video"}
        >
          <source src={file} type={mime} />
          Il tuo browser non supporta il video HTML5.{" "}
          <a href={file} download className="text-accent underline">
            Scarica il file
          </a>
          .
        </video>
      </div>
    );
  }

  // image
  return (
    <figure className="my-6">
      <img
        src={file}
        alt={title ?? ""}
        className="w-full rounded-xl border border-[color:var(--gray-200)]"
        loading="lazy"
      />
    </figure>
  );
}
