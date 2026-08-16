# Protocolo de reconciliación de candidatos lexicográficos

## Propósito

La fase de reconciliación no vuelve a extraer el vocabulario ni identifica automáticamente cada candidato geométrico con una entrada. Su objetivo es relacionar, con procedencia explícita, la capa de candidatos producida por `scripts/extract_vocab_candidates.py` con la capa curatorial de artículos históricos.

La unidad de revisión es el **candidato de frontera**, no el lema moderno.

## Precondición de reproducibilidad — satisfecha

El inventario canónico de `hybrid_margin_mode_v0.2` contiene **2,072 candidatos** para las 45 páginas digitales 133–177 y está persistido de manera fila-a-fila, lossless, reconstruible y verificable.

La generación quedó fijada a:

- revisión `f175b4bc455ff40a066d092a94e0a89a0ca2ae10`;
- `extract_vocab_candidates.py` blob `0ac729164895b0b4afd462350892426aca6e5f3d`;
- `extract_vocab_layout.py` blob `e0bee9ddaad0c114405f13d456cc2a00317d7107`;
- PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`;
- JSONL canónico SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

El JSONL se conserva mediante una transformación reversible `JSONL → gzip determinista → base64 → 12 partes UTF-8`. `data/lexicon/candidates/candidate_inventory_manifest.json` registra hashes por parte y hashes agregados; `scripts/reconstruct_candidate_inventory.py` verifica integridad, conteo y parseo antes de reconstruir el JSONL.

`data/lexicon/candidates/inventory_status.json` marca `reconciliationPrecondition: satisfied` y `exhaustiveReconciliationAllowed: true`.

El antiguo `p134_candidates.jsonl` pertenece a `indentation_margin_v0.1` y es **legacy/no canónico**.

## Clasificación editorial

Cada candidato deberá recibir exactamente una clasificación primaria conforme a `schemas/lexicon-candidate-review.schema.json`:

- `article`: la frontera corresponde a uno o más artículos históricos reales;
- `paratext`: el candidato corresponde a reclamo, encabezado, número de página, rótulo u otro elemento no léxico;
- `continuation`: el candidato empieza dentro de un artículo que comenzó previamente o representa una continuidad física;
- `false_positive`: la frontera propuesta no corresponde a una unidad material relevante;
- `unresolved`: la evidencia disponible no permite una decisión responsable.

La clasificación se mantiene separada de `boundaryAssessment`, que describe la calidad geométrica de la frontera: `exact`, `oversegmented`, `undersegmented`, `merged_articles`, `ambiguous` o `not_applicable`.

## Enlace con artículos históricos

Un candidato clasificado como `article` debe enlazarse a uno o más `ALC1737-art-XXXXXX`. La relación puede ser muchos-a-uno o uno-a-muchos porque el OCR/layout puede:

- fragmentar un artículo histórico;
- fusionar varios artículos en un solo candidato;
- cortar un artículo entre columnas o páginas.

Por ello no se presupone una correspondencia 1:1. Si el facsímil muestra un artículo real que todavía no tiene objeto curatorial, primero debe promoverse o registrarse explícitamente como pendiente; no se fabricará un enlace inexistente.

## Paratexto y materialidad

Los reclamos tipográficos ya documentados en `data/lexicon/boundary_markers/` son evidencia de que una línea visible puede no ser un artículo. Las continuidades trans-página y trans-columna representadas mediante `sourceSpans` deben utilizarse para distinguir `continuation` de `false_positive`.

Las lagunas del testimonio, especialmente `ALC1737-gap-0001`, y la anomalía `Lucer-` 161→162 no deben resolverse por conocimiento externo durante esta clasificación.

## Lotes de reconciliación

La reconciliación se versionará por lotes pequeños y auditables. Cada lote deberá indicar:

1. páginas y candidatos cubiertos;
2. inventario canónico de procedencia;
3. artículos históricos enlazados;
4. conteos por clasificación y calidad de frontera;
5. decisiones `unresolved` y falsos negativos observados;
6. estado de revisión humana.

El primer tramo de control es pp.133–134. Se permite comenzar con un subconjunto de alta confianza, siempre que la cobertura del lote se declare explícitamente y no se confunda con reconciliación completa de las páginas.

## QA y muestreo

`data/lexicon/review/stratified_boundary_evaluation.json` ya contiene un diagnóstico intencional sobre pp.133, 134, 150 y 177. En esa muestra se registran 171 candidatos frente a 188 inicios visibles, con 163 verdaderos positivos, 8 falsos positivos y 25 falsos negativos. Sus métricas agregadas son precisión 0.9532, recobrado 0.8670 y F1 0.9081.

Estas cifras son **diagnósticas, no inferenciales**: el propio diseño se declara `purposive_stratified_diagnostic`, no probabilístico. No deben presentarse con intervalos de confianza ni extrapolarse como desempeño exacto sobre las 45 páginas.

La siguiente evaluación deberá aumentar el tamaño muestral y estratificar al menos por inicio/medio/final del vocabulario, densidad de artículos, presencia de `Buſca` y `Lo miſmo`, continuidad de página/columna, proximidad a lagunas/anomalías y calidad OCR.

## Autoridad

Una clasificación IA-asistida permanece `machine_corrected_unverified` o `unresolved`. `human_verified` exige una persona revisora identificable y cotejo contra el facsímil. La reconciliación exhaustiva podrá completarse técnicamente antes de que exista revisión humana independiente, pero ambos estados deben permanecer claramente diferenciados.

## Productos de esta fase

La fase se considerará técnicamente completa cuando existan:

1. inventario canónico reproducible de candidatos — **completado**;
2. un registro de reconciliación por cada candidato persistido;
3. métricas agregadas por clase y página;
4. lista de candidatos/artículos `unresolved`;
5. exportación canónica de artículos sin duplicados;
6. informe de QA que distinga métricas automáticas, revisión editorial IA-asistida y revisión humana.
