# Revisión de remisiones históricas `Buſca`: estado de avance

Actualización: 21 de agosto de 2026.

## Alcance

Este documento registra el avance de la revisión post-cierre de las remisiones históricas del vocabulario de `ALC1737`. Debe leerse junto con `docs/CROSSREFERENCE_SOURCE_REVIEW_PROTOCOL.md` y no sustituye el grafo canónico estricto.

La arquitectura vigente conserva tres niveles separados: el **grafo canónico estricto**, que resuelve destinos únicamente por igualdad normalizada exacta; la **capa diagnóstica**, que prioriza los casos estrictamente no localizados mediante señales computacionales no vinculantes; y la **capa de revisión de fuente**, que registra decisiones editoriales explícitas con evidencia y autoridad declaradas.

## Estado canónico estricto

El inventario contiene **151 remisiones históricas**. El grafo estricto conserva **60 aristas `exact_unique`**, **90 remisiones `not_located`**, 1 remisión `not_busca` y 4 ciclos exactos. Estos conteos no se alteran por la revisión editorial posterior. Una propuesta de destino sustentada por fuente no se convierte retroactivamente en coincidencia estricta.

## Diagnóstico reproducible

La auditoría de las 90 remisiones estrictamente no localizadas conserva la clasificación original: **44 `A_unique_strong`**, **16 `B_multiple_strong`** y **30 `C_no_strong`**. Estas clases expresan prioridad diagnóstica, no resolución filológica.

## Revisión explícita acumulada

Se han registrado **52 revisiones explícitas**: los 44 casos Tier A y los primeros 8 casos Tier B. Todas mantienen `humanVerified=false`.

Del conjunto acumulado:

- **33** tienen `decisionStatus=source_supports_unique_target` y un `selectedTargetArticleId` explícito;
- 10 tienen `decisionStatus=source_or_destination_requires_recollation`;
- 5 tienen `decisionStatus=candidate_rejected`;
- 4 tienen `decisionStatus=target_not_located`.

La aritmética es deliberadamente explícita: 33 + 10 + 5 + 4 = 52. Las 33 propuestas editoriales no se promueven al grafo canónico estricto y ninguna equivale a validación humana.

## Tier A: cierre de revisión inicial

La revisión inicial `A_unique_strong` permanece cerrada **44/44**. Su distribución final es 29 propuestas editoriales, 8 recolaciones, 5 candidatos rechazados y 2 destinos no localizados. La evidencia detallada reside en los lotes `crossreference_source_review_batch01` a `batch06` y en la vista revisada reproducible.

Los ocho casos Tier A que requieren recolación directa de imagen son `Danzar`, `Apercibirſe para hazer algo`, `Yr delante`, `Loco bolverſe`, `Reglar con regla`, `Obligacion`, `Poco antes` y `Topo animal`. Entre ellos, `Poco antes` conserva una discrepancia material entre `targetRaw=mo hia mucho` y el OCR del testimonio, que muestra una remisión equivalente a `no ha mucho`; `Topo animal` conserva la diferencia `eſcarabajo` / `Eſcaravajo` sin normalizarla.

Los cinco candidatos Tier A rechazados son los asociados a `Nombrar, poner nombre`, `Rueda`, `Oprimido eſtar`, `Palillo oloroſo` y `Sazonarſe la fruta`. Los dos destinos no localizados son `Vadear el Rio → paſſar el Rio por vado` y `Vihuela, ó guitarra → guitarra`.

## Tier B: primera tanda, 8/16

