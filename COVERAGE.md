# Cobertura

Estado canónico de cobertura de Cahíta Histórico Digital para `ALC1737` — **21 de agosto de 2026**.

## Métricas vigentes

| Dimensión | Cobertura | Autoridad / nota |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digitales 15–132 ↔ impresas 1–118 |
| OCR paginado reproducible | **182 / 182** | derivado; no transcripción |
| Transcripciones diplomáticas `full_page` | **128 páginas** | preliminares textuales + Arte completo hasta digital 132 |
| Partes I–IV del Arte | **completas en capa IA-asistida** | fronteras intra-página 69 y 105 preservadas |
| Sistema numeral histórico | **1 bloque estructurado** | digitales 178–180 |
| Candidatos lexicográficos v0.2 | **2,072 / 2,072** | inventario canónico reconstruible |
| Artículos históricos estructurados | **2,302** | conteo actual de `articleId` únicos |
| Páginas del Vocabulario representadas | **45 / 45** | digitales 133–177 |
| Páginas con reconciliación candidate-level completa | **45 / 45** | IA-asistido |
| Páginas con censo visible exhaustivo | **45 / 45** | inicios visibles y falsos negativos modelados |
| Páginas con promoción/enlace cerrado | **45 / 45** | `pending_promotion = 0` |
| Páginas con cierre técnico | **45 / 45** | no equivale a revisión filológica humana |
| Subfase p.145–177 cerrada | **33 / 33** | resumen reproducible vigente |
| `pending_promotion` p.145–177 | **0** | fuente: resumen generado |
| Candidatos estructuralmente `unresolved` p.145–177 | **0** | no confundir con incertidumbre interna de artículos |
| Fronteras `ambiguous` p.145–177 | **0** | cierre estructural completo |
| Revisión humana independiente | **0** | `humanVerified=false` |
| QA automatizado | **activo** | inventario, IDs, schemas, reconciliaciones, missed starts, JSON central, colas y resumen maestro |

## Autoridad

`ALC1737` es la autoridad primaria de transcripción y segmentación. `BUE1890` puede emplearse únicamente como reimpresión histórica de control. No se trasladan silenciosamente formas de un testimonio secundario al testimonio de 1737.

El estado `machine_corrected_unverified` identifica trabajo IA-asistido cotejado con el facsímil. **Cierre técnico no significa edición diplomática o filológica humana cerrada.**

## Vocabulario — estado estructural final de esta etapa

El Vocabulario ocupa las páginas digitales **133–177**. El inventario canónico contiene **2,072 candidatos**, mientras que la capa curatorial contiene **2,302 artículos históricos estructurados**. La diferencia es esperable: un candidato geométrico puede contener más de un inicio histórico y el censo facsimilar detectó falsos negativos que no figuraban en el inventario candidato.

Las **45 páginas** han pasado por:

1. reconciliación de candidatos;
2. censo exhaustivo de inicios visibles;
3. identificación de continuidades y paratexto;
4. registro de falsos positivos y falsos negativos;
5. promoción/enlace de artículos;
6. conservación explícita de incertidumbre;
7. validación computacional mediante GitHub Actions.

El resumen regenerable de la subfase p.145–177 es `data/lexicon/reconciliation/phase2_open_work_summary.json`. Al cierre registra **0 pendientes, 0 candidatos estructuralmente unresolved, 0 fronteras ambiguous, 33/33 páginas con censo exhaustivo y 33/33 con cierre técnico**, con **2,302 artículos curatoriales** en el repositorio.

## Límite material del Vocabulario

La página digital **177** contiene el último artículo lexicográfico, `Vomitar. Biſata.`. Las digitales **178–180** corresponden al sistema numeral histórico y no continúan el Vocabulario. Esta frontera quedó modelada explícitamente en el cierre de p.177.

## Incertidumbres que permanecen abiertas

El cierre estructural no elimina problemas textuales internos. Permanecen, entre otros:

- `ALC1737-gap-0001`, discontinuidad material digital 157→158;
- artículos con microestructura o segmentos de baja confianza;
- `ALC1737-art-001045` (`Atormentar`) con incertidumbre localizada;
- anáforas históricas `Lo miſmo` aún no resueltas como red editorial;
- remisiones `Buſca` pendientes de cierre como grafo;
- atribuciones históricas `Hiaqui`, `Mayo`, `Thehueco` y variantes pendientes de inventario sistemático.

Estas incertidumbres no reabren la segmentación de las páginas: pertenecen al siguiente nivel editorial y semántico.

## Próximo frente de cobertura

La siguiente ampliación de cobertura no consiste en crear más promociones página por página. El frente es construir derivados canónicos y verificables a partir de los **2,302 artículos**:

- inventario maestro de artículos;
- exportaciones JSONL, JSON y CSV reproducibles;
- grafo de remisiones `Buſca`;
- inventario de anáforas `Lo miſmo`;
- atribuciones históricas internas;
- perfil TEI Lex-0 cuando la microestructura esté suficientemente estabilizada;
- QA de los nuevos derivados.

En paralelo siguen activas la Fase 2 de transcripción diplomática y la Fase 4 de gramática y variación histórica.
