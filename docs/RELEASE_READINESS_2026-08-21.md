# Cahíta Histórico Digital — estado de v1.0.0

Fecha de corte actualizada: **22 de agosto de 2026**.

## Resumen ejecutivo

Cahíta Histórico Digital alcanzó y publicó **v1.0.0 como GitHub Release científica estable dentro del alcance técnico declarado**. El vocabulario y la gramática numerada tienen cierre técnico; las remisiones `Buſca` y `Lo miſmo` poseen capas explícitas de revisión; TEI valida contra Lex-0 0.9.5; CLDF está diferido de forma explícita; los contratos y los datos científicos seleccionados están congelados por contenido; y las 22 recolaciones se publican como incertidumbres filológicas abiertas, no como lecturas resueltas.

La Release, el tag y sus tres assets fueron comprobados mediante una atestación reproducible que reconstruye el paquete desde el tag inmutable y exige identidad con los bytes publicados. La publicación GitHub está cerrada. El único gate externo restante es la preservación archivística y la asignación de DOI real.

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
- freeze byte-exacto de 267 archivos científicos / 2,698,997 bytes en `release/v1_data_manifest.json`.

## Identidad de publicación v1.0.0

- tag: `v1.0.0`;
- commit del tag: `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`;
- Release: `https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0`;
- publicada: `2026-08-22T05:34:07Z`;
- estable: `isDraft=false`, `isPrerelease=false`;
- ZIP: 1,076,296 bytes; SHA-256 `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`;
- `RELEASE_MANIFEST.json`: 67,757 bytes; SHA-256 `05970080840ed0cde9c4ca67b40432b492ba2f0afadade5efe2b9d0f60b8cb79`;
- `SHA256SUMS.txt`: 222 bytes; SHA-256 `8ffc5addb8389f8181152e98097aba8a3c4ae7486342bdbfaea046d9e59ba3e2`.

La atestación durable está en `release/github_release_attestation_v1.0.0.json`; su metodología se resume en `docs/RELEASE_PUBLICATION_2026-08-22.md`. El ZIP y el manifiesto publicados son byte-idénticos a una reconstrucción determinística desde el tag inmutable.

## Preservación y DOI

El depósito archivístico es ahora el único gate externo:

- `archivalDepositStatus=pending`;
- `versionDoi=null`;
- `conceptDoi=null`;
- `doiInferred=false`.

Estos campos sólo deben modificarse cuando un repositorio de preservación asigne identificadores reales. La ausencia temporal de DOI no debe suplirse con un identificador inventado. El procedimiento se rastrea en el issue #169.

## Distinción epistemológica

La release v1.0.0 es técnica, reproducible y científicamente publicable dentro del alcance declarado. No es una edición filológica íntegramente validada por especialistas. `humanVerified=0` se conserva donde corresponde y las 22 recolaciones permanecen abiertas para revisión post-v1 con evidencia admisible.
