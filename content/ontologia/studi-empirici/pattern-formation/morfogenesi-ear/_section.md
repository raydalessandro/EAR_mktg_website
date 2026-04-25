---
title: "Morfogenesi EAR — Scoperte strutturali e validazione empirica"
summary: Tre scoperte derivate (432 = D²·A³, Δ = π/A², ε = A/D) testate via simulazione Turing con kernel ontologico.
type: study
status: published
order: 10
icon: lab
tags: [empirico, morfogenesi, turing, validazione, P2, P3, P4, P6]
authors: [nodo432]
created: 2026-01-08
updated: 2026-01-11
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/SCOPERTE_STRUTTURALI_8_GENNAIO_2026.md
  format: md
  size: "~30 KB"
related:
  - ontologia/teoremi/2-conservazione-informazionale
  - ontologia/teoremi/3-soglia-critica
  - ontologia/teoremi/4-scaling-dimensionale
  - ontologia/teoremi/6-inseparabilita-attributi
  - ontologia/aila/derivazioni/scaling
  - ontologia/aila/empirico/coherence
featured: true
---

## Cosa è

Studio integrato che combina **derivazione formale** e **validazione
empirica** del framework EAR. Tre scoperte strutturali — emerse dal
confronto fra le 4 proposizioni testate e il trattato — vengono
verificate quantitativamente mediante simulazione di morfogenesi
(Gray-Scott) con un kernel derivato ontologicamente da `A = 3` e
`D = 4`.

## Le tre scoperte

| # | Scoperta | Forma compatta |
|---|---|---|
| 1 | Fattorizzazione duale di 432 | `432 = D² × A³ = 4² × 3³` |
| 2 | Perdita strutturale derivata | `Δ = π/A² ≈ 0.35%` |
| 3 | Scaling universale | `ε = A/D = 3/4` |

Tutte le costanti del framework — incluse `Σ ≈ 137,5` e l'esponente
`3/4` (Kleiber) — derivano esclusivamente da `A` (attributi) e `D`
(dimensioni). Nessun parametro libero.

## Validazione

Le proposizioni testate empiricamente mediante simulazione Turing:

- **[P2 — Conservazione](/ontologia/teoremi/2-conservazione-informazionale)**: somma del kernel = 1 invariante
- **[P3 — Soglia critica](/ontologia/teoremi/3-soglia-critica)**: transizione discreta osservata a `field_strength ≈ 0.05`
- **[P4 — Scaling](/ontologia/teoremi/4-scaling-dimensionale)**: bilanciamento invariante tra scale
- **[P6 — Inseparabilità](/ontologia/teoremi/6-inseparabilita-attributi)**: correlazione tra Δ, ⇄, ⟳ con `r > 0.5`

### Soglia critica

![Soglia critica: numero di centri (⬡) e contrasto (Δ) in funzione del field strength, con transizione discreta attorno a 0.05](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/soglia_critica.png)

I due tracciati mostrano un **salto netto** intorno a
`field_strength ≈ 0.05`: la dinamica passa da un regime omogeneo a
uno strutturato senza valori intermedi. Conferma quantitativa di P3.

### Confronto pattern

![Tre pattern affiancati: Turing classico, EAR moderato, EAR forte. Il terzo supera la soglia critica e produce una struttura asimmetrica complessa](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/confronto_pattern.png)

Il pattern EAR forte (terzo riquadro) supera la soglia e mostra
**rottura di simmetria** rispetto al kernel Turing classico (primo).
Le strutture emergenti sono asimmetriche e complesse — caratteristica
predetta da Corollario 3.3.

## Materiale

| Risorsa | Formato | Cosa contiene |
|---|---|---|
| **Scoperte strutturali** ([download](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/SCOPERTE_STRUTTURALI_8_GENNAIO_2026.md)) | md | Writeup formale: tre scoperte, derivazioni, verifiche numeriche |
| Esperimento Python (modulare) ([download](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/ear_morphogenetic_experiment.py)) | py | Simulazione Gray-Scott con 4 esperimenti |
| Esperimento Python (completo) ([download](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/EAR_Experiment_Complete.py)) | py | Versione estesa: aggiunge il test di rottura simmetria (Cor. 3.3) |
| Notebook Jupyter ([download](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/EAR_Morphogenetic_Experiment.ipynb)) | ipynb | Versione interattiva con output e interpretazioni inline |
| Figura: soglia critica ([download](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/soglia_critica.png)) | png | Grafico transizione (vedi sopra) |
| Figura: confronto pattern ([download](/downloads/ontologia/studi-empirici/pattern-formation/morfogenesi-ear/confronto_pattern.png)) | png | Confronto visivo Turing vs EAR (vedi sopra) |

## Connessione al trattato

Le tre scoperte sono proposte come estensione del trattato:

- **Cap. XX bis** — scaling come rapporto strutturale (richiama [P4](/ontologia/teoremi/4-scaling-dimensionale))
- **Sez. 22.5** — perdita strutturale derivata (richiama [P2](/ontologia/teoremi/2-conservazione-informazionale) + [P6](/ontologia/teoremi/6-inseparabilita-attributi))

## Come usarlo

- **Lettura rapida**: scarica il writeup markdown
- **Riproduzione**: clona uno dei due `.py` o apri il `.ipynb` (Python con numpy/scipy/matplotlib)
- **Pairing AI**: carica writeup + uno dei due `.py` come contesto, chiedi al modello di proporre varianti dei parametri o nuove proposizioni testabili

## Note

Studio del **8-11 gennaio 2026**. Singolo esperimento integrato — non
frammentato per artefatto. Aggiornamenti futuri saranno aggiunti
come pagine separate in questa cartella.
