# Protocolo de reconciliación de candidatos lexicográficos

## Propósito

La fase de reconciliación no vuelve a extraer el vocabulario ni identifica automáticamente cada candidato geométrico con una entrada. Su objetivo es relacionar, con procedencia explícita, la capa de candidatos producida por `scripts/extract_vocab_candidates.py` con la capa curatorial de artículos históricos.

La unidad de revisión es el **candidato de frontera**, no el lema moderno.

## Precondición de reproducibilidad

El extractor `hybrid_margin_mode_v0.2` reporta **2,072 candidatos** para las 45 páginas digitales 133–177. Sin embargo, el árbol versionado actual contiene como inventario candidato explícito únicamente `data/lexicon/candidates/p134_candidates.jsonl`. Por ello CHD **no afirma todavía que las 2,072 filas candidatas estén persistidas canónicamente en el repositorio**.

Antes de declarar una reconciliación exhaustiva se deberá:

1. ejecutar reproduciblemente `scripts/extract_vocab_candidates.py` contra el testimonio fijado de `ALC1737`;
2. obtener exactamente el conteo esperado o documentar cualquier divergencia de versión/entorno;
3. persistir una exportación canónica de candidatos, preferentemente por página o mediante un manifiesto verificable;
4. registrar hash, versión del extractor, versión del PDF y fecha/entorno de generación.

Hasta completar estos pasos, `2,072` es una **métrica de ejecución documentada**, no la prueba de que exista un inventario fila-a-fila completo bajo control de versiones.

## Clasificación editorial

Cada candidato persistido deberá recibir exactamente una clasificación primaria conforme a `schemas/lexicon-candidate-review.schema.json`:

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

Por ello no se presupone una correspondencia 1:1.

## Paratexto y materialidad

Los reclamos tipográficos ya documentados en `data/lexicon/boundary_markers/` son evidencia de que una línea visible puede no ser un artículo. Las continuidades trans-página y trans-columna representadas mediante `sourceSpans` deben utilizarse para distinguir `continuation` de `false_positive`.

Las lagunas del testimonio, especialmente `ALC1737-gap-0001`, y la anomalía `Lucer-` 161→162 no deben resolverse por conocimiento externo durante esta clasificación.

## QA y muestreo

`data/lexicon/review/stratified_boundary_evaluation.json` ya contiene un diagnóstico intencional sobre pp.133, 134, 150 y 177. En esa muestra se registran 171 candidatos frente a 188 inicios visibles, con 163 verdaderos positivos, 8 falsos positivos y 25 falsos negativos. Sus métricas agregadas son precisión 0.9532, recobrado 0.8670 y F1 0.9081.

Estas cifras son **diagnósticas, no inferenciales**: el propio diseño se declara `purposive_stratified_diagnostic`, no probabilístico. No deben presentarse con intervalos de confianza ni extrapolarse como desempeño exacto sobre las 45 páginas.

La siguiente evaluación deberá aumentar el tamaño muestral y estratificar al menos por:

- inicio/medio/final del vocabulario;
- densidad de artículos;
- presencia de `Buſca` y `Lo miſmo`;
- continuidad de página/columna;
- páginas próximas a lagunas o anomalías;
- calidad OCR alta/media/baja.

## Autoridad

Una clasificación IA-asistida permanece `machine_corrected_unverified` o `unresolved`. `human_verified` exige una persona revisora identificable y cotejo contra el facsímil. La reconciliación exhaustiva podrá completarse técnicamente antes de que exista revisión humana independiente, pero ambos estados deben permanecer claramente diferenciados.

## Productos de esta fase

La fase se considerará técnicamente completa cuando existan:

1. inventario canónico reproducible de candidatos;
2. un registro de reconciliación por cada candidato persistido;
3. métricas agregadas por clase y página;
4. lista de candidatos/artículos `unresolved`;
5. exportación canónica de artículos sin duplicados;
6. informe de QA que distinga métricas automáticas, revisión editorial IA-asistida y revisión humana.
