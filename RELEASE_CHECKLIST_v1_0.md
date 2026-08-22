# Cahíta Histórico Digital — Checklist de release v1.0.0

Estado de preparación para una primera versión científica estable. Actualización: **21 de agosto de 2026**.

Este checklist distingue entre criterios ya demostrados por el estado canónico/CI y gates que sólo pueden cerrarse al congelar una release. Una corrida verde no equivale a validación filológica humana.

## Identidad del recurso

- [x] Repositorio identificado
- [x] `CITATION.cff` disponible
- [x] Licencia documentada
- [x] Procedencia histórica documentada

## Núcleo de datos

- [x] Vocabulario p.133–177 con cierre técnico: 45/45 páginas reconciliadas; Phase II 33/33; 2,302 artículos curatoriales
- [x] Inventario canónico de candidatos reconstruible: 2,072/2,072
- [x] Gramática numerada estructuralmente cubierta: 371/371 unidades realmente impresas representadas
- [x] Remisiones `Buſca` inventariadas y revisión inicial cerrada: 150 referencias; 90/90 `not_located` revisadas
- [x] Fórmula histórica `Lo miſmo` separada del grafo de remisiones y auditada: 14/14 ocurrencias
- [ ] Completar o congelar explícitamente la política de los 22 casos `source_or_destination_requires_recollation`
- [ ] Congelar versión canónica de datos para release candidate
- [ ] Documentar cobertura y limitaciones definitivas del alcance v1.0

## Interoperabilidad

- [x] Exportaciones derivadas JSON/JSONL/CSV validadas y deterministas
- [x] JSON Schema y validadores activos sobre datos curatoriales/revisiones
- [ ] Estabilizar/versionar formalmente los esquemas JSON de producción para v1.0
- [ ] Definir y validar perfil TEI final
- [ ] Evaluar y, si procede, producir vista CLDF / Lex-0 derivada

## Reproducibilidad

- [x] CI/QA completo sobre `main` y pull requests
- [x] Doble corrida byte-a-byte de los principales exportadores lexicográficos y gramaticales
- [x] Hashes SHA-256 generados y comprobados para derivados actuales
- [ ] Ejecutar y documentar un pipeline de release desde checkout limpio hasta paquete final
- [ ] Generar paquete reproducible final de release
- [ ] Registrar hashes del paquete congelado de release
- [ ] Registrar commit/tag de release

## Preservación

- [ ] Crear release GitHub
- [ ] Depositar versión archivada en Zenodo u otro repositorio de preservación acordado
- [ ] Obtener DOI de versión y registrar Concept DOI cuando corresponda
- [ ] Sincronizar `CITATION.cff`, `codemeta.json`, changelog y metadatos de versión con el tag final

## Estado de preparación

El núcleo científico-computacional está cerrado en sus unidades básicas y sus derivados principales son reproducibles. Los gates pendientes se concentran en control textual de los 22 casos de recolación, interoperabilidad final, empaquetado reproducible y preservación.

**Estimación operativa actual para v1.0 técnica/publicable: 87–90 % completado.** Esta cifra no representa porcentaje de validación filológica humana: el corpus mantiene `humanVerified=0` donde corresponde y esa validación constituye una fase científica separada.

La versión continúa siendo desarrollo (`0.2.0-dev`) hasta completar los gates de release candidate y preservación.
