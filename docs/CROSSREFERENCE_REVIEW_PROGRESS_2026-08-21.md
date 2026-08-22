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

Se han registrado **76 revisiones explícitas**: los 44 casos Tier A, los 16 casos Tier B y 16 de los 30 casos Tier C. Todas mantienen `humanVerified=false`.

Del conjunto acumulado:

- **40** tienen `decisionStatus=source_supports_unique_target` y un `selectedTargetArticleId` explícito;
- 16 tienen `decisionStatus=source_or_destination_requires_recollation`;
- 5 tienen `decisionStatus=candidate_rejected`;
- 15 tienen `decisionStatus=target_not_located`.

La aritmética es 40 + 16 + 5 + 15 = 76. Las propuestas editoriales no se promueven al grafo canónico estricto y ninguna equivale a validación humana.

## Tier A y Tier B

`A_unique_strong` permanece cerrado **44/44**: 29 propuestas editoriales, 8 recolaciones, 5 candidatos rechazados y 2 destinos no localizados. `B_multiple_strong` permanece cerrado **16/16**: 8 propuestas editoriales, 4 recolaciones y 4 destinos no localizados.

## Tier C: 16/30

En `C_no_strong` las similitudes débiles se usan sólo como pistas. Una recuperación fuera del shortlist diagnóstico únicamente es admisible si existe evidencia positiva del mismo testimonio y evidencia de estructura canónica; nunca se transforma en coincidencia estricta.

### Lote 09

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Baſta, coſa ſin pulir` — `Buſca aſpero` | `source_supports_unique_target` → `Aſpera coſa`; flexión femenina motivada por `coſa`. |
| `Cueva` — `Buſca caverna` | `source_supports_unique_target` → `Caberna, ò cueva`; variante histórica `b/v`. |
| `Culpar à otro` — `Buſca acuſar` | `target_not_located`. |
| `Empacharſe` — `Buſca hartarſe` | `source_or_destination_requires_recollation`. |
| `Henchimiento` — `Buſca llenar` | `source_or_destination_requires_recollation`. |
| `Holgarſe` — `Buſca gozarſe` | `source_or_destination_requires_recollation`. |
| `Jubilo` — `Buſca gozo` | `target_not_located`. |
| `Legumbres` — `Buſca frixol, habas, &c.` | `target_not_located`. |

El lote 09 aportó 2 propuestas editoriales, 3 recolaciones y 3 destinos no localizados.

### Lote 10

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Mozo de edad` — `Buſca mancebo` | `target_not_located`; la remisión es legible, pero no existe una guía independiente `Mancebo` localizada. |
| `Montear` — `Buſca caçar` | `source_supports_unique_target` → `Cazar ſalir a caza`; la guía expresa la salida general de caza y excluye la entrada especializada `Cazar con ratonera`. |
| `Orejear` — `Buſca menear las orejas` | `source_or_destination_requires_recollation`; el OCR destruye parte material de la fórmula y no se sustituye por `Menear la cabeza`. |
| `Orina` — `Buſca meados` | `target_not_located`; no se localizó guía independiente `Meados`. |
| `Orinar` — `Buſca mear` | `target_not_located`; no se localizó guía independiente `Mear`. |
| `Oſado ſer` — `Buſca atrevido` | `target_not_located`; el target se conserva localmente, pero no aparece una guía independiente `Atrevido`. |
| `Placer regocijo` — `Buſca gozo` | `target_not_located`; `gozo` está atestiguado fuera del vocabulario, pero no como destino lexicográfico independiente. |
| `Pleyto aver` — `Buſca pelear` | `target_not_located`; `Pelearſe` no se colapsa con el target no reflexivo `pelear`. |

El lote 10 aporta 1 propuesta editorial, 1 recolación y 6 destinos no localizados. La recuperación `Montear → Cazar ſalir a caza` procede de evidencia semántica y estructural del mismo testimonio, no de los candidatos gráficos `Cabar`, `Cagar` o `Capar`.

## Vista revisada derivada

Tras el lote 10, la vista revisada debe contener:

- 151 remisiones representadas;
- 60 aristas estrictas con `edgeAuthority=strict_exact_normalized_equality`;
- 40 aristas editoriales con `edgeAuthority=editorial_source_review`;
- **100 aristas efectivas**;
- **16 casos `editorial_requires_recollation`**;
- 5 casos `editorial_candidate_rejected`;
- 15 casos `editorial_target_not_located`;
- **14 casos `strict_not_located_unreviewed`**;
- 0 aristas editoriales `humanVerified=true`.

Los exportadores JSONL, CSV y grafo JSON se validan mediante doble ejecución determinista byte a byte.

## Cola reproducible de trabajo

La cola permanente resta las **76 revisiones explícitas** al universo de 90 remisiones estrictamente `not_located`. Después del lote 10 debe producir **14 pendientes**: 0 `A_unique_strong`, 0 `B_multiple_strong` y 14 `C_no_strong`.

Tier C queda en **16/30**. El siguiente frente son los 14 casos finales, manteniendo búsqueda textual dirigida, variantes históricas y recolación explícita cuando el OCR no permite sostener una decisión.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica no es una resolución. Un candidato rechazado no desaparece de la historia de revisión. Un destino no localizado no debe sustituirse por una coincidencia aproximada. Cerrar un nivel significa que todos sus casos recibieron una decisión explícita; no que todos produjeron resoluciones positivas ni que exista validación filológica humana. Una corrida verde de QA no es validación filológica humana.**
