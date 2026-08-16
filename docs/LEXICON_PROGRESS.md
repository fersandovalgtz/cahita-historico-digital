# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor canónico `hybrid_margin_mode_v0.2` produce **2,072 candidatos** de frontera sobre 45 páginas. Un candidato geométrico no equivale automáticamente a un artículo histórico.

La capa curatorial contiene ahora **844 artículos históricos estructurados**. Las **45/45 páginas** tienen representación lexicográfica estructurada y las páginas **133–136** están cerradas, en capa IA-asistida, en los cuatro niveles operativos del protocolo: reconciliación de candidatos, censo de inicios visibles, promoción/enlace de artículos y QA computacional. **Ningún objeto ha sido declarado `human_verified`.**

## Inventario candidato canónico

Las **2,072 filas** de `hybrid_margin_mode_v0.2` están persistidas y reconstruibles. El inventario se fijó al PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37` y a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10`.

El JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`. `data/lexicon/candidates/candidate_inventory_manifest.json` y `scripts/reconstruct_candidate_inventory.py` controlan su integridad y reproducibilidad.

## Tramo cerrado pp.133–134

Las primeras dos páginas funcionan como tramo de control metodológico. El estado efectivo es:

- 61/61 candidatos reconciliados;
- 57 `article`, 4 `continuation`, 0 `unresolved`;
- 72 inicios históricos visibles en el censo cerrado;
- TP57 / FP4 / FN15;
- precisión 0.934426, recall 0.791667, F1 0.857143;
- 57/57 candidatos `article` enlazados;
- 15/15 falsos negativos visibles enlazados;
- `pending_promotion = 0`.

La apertura quedó resuelta como una sola unidad histórica: `A. denotando la persona que padece. A. Aa.` (`ALC1737-art-000778`). `BUE1890` se utiliza sólo como control histórico secundario concordante.

## Página 135

La p.135 cerró el primer ciclo completo posterior al tramo de control:

- 43/43 candidatos reconciliados;
- 35 `article`, 8 `continuation`, 0 `unresolved`;
- 47 inicios históricos visibles;
- TP35 / FP8 / FN12;
- precisión 0.813953, recall 0.744681, F1 0.777778;
- 35/35 candidatos `article` enlazados;
- 12/12 falsos negativos enlazados;
- `pending_promotion = 0`.

La colación dirigida corrigió `ALC1737-art-000704` de una lectura previa `Azotar. Ahlocotua.` a **`Azofar. Ahlocotua.`** y separó la entrada siguiente `Azotar con cuero, ò ſoga. Abeba.` (`ALC1737-art-000810`). `ALC1737-art-000809`, `Acoſtar à otro`, conserva `Senu[ileg.]` sin completar por inferencia.

## Página 136

`data/lexicon/reconciliation/p136_reconciliation_status.json` documenta el cierre de la página:

- **48/48 candidatos** reconciliados: 24 izquierda + 24 derecha;
- los 48 son `article` y los 48 límites son `exact` en la pasada visual IA-asistida;
- **49 inicios históricos visibles**;
- TP48 / FP0 / FN1;
- precisión **1.000000**;
- recall **0.979592**;
- F1 **0.989691**;
- el único inicio omitido es el primero de página, `Azotar con vara al caballo`, ya representado por `ALC1737-art-000705`;
- 48/48 candidatos enlazados;
- `pending_promotion = 0`.

Se promovieron **34 artículos nuevos**, `ALC1737-art-000811`–`ALC1737-art-000844`, elevando la capa estructurada a **844 artículos**.

### Continuidades materiales detectadas

La p.136 aporta dos casos especialmente útiles para el modelo físico del vocabulario.

`ALC1737-art-000821` cruza columnas dentro de la misma página: `Adobar cueros. Huacabeata-` al pie de la columna izquierda continúa como `buiaruna.` al inicio de la derecha. Se conserva una sola unidad mediante `sourceSpans`.

`ALC1737-art-000844` cruza la frontera p.136→137: `Afligirſe, ò apurarſe. Chuntia-` continúa al inicio de p.137 como `ca, l, chunti iauetua.`. También se conserva como un único artículo histórico mediante `sourceSpans`.

`ALC1737-art-000831`, `A ello, manos à la obra`, permanece `unresolved` a nivel de la expresión cahíta en tipo pequeño; la frontera y la guía española son seguras, pero no se normalizan caracteres inciertos.

## Remisiones, anáforas y agrupaciones

Las remisiones `Buſca` se modelan como relaciones documentales; por ejemplo, p.136 contiene `Adornar. Buſca aderezar.` (`ALC1737-art-000719`). `Lo miſmo` permanece como una anáfora distinta y no se resuelve automáticamente. `sourceGroupingRaw` conserva agrupaciones impresas y `sourceSpans` conserva continuidad física sin convertirla en una categoría lingüística moderna.

## QA automático

`.github/workflows/qa.yml` verifica:

- reconstrucción íntegra de las 2,072 filas canónicas;
- unicidad global de `articleId` y coherencia de autoridad;
- todos los artículos históricos contra `schemas/lexical-article.schema.json`;
- reconciliaciones contra `schemas/lexicon-candidate-review.schema.json`;
- falsos negativos contra `schemas/lexicon-missed-start.schema.json`;
- sintaxis de JSON de estado y control.

Una corrida verde constituye **QA computacional**, no revisión filológica humana.

## Fuentes de control textual

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` es una reimpresión histórica de control y no sustituye el impreso de 1737. `BNF1737-REPORTED` registra la noticia bibliográfica de un ejemplar independiente de 1737 en la BnF, pendiente todavía de verificación directa e ingestión separada.

## Incidencias abiertas

Permanecen activas, entre otras, `ALC1737-gap-0001` entre pp.157–158, el reclamo `Lucer-` de p.161 sin lema visible al comienzo de p.162 y varias formas de baja legibilidad marcadas de manera conservadora. Ninguna se completa mediante conocimiento externo sin procedencia explícita.

## Próximo frente

El siguiente ciclo es la **página digital 137**. Debe comenzar respetando que su primera línea pertenece al cierre de `ALC1737-art-000844`, no a un artículo nuevo; después se reconciliarán sus candidatos canónicos, se hará censo completo de inicios visibles, se promoverán faltantes y se cerrará QA antes de avanzar a p.138.
