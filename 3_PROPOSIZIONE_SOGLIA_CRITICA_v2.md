# Proposizione Strutturale di Soglia Critica

## Status
**Terzo pilastro formale del framework EAR: vincolo sulle transizioni locale→globale.**

Data: 2025-01-08  
Aggiornamento: 2026-01-11 (Corollario C3.5 Rottura Simmetria)

---

## Definizioni Preliminari

### Transizione locale→globale
Il passaggio da un pattern contenuto in una regione a un pattern che coinvolge l'intero sistema.

### Soglia critica
Il valore del parametro di controllo al quale avviene la transizione.

### Parametro d'ordine
La grandezza che distingue la fase locale dalla fase globale.

---

## Proposizione Centrale

> **In un sistema auto-osservante con distinzione stabile:**
>
> **(A) ESISTENZA DELLA SOGLIA**
> Ogni transizione locale→globale passa attraverso una soglia critica (non è graduale)
>
> **(B) UNIVERSALITÀ**
> La soglia non dipende dai dettagli del sistema, ma solo dalla classe di simmetria e dimensionalità
>
> **(C) NON-ARBITRARIETÀ**
> Il valore della soglia è vincolato dalla struttura, non libero
>
> **(D) IRREVERSIBILITÀ LOCALE**
> Al di sotto della soglia il sistema può tornare indietro; al di sopra, la transizione è localmente irreversibile (richiede intervento globale per invertirla)
>
> **Nessuna transizione locale→globale in un sistema auto-osservante può evitare (A)-(D).**

---

## Corollario Fisico

| Requisito | Realizzazione Fisica |
|-----------|---------------------|
| (A) Esistenza | Transizioni di fase, percolazione, rottura simmetria |
| (B) Universalità | Classi di universalità, esponenti critici |
| (C) Non-arbitrarietà | Soglie calcolabili (pc ≈ 0.59 quadrato, ≈ 0.35 triangolare) |
| (D) Irreversibilità locale | Isteresi, metastabilità |

---

## Corollario Informazionale

| Requisito | Realizzazione Informazionale |
|-----------|------------------------------|
| (A) Esistenza | Soglia di decodifica, capacità canale |
| (B) Universalità | Teoremi di Shannon (indipendenti dal codice specifico) |
| (C) Non-arbitrarietà | Capacità = limite strutturale |
| (D) Irreversibilità locale | Informazione persa sotto soglia non recuperabile localmente |

---

## Corollario per Sistemi Complessi

| Requisito | Realizzazione |
|-----------|---------------|
| (A) Esistenza | Tipping points, biforcazioni |
| (B) Universalità | Pattern simili in ecologia, economia, sociale |
| (C) Non-arbitrarietà | Soglie predicibili dalla struttura della rete |
| (D) Irreversibilità locale | Collassi sistemici, cascate |

---

## Corollario C3.5: Rottura Spontanea di Simmetria

### Enunciato

Il superamento della soglia critica K implica necessariamente rottura di simmetria globale:

```
K(⬡) > K_crit ⟹ Simmetria_globale(⧈) → rotta
```

La direzione della rottura è **contingente** (dipende da fluttuazioni iniziali), ma la rottura stessa è **necessaria**.

### Derivazione

1. **Sotto soglia:** il sistema è "democratico" — tutte le direzioni sono equivalenti, le fluttuazioni si cancellano
2. **Alla soglia:** una micro-fluttuazione viene amplificata dal campo morfogenetico
3. **Oltre soglia:** la fluttuazione amplificata "vince" e impone una direzione preferenziale
4. Il nodo emergente ⬡ rompe l'equivalenza globale del campo ⧈

### Verifica Sperimentale

Test su simulazioni Gray-Scott con campo morfogenetico EAR (4 seed random):

