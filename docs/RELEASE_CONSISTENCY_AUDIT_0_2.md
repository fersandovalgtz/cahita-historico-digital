# Auditoría de consistencia documental — serie 0.2.x

Fecha: 2026-08-20

## Estado actual

Cahíta Histórico Digital permanece en `0.2.0-dev`. Esta auditoría no modifica el estado de release; documenta la coherencia entre los principales archivos de gobernanza.

## Elementos revisados

- README.md
- CITATION.cff
- CHANGELOG.md
- ROADMAP.md
- documentos de cobertura y QA

## Hallazgos

### Coherencias

- El repositorio mantiene una separación explícita entre fuente histórica, OCR, capas computacionales y capas curatoriales.
- Las métricas principales se expresan como estados derivados de fuentes canónicas.
- La ausencia de `human_verified` se mantiene documentada.
- La versión actual se presenta correctamente como desarrollo y no como release científica.

### Pendientes antes de una versión estable

- completar la reconciliación del vocabulario hasta p.177;
- consolidar las métricas finales de cobertura;
- revisar que CITATION.cff, README y CHANGELOG compartan la misma versión objetivo;
- definir los artefactos definitivos de una release archivada.

## Criterio de salida

No se propone todavía una etiqueta `v1.0.0`. La liberación estable requiere que los datos canónicos, la documentación y los metadatos de citación representen el mismo estado del corpus.
