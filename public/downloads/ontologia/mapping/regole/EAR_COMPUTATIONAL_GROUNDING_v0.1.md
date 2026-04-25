# EAR COMPUTATIONAL GROUNDING — Bozza v0.1
## Da protocollo interpretativo a calcolo

**Date:** 2026-02-12  
**Status:** DRAFT — prima formalizzazione  
**Goal:** Trasformare ogni step di §8 da giudizio umano a funzione calcolabile  
**Input format:** Concetto C rappresentato come grafo semantico G(V, E)  
dove V = componenti concettuali, E = relazioni tipizzate

---

## §0. RAPPRESENTAZIONE INPUT

Prima di calcolare qualsiasi asse, il concetto deve essere in formato formale.

### §0.1 Grafo Semantico del Concetto

```
Dato un concetto C, costruisci G_C = (V, E) dove:

  V = {v₁, v₂, ..., vₙ} — componenti concettuali
  E = {(vᵢ, vⱼ, τ)} — relazioni tipizzate

Ogni edge ha un tipo τ ∈ T, dove:

  T_Δ = {boundary, classification, distinction, hierarchy, separation,
         identity, definition, category, partition}
  
  T_⇄ = {equivalence, correspondence, conservation, symmetry, mapping,
         exchange, balance, connection, bridge, invariance}
  
  T_⟳ = {evolution, transformation, dynamics, process, cycle, flow,
         causation, feedback, iteration, generation}
  
  T_temporal = {before, after, causes, evolves_to, during, rate_of}
  
  T_spatial_3D = {contains, volume_of, encloses, flows_through, field_in}
  
  T_spatial_2D = {pattern_on, cycle_in, interface, surface, network_on}
  
  T_self_ref = {applies_to_self, meta_level, about_own_category,
               decides_own_decidability, measures_own_complexity}
  
  T_cross_domain = {bridges, unifies_with, requires_independent_framework}
```

### §0.2 Costruzione del Grafo

```
METODO 1 — Da testo (NLP pipeline):
  1. Estrai entità dal definition text → V
  2. Estrai relazioni tra entità → E
  3. Classifica ogni relazione in T_* → τ per ogni edge
  
METODO 2 — Da embedding + struttura:
  1. Decompose concept into sub-concepts via clustering → V
  2. Compute pairwise semantic similarity → candidate E
  3. Classify edge types via trained classifier → τ
  
METODO 3 — Da knowledge graph esistente (Wikidata, ConceptNet):
  1. Query concept node
  2. Extract 2-hop neighborhood → G_C
  3. Map relation types to T_* taxonomy
```

---

## §1. CONSTRAINT TEST (calcolabile)

```
INPUT: G_C (grafo del concetto), D_domain (dominio del concetto)
OUTPUT: {CONSTRAINT, NODE}

STEP 1 — UNIVERSALITY SCORE:

  U(C) = |systems_obeying(C)| / |all_systems_in(D_domain)|
  
  Se U(C) = 1.0 → universale nel dominio
  Se U(C) < 1.0 → non universale → NODE
  
  CALCOLO PRATICO:
  → Conta le classi di sistemi in D_domain
  → Conta quante obbediscono a C
  → U = ratio
  
  Esempio:
    Heisenberg: tutti i sistemi quantistici → U = 1.0 ✓
    Pauli: solo fermioni (non bosoni) → U = 0.5 ✗

STEP 2 — CROSS-DOMAIN TEST:

  X_domain(C) = |{D : C applies in D}| / |{all domains}|
  
  Se X_domain < threshold_constraint (= 0.8) → NODE
  Se X_domain ≥ 0.8 → CONSTRAINT candidate
  
  Esempio:
    Heisenberg → applies in QM, QFT, quantum optics, ... → X_domain alta
    CAP → applies only in distributed systems → X_domain bassa → NODE

STEP 3 — STRUCTURAL TEST:

  S(C) = proportion of T_Δ edges that are {boundary, partition, separation}
          targeting THE STRUCTURE ITSELF (not objects within structure)
  
  Operazionalizzazione:
  → Se gli edge Δ di C puntano a "measurement," "observation," 
    "formal system" (struttura stessa) → S alta → CONSTRAINT
  → Se gli edge Δ puntano a "particles," "systems," "specific objects" 
    → S bassa → NODE

DECISION:
  CONSTRAINT iff U(C) ≥ 1.0 AND X_domain(C) ≥ 0.8 AND S(C) ≥ 0.7
  Else → NODE
```

