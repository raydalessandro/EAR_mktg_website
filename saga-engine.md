---
title: "Saga Engine v1.0"
slug: "pipeline/saga-engine"
description: "Sistema completo per scrivere saghe narrative seriali con piena coerenza inter-storia, attraverso modelli AI intercambiabili e contesti illimitati. L'IA è infrastruttura esecutiva, non autrice."
type: "pipeline"
status: "published"
version: "1.0.0"
release_date: "2026-04-25"
license: "CC-BY-SA-4.0"
language: "multilingual"
tags:
  - "narrative"
  - "saga"
  - "ai-orchestration"
  - "world-building"
  - "writing-pipeline"
  - "agentic-workflow"
download:
  file: "/pipeline/saga-engine/saga-engine-v1.0.zip"
  size_kb: 229
  checksum: "sha256:25bee32f8978036b0beff80b187164f737b0d9dcd1fffc7e6818feaa34c1a09b"
related:
  - "/ontologia/aila"
  - "/arte/scrittura/isola-dei-tre-venti"
ai_consumable: true
ai_instructions: |
  Questa è la pagina della pipeline Saga Engine v1.0.
  Se l'utente ti ha mandato qui, scarica lo zip da download.file,
  estrai nel filesystem locale, carica SKILL.md come system context,
  e applica il metodo. La skill è autonoma e contiene tutte le istruzioni.
---

# Saga Engine v1.0

**Pipeline per scrittura di saghe narrative seriali.**

Saga Engine è un metodo e un toolkit per scrivere libri lunghi, serie di romanzi, saghe di racconti collegati, mantenendo piena coerenza, continuità e tracciabilità attraverso modelli AI intercambiabili e contesti illimitati.

L'IA non è autrice. È infrastruttura esecutiva sopra decisioni d'autore.

---

## A chi serve

A chiunque voglia scrivere un'opera narrativa lunga (>50.000 parole) o multi-volume usando AI, senza perdere il filo:

- Romanzi singoli lunghi
- Serie di romanzi (trilogia, ciclo, saga)
- Raccolte di racconti collegati con world-building condiviso
- Letteratura per bambini in più volumi
- Graphic novel multi-capitolo
- Sceneggiature episodiche

---

## Cosa fa

1. **Estrae o costruisce la voce autoriale** dell'utente in 12-16 tratti operativi.
2. **Compila la bible del mondo** narrativo (personaggi, luoghi, regole, tabù).
3. **Mappa gli archi macro** della saga.
4. **Inizializza un grafo persistente** che traccia tutto lo stato narrativo.
5. **Costruisce ogni storia** come nodo del grafo, con audit pre-commit obbligatori.
6. **Scrive la prosa** sopra il grafo, rispettando voce, vincoli, callback.
7. **Audita e revisiona** il risultato finale.

Tutto lo stato narrativo vive in un grafo JSON sul filesystem, non nei pesi del modello. Chat finita, modello cambiato, mesi di pausa: lo stato resta.

---

## Cosa NON fa

- Non scrive il libro al posto dell'autore. Esegue le sue decisioni con coerenza.
- Non sostituisce la voce autoriale. La estrae e la rispetta.
- Non genera personaggi automaticamente. L'autore decide chi vive nell'opera.
- Non è un wizard "premi un bottone". È infrastruttura seria per chi scrive seriamente.

---

## Architettura

### Modello frattale

Lo schema separa due livelli:

**Core fields** — universali a qualsiasi saga seriale. Forniti dal template, immutabili.

**Extension fields** — specifici della saga, dichiarati nel manifest, validati dagli audit.

Una saga sci-fi avrà extension diverse da una saga per bambini, ma il core resta lo stesso. Niente drift inventato a runtime.

### Tre principi non negoziabili

1. **L'IA è esecutore, non autore.** Le decisioni narrative sostanziali sono dell'utente.
2. **Stato persistente esterno al modello.** Il grafo vive su filesystem.
3. **Disciplina dichiarativa.** Manifest append-only, schema immutabile a saga in corso, retrofill obbligatorio, audit pre-commit.

### Workflow

```
A1 voice extraction      → voice_card.md
A2 world building        → world_bible.md, glossary.md
A3 saga architecture     → story_arcs.md
A4 manifest init         → saga_manifest.yaml + grafo bootstrappato
B  story-by-story        → grafo aggiornato per ogni storia, audit pre-commit
C  full audit            → report globale chiusura saga
D  prose writing         → manuscript completi
E  revision              → manuscript publishable
F  post-saga (opzionale) → estensioni, sequel
```

