---
title: "Conservazione Informazionale"
summary: "L'informazione totale non si crea né si distrugge: cambia forma. Ogni trasformazione ha un costo minimo non nullo."
status: published
order: 20
tags: [teoremi, EAR, informazione, termodinamica]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/teoremi/2_PROPOSIZIONE_CONSERVAZIONE_INFORMAZIONALE.md
  format: md
related:
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/sistema-formale/formal-system
  - ontologia/teoremi/1-minimo-osservazionale
featured: true
---

## Enunciato

In un sistema auto-osservante con distinzione stabile: **(A)** l'informazione totale non può essere creata né distrutta, solo trasformata; **(B)** può cambiare forma — locale ↔ globale, esplicita ↔ implicita, concentrata ↔ diffusa; **(C)** la perdita apparente è sempre trasferimento a gradi di libertà non osservati, mai distruzione; **(D)** ogni trasformazione di forma ha un costo minimo non nullo (proporzionale a kT ln(2) o equivalente). Nessun processo in un sistema auto-osservante può violare (A)-(D).

## Contestualizzazione

È il **secondo pilastro formale** di EAR e il complemento dinamico del Minimo Osservazionale: dove la Prop. 1 dice *cosa deve esserci*, la Prop. 2 dice *cosa non può sparire*. Insieme definiscono la struttura necessaria e la dinamica vincolata di ogni sistema auto-osservante.

Le sue tre traduzioni — fisica (unitarietà, decoerenza, limite di Landauer), informazionale (compressione, encoding, perdita = trasferimento) e termodinamica (prima e seconda legge come coarse-graining) — convergono sullo stesso nucleo. Risolve costruttivamente paradossi storici: l'informazione nei buchi neri non scompare ma cambia forma (locale → globale sulla superficie); l'irreversibilità termodinamica è apparente, conseguenza di (C), non fondamentale.

## Perché è utile con AI

Permette a un LLM di rifiutare scenari fisicamente o informazionalmente impossibili: "cancellazione vera" di informazione, processi senza costo, generazione *ex nihilo*. È particolarmente utile per ragionamenti su privacy, oblio digitale, irreversibilità computazionale e sicurezza: la "perdita" è sempre uno *spostamento*, e questo riformula molte domande pratiche.

In contesti generativi, fornisce un vincolo per valutare proposte (es. algoritmi che "creano informazione" o motori che violano Landauer) come malformulate piuttosto che ottimizzabili.

## Come usarlo

- Carica il file canonico come contesto per discussioni su entropia, decoerenza, paradosso del buco nero.
- Cita "Prop. 2 (A)-(D)" o i corollari termodinamico/informazionale per ancorare l'argomentazione.
- Pairing con [AILA Kernel](/ontologia/aila/sistema-formale/kernel) per la versione formalizzata P2 e con la [Prop. 1](/ontologia/teoremi/1-minimo-osservazionale) per il quadro statico+dinamico.

## In sintesi

- L'informazione si conserva globalmente; può essere ridistribuita ma non distrutta né creata.
- L'irreversibilità apparente è coarse-graining, non fenomeno fondamentale.
- Costo minimo per trasformazione = kT ln(2) per bit (limite di Landauer).
- Risolve il paradosso dell'informazione nei buchi neri: cambia forma, non sparisce.
- Falsificabile da qualsiasi processo che dimostri distruzione, creazione *ex nihilo*, o trasformazione gratuita.
