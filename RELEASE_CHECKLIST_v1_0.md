# Cahíta Histórico Digital — Checklist de release v1.0.0

Estado de preparación para una primera versión científica estable. Actualización: **21 de agosto de 2026**.

Este checklist distingue criterios demostrados por datos/CI de gates de cierre. Una corrida verde no equivale a validación filológica humana.

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
- [ ] Congelar los bytes finales de los datos canónicos después de la decisión sobre recolaciones

## Interoperabilidad y contratos

- [x] Exportaciones JSON/JSONL/CSV deterministas
- [x] JSON Schema y validadores activos
- [x] Perfil TEI Lex-0 0.9.5 definido y validado externamente con Jing
- [x] Decisión CLDF/v1.0 formalizada: TEI Lex-0 primario; CLDF diferido como derivado analítico posterior
- [x] **22 JSON Schema de producción congelados para v1.0 por SHA-256**
- [x] **4 metadatos fuente de alcance `ALC1737` congelados por SHA-256**
- [x] Manifiesto `release/v1_contract_manifest.json`: 26 contratos, SHA-256 `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`
- [x] CI regenera el manifiesto y falla ante adiciones, eliminaciones o cambios de bytes no declarados
- [x] Política de evolución: cambios post-v1 requieren nuevo manifiesto; cambios silenciosos bajo el mismo freeze están prohibidos
- [ ] Finalizar metadatos de identidad de release (`CITATION.cff`, `codemeta.json`, versión/tag y DOI) en el gate de tag/release

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

El núcleo científico-computacional, TEI Lex-0, el alcance CLDF, el empaquetado reproducible y los contratos de datos v1.0 están técnicamente cerrados. Los gates del release candidate quedan reducidos a **tres**: tratamiento final de las 22 recolaciones, tag/changelog final y preservación/DOI.

**Estimación operativa actual para v1.0 técnica/publicable: 95–97 % completado.** Esta cifra no representa validación filológica humana; `humanVerified=0` se mantiene donde corresponde.

Los metadatos de identidad de release no forman parte del freeze de contratos porque necesariamente deben incorporar el tag y DOI definitivos. Se cierran en el gate posterior, no mediante una excepción silenciosa al manifiesto.
