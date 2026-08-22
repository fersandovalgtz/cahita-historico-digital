# CHD — cola de recolación directa de remisiones `Buſca`

Fecha de referencia: 21 de agosto de 2026.

## Alcance

La primera revisión editorial de las 90 remisiones `Buſca` que no resolvían por igualdad estricta ya está completa. Dentro de esas 90 revisiones, **22 casos** permanecen con `decisionStatus=source_or_destination_requires_recollation`.

Estos 22 casos no son fronteras lexicográficas pendientes ni artículos sin estructurar. Son lecturas puntuales en las que el OCR del mismo testimonio, la estructura canónica o los candidatos diagnósticos no bastan para confirmar con seguridad la remisión o su destino. Su resolución exige cotejo directo contra imagen del testimonio `ALC1737`.

## Artefacto derivado

`scripts/export_crossreference_recollation_queue.py` reconstruye una cola determinista desde los archivos `data/lexicon/review/crossreference_source_review_*.jsonl` y selecciona exclusivamente los registros con:

`source_or_destination_requires_recollation`

El exportador produce:

- `chd_crossreference_recollation_queue.jsonl`;
- `chd_crossreference_recollation_queue.csv`;
- `manifest.json` con conteos, fuentes y SHA-256 de los artefactos.

La cola actual contiene **22 casos** distribuidos en:

- **8** `A_unique_strong`;
- **4** `B_multiple_strong`;
- **10** `C_no_strong`.

El orden prioriza primero el tier diagnóstico y después página, columna y `articleId`. Este orden es de trabajo, no de autoridad filológica.

## Regla de resolución

Un caso sale de esta cola únicamente cuando existe evidencia suficiente para cambiar explícitamente su `decisionStatus` en la capa de revisión. El procedimiento recomendado es:

1. abrir la página digital de origen en el testimonio `ALC1737`;
2. verificar guía castellana, marcador `Buſca` y lectura exacta del destino remitido;
3. cuando corresponda, abrir también la página del artículo de destino candidato;
4. registrar evidencia de tipo `same_witness_facsimile` con localizador reproducible;
5. decidir entre destino único sustentado, múltiples destinos sustentados, candidato rechazado, destino no localizado o permanencia en recolación;
6. mantener `humanVerified=false` mientras la decisión siga siendo una revisión IA-asistida sin una persona identificable que haya certificado el cotejo filológico.

## Guardas metodológicas

La cola **no** modifica el grafo canónico estricto, no convierte similitud diagnóstica en enlace, no completa OCR por analogía y no interpreta una corrida verde de CI como validación filológica humana.

La evidencia OCR puede ayudar a localizar un punto de lectura, pero el criterio específico de salida de esta cola es la consulta de imagen del mismo testimonio o una justificación editorial explícita de por qué el destino no puede determinarse.

## QA

`scripts/validate_crossreference_recollation_queue.py` verifica:

- que la cola sea exactamente el subconjunto de registros en estado de recolación;
- 22 casos únicos;
- distribución vigente 8 A / 4 B / 10 C;
- `humanVerified=0`;
- doble exportación byte-a-byte idéntica;
- hashes deterministas;
- ausencia de modificación del grafo estricto.

Este artefacto convierte el principal pendiente filológico lexicográfico de CHD en una cola finita, reproducible y auditable.