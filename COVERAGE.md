# Cobertura

Estado de cobertura de Cahíta Histórico Digital para `ALC1737` — 2026-08-16.

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
| Sistema numeral histórico | **1 bloque estructurado** | digitales 178–180; cardinales 1–10 + orden/distributivos/adverbiales |
| Observaciones de variación histórica | **17+** | fuente histórica; nuevas observaciones numéricas pendientes de integración al corpus combinado |
| Candidatos lexicográficos v0.2 | **2,072** | 45 páginas; no equivalen a artículos publicados |
| Artículos históricos estructurados | **673** | p.134 + pase selectivo continuo pp.138–177 |
| Páginas con pase selectivo continuo | **40 / 40** | pp.138–177 |
| Páginas iniciales por retroprocesar | **4** | p.133 y pp.135–137; p.134 posee piloto |
| Pilotos lexicográficos fuera de secuencia | **0** | p.165 reconciliado e integrado |
| Ciclos/reciprocidades de remisión modelados | **1+** | incluye `Demonio ↔ Diablo` y reciprocidades ofender/ofensa/pecar |
| Lagunas/discontinuidades del testimonio registradas | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA de identificadores | **validador incorporado** | `scripts/validate_lexicon_ids.py` |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. La digital 132 / impresa 118 conserva `INTERJECCIONES`, la nota `No ſe hallan en los Artes, el vſo las dará` y `FIN DEL ARTE`.

Este hito significa cobertura de superficie textual, no edición crítica cerrada. Las lecturas `unresolved` permanecen visibles y ninguna página ha sido declarada `human_verified`.

## Vocabulario

El vocabulario alfabético ocupa digitales 133–177. El pipeline geométrico v0.2 conserva **2,072 candidatos**. La secuencia curatorial contiene **673 artículos históricos efectivamente estructurados**.

El pase selectivo es ahora continuo desde **p.138 hasta p.177**. La p.177 cierra materialmente la serie alfabética con voces de V; la p.178 cambia a X/Z y después a `NOMBRES NUMERALES`.

Quedan pendientes de retroprocesamiento p.133 y pp.135–137. P.134 posee un piloto de 12 artículos, por lo que todavía no debe describirse el vocabulario completo como exhaustivamente curado.

### Fronteras y reclamos

La secuencia 168–177 confirma continuidad normal mediante los reclamos `Pie-`, `Por`, `Que-`, `Relam-`, `Rubio,`, `S`, `Tar-`, `Tor-` y `Vn par`. `Pie-` quedó resuelto contra `Piedra de que ſe ſacan navajas` en p.169.

La anomalía `Lucer-` p.161→162 sigue abierta. La laguna F→H p.157→158 continúa documentada como `ALC1737-gap-0001` y no se rellena desde conocimiento externo.

## Sistema numeral — digitales 178–180

Se añadieron:

- `schemas/numeral-system.schema.json`;
- `data/grammar/numerals_p178_p180.json`;
- `docs/NUMERAL_SYSTEM.md`.

La primera estructuración conserva los cardinales de alta confianza 1–10 (`ſenu`, `uoi`, `vabi`, `naequi`, `mammi`, `buſani`, `uobuſani`, `uonaequi/uonaiequi`, `batani`, `uomamni`), la descripción histórica de ordinales, la regla de reduplicación de distributivos y una serie inicial de adverbios numerales.

Las páginas 179–180 contienen además observaciones explícitas sobre `Naciones` y `Hiaqui`; se preservan como descripción histórica y todavía deben integrarse formalmente a la capa combinada de variación.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica de la regla 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- posible ausencia visible de 294;
- discontinuidad del vocabulario F→H entre digitales 157 y 158;
- reclamo `Lucer-` en p.161 sin lema visible al comienzo de p.162.

El reclamo `Pie-` ya está resuelto y la colisión de identificadores del piloto p.165 también.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana ni completa lagunas sin una capa de procedencia separada.

## Siguiente frente

Retroprocesar **p.133 y pp.135–137**, integrar formalmente las observaciones numéricas de variación y comenzar la reconciliación exhaustiva de los 2,072 candidatos con artículos, paratexto y falsos positivos.
