# CHD — perfil TEI Lex-0 0.9.5

Fecha de corte: 21 de agosto de 2026.

## Estado

CHD dispone de una vista TEI P5 determinista del vocabulario histórico de `ALC1737` que **valida contra el Relax NG oficial archivado de TEI Lex-0 0.9.5**. El JSONL curatorial continúa siendo la representación canónica; TEI es un derivado interoperable reconstruible.

La validación externa usa exclusivamente:

- versión: **TEI Lex-0 0.9.5**;
- schema: `https://lex-0.org/releases/v0.9.5/schema/lex-0.rng`;
- tamaño observado: **381,270 bytes**;
- SHA-256 fijado: `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`;
- validador: **Jing**.

La URL móvil `https://lex-0.org/schema/lex-0.rng` produjo bytes distintos durante el sondeo y por ello no se usa como referencia reproducible. El CI descarga la copia archivada, comprueba el SHA-256 antes de validarla y falla si el schema cambia o si el XML deja de cumplirlo.

## Proyección vigente

La exportación validada contiene:

- **2,302** `<entry type="mainEntry">` con `xml:id` persistente;
- **2,221** citas de traducción;
- **150** remisiones históricas `Buſca`;
- **60** `ref/@target` correspondientes únicamente a resoluciones estrictas `exact_unique`;
- XML de **1,391,422 bytes**;
- SHA-256 del XML validado: `bad06dad39f216b8dde661b4219845c4c19db945bdfbc4478ff5e0846b72e828`.

El elemento raíz declara `type="lex-0"`. La descripción bibliográfica del testimonio sigue la estructura exigida por el perfil, y la licencia de las capas originales CHD se registra en `availability/licence` sin relicenciar el facsímil histórico.

## Principios de autoridad

1. El JSONL curatorial sigue siendo canónico; TEI no sustituye los objetos CHD.
2. La guía castellana se proyecta como lema histórico.
3. Las formas de lengua meta conservan `xml:lang="und"`: el rótulo histórico `Cahita` no se equipara automáticamente con una identidad lingüística moderna ni recibe un código ISO contemporáneo por analogía.
4. Las 40 aristas editoriales de la vista revisada no se convierten en `@target` canónicos.
5. No se incorporan destinos fuzzy, equivalencia semántica, cognación ni préstamo inferidos.
6. Las 14 fórmulas `Lo miſmo` permanecen fuera del grafo de remisiones.
7. Localización, transcripción histórica y estado CHD se preservan como trazabilidad derivada.
8. `humanVerified=0` continúa siendo independiente de la conformidad XML: un documento válido Lex-0 no equivale a colación filológica humana.

## QA

`scripts/validate_tei_export.py` ejecuta dos exportaciones y exige igualdad byte-a-byte, IDs únicos, conteos canónicos, 60 targets estrictos resolubles y todas las guardas de no inferencia.

`scripts/validate_tei_lex0_external.sh` constituye el gate externo: descarga el schema archivado 0.9.5, verifica el hash fijado y ejecuta Jing sobre un XML recién generado. `CHD QA` instala Jing y ejecuta ambos validadores en pull requests y `main`.

## Alcance de la conformidad

La bandera `teiLex0ConformanceClaimed=true` significa que **los bytes producidos por el exportador pasan el schema oficial archivado 0.9.5 dentro del CI reproducible de CHD**. No significa validación lingüística moderna, identificación taxonómica de la lengua histórica ni certificación filológica humana.
