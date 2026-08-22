# Changelog

Todos los cambios relevantes de Cahíta Histórico Digital se documentan en este archivo.
## [1.0.0] - 2026-08-21

### Release científica estable

- 2,302 artículos lexicográficos históricos en 211 JSONL y 2,072/2,072 candidatos canónicos reconstruibles.
- vocabulario p.133–177 reconciliado 45/45; Phase II p.145–177 cerrada técnicamente 33/33.
- 150 remisiones históricas `Buſca`: 60 `exact_unique`, 90 `not_located`, 4 ciclos estrictos; 90/90 no localizadas con revisión explícita.
- 22 casos de recolación preservados en v1.0 como `frozen_open_uncertainty` (8 A / 4 B / 10 C), con 0 destinos seleccionados, 0 cambios canónicos y `humanVerified=false`.
- 14/14 ocurrencias de `Lo miſmo` auditadas fuera del grafo de remisiones, sin inferir función exacta.
- 302 objetos gramaticales, 1,215 filas de evidencia y 371/371 unidades numeradas realmente impresas representadas.
- proyección TEI Lex-0 0.9.5 con 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 `@target` estrictos, validada externamente con Jing.
- TEI Lex-0 definido como perfil interoperable primario; CLDF diferido como derivado analítico post-v1.
- 26 contratos v1.0 congelados por SHA-256 y freeze byte-exacto de artículos, candidatos, revisiones y gramática.
- paquete científico v1.0 determinista con datos canónicos congelados, derivados reproducibles, manifiestos y checksums.
- esta versión no declara validación filológica humana integral; las incertidumbres siguen explícitas y el facsímil histórico no se relicencia.
- DOI de versión y Concept DOI quedan pendientes hasta el depósito archivístico; no se infieren ni se inventan.


## [0.2.0-dev] - 2026-08-16

### Hito científico

- el cuerpo gramatical del *Arte* quedó representado de forma continua en la capa de transcripción IA-asistida hasta `FIN DEL ARTE`;
- la cobertura `full_page` alcanza **128 páginas**;
- se estructuraron capas específicas para modalidad, formas no finitas, participios, predicación, verbos irregulares, preposiciones, adverbios, conjunciones/metacategorías y numerales;
- se identificaron **17+ observaciones de variación histórica**, con consolidación combinada todavía pendiente;
- las fronteras intra-página 69 (II→III) y 105 (III→IV) quedaron preservadas estructuralmente.

### Corpus lexicográfico

- el inventario `hybrid_margin_mode_v0.2` de **2,072 candidatos** quedó persistido canónicamente en una representación fila-a-fila lossless y reconstruible;
- se fijaron revisión generadora, hashes del PDF y del JSONL canónico, manifiesto de integridad y script de reconstrucción;
- las **45/45 páginas** del vocabulario tienen representación lexicográfica estructurada;
- la capa curatorial alcanza **1,045 artículos históricos estructurados**;
- se modelaron remisiones `Buſca`, anáforas `Lo miſmo`, agrupaciones históricas, catchwords y spans entre columnas/páginas;
- se registraron la discontinuidad `ALC1737-gap-0001` (157→158) y la anomalía `Lucer-` (161→162);
- se corrigió una colisión histórica de identificadores del antiguo piloto de p.165 y se incorporó un validador de unicidad;
- el piloto botánico de p.142 fue recotejado a 600 dpi, corrigiendo `ALC1737-art-000131` de `Hohuno` a `Hohuo` y `ALC1737-art-000135` de `Maccchua` a `Maccehua`, sin cambiar sus IDs ni elevar su autoridad editorial;
- la capa seleccionada de p.143 fue recotejada a 600 dpi, corrigiendo `ALC1737-art-000143` de `Hilobue` a `Hiolhue` y `ALC1737-art-000153` de `Curuat` a `Curuas`, con proveniencia versionada separadamente;
- la capa seleccionada de p.144 fue recotejada a 600 dpi con seis correcciones versionadas, entre ellas `000156 Ahuma→Ahima`, `000160 Aletear/Amumuifuc→Aſaetear/Amumuiſuc`, `000162 Aſir/Auhinei→Aſſir/Auhineu` y `000165 Tapeto→Tapeti`.

### Reconciliación y QA

