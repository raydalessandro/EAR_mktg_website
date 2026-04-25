---
title: "Verifica scaling 3/4 in letteratura"
summary: "L'esponente 3/4 = A/D non è universale: la variabilità osservata (Glazier, Hu, van Valkengoed) conferma EAR."
status: published
type: study
version: "1.0"
order: 20
icon: lab
tags: [empirico, trasversale, scaling, allometria, P4]
authors: [EAR Lab]
created: 2026-01-10
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/studi-empirici/trasversale/verifica-scaling-34/VERIFICA_SCALING_34_LETTERATURA.md
  format: md
  size: "~8 KB"
related:
  - ontologia/teoremi/4-scaling-dimensionale
  - ontologia/aila/derivazioni/scaling
  - ontologia/aila/in-prosa/derivazione-scaling-prosa
  - ontologia/studi-empirici/pattern-formation/morfogenesi-ear
featured: false
---

## Cos'è

Prima verifica sistematica (10 gennaio 2026) della derivazione EAR
dell'esponente di scaling allometrico:

```
ε = A / D = 3 / 4

A = 3 attributi fondamentali (Distinzione, Relazione, Processo)
D = 4 dimensioni necessarie all'auto-osservazione
```

Il documento confronta la predizione con la letteratura recente su
allometria metabolica, mostrando che la variabilità osservata
**non contraddice** EAR ma anzi è una sua predizione diretta:
sistemi incompleti deviano da 3/4 in modo strutturalmente
prevedibile.

## Materiale

File unico `VERIFICA_SCALING_34_LETTERATURA.md` (~8 KB): documento
markdown con tabelle, formalizzazione dell'operatore di scaling
`D = x^μ ∂_μ + Δ`, e bibliografia con DOI cliccabili.

## Contenuto

Le evidenze principali raccolte:

| Stato del sistema | Attributi | ε predetto | Osservato |
|---|---|---|---|
| Completo (adulto sano) | 3/3 | 0.75 | 0.75 ± 0.01 |
| In sviluppo (neonato) | < 3 | > 1 (costruzione) | 1.5 – 3.5 (Hu 2022) |
| Transizione (1–5 anni) | 2–3 | variabile | 0.7 – 1.0 |
| Isometrico (alcuni taxa) | 2/3 | 0.5 | ~0.5 – 0.67 |

Le quattro fonti chiave:

- **van Valkengoed et al. (2024)** — review che documenta l'assenza
  di supporto scientifico per un esponente universale e la crisi del
  framework WBE
- **Glazier (2005, 2022)** — i quattro tipi di scaling metabolico
  intraspecifico (b<1, b=1, transizione, fase superlineare→sublineare)
- **Hu (2022)** — modello bifasico nascita→età adulta con punto di
  transizione a ~10 kg

Il Tipo IV di Glazier (shift da b > 1 a b < 1 durante lo sviluppo)
corrisponde esattamente alla predizione EAR di un sistema che
**costruisce** struttura prima di raggiungere completezza.

## Connessione all'ontologia

Verifica empirica diretta della
[**Prop. 4 — Scaling dimensionale**](/ontologia/teoremi/4-scaling-dimensionale):

- per il fondamento formale, vedi
  [derivazione AILA dello scaling](/ontologia/aila/derivazioni/scaling)
- per la versione narrativa, vedi
  [derivazione in prosa](/ontologia/aila/in-prosa/derivazione-scaling-prosa)
- per la verifica via simulazione Turing, vedi
  [Morfogenesi EAR](/ontologia/studi-empirici/pattern-formation/morfogenesi-ear)

Il documento collega inoltre l'esponente 3/4 alla resistenza
strutturale Σ = 432/π ≈ 137.5 e suggerisce che α ≈ 1/137 e ε = 3/4
siano manifestazioni della stessa struttura ontologica A × D.

## Come usarlo

- **Lettura**: scarica il `.md` — testo breve, con tabelle e DOI
- **Punto di partenza** per nuovi test: i tre scenari proposti
  (sistemi patologici, organismi semplici, transizioni di fase)
- **Pairing AI**: carica il documento come contesto, chiedi al
  modello di mappare nuovi dataset di allometria sui quattro
  tipi di Glazier

## Note

Il documento è qualificato come "prima verifica sistematica" e
proposto come Capitolo XX.5 (oppure Appendice C — verifiche
empiriche) del trattato. WBE cerca una legge universale e fallisce
sulla variabilità; EAR predice la variabilità come funzione della
completezza del sistema.