---

## §2. DIMENSION D (calcolabile)

```
INPUT: G_C con edge tipizzati
OUTPUT: D ∈ {1, 2, 3, 4}

CALCOLO:

  w₄ = |{e ∈ E : τ(e) ∈ T_temporal}| / |E|
  w₃ = |{e ∈ E : τ(e) ∈ T_spatial_3D}| / |E|
  w₂ = |{e ∈ E : τ(e) ∈ T_spatial_2D}| / |E|
  w₁ = 1 - w₄ - w₃ - w₂

R1 CASCADE (calcolato):

  if w₄ > θ_D → D = 4      (θ_D = 0.25, threshold)
  elif w₃ > θ_D → D = 3
  elif w₂ > θ_D → D = 2
  else → D = 1

ESSENTIAL CONTENT TEST (raffinamento):
  
  Per confermare D=4, verifica:
  → Rimuovi tutti gli edge temporali da G_C
  → Calcola connectedness(G_C_reduced)
  → Se il grafo si disconnette → tempo ERA essenziale → D=4 confermato
  → Se il grafo resta connesso → tempo era accessorio → declassa a D=3 o meno
  
  Stessa logica per D=3 (rimuovi spatial_3D), D=2 (rimuovi spatial_2D)

OUTPUT: D = max{d : rimozione degli edge di tipo d disconnette G_C}
        Se nessuna rimozione disconnette → D=1 (fallback)
```

---

## §3. ATTRIBUTE A (calcolabile)

```
INPUT: G_C con edge tipizzati
OUTPUT: A ∈ {1(Δ), 2(⇄), 3(⟳)}

### 3.1 ELIMINATION TEST (formalizzato)

Per ogni attributo a ∈ {Δ, ⇄, ⟳}:

  G_C^(-a) = grafo G_C con tutti gli edge di tipo T_a rimossi
  
  fragmentation(a) = |connected_components(G_C^(-a))| / |V|
  
  Se fragmentation(a) è alto → rimuovere a distrugge il concetto → a è dominante

FORMULA:

  A = argmax_a { fragmentation(a) }
  
  equivalentemente:
  
  A = argmax_a { |connected_components(G_C^(-a))| }

### 3.2 OSCILLATION DETECTION

  Se |fragmentation(a₁) - fragmentation(a₂)| < ε (= 0.05):
  → oscillazione tra a₁ e a₂
  
  RESOLUTION (calcolabile):
  
  Step 1 — PRESUPPOSITION vs ASSERTION:
    presup(a) = |{e ∈ T_a : e.source ∈ V_input}| — edge che PARTONO da premesse
    assert(a) = |{e ∈ T_a : e.target ∈ V_output}| — edge che ARRIVANO a conclusioni
    
    Se presup(a₁) > assert(a₁) AND assert(a₂) > presup(a₂):
    → a₁ è presupposto, a₂ è asserito → A = a₂
  
  Step 2 — MECHANISM vs ESSENCE:
    Calcola betweenness centrality degli edge per tipo
    mechanism_a = mean betweenness of T_a edges (alti = meccanismo/pathway)
    essence_a = 1 - mechanism_a (complementare)
    
    Se mechanism(a₁) > mechanism(a₂):
    → a₁ è meccanismo, a₂ è essenza → A = a₂

### 3.3 TOPOLOGICAL VALIDATION

  Dopo aver determinato A, valida:
  
  topology(G_C) = classify_graph_structure(G_C)
    → "tree" se max_branching > 2 AND cycles = 0
    → "lattice" se avg_degree > 2 AND reciprocal_edges > 0.3
    → "loop" se cycles > 0 AND feedback_edges > 0.2
  
  expected_topology = {Δ: "tree", ⇄: "lattice", ⟳: "loop"}
  
  Se topology(G_C) = expected_topology[A] → validation ✓
  Se mismatch → flag, possibile oscillazione non risolta
```

