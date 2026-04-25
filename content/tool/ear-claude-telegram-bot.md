---
title: "Claude Code via Telegram"
summary: "Bot Telegram per controllare Claude Code da telefono. Testo, voce, foto, documenti, multi-sessione, streaming."
status: published
type: tool
version: "1.0"
order: 10
icon: bot
tags: [tool, telegram, bot, claude-code, mobile, voice, multi-session, bun, typescript]
authors: [nodo432]
created: 2026-03-26
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/tool/ear-claude-telegram-bot/EAR_CLAUDE_TELEGRAM_BOT.zip
  format: zip
  size: "104 KB"
related:
  - tool
featured: true
---

## Cos'è

**Bot Telegram self-hosted** che ti permette di controllare Claude Code
dal tuo telefono come se fossi davanti al terminale. Mandi testo, vocali,
foto, documenti — ricevi risposte in **streaming** con stato dei tool in
tempo reale. È pensato per quando sei in giro e ti viene un'idea, vuoi
modificare un repo, leggere un file, fare un commit, senza aprire il
laptop.

Stack: **Bun + TypeScript**, ~150 KB di codice sorgente, **624 test** in
TDD. Self-hosted perché il bot parla direttamente col tuo Claude Code
locale — niente intermediari, le tue chiavi e i tuoi file restano tuoi.

## Cosa puoi fare

- **Testo** — chat normale con Claude Code, streaming dei tool, status
  in diretta (`Read… Edit… Bash…`)
- **Voice** — mandi un vocale, viene trascritto **in locale via Whisper**
  e poi inoltrato a Claude. Niente cloud per il tuo audio.
- **Foto e documenti** — invia un PDF, un'immagine, un file di testo
  per analisi
- **Multi-sessione** — fino a 20 sessioni salvate, riprendibili in
  qualsiasi momento, rinominabili con `/title`
- **17 comandi** — switch modello (opus/sonnet/haiku), git status, dir
  listing, thinking mode, ecc.
- **Smart splitting** — i messaggi Telegram lunghi vengono riassemblati
  in input; le risposte lunghe vengono spezzate in modo sicuro
- **Security** — user allowlist, rate limiting, path validation, command
  safety checks

## Comandi principali

| Comando | Cosa fa |
|---|---|
| `/new` | Nuova sessione |
| `/resume` | Lista e riprendi sessioni salvate |
| `/title Bot v2` | Rinomina sessione corrente |
| `/model sonnet` | Cambia modello (opus / sonnet / haiku) |
| `/dir C:\projects` | Cambia working directory |
| `/files` | Lista file della directory corrente |
| `/git` | Git status (anche `/git log`, `/git diff`) |
| `/think` | Toggle thinking mode (off → normal → deep) |
| `/stop` | Ferma la query in corso |
| `/status` | Stato bot e consumo token |

Tip: prefisso `!` per **interrompere e sostituire** la query in corso —
es. `!nuova domanda qui`.

## Setup rapido

```bash
# 1. Installa Bun
curl -fsSL https://bun.sh/install | bash    # macOS/Linux
# (Windows: powershell -c "irm bun.sh/install.ps1 | iex")

# 2. Crea il bot Telegram
#   - messaggia @BotFather → /newbot → ottieni il token
#   - messaggia @userinfobot → ottieni il tuo user ID

# 3. Estrai lo zip + installa dipendenze
cd EAR_CLAUDE_TELEGRAM_BOT
bun install

# 4. Configura
cp .env.example .env
# Modifica .env:
#   TELEGRAM_BOT_TOKEN=...
#   TELEGRAM_ALLOWED_USERS=il-tuo-user-id
#   CLAUDE_WORKING_DIR=path/dei/tuoi/progetti
#   ALLOWED_PATHS=path1,path2

# 5. Avvia
bun run start
```

Il bot legge automaticamente `CLAUDE.md` dalla `CLAUDE_WORKING_DIR`
all'avvio sessione.

### Voice (opzionale)

Per i vocali serve **Whisper locale**:

```bash
pip install openai-whisper
```

Aggiungi in `.env`:

```
PYTHON_PATH=path/to/python
```

## Architettura

```
src/
├── index.ts              # entry point
├── config.ts             # config + env validation
├── session.ts            # multi-session manager (20 slot)
├── multi-chat.ts         # routing per chat
├── security.ts           # allowlist, rate limit, path checks
├── formatting.ts         # markdown ↔ Telegram MarkdownV2
├── media-pipeline.ts     # foto/doc handling
├── chat-state.ts         # stato per chat
├── transcribe_voice.py   # wrapper Whisper
└── handlers/
    ├── text.ts, voice.ts, photo.ts, document.ts
    ├── commands.ts (17 cmd), callback.ts, streaming.ts
    ├── media-group.ts, text-buffer.ts
```

## Perché è utile

Concretamente: **Claude Code in tasca**. Mentre cammini ti viene un
fix, lo dici a voce, il bot trascrive e Claude lo applica. Mentre sei
sul treno controlli `git status` di tre repo, leggi un PDF allegato
in un thread, riprendi la sessione di ieri.

Per orchestrazione AI nodo432: è il primo **tool concreto** della
sezione, esempio del pattern "interfaccia mobile su agente codice".
Le versioni successive potranno integrare gli endpoint di nodo432
(`/index.json`, `/llms-full.txt`, MCP server) per ragionamento sui
contenuti del sito direttamente da chat.

## Note

- Self-hosted, una sola persona alla volta (allowlist)
- I file `.env` non sono nello zip — c'è `.env.example` da copiare
- Test suite (624 test) inclusa nel sorgente, eseguibile con `bun test`
- Licenza CC-BY-SA-4.0 — fork e adattamenti incoraggiati
