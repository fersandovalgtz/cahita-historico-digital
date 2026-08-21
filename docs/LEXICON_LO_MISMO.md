# Cola reproducible de fórmulas `Lo miſmo`

## Objetivo

El vocabulario histórico contiene fórmulas `Lo miſmo` que pueden funcionar anafóricamente. Resolverlas exige contexto editorial y no debe hacerse por automatismo. Esta capa identifica únicamente **candidatos de superficie** en la transcripción canónica para convertir un problema disperso en una cola explícita y auditable.

El generador es:

```bash
python scripts/export_lexicon_lo_mismo.py
```

Por omisión produce en `build/lexicon-lo-mismo/`:

- `chd_lexicon_lo_mismo_candidates.jsonl`
- `chd_lexicon_lo_mismo_candidates.csv`
- `manifest.json`

## Método de detección

La detección se limita a `transcriptionRaw` de los artículos canónicos. Para localizar la fórmula se aplica únicamente una normalización técnica no destructiva:

- Unicode NFKC;
- `ſ → s`;
- insensibilidad a mayúsculas/minúsculas;
- compactación de espacios.

La salida conserva `transcriptionRaw` sin modificar. Una coincidencia recibe `anaphoraCandidateType: lo_mismo_surface_formula`.

## Lo que la capa no hace

El manifiesto declara expresamente:

- `anaphoraResolutionPerformed: false`;
- `semanticEquivalenceInferred: false`.

Por tanto, la presencia de `Lo miſmo` no autoriza a copiar la forma cahíta del artículo anterior, inferir un lema moderno ni completar una equivalencia ausente. Es una cola de revisión estructurada, no una resolución anafórica.

## Campos

Cada artículo candidato registra:

- `articleId`;
- página digital y columna;
- tipo de artículo;
- guía castellana;
- `transcriptionRaw`;
- número de coincidencias de superficie;
- `reviewStatus` y `humanVerified`;
- tipo de candidato anafórico.

El orden es determinista por `articleId` numérico ascendente.

## Siguiente etapa

Una futura resolución puede añadir una capa separada con campos como artículo antecedente candidato, evidencia de contigüidad, tipo de relación, confianza y estado editorial. Esa capa deberá conservar sin cambios el artículo histórico de origen y admitir explícitamente el estado `unresolved` cuando la evidencia no sea suficiente.

## QA

`CHD QA` genera esta cola en un directorio temporal y comprueba que el inventario sea no vacío, el manifiesto válido y que ninguna bandera indique resolución automática. Una corrida verde valida el procedimiento de extracción, no el contenido semántico de la anáfora.
