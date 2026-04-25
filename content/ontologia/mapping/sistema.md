---
title: "Sistema knowledge_mapping"
summary: "Codice del sistema di mapping — mapper, synthesizer, scripts, docs. ZIP del repo working."
status: published
type: tool
version: "2.2"
order: 40
tags: [mapping, sistema, codice, python]
authors: [nodo432]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/mapping/system/knowledge_mapping_system.zip
  format: zip
related:
  - ontologia/mapping/regole
  - ontologia/mapping/pipeline
  - ontologia/mapping/diagnostica
featured: false
---

## Cosa è

Lo **snapshot del repo working** del sistema di mapping. ZIP che
contiene mapper, synthesizer, scripts CLI, docs (synthesis guidelines,
review notes, revised mappings) e diagnostics.

## Cosa c'è dentro

```
knowledge_mapping/
├── mapper/                    # protocol.py v2.2 (deriva D, A, X, P)
├── concept_synthesizer/       # protocol.py + auto_synthesis.py + LLM-backed v3
├── scripts/                   # batch_map.py + map_concepts.py + test_*.py
├── diagnostics/               # network_diagnostics.py (rigenera report)
├── docs/                      # SYNTHESIS_GUIDELINES, new_syntheses_for_opus_review,
│                              # REVISED_MAPPINGS
├── batches/                   # input synthesis JSONs (vedi /batches per la versione canonical)
├── results/                   # output coordinate JSONs (idem)
└── README.md                  # overview del sistema
```

> **Nota:** i file di batch e i risultati canonici sono indicizzati
> singolarmente in [`/batches`](/ontologia/mapping/batches). Lo zip qui
> è il sistema completo (codice + docs).

## Come usarlo

```bash
unzip knowledge_mapping_system.zip
cd knowledge_mapping
pip install -r requirements.txt
python scripts/map_concepts.py batch_X_domain.json
```

Necessita Python 3.10+ e qualche dipendenza standard (vedi `requirements.txt` dentro lo zip).

## Note

**Versione 2.2** del mapper (legge polarity hints come da SYNTHESIS_GUIDELINES v2.0).
Questo è uno snapshot tematico — la versione "live" del codice
potrebbe migrare a un repo dedicato se cresce molto.
