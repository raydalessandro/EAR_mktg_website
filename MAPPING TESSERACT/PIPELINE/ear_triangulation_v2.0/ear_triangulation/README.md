# EAR Triangulation Engine v2.0

**7-agent architecture for mapping concepts to EAR's 72-cell tesseract.**

## Architecture

```
DIRECTOR (all docs + network state)
    │ proposes concept + domain
    ▼
┌───────┬───────┬───────┬───────┐
│ SYNTH │ Ag-Δ  │ Ag-⇄  │ Ag-⟳  │  ← 4 parallel mappers, blind to each other
│(all   │(Rules │(Kernel│(Arche)│
│docs)  │only)  │only)  │only)  │
│ REF   │       │       │       │
└───┬───┴───┬───┴───┬───┴───┬───┘
    │       │       │       │
    ▼       ▼       ▼       ▼
  REF      r-Δ     r-⇄     r-⟳
    │       │       │       │
    └───────┴───────┴───────┘
            ▼
TRIBUNAL: r-Δ==REF? r-⇄==REF? r-⟳==REF?  (mechanical, no LLM)
    │
    ├── 3/3 match ──→ SCRIBA (insert into network + backup)
    │
    └── <3/3 ───────→ ARBITER (blind spot analysis → review list)
    │
    (mutual exclusion: only one runs per concept)
    ▼
DIRECTOR ← receives outcome, proposes next concept
```

## 7 Agents

| # | Agent | Sees | Role |
|---|-------|------|------|
| 1 | **Director** | All docs + network state | Proposes concepts, handles outcomes |
| 2 | **Synth** | All 3 docs | Reference benchmark mapper |
| 3 | **Ag-Δ** | Rules v1.2 only | Maps from procedure (§8 protocol) |
| 4 | **Ag-⇄** | Nano Kernel only | Maps from axioms/constraints |
| 5 | **Ag-⟳** | Archetypes only | Maps from pattern/resonance |
| 6 | **Scriba** | Network only | Writes valid nodes + backups |
| 7 | **Arbiter** | 4 outputs + blind spots | Analyzes divergences |

## Key Principle

**Synth = Reference.** Three monodoc agents independently arrive at coordinates. 
If all 3 match Synth → validated (Scriba inserts). If any diverge → Arbiter 
analyzes whether divergence is on agent's blind spot (Synth likely right) or 
strength (serious signal, needs review).

## Usage

```bash
# Setup
cp config.json.example config.json
# Edit config.json with your LLM provider + API key
# Place EAR documents in data/

# Map one concept
python run.py map "Schwarzschild Metric" --domain physics

# Map batch from file (one concept per line)
python run.py batch concepts.txt --domain physics

# Director proposes next batch
python run.py propose --domain biology

# Autonomous loop (Director → Engine → Director)
python run.py auto 5 --domain physics

# Status
python run.py status

# Review pending Arbiter outputs
python run.py reviews
```

## Configuration

```json
{
  "llm": {
    "provider": "deepseek",          // deepseek | claude | ollama | openai
    "api_key": "YOUR_KEY",
    "model": "deepseek-chat"
  },
  "documents": {
    "rules": "data/EAR_MAPPING_RULES_v1.2.md",
    "kernel": "data/EAR_NANO_KERNEL_AILA_v1_0.md",
    "archetypes": "data/EAR_ARCHETYPES_72.md"
  }
}
```

Supported providers: DeepSeek, Claude, Ollama (local), OpenAI-compatible.

## Files

```
ear_triangulation/
├── run.py                    # CLI entry point
├── config.json               # LLM + document paths
├── orchestrator.py           # Main pipeline (4 parallel → tribunal → route)
├── core/
│   ├── llm_adapter.py        # Multi-provider LLM client
│   ├── tribunal.py           # Mechanical 3-vs-reference comparator
│   └── streamer.py           # WebSocket event streamer
├── agents/
│   ├── prompts.py            # All agent system prompts + blind spot doc
│   ├── director.py           # Director + NetworkState + AutonomousLoop
│   └── scriba.py             # Network writer with backup
├── data/
│   ├── EAR_ARCHETYPES_72.md  # 72-cell archetype template
│   ├── network_state.json    # Living network (Scriba writes)
│   └── backups/              # Scriba backups before each modification
├── results/                  # Per-concept JSON results
│   └── review/               # Arbiter review files
├── dashboard.jsx             # React visualization (optional)
└── templates/                # Archetype template
```

## v1.0 → v2.0 Changes

- **Synth** promoted from pre-processor to parallel reference benchmark
- **Tribunal** rewritten: 3-monodoc-vs-Synth (was 4-way vote)
- **Scriba** added: dedicated network writer with automatic backups
- **Arbiter** rewritten: blind spot analysis with strength/weakness classification
- **Mutual exclusion**: Scriba XOR Arbiter per concept
- **Director's NetworkState**: reads Scriba's format, separate director_state.json
- **No more REJECT**: concepts are either VALID (3/3) or REVIEW (divergence)
