# Cobertura

Estado de cobertura de Cahíta Histórico Digital para `ALC1737` — 2026-08-16.

## Métricas vigentes

| Dimensión | Cobertura | Autoridad / nota |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digitales 15–132 ↔ impresas 1–118 |
| OCR paginado reproducible | **182 / 182** | derivado; no transcripción |
| Diagnóstico OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Transcripciones diplomáticas `full_page` | **128 páginas** | portada + preliminares textuales + todo el Arte impreso pp.1–118 |
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
| Sistema numeral histórico | **1 bloque estructurado** | digitales 178–180 |
| Observaciones de variación histórica | **17+** | nuevas observaciones numéricas pendientes de integración combinada |
| Candidatos lexicográficos v0.2 | **2,072 / 2,072 persistidos canónicamente** | inventario fila-a-fila reconstruible y verificable |
| Diagnóstico de fronteras | **4 páginas / 171 candidatos** | muestra intencional: precisión 0.9532, recobrado 0.8670, F1 0.9081; no probabilística |
| Artículos históricos estructurados | **734** | representación selectiva de digitales 133–177 |
| Páginas de vocabulario con al menos representación estructurada | **45 / 45** | cobertura selectiva inicial completa |
| Pilotos lexicográficos fuera de secuencia | **0** | p.165 reconciliado; p.134 es parte de la secuencia de cobertura |
| Lagunas/discontinuidades del testimonio registradas | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA de identificadores | **validador incorporado** | `scripts/validate_lexicon_ids.py`; ejecución CI aún no afirmada |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. La digital 132 / impresa 118 conserva `INTERJECCIONES`, la nota `No ſe hallan en los Artes, el vſo las dará` y `FIN DEL ARTE`.

Este hito significa cobertura de superficie textual, no edición crítica cerrada. Las lecturas `unresolved` permanecen visibles y ninguna página ha sido declarada `human_verified`.

## Vocabulario

El vocabulario ocupa digitales 133–177. El pipeline geométrico v0.2 produce **2,072 candidatos de frontera**. La capa curatorial contiene **734 artículos históricos estructurados** y todas las **45 páginas** poseen al menos una representación lexicográfica estructurada.

La cobertura por página es **selectiva**. No significa que 734 sea el número final de entradas históricas. La diferencia entre candidato geométrico y artículo histórico se conserva explícitamente.

### Inventario candidato canónico

El inventario fila-a-fila de los **2,072 candidatos** quedó fijado a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10` y al PDF con SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

El JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`. Para conservarlo mediante artefactos UTF-8 se almacena de forma **lossless** como gzip determinista → base64 → 12 partes ordenadas. `data/lexicon/candidates/candidate_inventory_manifest.json` registra los hashes por parte y los hashes de las representaciones JSONL/gzip/base64. `scripts/reconstruct_candidate_inventory.py` reconstruye el JSONL y verifica integridad, parseo y conteo de 2,072 filas.

El antiguo `data/lexicon/candidates/p134_candidates.jsonl` pertenece a `indentation_margin_v0.1`; se conserva únicamente como artefacto histórico/no canónico para comparación de algoritmos.

### QA diagnóstico de fronteras

`data/lexicon/review/stratified_boundary_evaluation.json` contiene una muestra intencional en pp.133, 134, 150 y 177: 171 candidatos, 188 inicios visibles, 163 verdaderos positivos, 8 falsos positivos y 25 falsos negativos. Las métricas agregadas son precisión **0.9532**, recobrado **0.8670** y F1 **0.9081**.

El diseño se declara `purposive_stratified_diagnostic`, no probabilístico. Estas cifras sirven para diagnóstico del algoritmo y no deben presentarse como estimadores con validez inferencial para todo el vocabulario.

### Apertura retroprocesada

Se añadieron lotes para p.133 y pp.135–137, además de un artículo trans-página 133–134. La frontera documenta:

`Ablandar lo que eſtá duro / como barro. Namacae-buaruna.`

El artículo se representa con `sourceSpans`; el salto físico no genera dos entradas.

### Continuidades, catchwords y anomalías

La arquitectura separa artículos, reclamos y lagunas. Las continuidades normales están documentadas a lo largo del vocabulario. Permanecen abiertas:

- la discontinuidad F→H p.157→158 (`ALC1737-gap-0001`);
- el reclamo `Lucer-` p.161 → p.162 sin lema visible correspondiente.

Ninguna se rellena desde conocimiento externo.

## Sistema numeral — digitales 178–180

La capa numeral incluye esquema, dataset y documentación para cardinales 1–10 de alta confianza, numerales de orden descritos por la fuente, distributivos y adverbios numerales. Las observaciones explícitas sobre `Naciones` y `Hiaqui/Hiaquis` permanecen como descripción histórica y deben integrarse todavía a la capa combinada de variación.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica de la regla 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- posible ausencia visible de 294;
- discontinuidad del vocabulario F→H entre digitales 157 y 158;
- reclamo `Lucer-` en p.161 sin lema visible al comienzo de p.162.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana ni completa lagunas sin una capa de procedencia separada.

## Siguiente frente

La precondición de inventario está satisfecha. La prioridad es ahora la **reconciliación exhaustiva de los 2,072 candidatos**: cada candidato deberá clasificarse como artículo histórico, paratexto, continuación física, falso positivo o `unresolved`, con calidad de frontera y trazabilidad separadas. El primer lote de reconciliación cubre pp.133–134.
