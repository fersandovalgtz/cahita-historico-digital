# Cahíta Histórico Digital — estado de preparación para v1.0

Fecha de corte: **21 de agosto de 2026**.

## Resumen ejecutivo

Cahíta Histórico Digital ha superado la fase de construcción gruesa del corpus. El vocabulario y la cobertura estructural de la gramática tienen cierre técnico, las remisiones históricas `Buſca` cuentan con una revisión editorial inicial completa, la fórmula `Lo miſmo` dispone de una capa de revisión propia y los principales derivados se reconstruyen de manera determinista en CI.

Para una **v1.0 técnica, reproducible y científicamente publicable dentro del alcance declarado**, la preparación se estima actualmente en **87–90 %**. El intervalo es deliberado: los últimos gates no tienen el mismo coste ni dependen todos del repositorio. En particular, las 22 recolaciones requieren cotejo directo de fuente y la preservación/DOI depende del paquete final congelado.

Esta estimación **no mide validación filológica humana**. Los estados `humanVerified=false` se conservan explícitamente y una futura edición revisada por especialistas constituye una meta distinta.

## Evidencia de cierre ya alcanzada

### Corpus lexicográfico

- 2,072/2,072 candidatos canónicos reconstruibles.
- 2,302 artículos históricos curatoriales en 211 archivos JSONL.
- 45/45 páginas del vocabulario p.133–177 con reconciliación candidate-level completa.
- Phase II p.145–177: 33/33 páginas con cierre técnico.
- `pendingPromotionTotal=0`, `unresolvedCandidateTotal=0`, `ambiguousBoundaryTotal=0`.

### Remisiones históricas `Buſca`

- 150 referencias canónicas, todas de clase `Buſca`.
- 60 resoluciones estrictas `exact_unique`.
- 90 `not_located` bajo igualdad normalizada estricta.
- 90/90 casos `not_located` con revisión editorial explícita.
- Decisiones: 40 `source_supports_unique_target`, 22 `source_or_destination_requires_recollation`, 5 `candidate_rejected`, 23 `target_not_located`.
- Vista revisada: 100 aristas efectivas = 60 estrictas + 40 editoriales.
- Cola inicial de revisión: 0 A / 0 B / 0 C.
- Ninguna propuesta editorial ha sido promovida silenciosamente al grafo estricto.

### Fórmula histórica `Lo miſmo`

- 14/14 ocurrencias superficiales inventariadas.
- 14/14 con revisión explícita.
- 0 `Lo miſmo` codificados como remisiones canónicas.
- La función exacta permanece `function_unresolved`; no se infieren automáticamente forma cahíta, préstamo, alcance referencial ni equivalencia semántica.

### Gramática

- 302 objetos estructurados en 24 archivos.
- 1,215 filas de evidencia en la concordancia derivada.
- 370/373 números nominales con reclamación estructurada; 127, 178 y 294 son omisiones documentadas del impreso.
- 371/371 unidades numeradas realmente impresas representadas.
- Concordancia y auditoría de cobertura deterministas byte-a-byte.

### Reproducibilidad y QA

- CI activo sobre `main` y pull requests.
- Validación de IDs, JSON Schema, reconciliaciones, estados de autoridad y documentación sincronizada.
- Exportadores lexicográficos, grafo de remisiones, diagnósticos, vista revisada, cola de revisión, `Lo miſmo`, variedad histórica, spans físicos y gramática sometidos a doble corrida determinista.
- Hashes SHA-256 verificados en cada ejecución de los derivados principales.

## Remanente técnico para v1.0

### Gate A — control textual prioritario

Quedan **22 casos `source_or_destination_requires_recollation`**. No constituyen 22 errores confirmados: son puntos donde la lectura o el destino no debe cerrarse sin volver a la imagen/testimonio. Para v1.0 hay dos salidas científicamente válidas: resolver los que puedan cotejarse antes del congelamiento o congelarlos como incertidumbres explícitas, documentadas y reproducibles. Lo que no es válido es resolverlos por similitud aproximada.

### Gate B — interoperabilidad

Falta definir el perfil TEI final y comprobar una exportación conforme al alcance real del proyecto. Debe evaluarse CLDF/Lex-0 como vista derivada sin transformar retrospectivamente el vocabulario histórico en un diccionario moderno ni en un corpus paralelo.

### Gate C — paquete de release

Falta un comando/pipeline de release que parta de un checkout limpio, regenere los derivados incluidos, produzca un paquete final, registre su manifiesto y sus hashes y permita verificar que la release puede reconstruirse sin estado local oculto.

### Gate D — congelamiento y metadatos

Antes del tag deben congelarse los contratos/esquemas de producción que formen parte de v1.0, fijarse cobertura y limitaciones, sincronizarse `CITATION.cff`, `codemeta.json` y changelog, y registrarse el commit/tag de release.

### Gate E — preservación

Faltan GitHub Release, depósito archivístico y DOI de versión. Estos pasos deben ejecutarse sólo después de que el paquete y sus metadatos estén congelados.

## Qué significa “terminar”

**Terminar v1.0** significa publicar una versión estable cuyo alcance, datos canónicos, incertidumbres, derivados, checksums, metadatos y procedimientos de reconstrucción estén explícitos y congelados. No exige fingir que las 22 recolaciones están resueltas ni que el corpus fue revisado humanamente.

**Terminar una edición filológica humana** implicaría otra escala de trabajo: colación especializada sistemática, validación lingüística y editorial, resolución o comentario humano de lecturas dudosas y cambio controlado de estados de autoridad. Ese objetivo debe medirse aparte y no reduce la legitimidad de una v1.0 histórico-digital transparente.

## Orden recomendado de cierre

1. cerrar política y, cuando sea posible, cotejo de las 22 recolaciones;
2. estabilizar perfil TEI y decisión CLDF/Lex-0;
3. construir el pipeline/paquete de release reproducible;
4. congelar esquemas, cobertura, metadatos y changelog;
5. ejecutar release candidate y auditoría desde checkout limpio;
6. tag v1.0.0, GitHub Release, depósito y DOI.

Mientras estos gates no estén completos, la versión debe permanecer `0.2.0-dev` o avanzar a una candidata intermedia sin etiquetarse prematuramente como v1.0.0.