El lote 07 inicia la revisión de `B_multiple_strong`, donde cada remisión presenta más de un candidato fuerte y, por tanto, el rango diagnóstico no basta para elegir destino.

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Yr por agua` — `Buſca agua traer` | `source_or_destination_requires_recollation`: el OCR fuente es ruidoso y compiten `Agua traer de la pila, ò del Rio` y `Agua traer para las manos`; `Agua` es demasiado genérico. |
| `Palo para eſcarbar tierra` — `Buſca coa` | `source_supports_unique_target` → `Coa de palo`; el descriptor `palo` excluye `Coa de hierro`. |
| `Piedra de que ſe ſacan navajas` — `Buſca pedernal prieto` | `source_supports_unique_target` → `Pedernal prieto para flechas`; preserva la secuencia remitida completa, a diferencia de `Prieto`. |
| `Plazo poner` — `Buſca ſeñalar dia` | `source_or_destination_requires_recollation`: el OCR de la remisión está degradado y los candidatos `Dia` y `Señalar` preservan sólo una parte del destino estructurado. |
| `Prieto` — `Buſca negro` | `source_supports_unique_target` → `Negro color`; `Negro hazer` cambia la función de la guía a una entrada verbal. |
| `Saltar` — `Buſca brincar` | `target_not_located`: sólo aparecen las guías especializadas `Brincar de alto abajo` y `Brincar por el ſuelo`; no se elige una sin evidencia de la distinción. |
| `Socorrer` — `Buſca ayudar` | `source_supports_unique_target` → `Ayudar à otro`; los demás candidatos fuertes son nominales o introducen contextos especializados (`Miſſa`, parto). |
| `Tener ſed` — `Buſca ſed tener` | `target_not_located`: el mejor candidato automático es la propia entrada por permutación de tokens y `Sed` sólo conserva una parte de la fórmula remitida. |

Este lote aporta 4 propuestas editoriales, 2 recolaciones y 2 destinos no localizados. No produce candidatos rechazados adicionales.

## Vista revisada derivada

`scripts/export_lexicon_crossreference_reviewed_view.py` genera una vista independiente que incorpora las decisiones editoriales sin alterar el grafo estricto. Con el lote 07, el estado esperado es:

- 151 remisiones representadas;
- 60 aristas estrictas con `edgeAuthority=strict_exact_normalized_equality`;
- 33 aristas editoriales con `edgeAuthority=editorial_source_review`;
- **93 aristas efectivas** en la vista revisada;
- **10 casos `editorial_requires_recollation`**;
- 5 casos `editorial_candidate_rejected`;
- 4 casos `editorial_target_not_located`;
- **38 casos `strict_not_located_unreviewed`**;
- 0 aristas editoriales `humanVerified=true`.

La vista se exporta en JSONL, CSV y grafo JSON y se valida mediante doble ejecución determinista byte a byte. Los hashes exactos pertenecen al manifiesto generado en cada estado.

## Cola reproducible de trabajo

La cola permanente `scripts/export_crossreference_review_queue.py` resta las 52 revisiones explícitas al universo de 90 remisiones estrictamente `not_located`. Después de este lote debe producir **38 casos pendientes**: 0 `A_unique_strong`, 8 `B_multiple_strong` y 30 `C_no_strong`.

El nivel A está, por tanto, agotado como cola de revisión inicial, y Tier B queda en 8/16. La siguiente tanda debe cubrir los ocho B restantes antes de pasar al nivel C.

## Criterio para Tier B

En Tier B no se acepta el primer candidato por rango. Una propuesta positiva requiere un discriminante observable en la fuente o en la estructura de las guías: preservación de la secuencia completa, descriptor explícito, función léxica compatible o exclusión clara de los candidatos alternativos. Si los candidatos sólo comparten material genérico, si el OCR fuente no permite leer la remisión con suficiente precisión o si elegir exige introducir una distinción no expresada, el caso permanece en recolación o como destino no localizado.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica fuerte no es una resolución. Un candidato rechazado no desaparece de la historia de revisión. Un destino no localizado no debe sustituirse por una coincidencia aproximada. Cerrar un nivel de revisión significa que todos sus casos recibieron una decisión explícita; no significa que todos produjeron resoluciones positivas ni que exista validación filológica humana. Una corrida verde de QA no es validación filológica humana.**
