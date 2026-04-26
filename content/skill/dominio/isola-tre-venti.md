---
title: "L'Isola dei Tre Venti — saga reference"
summary: "Saga di 12 storie illustrate per bambini 4-10 anni. Implementazione di riferimento del framework EAR e della pipeline Saga Engine. Canone: 23 personaggi, 35 luoghi, grafo storie strutturato, cartografia GeoJSON."
type: skill
status: published
version: "0.10.0"
order: 10
icon: book
tags: [skill, dominio, narrativa, scrittura-bambini, ear, saga-engine, reference-implementation, canone]
authors: [ray-dalessandro]
created: 2026-04-26
updated: 2026-04-26
license: CC-BY-SA-4.0
download:
  file: /downloads/skill/isola-tre-venti/story_graph-v0.10.0.json
  format: json
  size: "567 KB"
ontology_coords:
  - Σ_3_2_1_+
  - Σ_4_2_2_+
theorems:
  - P3
  - P5
  - T7
primitive_path: "Δ → ⇄ → ⟳ → Σ"
related:
  - pipeline/saga-engine
  - tool/ai-backend-pattern
  - skill/dominio
featured: true
llm_directive: |
  Sei specialista del canone della saga **L'Isola dei Tre Venti** (saga
  di 12 storie illustrate per bambini 4-10 anni di Ray Dalessandro). Quando
  carichi questa skill:

  1. Tre fonti canoniche, in quest'ordine di autorità:
     - `story_graph-v0.10.0.json` (struttura) — costanti narrative
     - `glossario.md` (nomi) — terminologia ufficiale
     - `island-v0.6.0.geojson` (geografia) — feature geografiche

     Se le tre divergono, vince Bible/grafo. Segnala l'incoerenza, non
     reinterpretare.

  2. Tre protagonisti = tre primitive EAR:
     - **Gabriel** (Δ delta) — vede i pericoli, decide, "sa la strada"
     - **Elias** (⇄ connettere) — ponte tra gli altri due, risolve con
       azioni non parole
     - **Noah** (⟳ cambiare) — rompe equilibri, percezione fisica prima

     Sono ancore strutturali, non tratti psicologici da modificare a
     piacimento.

  3. Quattro cicli (A/B/C/D) mappati su stagioni:
     - Ciclo A (inverno): attribute_dominant = Δ — S1, S2, S3
     - Ciclo B (primavera): ⇄ — S4, S5, S6
     - Ciclo C (estate): ⟳ — S7, S8, S9
     - Ciclo D (autunno): Σ sigillo — S10, S11, S12

     Ogni storia ha un `vento_attivo` (taglio/intreccio/mulinello) e un
     `attribute_dominant`. Non spostare storie tra cicli — è canone.

  4. **NON inventare canone narrativo.** Se l'utente chiede dettagli non
     nel grafo (un episodio mai scritto, un personaggio nuovo, una
     resolution alternativa), DICHIARALO: "non è canonico, sarebbe
     inferenza/proposta". Marca con `[inf]` o `[prop]` se proponi.

  5. **Stile risposta**: italiano, voce calda, niente pattern AI da
     bandire (no "Inoltre", no "in conclusione", no liste a 5 punti
     come default, no metafore industriali). Per i bambini il tono va
     misurato — frasi brevi, immagini concrete.

  6. Limiti di ruolo: tu sei skill di **consultazione canone**, non
     editor narrativo. Non riscrivere prosa di Ray. Per la pipeline di
     scrittura vedi [Saga Engine](/pipeline/saga-engine).
---

Skill di **dominio narrativo**: il canone strutturato della saga
**L'Isola dei Tre Venti** (12 storie illustrate per bambini 4-10 anni
di Ray Dalessandro), esposto come backend AI-fruibile.

