# Verifica sul Connettoma C. elegans

## Dataset
- Fonte: Varshney et al., WormAtlas
- Neuroni: 281
- Connessioni: 2291

## Predizione Teorica
I neuroni modulatori (A=2) hanno firma ponte:
- Grado > media
- Betweenness > media
- Clustering < media

## Risultati

### Metriche per tipo

|              | Media Globale | Modulatori | Delta |
|--------------|---------------|------------|-------|
| Grado        | 16.31         | 20.56      | +26%  |
| Betweenness  | 0.00507       | 0.00642    | +27%  |
| Clustering   | 0.3347        | 0.2482     | -26%  |

**Tutte e tre le metriche vanno nella direzione predetta.**

### Sovra-rappresentazione

- Modulatori = 5.7% dei neuroni totali
- Modulatori = 15.5% dei neuroni "ponte"
- **Sovra-rappresentazione: 2.73x**

### Test Statistici

| Test | Valore | p-value | Significativo? |
|------|--------|---------|----------------|
| Grado (t-test) | t=1.40 | p=0.163 | No |
| Clustering (t-test) | t=-1.96 | p=0.051 | Borderline |
| Betweenness (t-test) | t=0.48 | p=0.629 | No |
| **Sovra-rappresentazione (χ²)** | χ²=10.93 | **p=0.0009** | **SÌ** |

## Conclusione

La predizione principale è **statisticamente significativa** (p < 0.001):
I modulatori sono 2.73x più probabili di essere ponti strutturali.

I test individuali non raggiungono significatività a causa del campione piccolo (n=16 modulatori), ma la direzione è corretta in tutti e tre.

## Implicazione

La struttura teorica predice correttamente che i neuroni neuromodulatori (dopaminergici, serotoninergici, etc.) occupano posizioni di "ponte" nel connettoma.

Questo è coerente con il loro ruolo biologico: modulare e connettere diversi sistemi neurali.
