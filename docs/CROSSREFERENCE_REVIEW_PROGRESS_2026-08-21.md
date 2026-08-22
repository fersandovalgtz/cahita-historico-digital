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

Se han registrado **60 revisiones explícitas**: los 44 casos Tier A y los 16 casos Tier B. Todas mantienen `humanVerified=false`.

Del conjunto acumulado:

- **37** tienen `decisionStatus=source_supports_unique_target` y un `selectedTargetArticleId` explícito;
- 12 tienen `decisionStatus=source_or_destination_requires_recollation`;
- 5 tienen `decisionStatus=candidate_rejected`;
- 6 tienen `decisionStatus=target_not_located`.

La aritmética es 37 + 12 + 5 + 6 = 60. Las propuestas editoriales no se promueven al grafo canónico estricto y ninguna equivale a validación humana.

## Tier A: cierre de revisión inicial

La revisión inicial `A_unique_strong` permanece cerrada **44/44**. Su distribución final es 29 propuestas editoriales, 8 recolaciones, 5 candidatos rechazados y 2 destinos no localizados.

Los ocho casos Tier A que requieren recolación directa de imagen son `Danzar`, `Apercibirſe para hazer algo`, `Yr delante`, `Loco bolverſe`, `Reglar con regla`, `Obligacion`, `Poco antes` y `Topo animal`. Los cinco candidatos Tier A rechazados son los asociados a `Nombrar, poner nombre`, `Rueda`, `Oprimido eſtar`, `Palillo oloroſo` y `Sazonarſe la fruta`. Los dos destinos no localizados son `Vadear el Rio → paſſar el Rio por vado` y `Vihuela, ó guitarra → guitarra`.

## Tier B: cierre de revisión inicial, 16/16

La revisión inicial `B_multiple_strong` queda cerrada **16/16**. En este nivel nunca se eligió un candidato sólo por ocupar el primer rango diagnóstico: cada propuesta positiva exige un discriminante observable en la guía histórica, la secuencia remitida o la función lexicográfica.

### Lote 07

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Yr por agua` — `Buſca agua traer` | `source_or_destination_requires_recollation`: compiten dos destinos extendidos y el OCR fuente es ruidoso. |
| `Palo para eſcarbar tierra` — `Buſca coa` | `source_supports_unique_target` → `Coa de palo`; el descriptor `palo` excluye `Coa de hierro`. |
| `Piedra de que ſe ſacan navajas` — `Buſca pedernal prieto` | `source_supports_unique_target` → `Pedernal prieto para flechas`; preserva la secuencia remitida completa. |
| `Plazo poner` — `Buſca ſeñalar dia` | `source_or_destination_requires_recollation`: el OCR de la remisión está degradado y `Dia` / `Señalar` son sólo parciales. |
| `Prieto` — `Buſca negro` | `source_supports_unique_target` → `Negro color`; `Negro hazer` cambia la función de la guía. |
| `Saltar` — `Buſca brincar` | `target_not_located`: sólo se localizan guías especializadas `Brincar...`. |
| `Socorrer` — `Buſca ayudar` | `source_supports_unique_target` → `Ayudar à otro`; los demás candidatos son nominales o especializados. |
| `Tener ſed` — `Buſca ſed tener` | `target_not_located`: el mejor diagnóstico es un auto-candidato y `Sed` sólo conserva un componente. |

### Lote 08

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Favorecer` — `Buſca ayudar` | `source_supports_unique_target` → `Ayudar à otro`; `Ayuda` es nominal y las otras entradas de `Ayudar` son especializadas. |
| `Horadar` — `Buſca agujerear` | `target_not_located`: las cuatro guías `Agujerear...` localizadas son especializadas por instrumento u objeto; no se fuerza una como destino genérico. |
| `Mitad de alguna coſa` — `Buſca media` | `source_supports_unique_target` → `Media coſa la mitad`; la alternativa `A media noche` es temporal/adverbial. |
| `Oprimir` — `Buſca apretar` | `target_not_located`: sólo se localizan cinco guías `Apretar...` especializadas; ninguna está autorizada por la guía genérica `Oprimir`. |
| `Ribera de qualquiera agua` — `Buſca orilla` | `source_supports_unique_target` → `Orilla del agua`; conserva función nominal y el descriptor `agua`, a diferencia de `Abordar à la orilla`. |
| `Sanar á otro` — `Buſca curar` | `source_supports_unique_target` → `Curar enfermedad`; el otro candidato contiene `curar` sólo dentro de una descripción de `Arbol`. |
| `Simiente` — `Buſca orilla` | `source_or_destination_requires_recollation`: el OCR parece conservar la remisión, pero la relación fuente-destino es anómala y debe cotejarse con la imagen antes de crear arista. |
| segundo `Sueño tal` — `Buſca ſueño` | `source_or_destination_requires_recollation`: el OCR muestra dos `Sueño tal` consecutivos, uno con contenido y otro remisivo; no se colapsan ni se enlazan sin cotejo directo de los límites impresos. |

La distribución final de Tier B es 8 propuestas editoriales, 4 recolaciones y 4 destinos no localizados. No añadió candidatos rechazados.

## Vista revisada derivada

`scripts/export_lexicon_crossreference_reviewed_view.py` genera una vista independiente que incorpora las decisiones editoriales sin alterar el grafo estricto. Tras el cierre de Tier B, el estado esperado es:

- 151 remisiones representadas;
- 60 aristas estrictas con `edgeAuthority=strict_exact_normalized_equality`;
- 37 aristas editoriales con `edgeAuthority=editorial_source_review`;
- **97 aristas efectivas** en la vista revisada;
- **12 casos `editorial_requires_recollation`**;
- 5 casos `editorial_candidate_rejected`;
- 6 casos `editorial_target_not_located`;
- **30 casos `strict_not_located_unreviewed`**;
- 0 aristas editoriales `humanVerified=true`.

La vista se exporta en JSONL, CSV y grafo JSON y se valida mediante doble ejecución determinista byte a byte. Los hashes exactos pertenecen al manifiesto generado en cada estado.

## Cola reproducible de trabajo

La cola permanente `scripts/export_crossreference_review_queue.py` resta las 60 revisiones explícitas al universo de 90 remisiones estrictamente `not_located`. El nuevo corte debe producir **30 casos pendientes**: 0 `A_unique_strong`, 0 `B_multiple_strong` y 30 `C_no_strong`.

Los niveles A y B están agotados como colas de revisión inicial. El siguiente frente es `C_no_strong`, donde el diagnóstico no ofrece candidato fuerte alguno y la búsqueda debe apoyarse más en control textual, variantes gráficas, estructura local y eventual cotejo de facsímil.

## Criterio para Tier C

Tier C no autoriza ampliar automáticamente el umbral ni convertir similitud débil en resolución. Se debe distinguir entre: remisión legible con destino ausente; remisión OCR dañada; posible variante gráfica; error de segmentación o procedencia; y ausencia real de candidato en el corpus estructurado. Cualquier recuperación de destino debe registrarse como revisión editorial explícita y no como mutación retroactiva del grafo estricto.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica no es una resolución. Un candidato rechazado no desaparece de la historia de revisión. Un destino no localizado no debe sustituirse por una coincidencia aproximada. Cerrar un nivel de revisión significa que todos sus casos recibieron una decisión explícita; no significa que todos produjeron resoluciones positivas ni que exista validación filológica humana. Una corrida verde de QA no es validación filológica humana.**
