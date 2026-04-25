---
title: "P8 — Selezione strutturale: un calcolo formale per esiti quantistici osservatore-dipendenti"
summary: "Σ(O) come variabile nascosta nell'osservatore: 4 programmi sperimentali convergono su P8 (Wigner, eraser, contestualità, Darwinism)."
status: published
type: study
version: "1.0"
order: 20
icon: lab
tags: [empirico, fisica, quantistica, fondamenti, P8, Bell, contestualita]
authors: [EAR Lab]
created: 2026-01-15
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/studi-empirici/fisica/p8-structural-selection/EAR_QUANTUM_P8_Paper.docx
  format: docx
  size: "~22 KB"
related:
  - ontologia/aila/estensioni/quantum
  - ontologia/teoremi/3-soglia-critica
  - ontologia/teoremi/6-inseparabilita-attributi
featured: false
---

## Cos'è

Working paper che propone **Proposizione 8 (P8) — Selezione Strutturale**: la struttura dell'osservatore, formalizzata come coordinate ontologiche Σ(O), è correlata in modo non-arbitrario con gli esiti delle misure quantistiche. P8 è derivata dagli assiomi A1, A3, T2, P6 di EAR e fornisce ciò che Copenhagen, QBism, RQM e Many-Worlds non offrono: **una formula esplicita Σ(O) → Σ(esito)**, con 72 configurazioni distinte di osservatore (Σ_ijkp, |Ω| = 4·3·3·2). Il paper sostiene che Bell non esclude P8, perché Bell assume separabilità osservatore/sistema, assunto che EAR rifiuta.

## Materiale

| Risorsa | Formato | Cosa contiene |
|---|---|---|
| **Paper principale** ([download](/downloads/ontologia/studi-empirici/fisica/p8-structural-selection/EAR_QUANTUM_P8_Paper.docx)) | docx | 9 sezioni: framework formale, P8, supporto empirico, confronto interpretazioni, predizioni novel |
| **Sezione 10 supplementare** ([download](/downloads/ontologia/studi-empirici/fisica/p8-structural-selection/EAR_QUANTUM_P8_Section10.docx)) | docx | "Anomalies, Failed Predictions, and Discriminating Tests" — companion section con anomalie di Quantum Darwinism, IIT (XOR, fotodiodo, cervelletto), Bell senza entanglement, eraser |

## Risultati principali

- **Formalismo**: matrice ontologica Σ_ijkp con 4 dimensioni × 3 attributi × 3 assi × 2 poli = **72 tipi strutturali di osservatore**.
- **Convergenza empirica su P8** (Sez. 4):
  - Wigner's Friend (Proietti 2019): violazione 5σ — `Σ diversi → realtà diverse`.
  - Quantum eraser (Kim 2000): visibilità V passa 0 → 0.94 al variare del rivelatore.
  - Contestualità Kochen-Specker (Cabello 2022): violazione 2.291 ± 0.008 > 1.
  - Quantum Darwinism (Zhu 2025): la dimensione dell'ambiente seleziona pointer states.
- **Predizione testabile chiave**: `var(esiti) ∝ 1/K(O)` — discriminante diretto rispetto a Copenhagen (Sez. 6 + 10.5).
- **Esperimento Alice–Bob** proposto: stesso EPR, rivelatori a φ alta/bassa → EAR predice `var(Bob) > var(Alice)`, le altre interpretazioni no.
- **Risoluzioni in Sez. 10**: la circolarità di Kastner sull'einselection, il paradosso XOR di Aaronson, il paradosso del fotodiodo (Brette) e l'anomalia del cervelletto vengono ricondotti a P6 (squilibrio degli attributi Δ/⇄/⟳ → K incompleto).

## Connessione all'ontologia

Il paper è il documento di estensione quantistica del kernel: collegare a [AILA — Estensioni / Quantum](/ontologia/aila/estensioni/quantum) per la specifica formale ufficiale. P8 si appoggia su [Teorema 6 — Inseparabilità](/ontologia/teoremi/6-inseparabilita-attributi) (l'osservatore ha struttura Δ ∧ ⇄ ∧ ⟳) e su [Teorema 3 — Soglia critica](/ontologia/teoremi/3-soglia-critica) (transizione discontinua al K_crit fra dinamica quantistica e classica). Mappa esplicita di Quantum Darwinism, Contestualità e IIT come casi particolari di P8 in Sez. 7.

## Come usarlo

- **Lettura rapida**: abstract + Sez. 3 (enunciato P8) + Sez. 6 (predizioni).
- **Discussione critica**: leggere insieme Paper + Sezione 10 — la 10 contiene gli esperimenti discriminanti e la rassegna delle anomalie non risolte dagli altri framework.
- **Pairing AI**: carica i due docx come contesto per progettare un protocollo dell'esperimento Alice–Bob o per estendere la matrice Σ ad altri sistemi (NV centers, trapped ions).

## Note

Working Paper v1.0, gennaio 2026, EAR Lab. La Sezione 10 è distribuita come documento separato perché funge da appendice critica/discriminante del paper principale. Licenza CC-BY-SA-4.0; le citazioni sperimentali rinviano a DOI primari.