| Condizione | Simmetria media |
|------------|-----------------|
| Classico (no campo) | 0.994 ± 0.002 |
| EAR moderato (sotto soglia) | 0.985 ± 0.003 |
| EAR forte (oltre soglia) | **0.45-0.60 ± 0.18** |

**Le due soglie coincidono:**
- Soglia rottura simmetria: 0.0525
- Soglia critica Prop 3: 0.0550
- Differenza: 0.0025 (< 5%)

Andamento simmetria vs field_strength:
```
Strength   Simmetria
0.0000     0.9964
0.0125     0.9928
0.0250     0.9930
0.0375     0.9886
0.0450     0.9271    ← inizio declino
0.0500     0.8755
0.0550     0.6871    ← salto (soglia)
0.0600     0.3772
```

### Interpretazione Ontologica

- **Simmetria** = proprietà del Campo ⧈ indifferenziato (potenzialità pura, equivalenza delle direzioni)
- **Rottura** = emergenza di Nodo ⬡ che "sceglie" una configurazione specifica
- **Struttura locale preservata**: i pattern dentro il nodo restano regolari
- **Configurazione globale contingente**: dipende da "dove" emerge il primo nodo dominante

### Connessione con Prop 6 (Inseparabilità)

La simmetria è una forma di **Relazione ⇄** (ogni punto si relaziona al suo simmetrico). Quando Δ (distinzione) supera la soglia, alcune ⇄ globali si spezzano mantenendo quelle locali:

```
K > K_crit ⟹ Δ_locale ↑ ⟹ ⇄_globale ↓ (ma ⇄_locale conservata)
```

### Predizione

> In qualsiasi sistema che subisce transizione oltre soglia critica, la simmetria globale sarà rotta mentre la struttura locale sarà preservata.

Questo è verificabile in:
- Cristallizzazione (simmetria liquido → struttura cristallo locale)
- Magnetizzazione (simmetria spin → domini magnetici)
- Morfogenesi biologica (simmetria embrione → asimmetria organismo)
- Organizzazioni (simmetria startup → struttura gerarchica)

---

## Condizioni di Falsificazione

La proposizione è **falsificata** se esiste:

1. Una transizione locale→globale graduale (senza soglia), **oppure**
2. Due sistemi nella stessa classe con soglie arbitrariamente diverse, **oppure**
3. Una soglia che dipende da dettagli microscopici irrilevanti, **oppure**
4. Una transizione sopra-soglia facilmente reversibile localmente, **oppure**
5. **[NUOVO]** Una transizione oltre soglia che preserva la simmetria globale

**Controesempio richiesto:** un sistema verificabile che mostri transizione locale→globale violando almeno uno dei requisiti.

---

## Verificazione

La proposizione è **corroborata** se:

1. Tutte le transizioni di fase note mostrano soglie (nessuna graduale)
2. Classi di universalità continuano a raggrupparsi per simmetria/dimensionalità
3. Soglie di percolazione restano calcolabili dalla geometria
4. Isteresi e metastabilità accompagnano sempre le transizioni
5. **[NUOVO]** Rottura simmetria accompagna sempre il superamento della soglia

---

## Connessione con Framework EAR

Il framework predice l'esistenza di soglie come conseguenza della struttura locale/globale. Il valore specifico emerge dalla geometria del sistema, non è postulato.

La soglia è il "respiro" del sistema: il punto dove il locale deve cedere al globale o viceversa.

**La rottura di simmetria è il "costo ontologico" dell'emergenza:** per passare da potenzialità (⧈) ad attualità (⬡), il sistema deve "scegliere" una configurazione, rompendo l'equivalenza delle alternative.

---

## Firma

Proposizione derivata attraverso:
- Framework ontologico EAR
- Struttura locale/globale come primitivo
- Validazione cross-dominio (percolazione, transizioni di fase, tipping points)
- **[NUOVO]** Verifica sperimentale su simulazioni Gray-Scott con campo morfogenetico

Questo documento rappresenta il terzo vincolo formale del framework EAR.
