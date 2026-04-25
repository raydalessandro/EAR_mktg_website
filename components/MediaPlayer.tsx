type Download = {
  file?: string;
  format?: string;
};

type Props = {
  download: Download;
  title?: string;
};

const AUDIO_FORMATS = new Set(["mp3", "wav", "ogg", "flac", "m4a", "aac"]);
const VIDEO_FORMATS = new Set(["mp4", "webm", "mov"]);
const IMAGE_FORMATS = new Set(["png", "jpg", "jpeg", "webp", "gif", "svg"]);

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
};

export function MediaPlayer({ download, title }: Props) {
  const fmt = (download.format ?? "").toLowerCase();
  const file = download.file;
  if (!file || !fmt) return null;

  if (AUDIO_FORMATS.has(fmt)) {
    return (
      <div className="my-6 p-4 rounded-xl border border-[color:var(--gray-200)] bg-[color:var(--gray-50)]">
        <audio
          controls
          preload="metadata"
          className="w-full"
          aria-label={title ? `Player audio: ${title}` : "Player audio"}
        >
          <source src={file} type={MIME[fmt] ?? `audio/${fmt}`} />
          Il tuo browser non supporta l&apos;audio HTML5.{" "}
          <a href={file} download className="text-accent underline">
            Scarica il file
          </a>
          .
        </audio>
      </div>
    );
  }

  if (VIDEO_FORMATS.has(fmt)) {
    return (
      <div className="my-6 rounded-xl border border-[color:var(--gray-200)] overflow-hidden bg-black">
        <video
          controls
          preload="metadata"
          className="w-full block"
          aria-label={title ? `Player video: ${title}` : "Player video"}
        >
          <source src={file} type={MIME[fmt] ?? `video/${fmt}`} />
          Il tuo browser non supporta il video HTML5.{" "}
          <a href={file} download className="text-accent underline">
            Scarica il file
          </a>
          .
        </video>
      </div>
    );
  }

  if (IMAGE_FORMATS.has(fmt)) {
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

  return null;
}
