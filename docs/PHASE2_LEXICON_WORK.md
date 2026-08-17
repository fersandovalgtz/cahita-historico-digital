# Fase II — promoción, enlace y censo visible

Línea base computacional derivada de los estados `pNNN_machine_reconciliation_status.json` para p.145–177.

- Páginas cubiertas: **33**.
- Candidatos `pending_promotion`: **1051**.
- Candidatos estructuralmente `unresolved`: **1**.
- Páginas con censo visible exhaustivo: **0**.
- Corpus curatorial observado: **1,045 artículos**.

## Excepción estructural conservada

La única página con candidato estructural `unresolved` es **p.161**, donde R-016 permanece deliberadamente abierto por evidencia terminal no única. No debe forzarse su clasificación para producir un cero artificial.

## Priorización por volumen de promoción pendiente

| Página | `pending_promotion` |
|---:|---:|
| 177 | 42 |
| 149 | 41 |
| 154 | 41 |
| 172 | 41 |
| 150 | 40 |
| 167 | 40 |
| 156 | 38 |
| 165 | 38 |
| 152 | 37 |
| 147 | 36 |

## Regla de trabajo

La fase II separa tres operaciones: **promoción/enlace de artículos**, **registro de falsos negativos visibles** y **censo exhaustivo**. Un candidato no se promueve sólo porque el OCR sugiera una lectura: para texto cahíta incierto se exige evidencia del testigo ALC1737 suficientemente fuerte, y BUE1890 permanece como control secundario sin sustitución silenciosa.

El archivo `phase2_open_work_summary.json` es la fuente computacional de esta página y puede regenerarse con `python scripts/summarize_open_lexicon_work.py --output data/lexicon/reconciliation/phase2_open_work_summary.json`.
