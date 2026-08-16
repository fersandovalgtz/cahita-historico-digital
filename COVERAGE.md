# Cobertura

Estado de cobertura de Cahíta Histórico Digital para `ALC1737` — 2026-08-15.

## Métricas vigentes

| Dimensión | Cobertura | Autoridad / nota |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digitales 15–132 ↔ impresas 1–118 |
| OCR paginado reproducible | **182 / 182** | derivado; no transcripción |
| Diagnóstico OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Transcripciones diplomáticas `full_page` | **128 páginas** | portada + preliminares textuales + todo el Arte impreso pp. 1–118 |
| Partes I–IV del Arte | **completas en capa IA-asistida** | incluye fronteras intra-página 69 y 105 |
| Paradigmas históricos | **3** | estructurados |
| Construcciones modales | **9** | reglas 207–234 |
| Construcciones no finitas | **5** | reglas 237–256 |
| Construcciones participiales | **3** | reglas 257–265 |
| Construcciones predicativas/modales | **6** | reglas 266–284 |
| Verbos irregulares | **6 grupos** | reglas 286–291 |
| Preposiciones/grupos | **43** | reglas 293–340 |
| Grupos de adverbios | **11** | reglas 341–359 |
| Grupos de conjunciones/metacategorías | **6** | reglas 360–373 + interjecciones |
| Observaciones de variación histórica | **17 entidades** | fuente histórica; no taxonomía moderna |
| Candidatos lexicográficos v0.2 | **2,072** | 45 páginas; no equivalen a artículos publicados |
| Artículos históricos estructurados | **538** | p.134 + secuencia curatorial pp.138–168 |
| Pilotos lexicográficos fuera de secuencia | **0** | p.165 reconciliado e integrado |
| Ciclos recíprocos de remisión modelados | **1+** | incluye `Demonio ↔ Diablo`; nuevas reciprocidades ofender/ofensa/pecar |
| Lagunas/discontinuidades del testimonio registradas | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA de identificadores | **validador incorporado** | `scripts/validate_lexicon_ids.py` |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. La digital 132 / impresa 118 conserva `INTERJECCIONES`, la nota `No ſe hallan en los Artes, el vſo las dará` y `FIN DEL ARTE`.

Este hito significa cobertura de superficie textual, no edición crítica cerrada. Las lecturas `unresolved` permanecen visibles y ninguna página ha sido declarada `human_verified`.

## Fronteras materiales del Arte

Se han comprobado dos páginas `mixed`:

- digital 69 / impresa 55: cierre de Parte II e inicio de Parte III;
- digital 105 / impresa 91: cierre de Parte III e inicio de `IV. ULT. PARTE`.

Estas fronteras se conservan en `data/source/alc1737/sections.json` y en las unidades de página.

## Capas gramaticales derivadas

CHD conserva datasets estructurados para paradigmas, tiempos modales, construcciones no finitas, participios, predicación/modalidad, verbos irregulares, preposiciones, adverbios y conjunciones. Las categorías históricas del gramático se mantienen separadas de cualquier análisis lingüístico moderno.

## Vocabulario: estado de producción

El vocabulario ocupa digitales 133–177. El pipeline geométrico v0.2 produce **2,072 candidatos de frontera**, mientras la secuencia curatorial principal contiene **538 artículos históricos efectivamente estructurados** en p.134 y pp.138–168.

El modelo representa equivalencias, remisiones `Buſca`, anáforas `Lo miſmo`, agrupaciones históricas, artículos descriptivos, continuidad entre páginas/columnas, catchwords como paratexto, relaciones recíprocas de remisión y lagunas/anomalías documentales explícitas.

### Lotes pp.165–168

Se añadieron cuatro lotes de 15 artículos cada uno:

- `p165_selected_articles.jsonl`;
- `p166_selected_articles.jsonl`;
- `p167_selected_articles.jsonl`;
- `p168_selected_articles.jsonl`.

Total nuevo: **60 artículos**. Entre las nuevas relaciones aparecen `Ofender → pecar`, `Ofenſa → pecado`, `Ofenſor → pecador`, `Orejear → menear las orejas`, `Orina → meados`, `Orinar → mear`, `Oſado ſer → atrevido`, `Palo para eſcarbar tierra → coa`, `Pecado → ofenſa`, `Pecador → ofenſor` y `Pecar → ofender`.

### Reconciliación de identificadores en p.165

El antiguo `p165_cross_reference_pilot.jsonl` utilizaba `ALC1737-art-000013`–`000016`, identificadores ya usados por la secuencia principal de p.138. Los cuatro objetos documentales se conservaron, se reasignaron a `000490`–`000493` y se integraron en `p165_selected_articles.jsonl`; el piloto duplicado fue eliminado.

La migración queda documentada en `data/lexicon/provenance/p165_pilot_id_reconciliation.json`. Para evitar regresiones se añadió `scripts/validate_lexicon_ids.py`, que comprueba parseo JSONL, unicidad global de `articleId` y coherencia de estados de revisión.

### Catchwords y QA de frontera

`data/lexicon/boundary_markers/` registra ahora:

- p.164 `Obr-` → `Obra aſſi, hechura. Chupari.` p.165;
- p.165 `Paga-` → `Paga tal. Bebeti.` p.166;
- p.166 `Paſſo` → `Paſſo de las beſtias. Arabuerama.` p.167;
- p.167 `Pena-` → `Penacho` p.168;
- p.168 `Pie-` → pendiente de cotejo en p.169.

La anomalía anterior `Lucer-` p.161 → p.162 sigue abierta y no se reconstruye por conjetura.

### Discontinuidad digital 157→158

La p.157 termina con voces de F, incluida `Flecha. Huihua.`, y muestra un reclamo inferior que comienza `Fle...`. La digital 158 comienza directamente con voces de H. La incidencia está registrada como `ALC1737-gap-0001`; CHD no determina todavía el número de páginas/folios faltantes ni reconstruye el material ausente sin otro testimonio documentado.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica de la regla 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- posible ausencia visible de 294;
- discontinuidad del vocabulario F→H entre digitales 157 y 158;
- reclamo `Lucer-` en p.161 sin lema visible al comienzo de p.162;
- reclamo `Pie-` de p.168 pendiente de comprobación en p.169.

La colisión de identificadores del piloto p.165 **ya está resuelta** y no se considera una incidencia abierta.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana ni completa lagunas desde conocimiento externo sin una capa de procedencia separada.

## Siguiente frente

Continuar desde **digital 169**, resolver el reclamo `Pie-` y mantener sincronización GitHub ↔ Notion por lote sustantivo.
