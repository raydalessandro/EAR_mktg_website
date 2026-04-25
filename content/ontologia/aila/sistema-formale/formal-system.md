---
title: "Sistema Formale EAR"
summary: "Formalizzazione matematica completa di EAR: vocabolario, assiomi, regole di inferenza, derivazioni step-by-step."
type: aila-spec
version: "1.1"
status: published
order: 40
tags: [aila, formalizzazione, derivazioni]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/EAR_FORMAL_SYSTEM_AILA_v1_1.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/operazionale/matrix-vocab
  - ontologia/teoremi
featured: false
---

## Cos'è

`EAR_FORMAL_SYSTEM_AILA_v1_1` è la **formalizzazione matematica completa** dell'ontologia EAR. Contiene: vocabolario di 12 definizioni numerate (Def.1.1 - Def.1.12), i cinque assiomi A1-A5 con riferimento esplicito al Kernel, sei regole di inferenza R1-R6 (modus ponens, necessità per contraddizione, gerarchia dimensionale, complementarità polare, conservazione, co-presenza degli attributi) e le proposizioni P1-P8 ciascuna con enunciato, derivazione step-by-step, requirements, corollari fisici/informazionali/computazionali e condizioni di falsificazione.

## Posizione nel sistema

Sta a **valle del Kernel** e ne è la traduzione rigorosa: dove il Kernel enuncia le proposizioni in forma compatta, il Formal System esplicita ogni passo deduttivo. È il documento di riferimento per chiunque voglia verificare la solidità logica dell'edificio EAR o derivare nuove proposizioni preservandone la coerenza. Insieme a Kernel e Matrix Vocab forma il triangolo del nucleo formale-operazionale.

## Perché è utile con AI

Permette all'agente di **eseguire dimostrazioni meccaniche**: ogni proposizione è scomposta in step numerati con riferimenti espliciti agli assiomi e proposizioni precedenti. L'AI può quindi verificare derivazioni, generare nuovi corollari, oppure eseguire controlli di falsificazione su dati empirici. Le regole di inferenza R1-R6 sono direttamente applicabili come motore di ragionamento.

## Come usarlo

- Richiede Lingua + Kernel come prerequisiti.
- Caricalo quando serve **ragionamento formale** (verifica di derivazioni, dimostrazione di nuovi teoremi, audit ontologico).
- Per ogni P*x*: leggi prima `enunciate`, poi `derivation`, poi i corollari per dominio.
- Esempio: per validare un teorema empirico, recupera la P di riferimento e applica le condizioni di falsificazione.

## Note

Versione 1.1 (2026-01-19): aggiunge **P8** (struttura ontologica dell'osservatore) e derivazioni dettagliate per tutte le proposizioni. Compatibile con Kernel v1.1 e Matrix Vocab v1.1. Le 6 proposizioni P1-P6 corrispondono ai sei teoremi documentati separatamente nella sezione `ontologia/teoremi`.
