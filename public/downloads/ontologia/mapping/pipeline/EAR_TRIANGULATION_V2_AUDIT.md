# 🔬 AUDIT — EAR Triangulation Engine v2.0

**Auditor:** Claude Opus 4.6  
**Data:** 9 Febbraio 2026  
**Codebase:** ~3215 righe (8 Python + 1 JSX + 2 data/config)  
**Scope:** Bug logici, robustezza, design, confronto con audit precedenti

---

## VERDETTO COMPLESSIVO

**Qualità: 8.2/10** — Architettura eccellente, enormemente superiore ai progetti precedenti.

Il sistema dimostra un salto di maturità ingegneristica: separazione netta delle responsabilità (Scriba XOR Arbiter), mechanical tribunal senza LLM bias, blind spot analysis strutturata, backup automatici, stato persistente separato Director/Scriba. I problemi trovati sono prevalentemente edge cases e mancanze di robustezza, non errori architetturali fondamentali.

Per confronto: Teatro Narrativo era 5/10 (timeout/retry issues), Neural Mapping Network era 6/10 (5 bug critici A-level). Questo progetto ha solo 2 bug critici reali.

---

## A — BUG LOGICI (5 trovati)

### A1 ❌ CRITICO — `temperature` kwarg causa TypeError
**File:** `agents/director.py:254`  
**Problema:** `Director.propose_batch()` chiama `self.provider.complete(system=..., user=..., temperature=0.5)`, ma il metodo `complete()` di tutti i provider in `llm_adapter.py` accetta solo `system` e `user`. Qualsiasi chiamata a `propose_batch()` (e quindi tutto l'autonomous loop) esplode con `TypeError: complete() got an unexpected keyword argument 'temperature'`.

**Impatto:** Director non funziona. `cmd_propose`, `cmd_auto`, e `AutonomousLoop.run()` sono tutti broken.

**Fix (2 min):**
```python
# Option A: Rimuovi temperature da director.py:254
response = self.provider.complete(system=..., user=user_msg)

# Option B: Aggiungi **kwargs a LLMProvider.complete() e passalo ai provider
```

---

### A2 ❌ CRITICO — Dashboard v2 incompatibile con backend v2
**File:** `dashboard.jsx` (intero file)  
**Problema:** La dashboard aspetta strutture dati v1 che non esistono più:

| Dashboard aspetta | Backend v2 produce |
|---|---|
| `data.votes[]` con `{coord, majority, unanimous, dissenter}` | `tribunal.coordinate_matches[]` con `{coordinate, synth_value, agent_values, matches, dissenters}` |
| `data.verdict` ("VALID"/"REVIEW"/"REJECT") | `tribunal.route` (Route.SCRIBA / Route.ARBITER) |
| `data.analysis[]` con `{dissent_in_blind_spot, recommendation}` | `arbiter.divergences[]` con `{agent_area, classification}` |
| `data.final_recommendation.sigma` | `result.final.sigma` |

**Impatto:** Dashboard è completamente non-funzionale per visualizzare risultati v2. Renderizza pannelli vuoti o crashati.

**Fix (30 min):** Riscrivere `TribunalPanel`, `ArbiterPanel`, `FinalPanel`, e le funzioni `getTribunalData()`/`getArbiterData()` per mappare le strutture v2.

---

### A3 ⚠️ MEDIO — Backup filename collision
**File:** `agents/scriba.py:81`  
**Problema:** Il backup usa timestamp a risoluzione secondi: `%Y%m%d_%H%M%S`. Se due concetti vengono processati nello stesso secondo (improbabile ora dato che le LLM calls sono lente, ma possibile con parallelizzazione futura), il secondo backup sovrascrive il primo.

**Fix (1 min):** Aggiungere microsecondi: `%Y%m%d_%H%M%S_%f`

---

### A4 ⚠️ MEDIO — Stats accumulate cross-operation
**File:** `orchestrator.py:75-76`  
**Problema:** `self.total_tokens` e `self.total_calls` sono variabili d'istanza che non vengono mai resettate. Se usi lo stesso engine per `map_concept()` poi `map_batch()`, i contatori del batch includono quelli del single concept. I risultati JSON salvati riportano stats cumulative, non per-concept.

**Fix (3 min):** Salvare snapshot a inizio di `map_concept()` e calcolare delta:
```python
def map_concept(self, concept, domain=""):
    tokens_before = self.total_tokens
    calls_before = self.total_calls
    # ... pipeline ...
    result["stats"] = {
        "concept_tokens": self.total_tokens - tokens_before,
        "concept_calls": self.total_calls - calls_before,
        "session_tokens": self.total_tokens,
        "session_calls": self.total_calls
    }
```

---

### A5 ⚠️ BASSO — parse_agent_output() riusata per Director
**File:** `agents/director.py:258`  
**Problema:** `parse_agent_output()` da `tribunal.py` è progettata per parsing output mapper (con `sigma`, `coordinates`, ecc.). Viene riusata per parsing output Director (che ha `action`, `concepts[]`, `strategy`). Funziona perché il parser è generico (solo `json.loads` + cleanup), ma semanticamente è fuorviante e fragile — se il parser aggiunge validazione specifica per mapper in futuro, Director si rompe.

**Fix (5 min):** Creare `parse_json_output()` generico separato, o `parse_director_output()` dedicato.

---

## B — GAP DI ROBUSTEZZA (8 trovati)

### B1 — Nessun retry su LLM failure
**File:** `orchestrator.py:86-98`  
`_call_llm()` ha zero retry logic. Un singolo timeout (frequente con DeepSeek/Ollama) uccide l'intero concept mapping. Il Neural Mapping Network aveva lo stesso problema — qui è più grave perché ci sono 4-6 LLM calls per concept.

**Suggerimento:** Exponential backoff con max 3 retry, catchando `requests.Timeout`, `httpx.TimeoutError`, e status 429/500/502/503.

---

### B2 — Nessuna validazione schema output LLM
**File:** `orchestrator.py:114, 124, 134, 144`  
`parse_agent_output()` ritorna il dict JSON raw. Se un agent ritorna `{"concept": "X"}` senza `coordinates`, `sigma`, `type`, il tribunal va in crash su `synth.get("coordinates", {})` → OK, ma poi `match_coordinate()` riceve valori None → confronti insensati → risultati silenziosamente sbagliati (non crash, peggio).

**Suggerimento:** Aggiungere `validate_agent_output(parsed: dict) -> bool` che verifica campi required.

---

### B3 — Nessun file locking su network_state.json
**File:** `agents/scriba.py:70-76`  
Read-modify-write senza lock. Se due processi (es. test paralleli, o future parallelization) scrivono contemporaneamente, si perdono nodi. Ora è safe perché tutto è single-threaded, ma l'architettura suggerisce future parallelism.

**Suggerimento:** `fcntl.flock()` o atomicwrites.

---

### B4 — JSON parse failure non catturata per agent
**File:** `core/tribunal.py` → `parse_agent_output()`  
Se un LLM ritorna testo non-JSON (succede ~5% delle volte con modelli deboli), `json.loads()` solleva `JSONDecodeError`. L'orchestrator non cattura questo per singolo agent — l'intero concept mapping fallisce. In batch mode, il try/except generico in `map_batch()` lo prende, ma il messaggio d'errore è poco utile.

**Suggerimento:** Wrappare ogni `run_agent_*()` + `parse_agent_output()` in try/except con fallback che indica quale agent ha fallito e il raw output.

---

### B5 — WebSocket server senza autenticazione
**File:** `core/streamer.py`  
Chiunque sulla rete locale può connettersi e ricevere tutti gli eventi, inclusi concept names, coordinate mappings, e potenzialmente frammenti di documenti proprietari EAR.

**Suggerimento:** Token-based auth o bind solo a localhost (attualmente implicito ma non enforced).

---

### B6 — AutonomousLoop senza graceful shutdown
**File:** `agents/director.py:400-421`  
`loop.run(cycles)` non gestisce SIGINT/SIGTERM. Se interrompi durante una LLM call, nessun salvataggio parziale. Il network_state potrebbe essere inconsistente se Scriba era a metà write.

**Suggerimento:** Signal handler che setta un flag `self._stop_requested` controllato tra cicli.

---

### B7 — Director context troncato a 2000 chars hardcoded
**File:** `agents/director.py:316`  
`self.archetypes_doc[:2000]` taglia arbitrariamente. Con 72 celle e occupanti crescenti, 2000 chars copre solo D=1 (18 celle). D=2, D=3, D=4 sono invisibili al Director, che proporrà concetti per celle che crede vuote ma sono già occupate.

**Suggerimento:** Generare un summary compatto programmaticamente (sigma + n_occupanti per cella), non troncatura bruta.

---

### B8 — Nessun rate limiting in autonomous mode
**File:** `agents/director.py:400-421`, `orchestrator.py:311-349`  
In autonomous mode, il sistema fa 4-6 LLM calls per concept × 5 concepts per cycle × N cycles. Con DeepSeek (rate limited), 3 cicli = ~60-90 API calls in rapida successione. Nessun backoff tra calls.

**Suggerimento:** Aggiungere `time.sleep(delay)` configurabile tra concept mapping, e gestione 429 in `_call_llm()`.

---

## C — MIGLIORAMENTI DESIGN (7 suggeriti)

### C1 — Parallelizzazione 4 mapper (impatto: -75% latency)
**File:** `orchestrator.py:181-199`  
I 4 mapper sono sequenziali. Ogni LLM call richiede ~15-30s. Totale: 60-120s per concept. Con `concurrent.futures.ThreadPoolExecutor` si scende a 15-30s (speed up 4x).

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=4) as pool:
    futures = {
        pool.submit(self.run_synth, concept, domain): "synth",
        pool.submit(self.run_agent_delta, concept, domain): "delta",
        pool.submit(self.run_agent_rel, concept, domain): "rel",
        pool.submit(self.run_agent_proc, concept, domain): "proc",
    }
    results = {}
    for future in as_completed(futures):
        label = futures[future]
        results[label] = future.result()
