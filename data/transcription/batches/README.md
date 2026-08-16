# Lotes de transcripción

Los archivos de esta carpeta registran lotes incrementales de transcripción diplomática por página.

## Relación con `status.csv`

`data/transcription/status.csv` es el manifiesto maestro. En el estado actual está consolidado hasta la página digital 91 / impresa 77. Los lotes posteriores funcionan como **deltas versionados** hasta la próxima consolidación reproducible del manifiesto:

- `part_iii_p092_p096.csv`
- `part_iii_p097_p101.csv`
- `part_iii_iv_p102_p106.csv`

La cobertura efectiva del proyecto debe leerse en `COVERAGE.md`, que combina el manifiesto consolidado y estos deltas. Esta separación evita reescribir manualmente un manifiesto extenso mientras avanza la transcripción y mantiene trazabilidad de cada bloque de ingestión.

Una futura tarea de QA deberá regenerar `status.csv` desde las unidades JSON por página y los lotes, comparar la salida con el manifiesto anterior y validar que no existan páginas duplicadas, faltantes ni regresiones de estado.
