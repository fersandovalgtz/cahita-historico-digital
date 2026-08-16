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
| Artículos históricos estructurados | **388** | piloto p.134 + secuencia curatorial pp.138–158 |
| Artículos de remisión piloto adicionales | **4** | p.165; fuera del conteo principal |
| Ciclos recíprocos de remisión modelados | **1** | `Demonio ↔ Diablo` |
| Lagunas/discontinuidades del testimonio registradas | **1** | `ALC1737-gap-0001`, digital 157→158 |
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

El vocabulario ocupa digitales 133–177. El pipeline geométrico v0.2 produce **2,072 candidatos de frontera**, pero la secuencia curatorial principal contiene **388 artículos históricos efectivamente estructurados** en p.134 y pp.138–158.

El modelo ya representa:

- equivalencias simples y múltiples;
- remisiones `Buſca`;
- anáforas `Lo miſmo` mantenidas `unresolved`;
- agrupaciones históricas mediante `sourceGroupingRaw`;
- artículos descriptivos;
- continuidad entre páginas y entre columnas mediante `sourceSpans`;
- catchwords/reclamos como paratexto de frontera;
- relaciones recíprocas de remisión;
- lagunas documentales explícitas del testimonio.

### Catchwords

`data/lexicon/boundary_markers/catchwords_p153_p154.jsonl` documenta `Desbaſ-` (p.153 → `Desbaſtar madera`, p.154) y `Dar` (p.154 → serie inicial de p.155). Estos reclamos no se cuentan como artículos.

### Ciclo de remisión

Las pp.153–154 contienen el ciclo explícito `Demonio. Buſca diablo.` ↔ `Diablo. Buſca demonio.`. Se conserva en `data/lexicon/relations/reciprocal_cross_references.jsonl` sin escoger artificialmente un lema canónico.

### Discontinuidad digital 157→158

La p.157 termina con voces de F, incluida `Flecha. Huihua.`, y muestra un reclamo inferior que comienza `Fle...`. La digital 158 comienza directamente con voces de H (`Hallarſe bien en vn lugar`, `Hambre`, etc.). La representación HTML guardada reproduce el mismo salto.

La incidencia está registrada como `ALC1737-gap-0001` en `data/source/alc1737/gaps.jsonl` y documentada en `docs/SOURCE_GAPS.md`. CHD no determina todavía el número de páginas/folios faltantes y no reconstruye el material ausente sin otro testimonio documentado.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica de la regla 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- posible ausencia visible de 294;
- discontinuidad del vocabulario F→H entre digitales 157 y 158.

Ninguna incidencia se corrige silenciosamente.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana ni completa lagunas desde conocimiento externo sin una capa de procedencia separada.

## Siguiente frente

Continuar la promoción curatorial desde **digital 159**, manteniendo visible la laguna 157→158 y sincronizando cada lote sustantivo con GitHub y Notion.
