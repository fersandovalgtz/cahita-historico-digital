# Reporte de calidad — Cahíta Histórico Digital v1.0.0

Este reporte resume la calidad demostrable de la release v1.0.0. No asigna una puntuación global: separa dimensiones que sí están comprobadas de aquellas que permanecen abiertas.

## Resumen

| Dimensión | Estado | Evidencia principal |
|---|---|---|
| Identidad de fuente | Fuerte | `ALC1737`, metadatos, paginación, procedencia |
| Cobertura lexicográfica técnica | Cerrada para v1 | 2,302 artículos; 45/45 páginas p.133–177 |
| Cobertura gramatical numerada | Cerrada para v1 | 371/371 unidades impresas representadas |
| Validez estructural | Fuerte | 22 JSON Schema + CI |
| Estabilidad de contratos | Fuerte | freeze de 26 contratos |
| Reproducibilidad | Fuerte | exports deterministas, doble construcción, release attestation |
| Interoperabilidad lexicográfica | Fuerte | TEI Lex-0 0.9.5 + Jing |
| Procedencia | Fuerte | source spans, provenance layers, manifests |
| Revisión de remisiones | Fuerte en transparencia | 90/90 `not_located` revisadas; 22 abiertas |
| Validación filológica humana | No realizada de forma general | `humanVerified=0` |
| Preservación externa | Pendiente | issue #169 / DOI pendiente |

## Léxico

- 2,072/2,072 candidatos canónicos reconstruibles.
- 2,302 artículos históricos estructurados en 211 archivos JSONL canónicos.
- Vocabulario p.133–177: 45/45 páginas con reconciliación candidate-level técnicamente cerrada.
- Phase II p.145–177: 33/33 páginas técnicamente cerradas.
- `pendingPromotionTotal=0`.
- `unresolvedCandidateTotal=0` en el sentido estructural del inventario de fronteras; esto no elimina incertidumbres de microlectura dentro de objetos ya modelados.
- `ambiguousBoundaryTotal=0`.

## Remisiones y anáforas

- 150 remisiones canónicas `Buſca`.
- 60 aristas estrictas `exact_unique` bajo igualdad normalizada.
- 90 `not_located`, todas con revisión fuente explícita.
- 40 destinos editoriales sustentados forman una vista revisada sin modificar el grafo estricto.
- 22 casos requieren recolación y se publican como `frozen_open_uncertainty`: 8 A / 4 B / 10 C.
- 5 candidatos fueron rechazados y 23 destinos permanecen no localizados.
- 14/14 ocurrencias `Lo miſmo` están auditadas fuera de la red `Buſca`; su función exacta no se infiere automáticamente.

## Gramática

- Secuencia nominal histórica 1–373.
- 370/373 números con reclamación estructurada.
- 127, 178 y 294 se documentan como omisiones materiales del impreso.
- El número 129 aparece dos veces; ambas unidades se preservan.
- 371/371 unidades numeradas efectivamente impresas están representadas.
- 302 objetos gramaticales en 24 archivos.
- 1,215 filas de evidencia explícita.

## Contratos y consistencia

La release congela 22 JSON Schema Draft 2020-12 y cuatro metadatos que definen el alcance de `ALC1737`. El manifiesto contractual es `release/v1_contract_manifest.json` y su SHA-256 es `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`.

Además, 267 archivos científicos —artículos, candidatos, revisiones y gramática— se congelaron byte a byte. El manifiesto correspondiente tiene SHA-256 `8bb2274e13a82d3425a1ee985ce3077789d07c0d0479b63de7dda2767c6a495b`.

## TEI Lex-0

La proyección TEI contiene:

- 2,302 entradas;
- 2,221 citas de traducción;
- 150 remisiones;
- 60 `@target` estrictos.

Se valida con Jing contra el schema archivado de TEI Lex-0 0.9.5 fijado por SHA-256. El exportador no introduce equivalencias modernas de lengua ni convierte incertidumbres en hechos.

## Release reproducible

El tag `v1.0.0` apunta al commit `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`. La GitHub Release estable fue publicada y posteriormente atestada mediante reconstrucción determinística desde el tag.

Identidad final del ZIP publicado:

- bytes: `1,076,296`;
- SHA-256: `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`.

El `RELEASE_MANIFEST.json` publicado tiene 67,757 bytes y SHA-256 `05970080840ed0cde9c4ca67b40432b492ba2f0afadade5efe2b9d0f60b8cb79`. La atestación está en `release/github_release_attestation_v1.0.0.json`.

## Lo que este reporte no afirma

No afirma que todas las lecturas de 1737 hayan sido cotejadas por especialistas contra el facsímil. No afirma correspondencia automática entre `Cahita` histórico y una lengua moderna única. No afirma que las 22 recolaciones estén resueltas. No afirma DOI o preservación archivística que aún no existan.

## Prioridades de mejora post-v1

1. depósito archivístico y DOI real;
2. revisión filológica trazable de las 22 recolaciones;
3. ampliación de cotejo humano independiente de microlecturas seleccionadas;
4. consolidación analítica de las evidencias de variación histórica;
5. derivados comparativos modernos sólo como capas separadas y con política de identidad explícita.
