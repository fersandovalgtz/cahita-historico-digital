# Evidencia de variedad histórica en el léxico

## Objetivo

Esta capa consolida evidencia explícita o candidata de etiquetas históricas de variedad presentes en el corpus lexicográfico, sin atribuir una variedad por semejanza lingüística.

El generador es:

```bash
python scripts/export_lexicon_variety_evidence.py
```

Por omisión produce:

- `build/lexicon-variety-evidence/chd_lexicon_variety_evidence.jsonl`
- `build/lexicon-variety-evidence/chd_lexicon_variety_evidence.csv`
- `build/lexicon-variety-evidence/manifest.json`

## Dos clases de evidencia

`structured_form_metadata` recoge formas que ya poseen `historicalVariety != unspecified` o un `sourceQualifierRaw` explícito. En este caso se preservan tanto la etiqueta estructurada como el calificador histórico literal.

`transcription_surface_candidate` identifica menciones de superficie conservadoras en `transcriptionRaw` para las clases `Hiaqui`, `Mayo` y `Thehueco`, incluyendo sus plurales directos. Estas coincidencias son **candidatos de evidencia**, no atribuciones automáticas a una forma concreta.

## Límites

El manifiesto declara:

- `varietyAttributionInferred: false`;
- `linguisticSimilarityUsed: false`.

No se clasifica una forma como Hiaqui, Mayo o Thehueco por parecido moderno, cognación aparente, conocimiento externo ni posición en el artículo. Sólo se extraen marcas explícitas ya estructuradas y menciones literales de superficie.

## Uso editorial

El inventario permite:

1. cuantificar qué etiquetas están efectivamente presentes;
2. localizar artículos donde la fuente explicita variedad;
3. detectar menciones textuales aún no trasladadas a metadatos de forma;
4. preparar una futura reconciliación entre evidencia de superficie y `historicalVariety` sin reescribir el testimonio.

Una segunda etapa podrá comparar ambos tipos de evidencia y proponer enlaces estructurados, siempre con trazabilidad y estados de confianza explícitos.

## QA

`CHD QA` genera el inventario en un directorio temporal, verifica que sea no vacío y exige que las banderas de inferencia permanezcan en `false`. Una corrida verde valida la extracción reproducible, no una clasificación lingüística moderna.
