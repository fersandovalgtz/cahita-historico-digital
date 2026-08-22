# Enlaces explícitos entre gramática y denominaciones históricas

## Propósito

Esta capa post-v1 relaciona objetos gramaticales estructurados de Cahíta Histórico Digital con evidencia de denominaciones históricas **sólo cuando la atribución aparece dentro del mismo objeto gramatical y ya ha sido admitida por el índice histórico de variación**.

No se crean enlaces por compartir página, por parecido de formas, por cognación supuesta ni por identificación con lenguas o variedades modernas. La capa es documental: conserva las categorías y denominaciones de la fuente de 1737 y hace explícita su relación con reglas, paradigmas y otros objetos estructurados.

## Regla de enlace

El generador `scripts/export_grammar_variety_links.py` reconstruye primero el derivado de variación histórica y toma exclusivamente sus registros con:

- `sourceLayer=grammar`;
- `attributionExplicit=true`;
- `modernIdentityInferred=false`.

Cada evidencia se resuelve después contra **el mismo `sourcePath` y el mismo `objectId`** del objeto gramatical canónico. Sólo entonces se crea un enlace. Varias evidencias del mismo objeto y la misma clase documental se consolidan en un único registro `objeto × etiqueta`.

Por diseño:

- `pageProximityUsed=false`;
- `linguisticSimilarityUsed=false`;
- `modernIdentityInferred=false`;
- `dialectTaxonomyInferred=false`;
- `humanVerified=false`.

Las grafías de `labelsRaw` se filtran además por su propia `labelClass`: un enlace Hiaqui sólo puede conservar `Hiaqui/Hiaquis`, uno Mayo `Mayo/Mayos/Mayes`, uno Thehueco las grafías históricas correspondientes, etc. El QA rechaza contaminación cruzada de etiquetas entre enlaces.

## Censo terminal actual

Sobre el índice histórico vigente, la capa produce de forma determinista:

- **33 enlaces objeto × etiqueta documental**;
- **19 objetos gramaticales únicos**;
- **52/52 evidencias gramaticales explícitas upstream enlazadas**;
- **0 evidencias gramaticales explícitas sin enlace**;
- clases de enlace: **Hiaqui 10, Thehueco 9, Mayo 7, Naciones 6 y Cynaloa 1**;
- tipos de registro de enlace: **21 de regla, 5 de paradigma, 2 del sistema numeral y 5 de otros objetos gramaticales**.

Estos conteos expresan enlaces documentales, no cantidades de lenguas, dialectos o fenómenos modernos.

## Objetos y ejemplos de cobertura

La capa incluye tanto reglas numeradas como paradigmas cuando contienen atribución histórica explícita. Entre los casos que el QA exige conservar se encuentran:

- regla 88: distribución histórica explícita en `Teueco`;
- regla 91: observación prosódica comparativa `Hiaquis / Teuecos / Mayos`;
- regla 128: contraste de declinación `Tehuecos` frente a `Hiaqui / Mayo`;
- regla 130: atribuciones léxicas a `Mayos` y `Hiaqui` conservadas en la estructuración canónica;
- paradigma `ALC1737-par-0002`: comparación temporal explícita `Tehuecos / Hiaquis / Mayos`, vinculada a la regla 190 donde corresponde;
- paradigma `ALC1737-par-0003`: contraste optativo `Tehuecos / demás Naciones`, con localizadores explícitos de las reglas 198 y 200.

Estos casos son controles mínimos, no una lista manual exhaustiva. El exportador enlaza **toda** la evidencia gramatical explícita que el índice histórico vigente admite y falla si alguna evidencia queda sin resolver contra su objeto fuente.

## Productos

```bash
python scripts/export_grammar_variety_links.py \
  --out-dir build/grammar-variety-links
```

produce:

- `chd_grammar_variety_links.jsonl`: enlaces estructurados completos;
- `chd_grammar_variety_links.csv`: vista tabular;
- `manifest.json`: conteos de enlaces, objetos, reglas, clases documentales, cobertura de la evidencia upstream y checksums SHA-256.

Cada enlace incluye:

- ID estable `ALC1737-gvl-*`;
- objeto gramatical y tipo de objeto;
- reglas y páginas que el propio objeto declara;
- clase y grafías históricas de la denominación;
- IDs `CHD-var-evidence-*` del índice histórico que sustentan el vínculo;
- fragmentos documentales usados como evidencia;
- invariantes de autoridad.

## Cobertura y exhaustividad

La exhaustividad se define de forma limitada y comprobable: el derivado debe enlazar el **100 % de los registros de evidencia explícita de `sourceLayer=grammar`** del índice histórico vigente. El manifiesto registra:

- `historicalVariationGrammarEvidenceCount`;
- `linkedHistoricalVariationGrammarEvidenceCount`;
- `unlinkedHistoricalVariationGrammarEvidenceCount`.

El QA exige que los dos primeros conteos sean iguales y que el tercero sea cero. Esto no significa que el impreso de 1737 haya sido reinterpretado exhaustivamente con categorías modernas; significa únicamente que no queda evidencia gramatical explícita ya detectada por CHD sin representación en esta capa de enlaces.

## QA y determinismo

```bash
make grammar-variety-qa
```

construye la capa dos veces y exige igualdad byte a byte de JSONL, CSV y manifiesto. Además:

- valida todos los registros contra `schemas/post-v1/grammar-variety-link.schema.json`;
- exige cobertura completa de la evidencia gramatical upstream;
- comprueba vínculos documentales conocidos en reglas y paradigmas;
- exige que cada `labelsRaw` pertenezca exclusivamente a su `labelClass`;
- impide enlaces por proximidad de página o similitud lingüística;
- bloquea inferencia de identidad moderna o taxonomía dialectal;
- bloquea cualquier elevación de `humanVerified`.

El workflow `CHD Grammar Variety Links` ejecuta la misma prueba en GitHub Actions y publica el derivado como artifact temporal revisable.

## Relación con Fase 4

Esta capa responde al último entregable técnico de Fase 4: **relacionar explícitamente reglas/paradigmas y observaciones históricas de variedad cuando la fuente lo sustente, sin forzar enlaces por similitud**.

La eventual colación humana especializada permanece como una etapa posterior de mejora filológica. No es simulada por este derivado y no se utiliza para elevar `humanVerified`.