```

⚠️ Richiede B3 (file locking) e A3 (backup collision) risolti prima.

---

### C2 — Sigma notation inconsistency
**File:** `data/EAR_ARCHETYPES_72.md` vs `agents/scriba.py` vs `agents/director.py`  
L'archetype file usa subscript Unicode: `Σ₁₁₁₊`. Il codice Python produce: `Σ_111+`. Il Director `_build_cells()` genera: `Σ_1111+` (wait, no — riga 66: `f"Σ_{d}{a}{x}{p}"` che per d=1,a=1,x=1,p="+" dà `Σ_111+`).

Ma `NetworkState._build_cells()` confronta `node.get("sigma")` con le chiavi generate. Se un agent LLM produce sigma con subscript Unicode (copiandolo dal prompt degli archetypes), il match fallirà silenziosamente.

**Suggerimento:** Normalizzare sigma in `parse_agent_output()` — convertire subscripts a ASCII.

---

### C3 — SCRIBA_SYSTEM prompt è dead code
**File:** `agents/prompts.py:398-424`  
`SCRIBA_SYSTEM` è definito e importato ma mai usato. Scriba è pure Python (correttamente). Il prompt è orfano dalla v1.

**Suggerimento:** Rimuovere o commentare come "reference only".

---

### C4 — Confidence hardcoded a 0.95
**File:** `orchestrator.py:292`, `agents/scriba.py:211`  
Ogni mapping VALID riceve confidence 0.95 indipendentemente dalla qualità. Un 3/3 match dove ogni coordinate era unanime con alta confidenza dovrebbe avere 0.98+. Un 3/3 match dove gli agent avevano tutti `confidence_notes` pieni di dubbi dovrebbe avere 0.85.

**Suggerimento:** Calcolare confidence dal tribunal: base 0.90 + bonus per unanimità + malus per confidence_notes non vuote.

---

### C5 — Review resolution workflow incompleto
**File:** `agents/director.py`  
Il Director può proporre `RESOLVE_REVIEW` ma non c'è meccanismo per eseguirlo. `handle_result()` aggiunge a `review_queue` ma nessun metodo `resolve_review()` rimuove da queue e inserisce in network.

**Suggerimento:** Aggiungere `cmd_resolve` in `run.py` che mostra review item → chiede human input → accetta (Scriba insert) o rigetta (reject log).

---

### C6 — Duplicate check case-insensitive ma no normalization
**File:** `agents/scriba.py:137`  
`_is_duplicate()` confronta `.lower()` ma non normalizza whitespace, trattini, o Unicode. "Schrödinger Equation" vs "Schrodinger Equation" vs "schrödinger  equation" sono tutti diversi.

**Suggerimento:** `unicodedata.normalize("NFKD", concept).lower().strip()` + regex whitespace collapse.

---

### C7 — Batch non deduplicata
**File:** `orchestrator.py:311-349`  
Se un batch file contiene lo stesso concept due volte, entrambi vengono processati (4-6 LLM calls ciascuno). Il secondo viene rifiettato da Scriba come duplicate, ma solo dopo aver sprecato ~60 token-seconds.

**Suggerimento:** Deduplicare `concepts` a inizio di `map_batch()`.

---

## D — CONFRONTO CON AUDIT PRECEDENTI

| Dimensione | Teatro Narrativo | Neural Mapping | **EAR Triangulation v2** |
|---|---|---|---|
| **Architettura** | Monolitica, timeout issues | Centralizzata, single-point | **7-agent, mutual exclusion, clean pipeline** ✓✓ |
| **Bug critici** | Timeout/retry systemic | 5 (A1-A5) | **2** (A1-A2) |
| **Robustezza** | Fragile | 7 gap | **8 gap** (ma meno severe) |
| **Separation of concerns** | Debole | Media | **Eccellente** (Scriba/Director/Tribunal separati) |
| **Data integrity** | Nessuna | Nessuna | **Backup automatici** ✓ |
| **LLM independence** | Nessuna | Nessuna | **Tribunal meccanico** (no LLM bias) ✓✓ |
| **State management** | In-memory only | In-memory only | **Persistente** (JSON + backup) ✓ |
| **Extensibility** | Bassa | Media | **Alta** (multi-provider, config-driven) ✓ |
| **Voto** | 5/10 | 6/10 | **8.2/10** |

---

## E — PIANO FIX RACCOMANDATO

### Fase 1 — Critici (15 min)
| Fix | Tempo | File |
|---|---|---|
| A1: Rimuovi `temperature` kwarg | 2 min | `agents/director.py:254` |
| A4: Stats per-concept | 3 min | `orchestrator.py` |
| B4: Try/except per agent parse | 5 min | `orchestrator.py` |
| C3: Rimuovi SCRIBA_SYSTEM dead code | 1 min | `agents/prompts.py` |
| C7: Dedup batch | 2 min | `orchestrator.py` |
| A3: Backup microseconds | 1 min | `agents/scriba.py:81` |

### Fase 2 — Funzionalità (45 min)
| Fix | Tempo | File |
|---|---|---|
| A2: Dashboard v2 compatibility | 30 min | `dashboard.jsx` |
| B1: Retry logic con exponential backoff | 10 min | `orchestrator.py` |
| B2: Schema validation agent output | 5 min | `core/tribunal.py` |

### Fase 3 — Ottimizzazione (60 min)
| Fix | Tempo | File |
|---|---|---|
| C1: Parallel execution 4 mapper | 20 min | `orchestrator.py` |
| C2: Sigma normalization | 10 min | `core/tribunal.py` |
| B7: Director context summary dinamico | 10 min | `agents/director.py` |
| C4: Confidence calcolata | 10 min | `orchestrator.py`, `scriba.py` |
| C5: Review resolution workflow | 10 min | `run.py`, `director.py` |

**Totale: ~120 minuti per fix completo.**

---

## F — NOTE POSITIVE (cosa funziona bene)

1. **Tribunal meccanico** — Zero LLM bias nella validazione. Brillante.
2. **Mutual exclusion Scriba/Arbiter** — Impossibile inserire un concept non validato. Sicuro by design.
3. **Blind Spot Document** — Metadata epistemica strutturata. Ogni divergenza ha un peso basato su strength/weakness dell'agent. Questo è design di altissimo livello.
4. **Backup automatici** — Ogni modifica al network è preceduta da backup. Recovery garantito.
5. **Multi-provider** — DeepSeek, Claude, Ollama, OpenAI-compat. Switch con una riga di config.
6. **Director/Scriba separation** — Il Director non scrive mai il network. Solo Scriba scrive. Clean separation of concerns.
7. **AutonomousLoop** — Director → Engine → Director loop chiuso. Il sistema può auto-popolare il tesseratto con supervisione minima.
8. **CLI completa** — `map`, `batch`, `propose`, `auto`, `status`, `reviews`. Production-ready interface.

---

*Fine audit. 2 critici, 8 robustezza, 7 design. Piano fix 120 min totali.*
*Architettura best-in-class tra i tre progetti auditati.*
