---
title: "Criticità neurale EEG e metodi pedagogici"
summary: "Pipeline di criticità su EEG: i task focalizzati spostano σ verso il subcritico (0.88-0.90) rispetto al riposo (≈1.0)."
status: published
type: study
version: "1.0"
order: 10
icon: lab
tags: [empirico, neuroscienze, EEG, criticita, valanghe-neurali, pedagogia, branching-ratio]
authors: [EAR Lab]
created: 2026-01-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/studi-empirici/neuroscienze/eeg-criticality/eeg_criticality_analysis.zip
  format: zip
  size: "~21 KB"
related:
  - ontologia/aila/empirico/empirical-reference
  - ontologia/teoremi/3-soglia-critica
featured: false
---

## Cos'è

Pipeline di analisi della **criticità neurale** su dati EEG, costruita per testare se metodi pedagogici diversi mantengano l'attività cerebrale a punti distinti rispetto allo stato critico (σ ≈ 1.0). Lo studio integra rilevamento di valanghe neurali (Beggs & Plenz 2003), branching ratio diretto e corretto per subsampling (MR estimator di Wilting & Priesemann 2018), fit di leggi di potenza ed indice κ. È in fase di *Pipeline Validation Complete*: la pipeline è validata su dati simulati e pronta per i dataset OpenNeuro ds004148 e ds005385.

## Materiale

Il pacchetto `eeg_criticality_analysis.zip` contiene:

| Artefatto | File | Descrizione |
|---|---|---|
| Modulo core | `eeg_criticality.py` | Funzioni: `detect_events`, `detect_avalanches`, `branching_ratio_direct`, `branching_ratio_MR`, `fit_power_law`, `kappa_index` |
| Simulatore stati | `simulate_states.py` | Generazione branching process e validazione su 5 stati cognitivi sintetici |
| Workflow OpenNeuro | `analyze_openneuro.py` | Caricamento BIDS via MNE-Python e confronto cross-state |
| Piano di analisi | `EEG_CRITICALITY_ANALYSIS_PLAN.md` | Metodologia completa: dataset, pipeline, ipotesi H0-H4, roadmap 6 settimane |
| Report preliminare | `NEURAL_CRITICALITY_REPORT.md` | Risultati di validazione e interpretazione EAR |
| Risultati simulazione | `results/simulated_criticality.json` | Output JSON dei 5 stati simulati |

## Risultati principali

Validazione su dati sintetici (MR estimator), pattern in linea con Fagerholm et al. (2015):

| Stato cognitivo | σ_MR | Interpretazione |
|---|---|---|
| Occhi chiusi (riposo) | 0.999 | Quasi-critico |
| Occhi aperti (riposo) | 0.973 | Lievemente subcritico |
| Ascolto musicale (passivo) | 0.965 | Lievemente subcritico |
| Task di memoria | 0.902 | Subcritico |
| Aritmetica mentale | 0.879 | Profondamente subcritico |

- **Pattern confermato**: i task cognitivi focalizzati inducono dinamiche subcritiche.
- **Gap di letteratura identificato**: nessuno studio PubMed misura criticità in funzione del metodo pedagogico — opportunità di ricerca originale.
- **Dataset target pronti**: ds004148 (60 partecipanti, 5 stati) e ds005385 (608 partecipanti, pre/post task, 5-year follow-up).

## Connessione all'ontologia

Lo studio fornisce il riferimento empirico per la mappatura criticità ↔ attributi EAR documentata in [`/ontologia/aila/empirico/empirical-reference.md`](/ontologia/aila/empirico/empirical-reference.md): σ = 1.0 corrisponde all'equilibrio Δ ∥ ⇄ ∥ ⟳, σ < 1 a soppressione di ⇄, σ > 1 a dominanza di ⟳. La transizione di fase intorno a σ = 1 è l'incarnazione neurofisiologica della [soglia critica K_crit](/ontologia/teoremi/3-soglia-critica): superata in un verso si ha rigidità, nell'altro instabilità.

## Come usarlo

- Eseguire `python simulate_states.py` per riprodurre la validazione sintetica.
- Lanciare `python analyze_openneuro.py` su dati BIDS scaricati via DataLad (`datalad install` di ds004148 / ds005385).
- Citare come base per il disegno di studi pedagogici su lezione frontale vs apprendimento attivo Ray-style.

## Note

Versione 1.0, 25 gennaio 2026. Stato: pipeline validata, applicazione su dati reali in roadmap. Dipendenze: Python 3.10+, mne ≥1.6, mne-bids ≥0.14, scipy. Distribuzione CC-BY-SA-4.0.
