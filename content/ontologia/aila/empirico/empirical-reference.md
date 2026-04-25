---
title: "Empirical Reference"
summary: "Indice vivente delle validazioni empiriche EAR — oncologia, neuro, semantica, sintesi cross-dominio."
status: published
order: 95
tags: [aila, empirico, validazioni]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/EAR_EMPIRICAL_REFERENCE_AILA_v1.0.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/empirico/coherence
  - ontologia/aila/derivazioni/scaling
featured: false
---

## Cos'è

`EAR_EMPIRICAL_REFERENCE_AILA_v1.0` è un **living document** che indicizza
in formato AILA tutte le validazioni empiriche del framework EAR: studi,
dataset, metriche, risultati, statistiche, mapping a propositions e stato
epistemico. Non sostituisce gli studi originali — è un puntatore rapido
con risultati canonici già normalizzati.

## Posizione nel sistema

Funziona come **strato di evidenza** parallelo al corpus teorico AILA.
Raccoglie cinque famiglie di validazioni: oncologia (NSCLC ADC vs SCC,
`Δ = |β̄ - θ|`, `p < 0.0001`, `Cohen's d = 2.15`), neuroscienze in quattro
step (criticità SOC `τ = 1.52`, struttura informazionale vs spaziale 16:1,
omeostasi E/I via STDP, predizione INS-maturità), validazione semantica
(vettori ontologici Δ⇄⟳ su Tarot vs LLM, `r = 0.533`), sintesi cross-dominio
(metrica CHE = ↻/∞), e una tabella riassuntiva per proposition (P1–P8 + T7).

## Perché è utile con AI

Caricato come contesto, **ancora ogni claim del sistema a un riferimento
verificabile**: l'AI può citare statistiche esatte, distinguere risultati
"distintivi" (P5, P6) da quelli solo "coerenti con la letteratura" (P3, P4),
identificare gap aperti (P1, P2, P7, P8 non ancora testati direttamente)
ed evitare di rivendicare validazioni inesistenti. Riduce drasticamente il
rischio di overclaiming e abilita una conversazione calibrata sulle evidenze.

## Come usarlo

- Carica insieme a [Coherence](/ontologia/aila/empirico/coherence) per lo specchio
  teorico
- Usalo come **prima consultazione** prima di assertire validazione: cerca
  proposition o dominio nella tabella di sintesi
- Esempio: "P5 è validato? ⇒ sì, INS-maturity (Djalovski 2021, Zhou 2025),
  status STRONG.DISTINCTIVE.SUPPORT"
- Per gap analysis: scorri `gaps.requiring.research` per orientare nuovi
  esperimenti

## Note

Versione 1.0 (gennaio 2026), esplicitamente *living document* con
`@update: continuous`. Compilazione iniziale con oncologia, neurale (4 step),
semantica, sintesi CHE, status per proposition. Aggiornato ogni volta che
una nuova validazione consolida o falsifica una predizione.
