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
| Transcripciones diplomáticas `full_page` | **92 páginas** | preliminares textuales + Partes I–II + Parte III hasta p. 96 |
| **Parte I** | **completa** | digitales 15–50 / impresas 1–36 |
| **Parte II** | **completa hasta su cierre textual** | digitales 51–68 + segmento superior de digital 69 / impresa 55 |
| Parte III | **en curso hasta digital 96 / impresa 82** | reglas 189–264 representadas; regla 264 continúa |
| Reglas gramaticales estructuradas | **15** | lote inicial 46–60 |
| Paradigmas gramaticales estructurados | **3** | presente de `Eria`; comparación temporal; comparación optativa |
| Construcciones modales estructuradas | **9** | reglas 207–234; `vn supuesto` / `dos supuestos` |
| Construcciones no finitas estructuradas | **5** | infinitivos y gerundios; reglas 237–256 |
| Construcciones participiales estructuradas | **3** | reglas 257–264; `me`, `u`, `ye` |
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

La Fase 2 utiliza una unidad JSON por página. El manifiesto maestro [`data/transcription/status.csv`](data/transcription/status.csv) está consolidado hasta la página digital **91 / impresa 77**; el lote vigente adicional [`data/transcription/batches/part_iii_p092_p096.csv`](data/transcription/batches/part_iii_p092_p096.csv) añade las páginas 92–96 y constituye el delta que deberá incorporarse en la próxima consolidación del manifiesto.

La **Parte I** está completamente representada. La **Parte II** también está completa en su continuidad textual, incluyendo su cierre en el segmento superior de p. 69. La **Parte III** avanza desde el segmento inferior de p. 69 hasta p. 96 y cubre las reglas 189–264; la regla 264 queda abierta hacia p. 97.

Lotes recientes:

- [`data/transcription/batches/part_ii_p056_p069.csv`](data/transcription/batches/part_ii_p056_p069.csv)
- [`data/transcription/batches/part_iii_p069_p071.csv`](data/transcription/batches/part_iii_p069_p071.csv)
- [`data/transcription/batches/part_iii_p072_p076.csv`](data/transcription/batches/part_iii_p072_p076.csv)
- [`data/transcription/batches/part_iii_p077_p086.csv`](data/transcription/batches/part_iii_p077_p086.csv)
- [`data/transcription/batches/part_iii_p087_p091.csv`](data/transcription/batches/part_iii_p087_p091.csv)
- [`data/transcription/batches/part_iii_p092_p096.csv`](data/transcription/batches/part_iii_p092_p096.csv)

`full_page` significa que la superficie textual impresa de la página está representada editorialmente. Puede contener secuencias `[ileg.]`, lecturas provisionales o incertidumbres tipadas; **no equivale a `human_verified`**.

## Parte II: resultados acumulados

La Parte II ha aportado, entre otros objetos:

- regla 128: contraste `Tehuecos` frente a `Hiaqui, y Mayo` en la formación del oblicuo (`tuſta/maſta` frente a `tuhta/mahta`);
- p. 53 / impresa 39: `paros la liebre`, atribuida a `los Mayos, y el Hiaqui ſuaue`;
- p. 58 / impresa 44: `Los Hiaquis dicen nepo en lugar del inopo`, conservado como observación pronominal `ALC1737-var-0011`;
- duplicación histórica del número de regla `129`, preservada sin corrección silenciosa.

## Parte III: paradigmas, modalidad y variación

Las pp. 70–71 contienen un núcleo comparativo explícito:

- pretérito imperfecto: `Tehuecos = e`, `Hiaquis = n`, `Mayos = i`;
- perfecto: `c` para todos;
- pluscuamperfecto: `Tehuecos = cat`, `Hiaquis = can`, `Mayos = cai`;
- futuro imperfecto: `naque` para todos.

El modelo de paradigmas está formalizado en [`schemas/grammatical-paradigm.schema.json`](schemas/grammatical-paradigm.schema.json). Los dos primeros objetos están en [`data/grammar/paradigms_part_iii_p070_p071.jsonl`](data/grammar/paradigms_part_iii_p070_p071.jsonl).

