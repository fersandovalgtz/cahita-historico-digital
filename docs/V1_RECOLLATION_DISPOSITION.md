# Cahíta Histórico Digital — disposición v1.0 de las 22 recolaciones

Fecha: 21 de agosto de 2026.

## Decisión de release

Los **22 casos** actualmente clasificados como `source_or_destination_requires_recollation` se incorporan a v1.0 como **incertidumbres filológicas abiertas explícitas** (`frozen_open_uncertainty`). Esta decisión cierra el gate de release asociado a su tratamiento, pero **no resuelve filológicamente los casos**.

La distinción es deliberada:

- **gate de v1.0:** cerrado porque cada incertidumbre está identificada, trazable, reproducible y declarada;
- **resolución filológica:** abierta porque todavía requiere cotejo directo contra imagen del mismo testimonio o revisión filológica humana explícita.

## Estado cuantitativo

La cola canónica contiene 22 casos:

- 8 `A_unique_strong`;
- 4 `B_multiple_strong`;
- 10 `C_no_strong`.

Para los 22, la disposición v1.0 exige:

- `disposition = frozen_open_uncertainty`;
- `releaseScope = v1.0`;
- `canonicalAction = none`;
- `selectedTargetArticleId = null`;
- `humanVerified = false`;
- `sourceEvidenceStatus = insufficient_without_direct_same_witness_facsimile_recollation`.

## Qué no significa esta decisión

No significa que existan 22 errores confirmados. Tampoco significa que el OCR sea incorrecto en los 22 casos. Significa únicamente que la evidencia disponible no autoriza cerrar el destino o la lectura mediante reglas automáticas.

La capa v1.0 no acepta como sustituto del facsímil:

- OCR del mismo testimonio;
- similitud ortográfica o fuzzy matching;
- proximidad semántica;
- candidatos diagnósticos de Tier A/B/C;
- analogía con entradas próximas;
- testimonios posteriores usados sin una justificación editorial independiente.

## Evidencia requerida para una futura resolución

Un caso puede reabrirse después de v1.0 cuando exista al menos una de estas condiciones:

1. cotejo directo y documentado contra la página/columna del mismo testimonio `ALC1737`;
2. revisión filológica humana explícita con evidencia suficiente y trazabilidad a la fuente.

Una resolución futura deberá conservar el historial de la disposición v1.0 y distinguir entre corrección de lectura, identificación de destino y decisión editorial.

## Implementación reproducible

`scripts/export_v1_recollation_disposition.py` deriva la disposición directamente de la cola canónica de recolación y genera JSONL, CSV y manifiesto.

`scripts/validate_v1_recollation_disposition.py` exige:

- identidad exacta 22/22 con la cola fuente;
- tiers 8/4/10;
- cero destinos seleccionados;
- cero cambios canónicos;
- `humanVerified=0`;
- grafo estricto conservado en 60 `exact_unique` + 90 `not_located`;
- doble exportación determinista byte-a-byte;
- `philologicalResolutionStatus=open`.

## Consecuencia para v1.0

La existencia de estas 22 incertidumbres **no impide una release científica estable** siempre que se publiquen como tales. Una edición histórico-digital reproducible puede ser estable sin fingir una colación humana completa.

Por ello el gate `direct_facsimile_recollation_of_22_crossreference_cases` deja de ser un bloqueo de v1.0 y pasa al backlog filológico post-v1. El estado `humanVerified=0` permanece sin cambio.
