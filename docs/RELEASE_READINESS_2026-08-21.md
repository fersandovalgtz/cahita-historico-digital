# Cahíta Histórico Digital — estado de preparación para v1.0.0

Fecha de corte: **21 de agosto de 2026**.

## Resumen ejecutivo

Cahíta Histórico Digital alcanzó el estado de **payload científico v1.0.0 listo para publicación en GitHub**, sujeto a la validación del commit definitivo de `main`. El vocabulario y la gramática numerada tienen cierre técnico; las remisiones `Buſca` y `Lo miſmo` poseen capas explícitas de revisión; TEI valida contra Lex-0 0.9.5; CLDF está diferido de forma explícita; los contratos y los datos científicos seleccionados están congelados por contenido; y las 22 recolaciones se publican como incertidumbres filológicas abiertas, no como lecturas resueltas.

La identidad de release está fijada en `1.0.0` en `CITATION.cff`, `codemeta.json`, `CHANGELOG.md` y las notas de release. El constructor estable genera un paquete autocontenido con datos canónicos congelados, derivados reproducibles y manifiestos de integridad.

## Estado científico fijado

- 2,072/2,072 candidatos canónicos reconstruibles.
- 2,302 artículos lexicográficos históricos en 211 JSONL.
- 45/45 páginas p.133–177 reconciliadas; Phase II p.145–177 cerrada 33/33 técnicamente.
- 150 remisiones `Buſca`: 60 `exact_unique`, 90 `not_located`, 4 ciclos estrictos.
- 90/90 `not_located` con revisión explícita: 40 destinos sustentados, 22 recolaciones, 5 candidatos rechazados y 23 destinos no localizados.
- 22 recolaciones = 8 A / 4 B / 10 C; 22/22 `frozen_open_uncertainty`, 0 destinos seleccionados por la capa v1, 0 cambios canónicos, `humanVerified=false`.
- 14/14 ocurrencias `Lo miſmo` auditadas fuera del grafo canónico.
- 302 objetos gramaticales, 1,215 filas de evidencia; 370/373 números con reclamación estructurada y 371/371 unidades numeradas realmente impresas representadas.
- TEI Lex-0 0.9.5: 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 `@target` estrictos; validación externa con Jing.
- 26 contratos v1.0 congelados: 22 JSON Schema + 4 metadatos fuente.
- freeze byte-exacto adicional de artículos, candidatos, revisiones y gramática en `release/v1_data_manifest.json`.

## Publicación v1.0.0

La publicación está protegida por `release/v1_publish_intent.json` y `.github/workflows/publish-v1.yml`.

El workflow sólo corre cuando el archivo de intención llega a `main`. Antes del tag vuelve a validar inventario, artículos, documentación, derivados post-cierre, remisiones, recolaciones, `Lo miſmo`, TEI/Lex-0, gramática, freeze de contratos, freeze de datos y paquete estable.

El tag `v1.0.0` es inmutable por política de publicación: si ya existe en otro commit, el workflow falla y no lo mueve. La GitHub Release se crea como estable y adjunta el ZIP determinista, `RELEASE_MANIFEST.json` y `SHA256SUMS.txt`.

## Preservación y DOI

El depósito archivístico es el único gate posterior a la publicación de GitHub. En el payload v1.0.0:

- `archivalDepositStatus=pending`;
- `versionDoi=null`;
- `conceptDoi=null`;
- `doiInferred=false`.

Estos campos sólo deben modificarse cuando un repositorio de preservación asigne identificadores reales. La ausencia temporal de DOI no debe suplirse con un identificador inventado.

## Distinción epistemológica

La release v1.0.0 es técnica, reproducible y científicamente publicable dentro del alcance declarado. No es una edición filológica íntegramente validada por especialistas. `humanVerified=0` se conserva donde corresponde y las 22 recolaciones permanecen abiertas para revisión post-v1 con evidencia admisible.
