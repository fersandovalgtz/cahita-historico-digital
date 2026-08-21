# Protocolo de revisión de remisiones históricas `Buſca`

Actualización: 21 de agosto de 2026.

## Propósito

Este protocolo regula la revisión explícita de remisiones históricas `Buſca` cuyo destino no puede resolverse mediante la política canónica vigente de igualdad normalizada estricta entre `targetRaw` y `spanishGuideRaw`.

La revisión de fuente constituye una capa editorial separada. No modifica silenciosamente el grafo canónico ni convierte una semejanza gráfica, léxica o semántica en enlace histórico.

## Estado de partida

El inventario canónico contiene 151 remisiones históricas. De ellas, 150 pertenecen a la clase `Buſca`; 60 tienen una resolución estricta única, 90 permanecen `not_located` y una referencia no pertenece a la clase `Buſca`. El grafo estricto conserva cuatro ciclos exactos.

La auditoría diagnóstica post-cierre clasifica los 90 casos `not_located` en tres niveles operativos:

- `A_unique_strong`: un único candidato diagnóstico fuerte mostrado;
- `B_multiple_strong`: más de un candidato diagnóstico fuerte mostrado;
- `C_no_strong`: ningún candidato supera el umbral diagnóstico fuerte.

El umbral `0.90` es una regla de priorización computacional, no un umbral de verdad filológica.

## Cola reproducible de trabajo

`scripts/export_crossreference_review_queue.py` deriva la cola activa mediante una operación explícita: inventario diagnóstico de referencias estrictamente `not_located` menos registros de revisión de fuente ya existentes. La cola es, por tanto, estado de workflow reproducible; no es una nueva capa de resolución.

El exportador genera JSONL, CSV y un manifiesto con hashes, y conserva en cada fila la prioridad A/B/C, la remisión histórica y los candidatos diagnósticos. Para inspeccionar el siguiente lote sin crear instrumentación temporal puede utilizarse, por ejemplo:

```bash
python scripts/export_crossreference_review_queue.py --print-next 8 --tier A_unique_strong
```

`--print-next` y `--tier` afectan únicamente la salida de inspección en consola; los archivos exportados siguen conteniendo la cola completa y determinista. La cola no promueve candidatos a destinos editoriales, no crea aristas y no modifica artículos canónicos.

## Evidencia admisible

Una decisión editorial debe registrar al menos una evidencia explícita y localizable. Se distinguen cinco clases:

1. `same_witness_facsimile`: cotejo visual del ejemplar ALC1737;
2. `same_witness_ocr_control`: OCR del mismo testimonio, usado únicamente como ayuda de localización o control;
3. `canonical_article_structure`: evidencia procedente de los artículos históricos ya estructurados en CHD;
4. `historical_control_witness`: comparación con un testimonio histórico independiente o una reimpresión documentada;
5. `editorial_note`: razonamiento editorial que no sustituye la evidencia primaria.

Cuando facsímil y OCR discrepen, prevalece el facsímil. Un testimonio de control no sustituye silenciosamente la lectura de ALC1737.

## Estados de decisión

`pending_source_collation` indica que el caso sólo ha sido priorizado. `source_supports_unique_target` se utiliza únicamente cuando la evidencia material permite identificar un destino histórico concreto. `source_supports_multiple_targets` conserva una ambigüedad real. `candidate_rejected` documenta que los candidatos diagnósticos inspeccionados no sostienen la remisión. `target_not_located` registra que la búsqueda explícita no identificó destino. `source_or_destination_requires_recollation` abre una incidencia textual previa. `unresolved` conserva cualquier caso que no deba forzarse.

Toda decisión `source_supports_unique_target` debe declarar `selectedTargetArticleId` y evidencia positiva. La selección no autoriza por sí sola a alterar `crossReferences` en los artículos canónicos.

## Autoridad y revisión

Los registros IA-asistidos permanecen `machine_corrected_unverified` o `unresolved` y `humanVerified=false`. `editorial_proposal` identifica una propuesta editorial explícita que todavía no constituye validación humana independiente. `human_verified` sólo puede utilizarse conjuntamente con `humanVerified=true`.

## Separación de capas

La arquitectura conserva cuatro objetos con autoridad distinta:

- **grafo canónico estricto:** igualdad normalizada exacta; reproducible; sin fuzzy matching;
- **diagnóstico computacional:** candidatos priorizados mediante señales transparentes; no vinculante;
- **revisión de fuente:** decisiones editoriales explícitas con evidencia, procedencia y autoridad declaradas;
- **vista revisada derivada:** superposición reproducible de aristas estrictas y propuestas editoriales aceptadas, manteniendo `edgeAuthority` diferenciado.

La vista revisada no reemplaza el grafo estricto ni se presenta como resultado puramente computacional. La cola de trabajo tampoco constituye una quinta autoridad: sólo organiza los casos que todavía carecen de registro de revisión.

## Orden de trabajo

La revisión empieza por `A_unique_strong`, porque concentra los casos con mayor rendimiento esperado. Dentro de ese nivel se priorizan primero: inversiones completas de tokens, variantes gráficas de alta similitud y remisiones cuyo destino candidato contiene de forma inequívoca la expresión remitida como secuencia de palabras completas. Después se revisan `B_multiple_strong` y finalmente `C_no_strong`.

Las coincidencias con palabras demasiado generales —por ejemplo `cosa`, `estar`, `agua`, `orilla`— requieren especial cautela aunque obtengan puntuaciones altas.

## Criterio de cierre

La revisión de remisiones no se considerará cerrada por reducción numérica automática. El cierre exigirá que los 90 casos `not_located` tengan un registro de revisión explícito y validado por esquema, que las decisiones estén respaldadas por evidencia localizable y que cualquier vista derivada preserve la distinción entre resolución estricta, propuesta editorial y validación humana.
