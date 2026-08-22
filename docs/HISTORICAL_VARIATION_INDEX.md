# Índice combinado de variación histórica

## Propósito

Esta capa post-v1 consolida la evidencia explícita de variación y denominaciones históricas ya presente en las capas canónicas de Cahíta Histórico Digital. Su función es localizar, cuantificar y relacionar menciones documentales de `Hiaqui/Hiaquis`, `Mayo/Mayos/Mayes`, `Thehueco/Tehueco/Teueco`, `Nación/Naciones`, `Cynaloa/Sinaloa` y metadatos de variedad ya estructurados, sin transformar esas denominaciones en una clasificación lingüística contemporánea.

La release `v1.0.0` no se modifica. El índice es un producto derivado regenerable y queda fuera del freeze científico.

## Fuentes canónicas recorridas

El generador `scripts/export_historical_variation_index.py` recorre exhaustivamente las capas machine-readable actualmente disponibles:

- `data/transcription/pages/ALC1737_p*.json` para menciones explícitas dentro de transcripciones diplomáticas;
- `data/lexicon/articles/*.jsonl` para `historicalVariety`, `sourceQualifierRaw` y menciones explícitas dentro de `transcriptionRaw`;
- `data/grammar/**/*.json` y `data/grammar/**/*.jsonl`, incluidos los numerales, para campos y textos que contienen denominaciones históricas explícitas;
- `data/transcription/status.csv` para documentar la cobertura real de las 182 páginas digitales.

La búsqueda es documental. No se infiere una etiqueta de variedad a partir de una forma que se parezca a yaqui, mayo u otra lengua moderna.

## Productos

```bash
python scripts/export_historical_variation_index.py \
  --out-dir build/historical-variation-index
```

produce:

- `chd_historical_variation_index.jsonl`: índice analítico completo de evidencia;
- `chd_historical_variation_index.csv`: vista tabular del mismo índice;
- `chd_historical_variety_observations.jsonl`: subconjunto proyectado al contrato `historical-variety-observation.schema.json` cuando la evidencia permite una observación con página concreta;
- `chd_historical_variation_coverage.csv`: estado de cada una de las 182 páginas;
- `manifest.json`: conteos, clases documentales, cobertura, inputs y checksums.

## Tipos de evidencia

`explicit_surface_mention` procede de un párrafo de transcripción diplomática que contiene una denominación histórica explícita.

`structured_form_metadata` procede de metadatos lexicográficos ya estructurados como `historicalVariety` o `sourceQualifierRaw`.

`article_surface_candidate` conserva una mención explícita localizada en `transcriptionRaw` de un artículo. La palabra *candidate* significa únicamente que la mención no se asigna automáticamente a una forma concreta del artículo.

`structured_grammar_label_evidence` recupera campos o textos de los objetos gramaticales y numerales donde la denominación histórica ya está explícitamente presente.

## Cobertura y el significado de “exhaustivo”

El índice puede afirmar que la búsqueda es **exhaustiva sobre las capas canónicas machine-readable actuales**, porque el generador recorre todas las transcripciones, artículos lexicográficos y objetos gramaticales disponibles en el repositorio.

La Fase 2 alcanzó su estado terminal técnico: las **182 páginas digitales están contabilizadas**; seis corresponden a material no textual/no aplicable (`1, 2, 4, 14, 181, 182`) y las **176 páginas textuales disponen de transcripción diplomática `full_page` canónica**. La cola `pending/unreviewed` es, por tanto, **0**.

Esto permite afirmar una **transcripción diplomática exhaustiva de las 176 páginas textuales**. No se afirma una “transcripción de las 182 páginas”, porque seis páginas son material no textual y permanecen correctamente clasificadas como `not_applicable_material`.

El manifiesto conserva obligatoriamente:

- `exhaustiveAcrossCurrentCanonicalMachineReadableLayers: true`;
- `exhaustiveDiplomaticTranscriptionOfAll182Pages: false`.

La segunda afirmación no indica trabajo textual pendiente: expresa que seis páginas digitales no contienen texto sustantivo que deba transcribirse. El contrato terminal de QA exige simultáneamente `transcriptionFilePageCount=176`, `pendingOrUnreviewedPageCount=0` y el conjunto exacto de seis páginas materiales.

## Autoridad lingüística

Las clases del índice son claves documentales de búsqueda, no taxones lingüísticos modernos. Por ello, el manifiesto mantiene obligatoriamente:

- `modernLanguageIdentityInferred: false`;
- `dialectTaxonomyInferred: false`;
- `linguisticSimilarityUsed: false`;
- `cognacyInferred: false`;
- `sourceLabelsRemainHistoricalDocumentaryEvidence: true`.

`Naciones`, por ejemplo, se conserva como expresión histórica del texto cuando aparece; el exportador no decide qué poblaciones modernas incluye. Lo mismo ocurre con las grafías variantes `Thehueco`, `Tehueco` y `Teueco`.

## Observaciones estructuradas

El archivo `chd_historical_variety_observations.jsonl` reutiliza el contrato existente `schemas/historical-variety-observation.schema.json`. Se generan observaciones cuando existe una página concreta y un fragmento textual o metadato de variedad explícito suficiente para mantener la trazabilidad.

La clasificación semántica se mantiene conservadora. Las menciones textuales generales se registran como `other_explicit_source_attribution`; las formas lexicográficas que ya poseen metadato explícito se registran como `lexical`. El generador no intenta deducir automáticamente si cada pasaje constituye un fenómeno fonológico, morfológico o dialectológico: esa promoción requiere una decisión editorial posterior.

## Verificación humana

El índice reproduce los estados canónicos y no puede elevarlos. Mientras el corpus continúe sin colación humana identificable, el QA exige `humanVerified=0` también en este derivado.

Una futura revisión humana puede cambiar esta condición únicamente mediante una modificación explícita de la capa canónica correspondiente, con procedencia identificable; nunca mediante el exportador.

## QA y determinismo

```bash
make variation-qa
```

ejecuta dos construcciones independientes y exige igualdad byte a byte de todos los productos. También:

- valida las observaciones contra `historical-variety-observation.schema.json`;
- verifica que las 182 páginas estén contabilizadas;
- exige las 176 páginas textuales con archivo canónico `full_page` y cero páginas pendientes/unreviewed;
- preserva exactamente las seis páginas materiales no aplicables;
- comprueba la presencia de las clases documentales conocidas;
- bloquea cualquier cambio silencioso a inferencia de identidades modernas;
- bloquea cualquier elevación silenciosa de `humanVerified`.

El workflow `CHD Historical Variation` ejecuta esta misma prueba en GitHub Actions y publica el derivado validado como artifact temporal para revisión.

## Relación con Fase 4

El cierre diplomático elimina el antiguo pendiente de transcribir 138–180 y permite regenerar el índice sobre la totalidad de las páginas textuales. La infraestructura de consolidación y localización de variación histórica queda operativa sobre cobertura textual completa.

Fase 4 conserva trabajos filológicos distintos del cierre diplomático: segunda colación priorizada de lecturas inciertas, refinamiento de cantidades/variantes numerales, documentación derivada de irregularidades editoriales y relaciones explícitas regla/paradigma ↔ variedad únicamente cuando la fuente las sustenta. Ninguno de esos trabajos debe confundirse con `humanVerified`, que sigue en cero hasta existir revisión humana identificable.
