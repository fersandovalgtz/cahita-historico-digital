# Plan de trabajo post-Phase II — 2026-08-21

La reconciliación lexicográfica p.133–177 ya no es el cuello de botella principal. Este documento fija el orden de trabajo inmediatamente posterior al cierre técnico para evitar volver a dispersar el proyecto.

## 1. Sincronización documental y QA

Objetivo inmediato: que las métricas públicas y de planificación dependan de la misma fuente canónica que el corpus.

Criterios:

- README y ROADMAP deben reflejar 2,302 artículos y Phase II cerrada;
- `phase2_open_work_summary.json` sigue siendo la fuente canónica de estado de p.145–177;
- CI debe fallar si la documentación central vuelve a declarar métricas incompatibles con esa fuente;
- los documentos históricos de corrida pueden conservar cifras antiguas si están claramente fechados y no se presentan como estado vigente.

## 2. Exportación canónica del corpus lexicográfico

Siguiente bloque de ingeniería:

- construir un exportador determinista desde `data/lexicon/articles/*.jsonl`;
- producir al menos JSONL consolidado, JSON y CSV;
- ordenar de forma estable por página, columna y `articleId` o por un criterio explícito documentado;
- validar unicidad de `articleId` y recuento de 2,302 objetos;
- generar SHA-256 de cada artefacto;
- no convertir remisiones o anáforas en equivalencias durante la exportación.

## 3. Grafo de remisiones `Buſca`

Construir una capa derivada que preserve literalmente `markerRaw` y `targetRaw`, y que diferencie:

- destino localizable con alta confianza;
- destino probable pero no resuelto;
- referencia circular;
- referencia fuera del vocabulario o de formulación no normalizada.

La resolución debe ser un derivado trazable, no una modificación silenciosa del artículo histórico.

## 4. Inventario de `Lo miſmo`

Extraer todos los artículos anafóricos y clasificarlos sin completar automáticamente la equivalencia. El objetivo es disponer de una cola editorial explícita y cuantificable.

## 5. Etiquetas históricas de variedad

Auditar menciones explícitas `Hiaqui`, `Mayo`, `Thehueco` y variantes gráficas. Registrar sólo lo que la fuente dice; no inferir variedad por semejanza lingüística.

## 6. Continuidades y `sourceSpans`

Revisar artículos transcolumna/transpágina y anomalías materiales conocidas. El objetivo es que las exportaciones no pierdan estructura física del testimonio.

## 7. Interoperabilidad

Sólo después de estabilizar las exportaciones canónicas:

- definir un perfil TEI del artículo histórico;
- evaluar TEI Lex-0 como vista derivada;
- evaluar CLDF Dictionary como capa de interoperabilidad, no como reanálisis lingüístico automático;
- mantener identificadores, procedencia y estado de revisión en todos los formatos.

## 8. Release científica

El proyecto permanece `0.2.0-dev`. Antes de congelar una release deben cerrarse al menos exportaciones reproducibles, metadatos sincronizados, hashes, cobertura, control de artefactos y estrategia de preservación.

La secuencia recomendada sigue siendo gradual: snapshot científico intermedio antes de cualquier `v1.0.0`.
