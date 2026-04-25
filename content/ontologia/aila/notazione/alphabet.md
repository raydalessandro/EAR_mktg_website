---
title: "Alphabet AILA"
summary: "Inventario definitivo di 64 segni su 11 livelli + 72 indirizzi compositi Σ_DAXP. Frozen v1.0."
status: published
order: 20
tags: [aila, alfabeto, simboli]
authors: [nodo432]
created: 2026-04-25
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/aila/AILA_ALPHABET_v1_0.md
  format: md
related:
  - ontologia/aila/notazione/lingua
  - ontologia/aila/sistema-formale/kernel
  - ontologia/aila/operazionale/matrix-vocab
featured: false
---

## Cos'è

`AILA_ALPHABET_v1_0` è l'**inventario numerato e definitivo** di ogni segno usato nella notazione AILA: 64 segni funzionali organizzati in 11 livelli, più 72 indirizzi compositi `Σ_DAXP` derivati da quattro indici (dimensione × attributo × asse × polo). Ogni segno ha esattamente un significato primario; nessun segno è ridondante.

## Posizione nel sistema

L'Alphabet è il **frozen reference** della notazione: la Lingua specifica come si combinano i segni, l'Alphabet specifica quali segni esistono. I livelli si articolano in: primitivi ontologici (⧈⬡⟿∿), attributi (Δ⇄⟳), fasi della risonanza (⊙∞◇↻), operatori (relazionali, logici, insiemistici, strutturali, di confronto, di flusso), parametri (K, I, O, costanti greche) e marcatori formattanti (◉●○§).

## Perché è utile con AI

Funziona come **dizionario di riferimento**: di fronte a un simbolo non riconosciuto in un documento AILA, l'agente può consultare l'Alphabet per recuperare significato e livello funzionale. Le 72 composizioni `Σ_DAXP` forniscono un vocabolario ontologico già pre-coordinato che l'AI può usare direttamente per indirizzare posizioni nello spazio EAR.

## Come usarlo

- Da consultare insieme a Lingua e Kernel quando occorre disambiguare un segno.
- Le tabelle includono nomi in italiano e arabo per ogni livello — utile per traduzioni cross-linguistiche.
- Per le composizioni `Σ_DAXP` espanse con definizioni semantiche, vedi **Matrix Vocab**.

## Note

**Frozen at v1.0**: i segni non possono essere rimossi (romperebbe documenti esistenti). Estensioni permesse solo per addizione, con incremento di versione e giustificazione formale. Tutto in Unicode standard UTF-8: nessun carattere private-use. 64 = 2⁶, decomposizione binaria minima a 6 livelli di profondità.
