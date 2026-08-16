# Cobertura

Estado canónico de cobertura de Cahíta Histórico Digital para `ALC1737` — 2026-08-16.

## Métricas vigentes

| Dimensión | Cobertura | Autoridad / nota |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digitales 15–132 ↔ impresas 1–118 |
| OCR paginado reproducible | **182 / 182** | derivado; no transcripción |
| Diagnóstico OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Transcripciones diplomáticas `full_page` | **128 páginas** | preliminares textuales + Arte completo hasta digital 132 |
| Partes I–IV del Arte | **completas en capa IA-asistida** | fronteras intra-página 69 y 105 preservadas |
| Paradigmas históricos | **3** | estructurados |
| Construcciones modales | **9** | reglas 207–234 |
| Construcciones no finitas | **5** | reglas 237–256 |
| Construcciones participiales | **3** | reglas 257–265 |
| Construcciones predicativas/modales | **6** | reglas 266–284 |
| Verbos irregulares | **6 grupos** | reglas 286–291 |
| Preposiciones/grupos | **43** | reglas 293–340 |
| Grupos de adverbios | **11** | reglas 341–359 |
| Grupos de conjunciones/metacategorías | **6** | reglas 360–373 + interjecciones |
| Sistema numeral histórico | **1 bloque estructurado** | digitales 178–180 |
| Observaciones de variación histórica | **17+** | exportación combinada aún pendiente de consolidación |
| Candidatos lexicográficos v0.2 | **2,072 / 2,072 persistidos canónicamente** | inventario fila-a-fila reconstruible y verificable |
| Artículos históricos estructurados | **734** | capa curatorial actual; no conteo final del vocabulario |
| Páginas de vocabulario con representación estructurada | **45 / 45** | cobertura selectiva por página completa |
| Reconciliación candidata pp.133–134 | **61 / 61** | 57 article; 3 continuation; 1 unresolved |
| Inicios visibles omitidos observados pp.133–134 | **14** | capa separada de falsos negativos; conjunto aún no declarado exhaustivo |
| Artículos pendientes de promoción pp.133–134 | **36** | frontera confirmada; objeto curatorial aún pendiente |
| Lagunas/discontinuidades del testimonio registradas | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA de identificadores | **validador incorporado** | `scripts/validate_lexicon_ids.py`; CI aún pendiente |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. La digital 132 / impresa 118 conserva `INTERJECCIONES`, la nota `No ſe hallan en los Artes, el vſo las dará` y `FIN DEL ARTE`.

Las digitales 69 y 105 son páginas mixtas: en 69 cierra Parte II y comienza Parte III; en 105 cierra Parte III y comienza Parte IV. Ambas fronteras se conservan estructuralmente.

Este hito significa **cobertura de superficie textual**, no edición crítica cerrada. Las lecturas `unresolved` permanecen visibles y ninguna página ha sido declarada `human_verified`.

## Vocabulario

El vocabulario ocupa digitales 133–177. El pipeline geométrico vigente `hybrid_margin_mode_v0.2` produce **2,072 candidatos de frontera**. La capa curatorial contiene **734 artículos históricos estructurados** y todas las **45 páginas** poseen al menos una representación lexicográfica estructurada.

La diferencia entre candidato computacional, frontera editorial e artículo histórico se conserva explícitamente. **2,072 no es el número de entradas históricas y 734 tampoco es todavía el número final del vocabulario.**

### Inventario candidato canónico

El inventario fila-a-fila de los **2,072 candidatos** quedó fijado a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10` y al PDF con SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

El JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`. Se conserva de forma lossless como gzip determinista → base64 → 12 partes ordenadas. `data/lexicon/candidates/candidate_inventory_manifest.json` registra hashes y tamaños; `scripts/reconstruct_candidate_inventory.py` reconstruye y verifica integridad, parseo y conteo.

El antiguo `data/lexicon/candidates/p134_candidates.jsonl` corresponde a `indentation_margin_v0.1` y se conserva únicamente como artefacto histórico/no canónico.

### QA de fronteras: distinguir v0.1 y v0.2

La comparación documentada en `data/lexicon/review/boundary_algorithm_comparison.json` utiliza las mismas páginas intencionales 133, 134, 150 y 177.

| Método | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| `indentation_margin_v0.1` | 163 | 8 | 25 | 95.32% | 86.70% | 90.81% |
| `hybrid_margin_mode_v0.2` | 169 | 5 | 19 | **97.13%** | **89.89%** | **93.37%** |

Estas métricas son **diagnósticas y no probabilísticas**. Sus referencias de frontera proceden de cotejo visual IA-asistido sin validación humana independiente. Por tanto describen comportamiento de ingeniería editorial sobre la muestra, no desempeño filológico poblacional.

### Reconciliación pp.133–134

Las primeras dos páginas del vocabulario funcionan como tramo de control. `data/lexicon/reconciliation/p133_p134_reconciliation_status.json` registra:

- 61/61 candidatos canónicos reconciliados;
- 57 `article`;
- 3 `continuation`;
- 1 `unresolved` (`ALC1737-vcand-p133-L-002`);
- calidad geométrica: 52 `exact`, 5 `merged_articles`, 2 `oversegmented`, 1 `undersegmented`, 1 `ambiguous`;
- 21 candidatos `article` enlazados a 28 artículos históricos existentes;
- 36 candidatos `article` con `articleLinkStatus: pending_promotion`.

Además se registraron **14 inicios visibles omitidos observados** en una capa específica. Esto demuestra que completar la reconciliación de candidatos no equivale a capturar todos los inicios visibles.

### Continuidades, catchwords y anomalías

La arquitectura separa artículos, reclamos y lagunas. Permanecen abiertas:

- `ALC1737-gap-0001`: discontinuidad F→H entre digitales 157–158;
- p.161 `Lucer-` → p.162 sin lema visible correspondiente.

Ninguna se completa mediante conocimiento externo.

## Sistema numeral — digitales 178–180

La capa numeral incluye esquema, dataset y documentación para cardinales de alta confianza, numerales de orden descritos por la fuente, distributivos y adverbios numerales. Las observaciones explícitas sobre `Naciones` y `Hiaqui/Hiaquis` deben integrarse todavía a la capa combinada de variación histórica.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica de la regla 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- posible ausencia visible de 294;
- discontinuidad F→H entre digitales 157–158;
- reclamo `Lucer-` en p.161 sin lema visible al comienzo de p.162.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana ni rellena lagunas sin una capa de procedencia separada.

## Próximos criterios de cobertura

Antes de productos científicos finales, la cobertura deberá avanzar en cuatro frentes:

1. promover los 36 artículos pendientes y cerrar el inventario visible de pp.133–134;
2. escalar reconciliación candidata y falsos negativos a pp.135–177;
3. consolidar concordancias y exportaciones gramaticales/variacionales;
4. incorporar QA automático y revisión humana suficiente para el alcance de la futura release.
