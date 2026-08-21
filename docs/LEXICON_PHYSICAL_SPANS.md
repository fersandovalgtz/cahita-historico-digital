# Auditoría reproducible de `sourceSpans` y continuidades físicas

## Objetivo

Esta capa identifica los artículos del vocabulario que ya contienen metadatos de continuidad física —`sourceSpans`, `continuesFromPreviousPage` o `continuesToNextPage`— y los somete a una auditoría estructural conservadora.

No modifica los artículos canónicos y no corrige automáticamente ninguna lectura o continuidad.

El generador es:

```bash
python scripts/export_lexicon_physical_spans.py
```

Por omisión produce:

- `build/lexicon-physical-spans/chd_lexicon_physical_spans_audit.jsonl`
- `build/lexicon-physical-spans/chd_lexicon_physical_spans_audit.csv`
- `build/lexicon-physical-spans/manifest.json`

## Qué se deriva

Para cada artículo con alguna señal física se calculan:

- número de `sourceSpans`;
- número de páginas y columnas distintas representadas;
- `crossPageDerived`;
- `crossColumnDerived`;
- las banderas históricas `continuesFromPreviousPage` y `continuesToNextPage`;
- una lista `auditFlags` de posibles discordancias estructurales.

## Banderas de auditoría

Las banderas no significan por sí mismas que el artículo esté mal. Señalan casos que merecen cotejo editorial:

- `continuity_flag_without_source_spans`: existe una bandera de continuidad de página pero no una secuencia explícita de spans;
- `cross_page_source_spans_without_page_continuity_flag`: los spans abarcan más de una página pero las banderas de continuidad no lo expresan;
- `article_source_page_absent_from_source_spans`: la página principal del artículo no aparece dentro de sus spans;
- `article_source_column_absent_from_source_spans`: la columna principal no aparece dentro de sus spans;
- `page_continuity_flag_with_single_source_span`: existe continuidad de página pero sólo se conserva un span.

Estas comprobaciones son deliberadamente mínimas. No se infieren roles `start/end`, no se reconstruyen spans faltantes y no se cambia el artículo fuente.

## Guardas epistemológicas

El manifiesto declara expresamente:

- `automaticRepairPerformed: false`;
- `philologicalCorrectionInferred: false`.

Un hallazgo de auditoría es una señal de consistencia computacional, no una decisión filológica.

## Uso siguiente

Después de obtener el inventario cuantificado, los artículos marcados pueden revisarse uno por uno contra sus reconciliaciones y, cuando sea necesario, contra el facsímil ALC1737. Cualquier corrección deberá versionarse con procedencia separada.

## QA

La auditoría se incorpora a `scripts/validate_postclosure_exports.py`. El CI la ejecuta dos veces en directorios independientes y exige salidas byte-a-byte idénticas, además de mantener desactivadas las banderas de reparación automática e inferencia filológica.