---

## §4. COMPLEXITY X (calcolabile)

```
INPUT: G_C con edge tipizzati
OUTPUT: X ∈ {1, 2, 3}

### 4.1 SELF-REFERENCE SCORE

  self_ref(C) = |{e ∈ E : τ(e) ∈ T_self_ref}| / |E|
  
  Oppure (più robusto):
  
  self_ref(C) = |{paths in G_C that start and end in same TYPE-class of V}| / |all_paths|
  
  TYPE-class: raggruppamento dei nodi per dominio/categoria
  Un path che parte da "provability" e arriva a "provability" = self-reference

### 4.2 CROSS-DOMAIN BRIDGE SCORE

  cross(C) = |{e ∈ E : τ(e) ∈ T_cross_domain}| / |E|
  
  Oppure (più robusto):
  
  Partiziona V in cluster per dominio (via semantic embedding)
  cross(C) = |{e ∈ E : e.source.cluster ≠ e.target.cluster}| / |E|
  
  Misura quanti edge collegano domini genuinamente distinti

### 4.3 INDEPENDENCE TEST (per X=3)

  Per confermare X=3, non basta cross(C) alto.
  I framework collegati devono essere INDIPENDENTI:
  
  independence(d₁, d₂) = 1 - semantic_similarity(centroid(d₁), centroid(d₂))
  
  Se independence > θ_indep (= 0.6) → genuinamente indipendenti → X=3 confermabile
  Se independence < θ_indep → derivano dallo stesso framework → X=1

### 4.4 DECISION

  if self_ref(C) > θ_self (= 0.15) → X = 2
  elif cross(C) > θ_cross (= 0.3) AND independence > θ_indep → X = 3
  else → X = 1
  
  PRIORITY: X=2 ha precedenza (se è self-referential E cross-domain → X=2,
    perché la self-reference è più strutturalmente profonda della synthesis)
  
  EXCEPTION: Se cross(C) > 0.5 AND self_ref(C) < 0.05 → X = 3 anche se 
    self_ref suggerisce X=1 (la synthesis domina)
```

---

## §5. POLARITY P (calcolabile)

```
INPUT: G_C, knowledge_graph K (grafo della conoscenza globale)
OUTPUT: P ∈ {+, -}

### 5.1 EXPANSION/CONTRACTION SCORE

METODO GRAPH-BASED:

  Inserisci C nel knowledge graph K.
  
  expansion(C) = |{concepts in K reachable BECAUSE of C}| 
                 — concetti che C abilita/crea
  
  contraction(C) = |{concepts in K unreachable BECAUSE of C}|
                   — concetti che C elimina/proibisce
  
  P = + se expansion(C) > contraction(C)
  P = - se contraction(C) > expansion(C)

METODO LINGUISTICO (fallback se K non disponibile):

  Analizza il testo definitorio di C.
  
  pos_markers = {enables, creates, classifies, establishes, opens, 
                 generates, proves_existence, constructs}
  neg_markers = {forbids, eliminates, constrains, reduces, proves_impossibility,
                 limits, prohibits, bounds, excludes}
  
  p_score = Σ count(pos_markers) / (Σ count(pos_markers) + Σ count(neg_markers))
  
  P = + se p_score > 0.5
  P = - se p_score ≤ 0.5

### 5.2 ARCHETYPE VALIDATION

  Dopo aver calcolato D, A, X, P:
  → Lookup archetype name per Σ_DAXP
  → Calcola semantic_similarity(concept_embedding, archetype_embedding)
  → Se similarity > θ_arch (= 0.3) → validation ✓
  → Se similarity < θ_arch → flag, possibile mismap
  
  Questo SOSTITUISCE il "resonance check" soggettivo con una misura
```

