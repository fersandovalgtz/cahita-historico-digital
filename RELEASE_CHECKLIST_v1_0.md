# Cahíta Histórico Digital — Checklist de release v1.0.0

Estado de preparación para una primera versión científica estable. Actualización: **21 de agosto de 2026**.

Este checklist distingue criterios demostrados por datos/CI de gates que sólo se cierran al congelar la release. Una corrida verde no equivale a validación filológica humana.

## Identidad del recurso

- [x] Repositorio identificado
- [x] `CITATION.cff` disponible
- [x] Licencia documentada
- [x] Procedencia histórica documentada

## Núcleo de datos

- [x] Vocabulario p.133–177 con cierre técnico: 45/45 páginas; 2,302 artículos curatoriales
- [x] Inventario canónico reconstruible: 2,072/2,072 candidatos
- [x] Gramática numerada: 371/371 unidades realmente impresas representadas
- [x] Remisiones `Buſca`: 150 referencias; 90/90 `not_located` con revisión inicial explícita
- [x] Fórmula `Lo miſmo`: 14/14 ocurrencias auditadas fuera del grafo de remisiones
- [x] Cola de recolación explícita y reproducible: 22 casos = 8 A / 4 B / 10 C
- [ ] Resolver por facsímil o congelar explícitamente como incertidumbres documentadas los 22 casos de recolación
- [ ] Congelar versión canónica final de datos y límites del alcance v1.0

## Interoperabilidad

- [x] Exportaciones JSON/JSONL/CSV deterministas
- [x] JSON Schema y validadores activos
- [x] Perfil TEI Lex-0 0.9.5 definido
- [x] Exportación TEI de 2,302 entradas validada externamente con Jing contra schema archivado y fijado por SHA-256
- [ ] Decidir formalmente si CLDF forma parte de v1.0 o queda como vista analítica futura
- [ ] Congelar/versionar formalmente esquemas JSON de producción para v1.0

## Reproducibilidad

- [x] CI/QA sobre `main` y pull requests
- [x] Doble corrida byte-a-byte de los principales exportadores
- [x] Hashes SHA-256 comprobados
- [x] Pipeline de release candidate desde checkout limpio
- [x] Paquete reproducible de release candidate con manifiesto y hashes
- [ ] Registrar commit/tag y changelog final de release

## Preservación

- [ ] Crear GitHub Release estable
- [ ] Depositar versión archivada en Zenodo u otro repositorio acordado
- [ ] Obtener DOI de versión y registrar Concept DOI cuando corresponda
- [ ] Sincronizar `CITATION.cff`, `codemeta.json`, changelog y metadatos con el tag final

## Estado de preparación

El núcleo de datos, las exportaciones principales, el perfil TEI Lex-0 y la infraestructura de empaquetado reproducible están técnicamente cerrados. Los gates reales se concentran ahora en la política/cotejo de 22 recolaciones, decisión CLDF, congelamiento final de contratos y metadatos, y preservación.

**Estimación operativa actual para v1.0 técnica/publicable: 91–93 % completado.** El intervalo no representa validación filológica humana: `humanVerified=0` se mantiene donde corresponde y esa validación pertenece a otra fase científica.

La versión continúa siendo desarrollo (`0.2.0-dev`) hasta cerrar los gates restantes y congelar una candidata final.