- se definió `schemas/lexicon-candidate-review.schema.json` y el protocolo formal de reconciliación;
- se añadió `articleLinkStatus` para separar frontera confirmada de promoción curatorial;
- las páginas digitales **133–144** tienen ya ciclo cerrado de candidato → censo visible → promoción → QA;
- en ese tramo se reconciliaron **514/514 candidatos canónicos**;
- el censo facsimilar registra **541 inicios históricos visibles**: TP483 / FP31 / FN58; precisión **0.939689**, recall **0.892791** y F1 **0.915640**;
- todos los candidatos `article` y todos los falsos negativos visibles del tramo cerrado están enlazados; **`pending_promotion = 0`**;
- la p.140 cerró con 47 candidatos, 48 inicios visibles, TP44 / FP3 / FN4, F1 0.926316 y 12 promociones nuevas `ALC1737-art-000899`–`000910`;
- la p.141 cerró con 41 candidatos, 40 inicios visibles, TP34 / FP7 / FN6, F1 0.839506 y 29 promociones nuevas `ALC1737-art-000911`–`000939`; `000930` y `000936` conservan microestructura `unresolved` en lugar de imponer segmentaciones no demostradas;
- la p.142 cerró con 53 candidatos, 50 inicios visibles, TP50 / FP3 / FN0, precisión 0.943396, recall 1.000000 y F1 0.970874; se promovieron 40 artículos nuevos `ALC1737-art-000940`–`000979`;
- en p.142 los candidatos L-006 y R-004 se clasificaron como encabezados de agrupación, L-020 como falso positivo OCR/layout, y los encabezados/reclamos absorbidos en R-022/R-033 se excluyeron del conteo lexicográfico;
- la p.143 cerró con 46 candidatos, 48 inicios visibles, TP44 / FP2 / FN4, precisión 0.956522, recall 0.916667 y F1 0.936170; se promovieron 34 artículos nuevos `ALC1737-art-000980`–`001013`;
- los cuatro falsos negativos de p.143 son `Arbol. Sapo.`, `Arenal. Sepai.`, `Armarſe para la batalla...` y `Arriba como en la ſotea. Catabepa.`; los candidatos L-021 y L-027 son continuaciones físicas, no entradas nuevas;
- el separador histórico `l` de `Arrendar dar algo à renta. Hitare urec, l, reureuri.` se conserva como evidencia sin interpretación lingüística moderna;
- la p.144 cerró con 39 candidatos, 46 inicios visibles, TP39 / FP0 / FN7, precisión 1.000000, recall 0.847826 y F1 0.917647; se promovieron **32 artículos nuevos** `ALC1737-art-001014`–`001045`;
- los siete falsos negativos de p.144 son `Arrimarſe à alguna coſa`, `Arrugada tener la cara`, `Aſpera coſa`, `Aſſiento donde ſientan`, `Aſſomar la cabeza`, `Atar los pies` y `Ataviarſe`; cinco candidatos contienen dos comienzos históricos visibles y se modelan como `merged_articles`;
- el borde derecho recortado de p.144 se resolvió con ALC1737 como autoridad primaria y BUE1890 sólo como control secundario explícito; no se sustituyeron lecturas silenciosamente;
- `Atormentar` (`001045`) quedó modelado como artículo trans-página 144→145 y `unresolved` únicamente en la lectura fina de su segunda forma, preservando el reclamo `chum-` y la continuidad física;
- `CHD QA` valida inventario canónico, unicidad/autoridad de IDs, artículos contra schema, lotes de reconciliación, capas de inicios omitidos y sintaxis JSON;
- el workflow se amplió sucesivamente para validar explícitamente las reconciliaciones, capas de inicios omitidos y estados JSON hasta p.144;
- **CHD QA run #148** concluyó en `success` con la cobertura ampliada de p.144;
- la comparación v0.2 sobre pp.133, 134, 150 y 177 conserva precisión 97.13%, recall 89.89% y F1 93.37%, con muestra intencional e IA-asistida.

### Auditoría de consistencia

- `README.md`, `ROADMAP.md` y `COVERAGE.md` fueron sincronizados durante la serie 0.2.x con el estado real del repositorio;
- `COVERAGE.md` registra actualmente **1,045 artículos** y reconciliación cerrada hasta p.144;
- se distinguieron explícitamente las métricas históricas v0.1 de las vigentes v0.2;
- el estado de desarrollo permanece en **`0.2.0-dev`** sin declarar una release científica estable;
- permanece **0 `human_verified`** y no existe aún DOI del proyecto.