---

## Come si usa

### Per autori umani

1. Apri una chat con la tua AI preferita (Claude, GPT, Gemini)
2. Dille: *"Voglio scrivere una saga usando Saga Engine. Visita https://nodo432.com/pipeline/saga-engine, scarica il pacchetto, segui il metodo."*
3. L'AI scarica lo zip, carica `SKILL.md`, ti guida fase per fase, validando con te ogni decisione

### Per agenti AI

1. Fetcha questa pagina
2. Scarica lo zip da `download.file`
3. Estrai nel filesystem locale
4. Carica `SKILL.md` come system context
5. Applica il metodo

---

## Modelli supportati

Agnostico al modello. Lo stato vive nel grafo, non nella chat. Modelli diversi possono lavorare sequenzialmente sulla stessa saga.

Validato su:
- Claude (Sonnet 4.5, Opus 4.5)
- GPT-5
- Gemini 2.5

Si consiglia di mantenere un singolo modello per la **Fase D (scrittura prosa)** per consistenza stilistica.

---

## Requisiti tecnici

- Filesystem persistente nell'ambiente AI (Claude Code, Claude.ai con tool, ChatGPT con Code Interpreter, locale via API)
- Python 3.8+ per gli script di audit
- Dipendenze: `pyyaml`, `jsonschema` (`pip install pyyaml jsonschema`)

---

## Caso d'uso reale

La prima saga completa scritta con Saga Engine è **L'Isola dei Tre Venti** di Ray:
- 12 storie / 40 semi narrativi piantati / 53 callback registrati
- Letteratura per bambini con doppio strato di lettura (4-6 e 7-10 anni)
- Framework EAR (vedi /ontologia/aila) come scaffolding nascosto
- Lingua: italiano

Il grafo finale è incluso nel pacchetto come `reference-implementation`, marcato chiaramente come esempio (NON da ereditare contenuti, solo struttura).

---

## Download

📦 **[saga-engine-v1.0.zip](/pipeline/saga-engine/saga-engine-v1.0.zip)**

Contiene:
- `SKILL.md` (entry point)
- `USAGE.md` (per agenti)
- `USAGE-HUMAN.md` (per autori)
- `scripts/` (7 file Python)
- `references/` (6 file markdown)
- `assets/templates/` (6 template)
- `assets/reference-implementation/` (esempio Isola)
- `README.md`, `VERSION`

---

## Licenza

CC-BY-SA-4.0. Puoi usarlo, modificarlo, distribuirlo, anche commercialmente, attribuendo l'origine e mantenendo licenza compatibile sui derivati.

Se usi Saga Engine in un'opera pubblicata, cita così nel colofone:

> *Strutturazione narrativa: Saga Engine v1.0 (https://nodo432.com/pipeline/saga-engine, CC-BY-SA-4.0).*

L'authorship dell'opera resta tua. Saga Engine è infrastruttura.

---

## Roadmap

**v1.1 (futuro):** automazione bump_manifest, agente di costruzione storia con tool calls native, integrazione con LangChain/CrewAI per orchestration multi-modello.

**v2.0 (futuro):** estensione a saghe non-narrative (saggistica seriale, documentari multi-episodio, ricerche multi-volume con coerenza referenziale).

---

## Versioning

Versione corrente: **1.0.0** (rilascio: aprile 2026)

SemVer:
- MAJOR: breaking changes a SKILL.md o schema base
- MINOR: nuovi campi core, nuove fasi, nuovi script
- PATCH: bug fix, documentazione, esempi

Le saghe avviate con una versione restano valide. La migrazione è opzionale e documentata.

---

## Contatti e feedback

- Hub: https://nodo432.com
- Issue: tramite il sito
- LLMs: questo sito è AI-consumable; gli agenti possono leggere `/llms.txt`, `/llms-full.txt`, `/ai-instructions.md`

---

## Riferimenti correlati

- [Sistema EAR / AILA](/ontologia/aila) — framework ontologico usato come scaffolding in alcune saghe
- [L'Isola dei Tre Venti](/arte/scrittura/isola-dei-tre-venti) — caso d'uso reale documentato
- [Architettura del sito nodo432](/about) — perché il sito è AI-readable