Las pp. 73–74 añaden un segundo contraste histórico: la regla 198 distribuye `hau` para `los Tehuecos` y `amatuc` para `las demás Naciones`; la regla 200 afirma que los Tehuecos usan el optativo en `na` solamente en primera persona y sin semipronombre, mientras las demás Naciones lo usan para todas las personas con semipronombres. Estas evidencias están en `ALC1737-var-0012`, `ALC1737-var-0013` y `ALC1737-par-0003`.

### Sistema de tiempos modales

Las pp. 77–86 / impresas 63–72 contienen un bloque coherente de reglas 207–234. CHD creó un modelo específico en [`schemas/modal-construction.schema.json`](schemas/modal-construction.schema.json) y una primera exportación de **9 construcciones históricas** en [`data/grammar/modal_constructions_part_iii_p077_p086.jsonl`](data/grammar/modal_constructions_part_iii_p077_p086.jsonl).

El dataset preserva la oposición interna del impreso entre `vn supuesto` y `dos supuestos` y organiza, sin modernizarlas, las series asociadas a `ſi`, `antes`, `como`, `quando`, `aunque`, `deſpues`, `porque`, `para / paraque` y `como ſi`. Entre los marcadores documentados aparecen `teca`, `cari`, `cacari`, `yo`, `co`, `caco`, `ituca`, `varecari`, `rocacari`, `poea`, `iyaacari`, `teeiacari`, `ten`, `tzaua` y `ven / veni`.

→ [`docs/MODAL_CONSTRUCTIONS.md`](docs/MODAL_CONSTRUCTIONS.md)

### Infinitivos y gerundios

Las pp. digitales 87–93 / impresas 73–79 cierran los tiempos modales y desarrollan el sistema de construcciones no finitas. CHD formalizó [`schemas/nonfinite-construction.schema.json`](schemas/nonfinite-construction.schema.json) y mantiene **5 objetos** en [`data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl`](data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl).

Los objetos distinguen:

- primer modo de infinitivo, reglas 237–241;
- segundo modo de infinitivo, regla 242;
- gerundios en `DI`, reglas 243–245;
- gerundio en `DO`, reglas 246–249;
- gerundio en `DVM`, reglas 250–256.

La lectura visual de la página 89 apoya **242** para `SEGUNDO MODO DE INFINITIVO`, aunque el OCR de esa página produjo 241. CHD conserva explícitamente este desacuerdo entre capas en vez de corregirlo sin registro.

→ [`docs/NONFINITE_CONSTRUCTIONS.md`](docs/NONFINITE_CONSTRUCTIONS.md)

### Participios

Las pp. digitales 94–96 / impresas 80–82 abren `§ II. DE LOS PARTICIPIOS EN COMUN` y desarrollan tres núcleos: participios comunes en `me`, participios en `u` y nombres verbales/participios en `ye`. CHD creó [`schemas/participle-construction.schema.json`](schemas/participle-construction.schema.json) y **3 objetos iniciales** en [`data/grammar/participles_part_iii_p094_p096.jsonl`](data/grammar/participles_part_iii_p094_p096.jsonl).

La fuente atribuye a los participios en `u` valores discursivos de acción o estado ya terminado, pérdida o cese, lamentación y ausencia prolongada; CHD registra esas formulaciones como análisis histórico del gramático y no como etiquetas aspectuales modernas asumidas. La regla 264 inicia además una derivación instrumental de los participios en `ye` mediante `aye / ayeye` y continúa en p. 97.

→ [`docs/PARTICIPLES.md`](docs/PARTICIPLES.md)

## Variación histórica: estado de exportación

La exportación combinada [`data/linguistic/variety_observations.jsonl`](data/linguistic/variety_observations.jsonl) contiene todavía las **10 entidades** iniciales. Las nuevas observaciones modulares se encuentran en:

- `data/linguistic/variety_observations/ALC1737_var_0011.json`
- `data/linguistic/variety_observations/ALC1737_var_0012.json`
- `data/linguistic/variety_observations/ALC1737_var_0013.json`

La exportación combinada deberá regenerarse de manera reproducible, sin copiar manualmente datos que ya tienen una fuente modular autoritativa.

## Corpus lexicográfico

El vocabulario mantiene **2,072 candidatos v0.2** sobre 45 páginas. Ese número representa propuestas de frontera y no entradas históricas publicadas. La promoción a entrada de producción continúa requiriendo revisión de frontera, microestructura, procedencia y estado explícito.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana, ni una categoría del gramático de 1737 en una descripción moderna sin una capa analítica separada.
