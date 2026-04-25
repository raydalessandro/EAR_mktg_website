---
title: "Divergenza dello scaling strutturale e metabolico nei tumori NSCLC"
summary: "Δ = |β̄ - θ| come firma di incoerenza gerarchica: SCC vs ADC su 52 pazienti, p < 0.0001, d = 2.15."
status: published
type: study
version: "1.0"
order: 10
icon: lab
tags: [empirico, biologia, oncologia, scaling, allometria, NSCLC, P6]
authors: [EAR Lab]
created: 2026-01-10
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/studi-empirici/biologia/scaling-tumori-nsclc/Studio_divergenza_scaling_tumori.zip
  format: zip
  size: "~1.3 MB"
related:
  - ontologia/aila/empirico/coherence
  - ontologia/teoremi/4-scaling-dimensionale
  - ontologia/teoremi/6-inseparabilita-attributi
featured: false
---

## Cos'è

Studio empirico di riferimento sulla **divergenza fra esponente di scaling strutturale (β̄, vasi)** ed **esponente metabolico (θ, SUVmax/MTV)** nei tumori non a piccole cellule del polmone (NSCLC). L'ipotesi: la patologia tumorale non è caratterizzata da uno spostamento di un singolo esponente, ma dalla **perdita di coerenza gerarchica** che normalmente coordina struttura (R) e processo (P). La divergenza Δ = |β̄ − θ| viene proposta come marcatore quantitativo di questa incoerenza.

## Materiale

| Risorsa | Formato | Cosa contiene |
|---|---|---|
| **Pacchetto completo** ([download](/downloads/ontologia/studi-empirici/biologia/scaling-tumori-nsclc/Studio_divergenza_scaling_tumori.zip)) | zip | Tutti gli artefatti elencati sotto |
| Manuscript principale | md | Testo completo del paper (~2.800 parole, 10 referenze) |
| Abstract standalone | md | Sintesi 247 parole con tabella risultati |
| Cover letter | md | Presentazione editoriale |
| Codice `analysis_divergence.py` | py | Pipeline principale di analisi |
| Codice `analisi_scaling_NSCLC.py` | py | Script preparatorio scaling NSCLC |
| Dati `tumor_vessel_scaling.xlsx` | xlsx | Dataset Brummer & Savage (2021), 52 pazienti |
| Materiali supplementari | md | Note metodologiche estese |
| Figure | png | Boxplot divergenza + scatter β̄ vs θ |
| LICENSE | — | MIT |

## Risultati principali

- **Coorte**: 52 pazienti NSCLC (38 ADC, 14 SCC) dal NSCLC Radiogenomics dataset.
- **Esponenti**: ADC β̄ = 0.914, θ = 0.337; SCC β̄ = 0.920, θ = 0.228. Entrambi i tipi mostrano scaling strutturale vicino all'isometrico (≈ 1.0) e scaling metabolico depresso rispetto a 0.75.
- **Divergenza**: Δ_ADC = 0.577, Δ_SCC = 0.692 (+19,9% in SCC).
- **Significatività**: Welch's t = 5.888, Mann–Whitney U = 511.0, entrambi p < 0.0001; **Cohen's d = 2.15** (effetto molto grande).
- **Conclusione operativa**: Δ discrimina i sottotipi tumorali meglio di ciascun esponente preso singolarmente.

## Connessione all'ontologia

Lo studio fornisce validazione empirica diretta del framework R/P/D (Relazione, Processo, Distinzione/gerarchia) e della sua articolazione in [AILA — Coherence](/ontologia/aila/empirico/coherence), dove la validazione NSCLC è esplicitamente richiamata. La perdita di coordinazione fra β̄ e θ è la traduzione clinica del [Teorema 6 — Inseparabilità degli attributi](/ontologia/teoremi/6-inseparabilita-attributi): quando D si degrada, R e P si scollano e gli scaling divergono. Il riferimento allo [scaling 3/4](/ontologia/teoremi/4-scaling-dimensionale) è teorico (WBE/Kleiber).

## Come usarlo

- **Lettura rapida**: apri `manuscript/abstract_standalone.md`.
- **Riproduzione**: `pip install -r code/requirements.txt`, poi `python code/analysis_divergence.py` con il dataset Excel allegato.
- **Pairing AI**: carica abstract + `analysis_divergence.py` come contesto e chiedi varianti su altri tipi tumorali o analisi longitudinali.

## Note

Working paper v1.0, gennaio 2026. Limiti dichiarati: campione 52 pazienti, assenza dati di stadiazione, singolo tipo tumorale (NSCLC), θ calcolato a livello di gruppo. Dati originari MIT (Brummer & Savage 2021); pacchetto distribuito CC-BY-SA-4.0.