---

## §6. CLUSTER VALIDATION (calcolabile)

```
INPUT: Σ_DAXP assegnata, database di tutti i concetti già mappati
OUTPUT: coherence_score, isomorphism_flag

### 6.1 INTRA-CLUSTER COHERENCE

  cluster_C = {tutti i concetti nella stessa cella Σ_DAXP}
  
  coherence = mean pairwise semantic_similarity tra tutti i concetti in cluster_C
  
  Se coherence > θ_coh (= 0.4) → cluster coerente ✓
  Se coherence < θ_coh → flag: C potrebbe essere nella cella sbagliata

### 6.2 CROSS-DOMAIN ISOMORPHISM

  Per ogni coppia (C₁, C₂) nella stessa cella ma da domini diversi:
  
  isomorphism_score = graph_edit_distance_normalized(G_C₁, G_C₂)
  
  Dove GED misura quante operazioni servono per trasformare G_C₁ in G_C₂
  (normalizzato per dimensione dei grafi)
  
  Se isomorphism_score < θ_iso (= 0.4) → strutturalmente isomorfi ✓
  Se isomorphism_score > θ_iso → flag: stessa cella ma struttura diversa

### 6.3 COMPLEMENT PREDICTION

  Data Σ_DAX+, predici Σ_DAX-:
  
  complement_candidates = {concetti noti con polarità opposta nello stesso DAX}
  
  Se |complement_candidates| > 0:
    complement_coherence = mean similarity(C, complement_candidates)
    Se complement_coherence in range [0.2, 0.6] → complementi plausibili ✓
    (non troppo simili [sarebbe stessa polarità], non troppo diversi [sarebbe altra cella])
  
  Se |complement_candidates| = 0:
    → Genera via embedding: nearest_concept con polarità invertita
    → Flag: "complement non osservato — possibile concetto mancante"
```

---

## §7. CONFIDENCE SCORE (calcolabile)

```
INPUT: tutti i punteggi precedenti
OUTPUT: confidence ∈ [0, 1]

confidence(C) = w₁ · constraint_clarity
              + w₂ · dimension_separation  
              + w₃ · attribute_dominance
              + w₄ · complexity_clarity
              + w₅ · polarity_margin
              + w₆ · archetype_resonance
              + w₇ · cluster_coherence
              + w₈ · isomorphism_score

Dove:
  constraint_clarity = |max(U,X_domain,S) - threshold| — quanto è chiaro node vs constraint
  dimension_separation = max(w₄,w₃,w₂,w₁) - second_max — gap tra prima e seconda D
  attribute_dominance = max(frag) - second_max(frag) — gap nell'elimination test
  complexity_clarity = |self_ref - θ_self| + |cross - θ_cross| — distanza dalle soglie
  polarity_margin = |p_score - 0.5| — quanto è chiara la polarità
  archetype_resonance = semantic_similarity(C, archetype)
  cluster_coherence = intra-cluster coherence score
  isomorphism_score = 1 - GED se stessa cella ha altri concetti

Pesi w₁..w₈ da calibrare sui 65 concetti già mappati (training set).
```

---

## §8. PIPELINE COMPLETA