### Pendientes de la serie 0.2.x

- escalar la reconciliación exhaustiva desde p.145 hasta p.177;
- normalizar `sourceSpans` de `ALC1737-art-000068` y realizar la recollación versionada de `000073`/`000074` detectada al cerrar p.139;
- consolidar documentación y metadatos restantes;
- actualizar Issues históricos que aún describen estados superados;
- consolidar variación histórica y concordancias gramaticales;
- buscar testimonios independientes útiles para control textual;
- preparar interoperabilidad y revisión humana antes de una release estable.

## [0.1.5-dev] - 2026-08-15

### Mejorado

- `scripts/extract_vocab_candidates.py` pasa a `hybrid_margin_mode_v0.2`;
- el método utiliza margen modal en pp. 134–177 y conserva el criterio v0.1 en la primera página del vocabulario, p. 133;
- el esquema de candidatos conserva compatibilidad con `indentation_margin_v0.1` y añade metadatos de regla de página y margen estimado;
- se documenta la comparación v0.1/v0.2 en `docs/VOCAB_BOUNDARY_V02.md` y `data/lexicon/review/boundary_algorithm_comparison.json`.

### Resultado

La corrida v0.2 sobre pp. 133–177 produjo **2,072 candidatos**: 1,055 en columna izquierda y 1,017 en derecha. Los **2,072 / 2,072** objetos pasaron validación estructural. El JSONL derivado completo tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

Sobre la misma muestra diagnóstica de pp. 133, 134, 150 y 177, v0.2 mejora la evaluación de comienzos de artículo de **95.32% / 86.70% / 90.81%** a **97.13% / 89.89% / 93.37%** en precisión / recall / F1.

### Salvaguardas

La cifra 2,072 sigue siendo un número de **candidatos computacionales**, no de entradas históricas. La muestra de evaluación es intencional y el cotejo visual es IA-asistido, sin revisión humana independiente. La versión v0.1 permanece preservada en el historial y mediante hashes documentados.

## [0.1.4-dev] - 2026-08-15

### Añadido

- `scripts/extract_vocab_candidates.py`, extractor conservador de candidatos de límites de artículo basado en indentación y layout;
- `schemas/vocabulary-candidate.schema.json`, contrato que separa formalmente un candidato OCR de una entrada lexicográfica;
- muestra auditable de 38 candidatos de la página digital 134 en `data/lexicon/candidates/p134_candidates.jsonl`;
- documentación metodológica y limitaciones en `docs/VOCAB_CANDIDATES.md`.

### Resultado

La corrida completa sobre páginas digitales 133–177 produjo **1,680 candidatos**: 903 en columna izquierda y 777 en derecha, con una media de 37.33 candidatos por página. Los **1,680 / 1,680** objetos pasaron validación estructural contra su JSON Schema. El JSONL completo derivado tiene SHA-256 `f00318329c1116254388aac0ffe978fea330c8466f3863e318df1f01fd010b59`.

### Salvaguardas

La cifra 1,680 **no se presenta como número de entradas históricas**. El algoritmo conserva falsos comienzos y posibles continuaciones como candidatos revisables; no divide automáticamente lema castellano y forma cahíta, y no promueve ningún objeto a `lexical_entry`.

## [0.1.3-dev] - 2026-08-15

### Añadido

- diagnóstico estratificado y reproducible de calidad OCR en seis zonas del volumen;
- `scripts/evaluate_ocr_sample.py`;
- referencias de evaluación en `data/validation/ocr_sample_references.json`;
- resultados versionados en `data/validation/ocr_sample_results.json`;
- documentación metodológica en `docs/OCR_QUALITY.md`.

### Resultado

La muestra diagnóstica arroja **micro-CER 25.66%** y **micro-WER 51.96%** después de una normalización que mapea `ſ → s`, elimina marcas diacríticas combinantes, minúsculiza y neutraliza puntuación/espaciado. El resultado confirma que el OCR bruto no debe promoverse directamente a corpus científico.

La muestra del vocabulario (p. 134) usa reconstrucción de columna mediante `-bbox-layout` y obtiene CER 9.68% en el fragmento seleccionado; este valor se interpreta como indicio de que la geometría de dos columnas constituye una parte importante del problema, no como tasa global del vocabulario.

