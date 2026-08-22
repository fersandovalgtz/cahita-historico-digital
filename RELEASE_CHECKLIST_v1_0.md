# Cahíta Histórico Digital — Checklist de release v1.0.0

Estado de preparación para la primera versión científica estable. Actualización: **21 de agosto de 2026**.

Este checklist distingue criterios demostrados por datos/CI de acciones externas de publicación y preservación. Una corrida verde no equivale a validación filológica humana.

## Identidad del recurso

- [x] Repositorio identificado
- [x] `CITATION.cff` fijado en versión `1.0.0`
- [x] `codemeta.json` fijado en versión `1.0.0`
- [x] `CHANGELOG.md` con entrada `1.0.0`
- [x] Licencias y procedencia documentadas
- [x] Notas de release `release/RELEASE_NOTES_v1.0.0.md`

## Núcleo de datos

- [x] Vocabulario p.133–177 con cierre técnico: 45/45 páginas; 2,302 artículos curatoriales
- [x] Inventario canónico reconstruible: 2,072/2,072 candidatos
- [x] Gramática numerada: 371/371 unidades realmente impresas representadas
- [x] Remisiones `Buſca`: 150 referencias; 90/90 `not_located` con revisión explícita
- [x] Fórmula `Lo miſmo`: 14/14 ocurrencias auditadas fuera del grafo de remisiones
- [x] Cola de recolación reproducible: 22 casos = 8 A / 4 B / 10 C
- [x] Disposición v1.0: 22/22 como `frozen_open_uncertainty`, 0 destinos seleccionados, 0 cambios canónicos, `humanVerified=false`
- [x] Freeze byte-exacto de artículos, candidatos, capas de revisión y gramática en `release/v1_data_manifest.json`

## Interoperabilidad y contratos

- [x] Exportaciones JSON/JSONL/CSV deterministas
- [x] JSON Schema y validadores activos
- [x] TEI Lex-0 0.9.5 validado externamente con Jing
- [x] TEI Lex-0 como perfil primario; CLDF diferido como derivado analítico post-v1
- [x] 22 JSON Schema + 4 metadatos fuente congelados como 26 contratos v1.0
- [x] Manifiesto de contratos SHA-256 `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`
- [x] CI bloquea deriva silenciosa de contratos y datos científicos congelados

## Empaquetado y publicación GitHub

- [x] Constructor determinista del paquete estable `cahita-historico-digital-v1.0.0.zip`
- [x] Paquete estable incluye datos canónicos congelados, derivados, manifiestos, citación y changelog
- [x] Validador construye el paquete dos veces y exige identidad byte-a-byte
- [x] Intención de publicación versionada; sobrescritura/movimiento del tag prohibidos
- [x] Workflow post-merge vuelve a validar el commit definitivo antes de publicar
- [ ] Crear tag inmutable `v1.0.0` sobre el commit definitivo de `main`
- [ ] Crear GitHub Release estable y adjuntar ZIP, `RELEASE_MANIFEST.json` y `SHA256SUMS.txt`

## Preservación archivística

- [ ] Depositar la versión en Zenodo u otro repositorio de preservación acordado
- [ ] Obtener DOI de versión y registrar Concept DOI cuando corresponda
- [ ] Incorporar los DOI reales a los metadatos posteriores sin alterar ni inventar la identidad histórica del tag

## Estado

El corpus, interoperabilidad, contratos, incertidumbres, freeze de datos, citación, changelog y paquete estable están preparados para el tag `v1.0.0`. La publicación de GitHub se ejecuta únicamente desde el commit definitivo de `main` después de validación post-merge.

El único gate científico externo posterior a GitHub es la **preservación archivística/DOI**. Las 22 recolaciones siguen abiertas filológicamente y pertenecen al backlog post-v1; no bloquean el alcance técnico declarado.

`humanVerified=0` se conserva donde corresponde. Ningún DOI se declara hasta que sea efectivamente asignado.