```
function map_concept(C, text_definition, domain):
    
    # Step 0: Build graph representation
    G_C = build_semantic_graph(text_definition)
    
    # Step 1: Constraint check
    if constraint_test(G_C, domain) == CONSTRAINT:
        return {type: CONSTRAINT, mapping: identify_constraint_type(G_C)}
    
    # Step 2: Dimension
    D = calculate_dimension(G_C)
    
    # Step 3: Attribute
    A = calculate_attribute(G_C)
    oscillation = detect_oscillation(G_C)
    if oscillation:
        A = resolve_oscillation(G_C, oscillation)
    
    # Step 4: Complexity
    X = calculate_complexity(G_C)
    
    # Step 5: Polarity
    P = calculate_polarity(G_C, knowledge_graph)
    
    # Step 6: Assign
    sigma = f"Σ_{D}{A}{X}{P}"
    
    # Step 7: Validate
    arch_score = archetype_validation(sigma, C)
    cluster_score = cluster_validation(sigma, C, existing_mappings)
    iso_score = isomorphism_validation(sigma, C, existing_mappings)
    
    # Step 8: Confidence
    conf = calculate_confidence(all_scores)
    
    return {
        coordinate: sigma,
        confidence: conf,
        archetype_resonance: arch_score,
        cluster_coherence: cluster_score,
        tensions: oscillation,
        flags: [f for f in validations if f.score < threshold]
    }
```

---

## §9. THRESHOLDS DA CALIBRARE

```
Tutti i threshold (θ) sono parametri da calibrare sul training set
dei 65 concetti già mappati manualmente. 

METODO DI CALIBRAZIONE:
  1. Per ogni concetto già mappato, calcola i punteggi algoritmici
  2. Confronta con il mapping manuale (ground truth)
  3. Ottimizza θ per massimizzare agreement
  4. Cross-validate (leave-one-batch-out)

THRESHOLD INIZIALI (da mie stime, da validare):
  θ_D = 0.25        (fraction di edge temporali per D=4)
  θ_self = 0.15     (fraction di self-ref edges per X=2)
  θ_cross = 0.30    (fraction di cross-domain edges per X=3)
  θ_indep = 0.60    (independence tra framework per X=3)
  θ_arch = 0.30     (archetype resonance minima)
  θ_coh = 0.40      (cluster coherence minima)
  θ_iso = 0.40      (isomorphism GED threshold)
  ε = 0.05          (oscillation detection margin)

NOTA: Questi valori sono IPOTESI INIZIALI. Il vero valore emerge
dalla calibrazione sui dati. I 65 concetti dei batch 1-6 sono
il training set naturale.
```

---

## §10. COSA MANCA ANCORA

```
1. IMPLEMENTAZIONE del graph builder (§0.2)
   → Serve un NLP pipeline o un mapping da knowledge graph a G_C
   → Questo è il pezzo più ingegneristico

2. EDGE TYPE CLASSIFIER
   → Classificare le relazioni in T_Δ / T_⇄ / T_⟳
   → Trainabile sui 65 concetti come training set
   → Oppure rule-based con keyword matching come bootstrap

3. CALIBRAZIONE dei θ
   → Richiede implementazione + run sui 65 concetti
   → Output: θ ottimali + agreement score con mapping manuale

4. KNOWLEDGE GRAPH per §5 (polarity)
   → Serve un grafo delle dipendenze tra concetti
   → Wikidata? ConceptNet? Custom?

5. VALIDATION su concetti NUOVI (non nel training set)
   → Batch 7 (Millennium Problems) come test set?
   → O nuovo batch mappato prima manualmente, poi algoritmicamente

6. IL TERMINE MANCANTE
   → Ray sente che manca un termine nell'ontologia
   → Potrebbe emergere dalla calibrazione: se nessun θ produce
     buon agreement, forse la griglia 4×3×3×2 ha bisogno 
     di una dimensione aggiuntiva o una raffinatura di asse
```

---

## APPENDICE: TEST RAPIDO SUI 65 CONCETTI

Per validare immediatamente questo framework senza implementazione 
completa, si può fare un TEST MANUALE ACCELERATO:

Per 5-10 concetti campione, costruire G_C a mano e calcolare:
  1. fragmentation test per A → concorda con mapping manuale?
  2. temporal edge count per D → concorda?
  3. self_ref edge count per X → concorda?

Se 8/10 concordano → framework promettente, vale implementare
Se < 5/10 concordano → framework necessita revisione prima di implementare
