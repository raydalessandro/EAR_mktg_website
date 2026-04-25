---
title: Musica
summary: Canzoni, sound design, composizioni. Player in-page, download canonico.
type: collection
status: wip
order: 20
icon: music
tags: [arte, musica, audio]
license: CC-BY-SA-4.0
---

Sezione in costruzione. Ospiterà brani audio — canzoni, sound design,
composizioni — con **player audio nativo** in pagina e file canonico
scaricabile.

## Come funziona

Quando una scheda ha un `download.format` audio (`mp3`, `wav`, `ogg`,
`flac`, `m4a`), la pagina del documento mostra automaticamente un
**player HTML5** in cima al corpo. Niente librerie extra, niente
JavaScript custom: è il `<audio controls>` nativo del browser. Funziona
ovunque (mobile incluso) e l'AI legge comunque la scheda + il link al
canonico.

## Convenzione di scheda

```yaml
---
title: "Titolo del brano"
type: canzone
status: published
authors: [Artista]
created: 2026-XX-XX
license: All rights reserved   # o CC-BY-SA-4.0 se decidi di rilasciare
tags: [musica, <genere>]
download:
  file: /downloads/arte/musica/titolo.mp3
  format: mp3
  size: "5.4 MB"
duration: "3:42"               # opzionale (campo libero, mostrato se presente)
---

## Note di composizione

Il testo, contesto, riferimenti del brano.

## Testo

(Lyrics se applicabile)
```

## Sui pesi

Una canzone in MP3 a 192 kbps pesa ~1.4 MB/min → un album da 10 brani
(~40 min) è ~55 MB. Sotto soglia repo (100 MB) per ora. Quando la
collezione cresce migriamo i file canonici su Cloudflare R2 / GitHub
Releases (vedi README, sezione Migrazione storage) — basta cambiare
`download.file` da `/downloads/...` a `https://cdn.../...`.

## Licenze

Ogni brano dichiara la propria licenza. Default suggerito per opere
nuove: `CC-BY-SA-4.0`. Per opere riservate: `All rights reserved`.
