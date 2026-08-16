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

## Política de verificación vigente — sin intervención humana

El flujo editorial vigente de Cahíta Histórico Digital **no contempla una capa posterior de verificación humana independiente**. En consecuencia, `humanVerified` permanecerá en `false` para los objetos producidos bajo esta política y no se utilizará `human_verified` como estado operativo de cierre.

El valor `human_verified` se conserva en el esquema únicamente como estado reservado para compatibilidad y para una eventual modificación futura de la política; no constituye un hito esperado ni una condición pendiente del proyecto actual.

Una página puede alcanzar **cierre técnico o estructural IA-asistido** cuando se cumplan conjuntamente estas condiciones: todos sus candidatos canónicos están clasificados; los inicios visibles pueden censarse con la evidencia de máquina disponible; los enlaces y promociones están resueltos o sus incertidumbres se registran explícitamente; las continuidades físicas están modeladas; no se fabrican lecturas para eliminar huecos; y el QA computacional correspondiente resulta satisfactorio.

Ese cierre técnico **no equivale a autoridad diplomática o filológica humana**. Una lectura puede permanecer `unresolved`, de baja confianza o `[ileg.]` dentro de una página técnicamente cerrada si la incertidumbre está localizada, documentada y no altera la frontera estructural. Cuando la evidencia de máquina tampoco permite resolver la estructura, la página permanece abierta o parcialmente reconciliada.

## Clasificación editorial

Cada candidato deberá recibir exactamente una clasificación primaria conforme a `schemas/lexicon-candidate-review.schema.json`:

- `article`: la frontera corresponde a uno o más artículos históricos reales;
- `paratext`: el candidato corresponde a reclamo, encabezado, número de página, rótulo u otro elemento no léxico;
- `continuation`: el candidato empieza dentro de un artículo que comenzó previamente o representa una continuidad física;
- `false_positive`: la frontera propuesta no corresponde a una unidad material relevante;
- `unresolved`: la evidencia disponible no permite una decisión responsable.

La clasificación se mantiene separada de `boundaryAssessment`, que describe la calidad geométrica de la frontera: `exact`, `oversegmented`, `undersegmented`, `merged_articles`, `ambiguous` o `not_applicable`.

## Enlace con artículos históricos

La clasificación de una frontera y el estado de promoción del artículo son dimensiones distintas. Un candidato clasificado como `article` puede tener:

- `articleLinkStatus: linked`: ya existe al menos un objeto `ALC1737-art-XXXXXX` enlazable;
- `articleLinkStatus: pending_promotion`: la evidencia de máquina sostiene que la frontera inicia un artículo histórico, pero el objeto curatorial correspondiente todavía no puede promoverse con lectura suficiente; `linkedArticleIds` queda vacío hasta entonces.

`pending_promotion` **no equivale a `unresolved`**. Se usa cuando la frontera está resuelta pero falta una operación posterior del pipeline. `unresolved` queda reservado para evidencia material insuficiente o ambigua.

La relación candidato↔artículo puede ser muchos-a-uno o uno-a-muchos porque el OCR/layout puede fragmentar un artículo histórico, fusionar varios artículos en un solo candidato o cortar un artículo entre columnas o páginas. Por ello no se presupone una correspondencia 1:1 y nunca se fabricará un `articleId` para cerrar artificialmente una reconciliación.

## Jerarquía de evidencia de máquina

La reconciliación utilizará, en este orden, evidencia convergente y con procedencia explícita: facsímil de `ALC1737` cuando sea accesible; geometría del inventario canónico; objetos ya colacionados y continuidades físicas persistidas; OCR/layout derivados del mismo testimonio; páginas adyacentes para resolver bordes; y testigos históricos secundarios registrados, como `BUE1890`, únicamente como control explícito.

La indisponibilidad temporal de una fuente externa no autoriza a rellenar lecturas. Si la geometría permite resolver una frontera pero el texto no, se resuelve la estructura y se conserva la lectura como incierta. Si tampoco la frontera es recuperable, se usa `unresolved`.

## Paratexto y materialidad

Los reclamos tipográficos ya documentados en `data/lexicon/boundary_markers/` son evidencia de que una línea visible puede no ser un artículo. Las continuidades trans-página y trans-columna representadas mediante `sourceSpans` deben utilizarse para distinguir `continuation` de `false_positive`.

Las lagunas del testimonio, especialmente `ALC1737-gap-0001`, y la anomalía `Lucer-` 161→162 no deben resolverse por conocimiento externo durante esta clasificación.

## Lotes de reconciliación

La reconciliación se versionará por lotes pequeños y auditables. Cada lote deberá indicar:

1. páginas y candidatos cubiertos;
2. inventario canónico de procedencia;
3. artículos históricos enlazados y artículos pendientes de promoción;
4. conteos por clasificación y calidad de frontera;
5. decisiones `unresolved` y falsos negativos observados;
6. estado epistemológico y nivel de evidencia utilizado.

El primer tramo de control es pp.133–134. La cobertura de candidatos y la cobertura de **inicios visibles** deben informarse por separado: completar todos los candidatos de una página no elimina los falsos negativos del extractor.

## QA y muestreo

`data/lexicon/review/stratified_boundary_evaluation.json` ya contiene un diagnóstico intencional sobre pp.133, 134, 150 y 177. En esa muestra se registran 171 candidatos frente a 188 inicios visibles, con 163 verdaderos positivos, 8 falsos positivos y 25 falsos negativos. Sus métricas agregadas son precisión 0.9532, recobrado 0.8670 y F1 0.9081.

Estas cifras son **diagnósticas, no inferenciales**: el propio diseño se declara `purposive_stratified_diagnostic`, no probabilístico. No deben presentarse con intervalos de confianza ni extrapolarse como desempeño exacto sobre las 45 páginas.

No se calcularán TP/FP/FN, precisión, recobrado o F1 para una página cuando no exista un denominador de inicios visibles suficientemente defendible. En tal caso debe registrarse expresamente que el censo es incompleto y retenerse las métricas como `null` en lugar de estimarlas.

## Autoridad

Bajo la política vigente, una clasificación IA-asistida permanece `machine_corrected_unverified` o `unresolved` y `humanVerified:false`. El proyecto distingue por diseño **cierre técnico** de **verificación humana**: el primero sí forma parte del pipeline actual; la segunda no.

`ALC1737` conserva primacía como testimonio fuente. `BUE1890` y otros controles no sustituyen silenciosamente una lectura del impreso de 1737. La trazabilidad, la reproducibilidad y la conservación explícita de incertidumbre son los mecanismos de control epistemológico del flujo actual.

## Productos de esta fase

La fase se considerará técnicamente completa cuando existan:

1. inventario canónico reproducible de candidatos — **completado**;
2. un registro de reconciliación por cada candidato persistido;
3. métricas agregadas por clase y página cuando el censo visible permita calcularlas responsablemente;
4. lista separada de candidatos `unresolved`, artículos pendientes de promoción y falsos negativos del extractor;
5. exportación canónica de artículos sin duplicados;
6. informe de QA que distinga extracción automática, revisión editorial IA-asistida y zonas irresueltas, sin presentar como revisión humana lo que no lo es.
