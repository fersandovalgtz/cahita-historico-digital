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
| Transcripciones diplomáticas `full_page` | **72 páginas** | preliminares textuales + Partes I–II + Parte III hasta p. 76 |
| **Parte I** | **completa** | digitales 15–50 / impresas 1–36 |
| **Parte II** | **completa hasta su cierre textual** | digitales 51–68 + segmento superior de digital 69 / impresa 55 |
| Parte III | **en curso hasta digital 76 / impresa 62** | segmento inferior de p. 69 + pp. 70–76 |
| Reglas gramaticales estructuradas | **15** | lote inicial 46–60 |
| Paradigmas gramaticales estructurados | **3** | presente de `Eria`; comparación temporal; comparación optativa |
| Observaciones de variación histórica | **13 entidades** | 10 en exportación JSONL + 3 modulares (`0011`–`0013`) |
| Extractos diplomáticos del vocabulario | **1 página** | p. 134, piloto |
| Entradas lexicográficas piloto | **12** | esquema válido; no producción |
| Revisión humana independiente | **0** | no iniciada |

## Segmentación refinada

La frontera entre Parte II y Parte III **ocurre dentro de la página digital 69 / impresa 55**. La parte superior concluye la regla 188 bajo el encabezado de Parte II; debajo aparece `PARTE III` y comienzan las reglas 189–190.

Por ello [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json) representa una frontera intra-página y [`schemas/page-transcription.schema.json`](schemas/page-transcription.schema.json) admite páginas `mixed` mediante `sectionSegments`.

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

La Fase 2 utiliza una unidad JSON por página y el manifiesto maestro [`data/transcription/status.csv`](data/transcription/status.csv), actualizado ahora hasta la página digital **76 / impresa 62**.

La **Parte I** está completamente representada. La **Parte II** también está completa en su continuidad textual, incluyendo su cierre en el segmento superior de p. 69. La **Parte III** avanza desde el segmento inferior de p. 69 hasta p. 76.

Lotes recientes:

- [`data/transcription/batches/part_ii_p056_p069.csv`](data/transcription/batches/part_ii_p056_p069.csv)
- [`data/transcription/batches/part_iii_p069_p071.csv`](data/transcription/batches/part_iii_p069_p071.csv)
- [`data/transcription/batches/part_iii_p072_p076.csv`](data/transcription/batches/part_iii_p072_p076.csv)

`full_page` significa que la superficie textual impresa de la página está representada editorialmente. Puede contener secuencias `[ileg.]`, celdas pendientes o incertidumbres tipadas; **no equivale a `human_verified`**.

## Parte II: resultados acumulados

La Parte II ha aportado, entre otros objetos:

- regla 128: contraste `Tehuecos` frente a `Hiaqui, y Mayo` en la formación del oblicuo (`tuſta/maſta` frente a `tuhta/mahta`);
- p. 53 / impresa 39: `paros la liebre`, atribuida a `los Mayos, y el Hiaqui ſuaue`;
- p. 58 / impresa 44: `Los Hiaquis dicen nepo en lugar del inopo`, conservado como observación pronominal `ALC1737-var-0011`;
- duplicación histórica del número de regla `129`, preservada sin corrección silenciosa.

## Parte III: paradigmas y variación

Las pp. 70–71 contienen un núcleo comparativo explícito:

- pretérito imperfecto: `Tehuecos = e`, `Hiaquis = n`, `Mayos = i`;
- perfecto: `c` para todos;
- pluscuamperfecto: `Tehuecos = cat`, `Hiaquis = can`, `Mayos = cai`;
- futuro imperfecto: `naque` para todos.

El modelo de paradigmas está formalizado en [`schemas/grammatical-paradigm.schema.json`](schemas/grammatical-paradigm.schema.json). Los dos primeros objetos están en [`data/grammar/paradigms_part_iii_p070_p071.jsonl`](data/grammar/paradigms_part_iii_p070_p071.jsonl).

Las pp. 73–74 añaden un segundo contraste histórico de alto valor. La regla 198 distribuye las notas optativas `hau` para `los Tehuecos` y `amatuc` para `las demás Naciones`; la regla 200 afirma que los Tehuecos usan el optativo en `na` solamente en primera persona y sin semipronombre, mientras las demás Naciones lo usan para todas las personas con semipronombres.

Estas dos observaciones se conservan como `ALC1737-var-0012` y `ALC1737-var-0013`, y se integraron además en el paradigma comparativo [`data/grammar/paradigms_part_iii_p073_p074.jsonl`](data/grammar/paradigms_part_iii_p073_p074.jsonl) como `ALC1737-par-0003`.

## Variación histórica: estado de exportación

La exportación combinada [`data/linguistic/variety_observations.jsonl`](data/linguistic/variety_observations.jsonl) contiene todavía las **10 entidades** iniciales. Las nuevas observaciones modulares se encuentran en:

- `data/linguistic/variety_observations/ALC1737_var_0011.json`
- `data/linguistic/variety_observations/ALC1737_var_0012.json`
- `data/linguistic/variety_observations/ALC1737_var_0013.json`

La exportación combinada deberá regenerarse de manera reproducible en el siguiente ciclo de exportación, sin copiar manualmente datos que ya tienen una fuente modular autoritativa.

## Corpus lexicográfico

El vocabulario mantiene **2,072 candidatos v0.2** sobre 45 páginas. Ese número representa propuestas de frontera y no entradas históricas publicadas. La promoción a entrada de producción continúa requiriendo revisión de frontera, microestructura, procedencia y estado explícito.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana, ni una categoría del gramático de 1737 en una descripción moderna sin una capa analítica separada.