### Salvaguardas

Las transcripciones de referencia de la evaluación son cotejos visuales IA-asistidos sin revisión humana independiente. Por tanto, el diagnóstico es una métrica de ingeniería editorial y no una evaluación filológica definitiva.

## [0.1.2-dev] - 2026-08-15

### Añadido

- extractor reproducible de disposición a dos columnas para el vocabulario: `scripts/extract_vocab_layout.py`;
- esquema `schemas/vocabulary-layout-line.schema.json` para conservar líneas OCR con página, columna, coordenadas y estado de evidencia;
- `scripts/validate_jsonl.py` y `requirements-dev.txt` para validación reproducible de JSONL;
- primer extracto diplomático IA-asistido del vocabulario, página digital 134;
- **12 entradas lexicográficas piloto** estructuradas y validadas contra `schemas/lexical-entry.schema.json`;
- documentación metodológica del piloto en `docs/PILOT_LEXICON_P134.md`.

### Resultados de extracción

Una corrida local de `extract_vocab_layout.py` sobre las páginas digitales 133–177 produjo **3,899 líneas OCR/layout**: 1,731 clasificadas en columna izquierda, 2,107 en derecha y 61 retenidas como `other` por fusiones o ambigüedad de layout. El JSONL completo derivado tiene SHA-256 `9b5eb47fc7d93a63e8345a33da844863d8228fe7149a303ee35a1c2c00cb1871`.

### Salvaguardas

Las 12 entradas del piloto están marcadas `machine_corrected_unverified`; ninguna se presenta como `human_verified`. La extracción de líneas no se interpreta como recuento de artículos lexicográficos.

## [0.1.1-dev] - 2026-08-15

### Añadido

- script de ingestión reproducible `scripts/ingest_alc1737.py`;
- checksums SHA-256 de los dos archivos de trabajo de `ALC1737`;
- manifiesto página por página para las **182 páginas digitales**, con sección y paginación impresa cuando existe;
- mapeo completo de las **118 páginas impresas numeradas** del cuerpo gramatical;
- documentación técnica de ingestión;
- convenciones explícitas para transcripción diplomática, corrección, `ſ`, abreviaturas, particiones de línea e incertidumbre;
- README específico de la fuente en `data/source/alc1737/`.

### Modificado

- la segmentación macro dejó de ser únicamente inferida por encabezados: sus fronteras principales fueron cotejadas visualmente en el facsímil;
- la documentación de la fuente incorpora ahora la descripción física del registro de Internet Archive/JCB y la discrepancia técnica entre el campo `Pages: 184` y el PDF de trabajo de 182 páginas;
- las métricas de cobertura distinguen OCR disponible, OCR extraído, payload versionado y transcripción filológica;
- las páginas 181–182 se identifican como finales materiales/cubierta posterior, no como una sección textual pendiente.

### Estado científico

- **0 / 182** páginas se declaran todavía como transcripción diplomática terminada;
- **0** entradas lexicográficas se promueven todavía al corpus estructurado de producción;
- **0** unidades se etiquetan como `human_verified`.

La fase 0.1.1-dev consolida la trazabilidad técnica necesaria antes de comenzar la extracción lexicográfica y la transcripción.

## [0.1.0] - 2026-08-15

### Añadido

- definición inicial del proyecto **Cahíta Histórico Digital**;
- registro canónico de la fuente `ALC1737`;
- documentación de la fuente histórica de 1737 y de su procedencia digital;
- política explícita para tratar la autoría histórica como cuestión no resuelta;
- política editorial por capas: testimonio, OCR, transcripción, normalización y datos derivados;
- `CITATION.cff` y `codemeta.json`;
- datasheet inicial del corpus;
- esquema JSON inicial para entradas lexicográficas;
- política de licencias separada para código, datos y materiales de terceros;
- hoja de ruta para ingestión, extracción lexicográfica, interoperabilidad y futura preservación en Zenodo;
- integración documental con el ecosistema de repositorios científicos de Fernando Sandoval Gutierrez.

### Estado científico

Esta versión es **pre-release**. Registra la infraestructura y la fuente, pero no declara terminada ni validada una transcripción crítica, un vocabulario estructurado o una edición filológica completa.
