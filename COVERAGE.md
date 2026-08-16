# Cobertura

Estado de cobertura de Cahíta Histórico Digital para la fuente `ALC1737`.

## Estado actual — 2026-08-15

| Dimensión | Cobertura | Estado |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digital 15–132 ↔ impresa 1–118 |
| Checksums de archivos fuente de trabajo | **2 / 2** | SHA-256 registrado |
| Extracción OCR paginada reproducible | **182 / 182** | derivado reproducible; no transcripción |
| Diagnóstico estratificado de OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Líneas OCR/layout del vocabulario | **3,899** | pp. 133–177 |
| Candidatos lexicográficos v0.2 | **2,072** | 2,072/2,072 estructuralmente válidos |
| Precisión / recall / F1 v0.2 | **97.13% / 89.89% / 93.37%** | muestra diagnóstica |
| Transcripciones diplomáticas `full_page` | **67 páginas** | preliminares textuales + Parte I + Parte II + apertura de Parte III |
| **Parte I** | **completa** | digitales 15–50 / impresas 1–36 |
| **Parte II** | **completa hasta su cierre textual** | digitales 51–68 + segmento superior de digital 69 / impresa 55 |
| Parte III | **iniciada** | segmento inferior de p. 69 + pp. 70–71 |
| Reglas gramaticales estructuradas | **15** | lote inicial 46–60 |
| Paradigmas gramaticales estructurados | **2** | presente de `Eria` + comparación Tehueco/Hiaqui/Mayo |
| Observaciones de variación histórica | **11 entidades** | 10 en exportación JSONL + nueva observación modular p. 58 |
| Extractos diplomáticos del vocabulario | **1 página** | p. 134, piloto |
| Entradas lexicográficas piloto | **12** | esquema válido; no producción |
| Revisión humana independiente | **0** | no iniciada |

## Segmentación refinada

La frontera entre Parte II y Parte III **no coincide exactamente con un salto de página**. La página digital 69 / impresa 55 contiene dos segmentos:

- en la parte superior continúa `CAHITA. PARTE II.` y concluye la regla 188;
- más abajo aparece el encabezado `PARTE III` y comienzan las reglas 189–190.

Por ello [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json) representa ahora la frontera como **intra-page section boundary**, y [`schemas/page-transcription.schema.json`](schemas/page-transcription.schema.json) admite páginas `mixed` mediante `sectionSegments`.

La segmentación vigente es:

| Sección | Páginas digitales | Páginas impresas |
|---|---:|---:|
| Preliminares | 1–14 | no paginadas |
| Parte I | 15–50 | 1–36 |
| Parte II | 51–69 parcial | 37–55 parcial |
| Parte III | 69 parcial–104 | 55 parcial–90 |
| Parte IV | 105–132 | 91–118 |
| Vocabulario | 133–177 | no paginado |
| Numerales | 178–180 | no paginados |
| Finales materiales | 181–182 | no paginados |

## Transcripción

La Fase 2 utiliza una unidad JSON por página y un manifiesto de 182 filas en [`data/transcription/status.csv`](data/transcription/status.csv).

La **Parte I está completamente representada** en digitales 15–50. La **Parte II también está completa en su continuidad textual**: digitales 51–68 y el segmento superior de la página 69, donde concluye la regla 188. La misma página 69 inaugura Parte III; las páginas 70–71 continúan con la descripción verbal y los primeros paradigmas.

Los nuevos lotes son:

- [`data/transcription/batches/part_ii_p056_p069.csv`](data/transcription/batches/part_ii_p056_p069.csv)
- [`data/transcription/batches/part_iii_p069_p071.csv`](data/transcription/batches/part_iii_p069_p071.csv)

`full_page` significa que la superficie textual impresa de la página está representada, incluso cuando existen secuencias `[ileg.]` o incertidumbres tipadas. No equivale a `human_verified`.

## Hallazgos de Parte II

La transcripción de Parte II añadió varios objetos útiles para investigación:

- regla 128: contraste `Tehuecos` frente a `Hiaqui, y Mayo` en la formación del oblicuo (`tuſta/maſta` frente a `tuhta/mahta`);
- p. 53 / impresa 39: `paros la liebre`, atribuida a `los Mayos, y el Hiaqui ſuaue`;
- p. 58 / impresa 44: `Los Hiaquis dicen nepo en lugar del inopo`, registrado como observación pronominal independiente;
- duplicación histórica visible del número de regla `129` en p. 52, preservada sin corrección silenciosa.

La observación de p. 58 se conserva modularmente en [`data/linguistic/variety_observations/ALC1737_var_0011.json`](data/linguistic/variety_observations/ALC1737_var_0011.json). La exportación combinada `variety_observations.jsonl` contiene todavía las diez entidades anteriores y deberá regenerarse al siguiente ciclo de exportación.

## Parte III y paradigmas

Las pp. 70–71 contienen uno de los núcleos comparativos más densos del *Arte*. La fuente declara:

- pretérito imperfecto: `Tehuecos = e`, `Hiaquis = n`, `Mayos = i`;
- perfecto: `c` para todos;
- pluscuamperfecto: `Tehuecos = cat`, `Hiaquis = can`, `Mayos = cai`;
- futuro imperfecto: `naque` para todos.

Se creó [`schemas/grammatical-paradigm.schema.json`](schemas/grammatical-paradigm.schema.json) y los dos primeros paradigmas en [`data/grammar/paradigms_part_iii_p070_p071.jsonl`](data/grammar/paradigms_part_iii_p070_p071.jsonl). El modelo se documenta en [`docs/PARADIGM_MODEL.md`](docs/PARADIGM_MODEL.md).

## Corpus lexicográfico

El vocabulario mantiene **2,072 candidatos v0.2** sobre 45 páginas. Ese número representa propuestas de frontera y no entradas históricas publicadas. La promoción a entrada de producción continúa requiriendo revisión de frontera, microestructura, procedencia y estado explícito.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana, ni una categoría del gramático de 1737 en una descripción moderna sin una capa analítica separada.
