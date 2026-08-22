# Revisión de remisiones históricas `Buſca`: estado de avance

Actualización: 21 de agosto de 2026.

## Alcance

Este documento registra el avance de la revisión post-cierre de las remisiones históricas del vocabulario de `ALC1737`. Debe leerse junto con `docs/CROSSREFERENCE_SOURCE_REVIEW_PROTOCOL.md` y no sustituye el grafo canónico estricto.

La arquitectura vigente conserva tres niveles separados: el **grafo canónico estricto**, que resuelve destinos únicamente por igualdad normalizada exacta; la **capa diagnóstica**, que prioriza los casos estrictamente no localizados mediante señales computacionales no vinculantes; y la **capa de revisión de fuente**, que registra decisiones editoriales explícitas con evidencia y autoridad declaradas.

## Estado canónico estricto

El inventario contiene **151 remisiones históricas**. El grafo estricto conserva **60 aristas `exact_unique`**, **90 remisiones `not_located`**, 1 remisión `not_busca` y 4 ciclos exactos. Estos conteos no se alteran por la revisión editorial posterior.

## Diagnóstico reproducible

La auditoría de las 90 remisiones estrictamente no localizadas conserva la clasificación original: **44 `A_unique_strong`**, **16 `B_multiple_strong`** y **30 `C_no_strong`**. Estas clases expresan prioridad diagnóstica, no resolución filológica.

## Revisión explícita acumulada

Se han registrado **68 revisiones explícitas**: los 44 casos Tier A, los 16 casos Tier B y los primeros 8 casos Tier C. Todas mantienen `humanVerified=false`.

Del conjunto acumulado:

- **39** tienen `decisionStatus=source_supports_unique_target` y un `selectedTargetArticleId` explícito;
- 15 tienen `decisionStatus=source_or_destination_requires_recollation`;
- 5 tienen `decisionStatus=candidate_rejected`;
- 9 tienen `decisionStatus=target_not_located`.

La aritmética es 39 + 15 + 5 + 9 = 68. Las propuestas editoriales no se promueven al grafo canónico estricto y ninguna equivale a validación humana.

## Tier A: cierre de revisión inicial

La revisión inicial `A_unique_strong` permanece cerrada **44/44**. Su distribución final es 29 propuestas editoriales, 8 recolaciones, 5 candidatos rechazados y 2 destinos no localizados.

## Tier B: cierre de revisión inicial

La revisión inicial `B_multiple_strong` permanece cerrada **16/16**. Su distribución final es 8 propuestas editoriales, 4 recolaciones y 4 destinos no localizados. En este nivel nunca se eligió un candidato sólo por ocupar el primer rango diagnóstico.

## Tier C: primera tanda, 8/30

El lote 09 inicia `C_no_strong`. En este nivel las similitudes débiles se usan sólo como pistas de búsqueda; las decisiones se apoyan en control textual directo, variantes gráficas, estructura de guía y evidencia del mismo testimonio.

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Baſta, coſa ſin pulir` — `Buſca aſpero` | `source_supports_unique_target` → `Aſpera coſa`; la fuente remite al adjetivo y el destino conserva la flexión femenina exigida por `coſa`. |
| `Cueva` — `Buſca caverna` | `source_supports_unique_target` → `Caberna, ò cueva`; recuperación por variante histórica `b/v` en el mismo testimonio. |
| `Culpar à otro` — `Buſca acuſar` | `target_not_located`; la remisión es legible, pero no se localizó una entrada independiente `Acuſar`. |
| `Empacharſe` — `Buſca hartarſe` | `source_or_destination_requires_recollation`; el OCR destruye parcialmente el target y no debe sustituirse por el débil candidato `Ahitarſe`. |
| `Henchimiento` — `Buſca llenar` | `source_or_destination_requires_recollation`; la remisión está gravemente dañada en OCR y no se localizó una guía independiente `Llenar`. |
| `Holgarſe` — `Buſca gozarſe` | `source_or_destination_requires_recollation`; la fórmula está dañada en OCR. La gramática atestigua `gozarſe`, pero eso no constituye un destino lexicográfico. |
| `Jubilo` — `Buſca gozo` | `target_not_located`; `gozo` está atestiguado en la gramática, pero no aparece una guía lexicográfica independiente localizada. |
| `Legumbres` — `Buſca frixol, habas, &c.` | `target_not_located`; la remisión listada es legible, pero las ocurrencias localizadas de `frixol` o `habas` pertenecen a guías especializadas distintas. |

El lote aporta 2 propuestas editoriales, 3 recolaciones y 3 destinos no localizados. No añade candidatos rechazados.

Dos resultados son metodológicamente relevantes. `Cueva → Caberna, ò cueva` demuestra que un caso Tier C puede resolverse editorialmente mediante una variante histórica `b/v` que el diagnóstico de similitud no elevó a candidato fuerte. `Baſta, coſa ſin pulir → Aſpera coſa` muestra que una flexión de género explícitamente motivada por la guía puede recuperar el destino sin convertir fuzzy matching en política de resolución.

## Vista revisada derivada

`scripts/export_lexicon_crossreference_reviewed_view.py` genera una vista independiente que incorpora las decisiones editoriales sin alterar el grafo estricto. Tras el lote 09, el estado esperado es:

- 151 remisiones representadas;
- 60 aristas estrictas con `edgeAuthority=strict_exact_normalized_equality`;
- 39 aristas editoriales con `edgeAuthority=editorial_source_review`;
- **99 aristas efectivas** en la vista revisada;
- **15 casos `editorial_requires_recollation`**;
- 5 casos `editorial_candidate_rejected`;
- 9 casos `editorial_target_not_located`;
- **22 casos `strict_not_located_unreviewed`**;
- 0 aristas editoriales `humanVerified=true`.

La vista se exporta en JSONL, CSV y grafo JSON y se valida mediante doble ejecución determinista byte a byte. Los hashes exactos pertenecen al manifiesto generado en cada estado.

## Cola reproducible de trabajo

La cola permanente `scripts/export_crossreference_review_queue.py` resta las 68 revisiones explícitas al universo de 90 remisiones estrictamente `not_located`. El nuevo corte debe producir **22 casos pendientes**: 0 `A_unique_strong`, 0 `B_multiple_strong` y 22 `C_no_strong`.

Tier C queda en **8/30**. Los siguientes casos deben seguir tratándose mediante búsqueda textual dirigida y control de variantes antes de considerar cualquier candidato débil.

## Criterio para Tier C

Tier C no autoriza ampliar automáticamente el umbral ni convertir similitud débil en resolución. Se distingue entre remisión legible con destino ausente, remisión OCR dañada, variante gráfica recuperable, flexión morfológica explícita, error de segmentación o procedencia y ausencia real de candidato en el corpus estructurado. Cualquier recuperación de destino se registra como revisión editorial explícita y no como mutación retroactiva del grafo estricto.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica no es una resolución. Un candidato rechazado no desaparece de la historia de revisión. Un destino no localizado no debe sustituirse por una coincidencia aproximada. Cerrar un nivel de revisión significa que todos sus casos recibieron una decisión explícita; no significa que todos produjeron resoluciones positivas ni que exista validación filológica humana. Una corrida verde de QA no es validación filológica humana.**
