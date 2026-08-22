# Cahíta Histórico Digital — estado de preparación para v1.0

Fecha de corte: **21 de agosto de 2026**.

## Resumen ejecutivo

Cahíta Histórico Digital está en fase de cierre de release. El vocabulario y la gramática numerada tienen cierre técnico; las remisiones `Buſca` y `Lo miſmo` tienen capas explícitas de revisión; los derivados principales son deterministas; existe un paquete científico reproducible; la vista TEI valida contra **TEI Lex-0 0.9.5**; la decisión CLDF está cerrada; y los contratos de datos de v1.0 quedan congelados por contenido exacto.

Para una **v1.0 técnica, reproducible y científicamente publicable dentro del alcance declarado**, la preparación se estima ahora en **95–97 %**. Esta estimación no mide validación filológica humana: `humanVerified=false` se conserva y una edición revisada por especialistas sigue siendo otra fase.

## Evidencia cerrada

### Corpus

- 2,072/2,072 candidatos canónicos reconstruibles.
- 2,302 artículos históricos en 211 archivos JSONL.
- 45/45 páginas p.133–177 reconciliadas; Phase II 33/33 cerrada técnicamente.
- 371/371 unidades gramaticales numeradas realmente impresas representadas.
- 302 objetos gramaticales y 1,215 filas de evidencia.

### Remisiones y microestructura

- 150 remisiones canónicas `Buſca`.
- 60 `exact_unique`, 90 `not_located`, 4 ciclos estrictos.
- 90/90 `not_located` revisadas: 40 destinos sustentados, 22 recolaciones, 5 candidatos rechazados y 23 destinos no localizados.
- vista revisada: 100 aristas = 60 estrictas + 40 editoriales.
- cola de recolación: 22 casos = 8 A / 4 B / 10 C.
- 14/14 fórmulas `Lo miſmo` auditadas; 0 convertidas en remisión canónica.

### Interoperabilidad

La vista TEI contiene 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 targets estrictos. El CI valida el XML contra el Relax NG archivado de TEI Lex-0 0.9.5, SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`. El XML validado conserva SHA-256 `bad06dad39f216b8dde661b4219845c4c19db945bdfbc4478ff5e0846b72e828` mientras no cambie su contenido.

TEI Lex-0 0.9.5 es el perfil lexicográfico interoperable primario de v1.0; CLDF queda diferido como derivado analítico posterior.

### Freeze de contratos v1.0

`release/v1_contract_manifest.json` congela **26 contratos**:

- 22 JSON Schema de producción;
- 4 metadatos fuente que fijan el alcance de `ALC1737`.

El manifiesto tiene SHA-256 `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`. El CI lo regenera y compara contra los bytes actuales. Una adición, eliminación o alteración provoca fallo; los cambios post-v1 requieren un nuevo freeze explícito.

`CITATION.cff`, `codemeta.json`, versión/tag y DOI no forman parte de este freeze porque son metadatos de identidad de la release y se finalizan en el gate posterior de tag/release.

### Release candidate reproducible

El paquete se construye dos veces y debe coincidir byte-a-byte. Su manifiesto registra tanto la decisión de interoperabilidad como el freeze de contratos y conserva `releaseReady=false` y `humanVerifiedCount=0`. El hash final del ZIP sólo se congelará en el commit candidato definitivo.

## Tres gates restantes

### A — 22 recolaciones

Cada caso debe cotejarse contra imagen del mismo testimonio cuando sea posible o congelarse como incertidumbre explícita. OCR y similitud diagnóstica no sustituyen el facsímil.

### B — tag, changelog y metadatos finales

Después de la decisión sobre recolaciones se congelan los bytes finales de datos, se sincronizan `CITATION.cff` y `codemeta.json`, se prepara el changelog y se reconstruye el paquete desde el commit definitivo antes del tag.

### C — preservación

Faltan GitHub Release, depósito archivístico y DOI de versión/Concept DOI cuando corresponda.

## Orden de cierre

**recolaciones → candidata final/tag/changelog/metadatos → preservación/DOI**.

Una v1.0 válida no requiere ocultar incertidumbres ni atribuir revisión humana inexistente. Requiere alcance estable, incertidumbres explícitas, contratos congelados, derivados interoperables, checksums, reconstrucción reproducible y preservación duradera.