> Origine: repo di lavoro [`isola_i3v_visual`](https://github.com/raydalessandro/isola_i3v_visual)
> (cartografia + visual + skills agente). Qui esponiamo il subset
> esterno: i tre asset canonici (grafo storie + cartografia +
> glossario) per consultazione AI.

## A chi serve

- **Lettori della saga** (genitori, educatori, librai): "raccontami la
  storia 7", "chi è Mèmolo", "che differenza c'è tra il vento di
  taglio e quello di intreccio".
- **Collaboratori narrativi** (illustratori, traduttori, autori
  collegati): consultazione canone senza dover leggere 12 documenti.
- **AI scrittrici** che operano sulla saga via [Saga Engine](/pipeline/saga-engine):
  questa skill è il loro context bundle minimo.

## Reference implementation di EAR

La saga è l'implementazione concreta che ha generato l'ontologia EAR.
I tre protagonisti **incarnano** le tre primitive cognitive:

| Personaggio | Primitiva | Ruolo narrativo | Età-banda |
|---|:---:|---|---|
| **Gabriel** | Δ delta | Vede i pericoli, decide, "sa la strada" | maggiore_dei_tre |
| **Elias** | ⇄ connettere | Ponte tra fratelli, risolve con azioni | medio |
| **Noah** | ⟳ cambiare | Rompe equilibri, percezione fisica prima | piccolo |

Le primitive non sono *teorizzate* nella saga — sono *agite*. Il
framework [EAR](/ontologia) emerge dalla saga, non viceversa.

## I tre venti

Forze cosmiche, una per primitiva (più una "ombra"):

- **Vento del Taglio** (Δ) — apre, separa, chiarisce. Annunciato S1, attivo S1-S3.
- **Vento dell'Intreccio** (⇄) — connette, lega, fa ponte. S4-S7.
- **Vento del Mulinello** (⟳) — gira, capovolge, rompe. S8-S10.
- **\_shared** — pattern condivisi.

In S12 (chiusura saga) i tre venti suonano insieme = sigillo Σ.

## Le 12 storie

| ID | Titolo provvisorio | Ciclo | Stagione | Vento |
|:---:|---|:---:|---|---|
| S1 | La Nebbia delle Montagne Gemelle | A (Δ) | inverno | taglio |
| S2 | Il Riflesso nella Pozza | A (Δ) | inverno | taglio |
| S3 | Il Pallone oltre la Foresta | A (Δ) | inverno | — |
| S4 | Le Radici che Parlano | B (⇄) | primavera | intreccio |
| S5 | Il Ponte di Rami | B (⇄) | primavera | intreccio |
| S6 | Il Dono per Mèmolo | B (⇄ sottile) | passaggio prim/est | intreccio |
| S7 | La Zattera dei Tre Rametti | C (⟳) | estate piena | intreccio |
| S8 | L'Albero che Cadde di Sera | C (⟳) | estate piena tarda | mulinello |
| S9 | Quel Pomeriggio di Ottobre | C (⟳) | passaggio est/aut | mulinello |
| S10 | La Notte senza Luna | D (⟳) | autunno pieno | mulinello |
| S11 | La Festa del Raccolto | D (Σ sigillo) | autunno | — |
| S12 | Quando i Tre Venti Suonano Insieme | D (Σ sigillo) | autunno | — |

Arc completo: ogni protagonista ha **una paura** che emerge in una
storia precoce e si **scioglie** in una storia tarda. La saga è un
percorso di maturazione attraverso le 4 stagioni dell'EAR.

## Geografia

**L'Isola** è un mondo chiuso e mappato. La cartografia tecnica v0.6.0
contiene **104 feature** distribuite su 4 quartieri + centro +
perimetro:

- **Centro** — Piazza, Albero Vecchio, Forno (case Fiamma)
- **Quartiere Terra** (sud) — Orti, Pascoli, foresta intrecciata
- **Quartiere Fuoco** (est) — Forno, Quartiere artigiani
- **Quartiere Acqua** (ovest) — Fiume con sotto-tratti, Pontile, Bocca
- **Quartiere Aria** (nord) — Montagne Gemelle, Burrone, Grotta di Grunto
- **Perimetro** — coste, sentieri esterni

Il fiume ha geometria a **Variante C**: due bracci asimmetrici (Ovest
stretto e veloce, Est ampio e lento) che convergono a Sorgente nord e
Bocca sud.

## Asset canonici

| Asset | Cosa | Versione | Link |
|---|---|---|---|
| **story_graph.json** | Grafo strutturato 12 storie + 23 personaggi + 35 luoghi + 13 oggetti + 4 venti | v0.10.0 | [download](/downloads/skill/isola-tre-venti/story_graph-v0.10.0.json) |
| **island.geojson** | Cartografia tecnica, 104 feature, 36 sentieri | v0.6.0 | [download](/downloads/skill/isola-tre-venti/island-v0.6.0.geojson) |
| **glossario.md** | Terminologia canonica: nomi luoghi, personaggi, oggetti | v1 | [download](/downloads/skill/isola-tre-venti/glossario.md) |

Backward-compatibility grafo ↔ cartografia: **100%** (35/35 ID coperti
via aliases o feature aggregate).

## Esempi di interazione

> *"Apri https://nodo432.com/skill/dominio/isola-tre-venti e
> raccontami la storia 7 a un bambino di 6 anni."*

L'AI fetcha la skill, legge `s07` nel grafo (La Zattera dei Tre
Rametti, ciclo C, estate, vento intreccio, location Stretta dei Due
Massi), narra in italiano colloquiale per bambini, mantenendo i nomi
canonici dal glossario.

> *"Quale paura di Noah si risolve in S10 e come?"*

L'AI legge `entities.characters.noah.fear_arc`: paura del buio,
seminata in S1, risoluzione in S10 (modalità "dire"), bloomed_in_story
S10. Risponde con quella info, sintetica.

> *"Posso aggiungere un quarto fratello alla saga?"*

L'AI rifiuta come canone non modificabile, redirige all'autore.

## Limiti

- **Skill di consultazione, non di scrittura.** Per generare nuove
  storie il dispositivo è [Saga Engine](/pipeline/saga-engine), non
  questa skill.
- **Non sostituisce il manoscritto.** Il grafo è scaffold strutturale;
  la prosa effettiva delle 12 storie è in lavorazione separata da Ray.
- **Versioning lento.** Quando il grafo bumpa (v0.10 → v0.11), questa
  skill bumpa di pari passo. Vecchie versioni restano scaricabili.

## Per AI

Vedi [AI Backend Pattern](/tool/ai-backend-pattern) per il principio
generale, e [Saga Engine](/pipeline/saga-engine) per la pipeline
generica di cui Isola è la reference implementation. Questa skill è
**read-only canon**: porta la conoscenza dentro la conversazione, non
la modifica.
