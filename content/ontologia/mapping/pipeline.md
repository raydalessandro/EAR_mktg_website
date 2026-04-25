---
title: "Pipeline EAR Triangulation v2.0"
summary: Pipeline operativa di mapping con orchestrator, dashboard e runner CLI.
status: published
type: pipeline
version: "2.0"
order: 20
tags: [mapping, pipeline, ear-triangulation, orchestrator]
authors: [Alessio Marrone]
created: 2026-02-08
updated: 2026-04-25
license: CC-BY-SA-4.0
download:
  file: /downloads/ontologia/mapping/pipeline/ear_triangulation_v2.0.zip
  format: zip
related:
  - ontologia/mapping/regole
  - ontologia/mapping/sistema
  - tesseract/grafo
featured: false
---

## Cosa è

La **pipeline operativa** che esegue mapping di batch su batch. Riceve
file di sintesi (`batch_X_<domain>.json`), applica le regole di
[derivazione](/ontologia/mapping/regole), produce coordinate Σ_DAXP
con metadata di confidenza e oscillazione.

Pacchetto `.zip` con:

- `ear_triangulation/orchestrator.py` — orchestrazione fra mapper e validator
- `ear_triangulation/run.py` — entry point CLI
- `ear_triangulation/dashboard.jsx` — UI di review
- `ear_triangulation/config.json` — configurazione default

## Audit & status

Vedi [`EAR_TRIANGULATION_V2_AUDIT.md`](/downloads/ontologia/mapping/pipeline/EAR_TRIANGULATION_V2_AUDIT.md) per
l'audit dello stato corrente della pipeline (cambiamenti rispetto a v1,
test eseguiti, edge cases noti).

## Come usarla

```bash
unzip ear_triangulation_v2.0.zip
cd ear_triangulation
python run.py --batch batch_X_domain.json --output results/
```

L'output è un JSON `batch_X_domain_results.json` con coordinate +
metadata, pronto per l'archiviazione in [`/batches`](/ontologia/mapping/batches).

## Note

Versione **2.0** stabile. Compatibile con il sistema di sintesi
v2 (`SYNTHESIS_GUIDELINES.md` v2.0 con polarity hints).
