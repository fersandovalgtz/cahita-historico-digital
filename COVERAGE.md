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
| Candidatos lexicográficos v0.2 | **2,072** | 45 páginas; no equivalen a artículos publicados |
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

El vocabulario ocupa digitales 133–177. El pipeline geométrico v0.2 conserva **2,072 candidatos de frontera**. La capa curatorial contiene ahora **734 artículos históricos estructurados** y todas las **45 páginas** poseen al menos una representación lexicográfica estructurada.

La cobertura por página es **selectiva**. No significa que los 2,072 candidatos hayan sido ya clasificados ni que 734 sea el número final de entradas históricas.

### Apertura retroprocesada

Se añadieron lotes para p.133 y pp.135–137, además de un artículo trans-página 133→134. La frontera documenta:

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

La prioridad deja de ser cubrir nuevas páginas del vocabulario. Pasa a ser la **reconciliación exhaustiva de los 2,072 candidatos**: cada candidato deberá clasificarse como artículo histórico, paratexto, continuación física o falso positivo, con métricas reproducibles y exportación canónica de producción.
