# Progreso del corpus lexicográfico

## Estado — 2026-08-21

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El inventario canónico `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera. La capa curatorial contiene actualmente **2,302 artículos históricos estructurados**.

La reconciliación estructural de todo el Vocabulario está cerrada dentro del alcance IA-asistido declarado:

- **45/45 páginas** con reconciliación candidate-level completa;
- **45/45 páginas** con censo exhaustivo de inicios visibles;
- **45/45 páginas** con promoción/enlace cerrado;
- **45/45 páginas** con cierre técnico;
- **0 candidatos `pending_promotion`** en la subfase p.145–177;
- **0 candidatos estructuralmente `unresolved`** y **0 fronteras `ambiguous`** en el resumen regenerable de esa subfase;
- **0 objetos `human_verified`**.

El cierre técnico no equivale a una edición filológica humana. Las incertidumbres internas de artículos, remisiones históricas, anáforas y problemas materiales permanecen explícitas cuando corresponde.

## Inventario canónico

Las **2,072 filas** candidatas están fijadas al PDF SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`; el JSONL canónico reconstruido tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

`scripts/reconstruct_candidate_inventory.py` verifica la representación lossless y `scripts/export_candidate_page.py` permite inspeccionar de manera reproducible una página/columna concreta.

## Resultado de la subfase p.145–177

La subfase de promoción/enlace y censo facsimilar de **33 páginas** terminó el 21 de agosto de 2026. Su resumen computacional, `data/lexicon/reconciliation/phase2_open_work_summary.json`, registra:

- `pages = 33`;
- `pendingPromotionTotal = 0`;
- `unresolvedCandidateTotal = 0`;
- `ambiguousBoundaryTotal = 0`;
- `pagesWithExhaustiveVisibleStartCensus = 33`;
- `pagesWithTechnicalClosure = 33`;
- `humanVerifiedPages = 0`;
- `currentCuratorialArticleCount = 2302`.

Los estados de página conservan snapshots históricos de cada pasada; el conteo vigente del corpus se obtiene de los `articleId` únicos presentes en `data/lexicon/articles/*.jsonl`.

## Crecimiento del corpus

El corpus llegó a **1,045 artículos** tras cerrar p.144. La fase p.145–177 añadió sucesivamente promociones y falsos negativos documentados hasta alcanzar **2,302 artículos** tras p.177.

Los cierres más recientes fueron:

| Página | Corpus tras el pase | Censo exhaustivo | Pendientes tras cierre |
|---|---:|---:|---:|
| 170 | 2,017 | sí | 0 |
| 171 | 2,057 | sí | 0 |
| 172 | 2,101 | sí | 0 |
| 173 | 2,141 | sí | 0 |
| 174 | 2,181 | sí | 0 |
| 175 | 2,219 | sí | 0 |
| 176 | 2,257 | sí | 0 |
| 177 | **2,302** | sí | 0 |

## Página 177 — cierre terminal

La página digital **177** fue el último frente abierto de la subfase. El cotejo directo del facsímil estableció:

- **57 candidatos canónicos**;
- **60 inicios léxicos visibles**;
- **57 verdaderos positivos**;
- **3 falsos negativos**;
- **0 falsos positivos**;
- precisión **1.0**;
- recall **0.95**;
- F1 **0.9743589743589743**;
- **45 artículos nuevos**, `ALC1737-art-002258`–`ALC1737-art-002302`;
- **0 fronteras ambiguas** tras recotejo.

Los falsos negativos fueron `Vana eſtar la fruta`, `Venenoſo ſer` y `Veſtir`. Las dos ambigüedades antiguas se resolvieron directamente del mismo testimonio: `Velarſe` y `Vida`. También se corrigieron, preservando las lecturas previas en notas, `Ver. Bicha.` → `Veer. Bicha.` y `Vencer. Anibuc.` → `Vencer. Aiubuc.`.

El último artículo lexicográfico es **`Vomitar. Biſata.`**. Las páginas digitales **178–180** pertenecen al sistema numeral histórico y no constituyen continuación del Vocabulario.

## Autoridad y estado epistemológico

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` funciona únicamente como reimpresión histórica de control y nunca sustituye silenciosamente al testimonio de 1737. `BNF1737-REPORTED` permanece como testimonio independiente reportado pendiente de verificación directa.

`humanVerified` permanece en `false`. Una corrida QA verde confirma consistencia computacional de IDs, esquemas, reconciliaciones y derivados; no certifica corrección filológica humana.

## Incertidumbres todavía abiertas

El cierre estructural no elimina incertidumbres internas en artículos ya creados. Entre ellas permanecen:

- `ALC1737-art-001045` (`Atormentar`), con microestructura cahíta parcialmente incierta;
- discontinuidad material `ALC1737-gap-0001` entre digitales 157–158;
- algunas lecturas de baja confianza;
- anáforas `Lo miſmo` aún no resueltas como red editorial;
- remisiones `Buſca` todavía no cerradas como grafo;
- atribuciones históricas `Hiaqui`, `Mayo`, `Thehueco` y variantes todavía no inventariadas exhaustivamente.

Estas cuestiones pertenecen al siguiente nivel de consolidación editorial y semántica; no reabren la segmentación de páginas ya cerradas.

## Siguiente frente

El siguiente frente de Fase 3 es construir un **corpus maestro reproducible** a partir de los 2,302 artículos:

1. inventario maestro final de artículos históricos, separado del inventario de candidatos;
2. exportaciones JSONL, JSON y CSV canónicas y deterministas;
3. grafo de remisiones `Buſca`;
4. inventario de anáforas `Lo miſmo`;
5. inventario de atribuciones históricas internas;
6. validadores que impidan duplicados, destinos imposibles y deriva de exportaciones;
7. preparación posterior de TEI Lex-0 cuando la microestructura esté estabilizada.

La regla editorial continúa siendo la misma: **preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable.**
