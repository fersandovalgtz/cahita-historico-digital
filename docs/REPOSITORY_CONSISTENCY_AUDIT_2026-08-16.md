# Auditoría de consistencia del repositorio — 2026-08-16

## Propósito

Esta auditoría identifica y corrige divergencias entre el estado científico real de Cahíta Histórico Digital (`ALC1737`) y documentos que habían quedado rezagados durante el procesamiento intensivo del corpus.

No constituye revisión filológica humana ni una release científica. Su función es establecer una **línea base canónica de estado** antes de continuar la reconciliación exhaustiva y antes de diseñar productos finales.

## Línea base canónica

A la fecha de esta auditoría, el estado que debe prevalecer en documentación y Issues es:

- 182/182 páginas digitales identificadas;
- 118/118 páginas impresas numeradas mapeadas;
- 128 páginas `full_page` en la capa de transcripción;
- Partes I–IV del Arte representadas de forma continua en capa IA-asistida hasta `FIN DEL ARTE`;
- 2,072/2,072 candidatos lexicográficos v0.2 persistidos canónicamente;
- JSONL candidato canónico SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`;
- 734 artículos históricos estructurados;
- 45/45 páginas del vocabulario con representación lexicográfica estructurada;
- pp.133–134: 61/61 candidatos reconciliados;
- 14 inicios visibles omitidos observados en pp.133–134;
- 36 candidatos `article` del tramo con `articleLinkStatus: pending_promotion`;
- 3 paradigmas, 9 construcciones modales, 5 no finitas, 3 participiales, 6 predicativas/modales, 6 grupos de verbos irregulares, 43 preposiciones/grupos, 11 grupos de adverbios y 6 grupos de conjunciones/metacategorías;
- sistema numeral estructurado en digitales 178–180;
- 17+ observaciones de variación histórica identificadas;
- 0 objetos `human_verified`;
- una discontinuidad material registrada (`ALC1737-gap-0001`, 157→158);
- una anomalía adicional abierta (`Lucer-`, 161→162);
- sin release científica estable ni DOI.

## Divergencias detectadas

### README

El README seguía describiendo una sola página con transcripción diplomática completa, una página piloto, 12 entradas lexicográficas piloto, 0 entradas de producción y estado `0.1.5-dev`. Ese estado había sido superado ampliamente.

### ROADMAP

La hoja de ruta conservaba cifras de la etapa inicial: 1,680 candidatos v0.1, 12 entradas piloto y Fase 4 todavía `pendiente`. La realidad actual es que Fase 3 y Fase 4 están activas y avanzadas.

### COVERAGE / QA

La documentación mezclaba en algunos lugares las métricas históricas de `indentation_margin_v0.1` (95.32 / 86.70 / 90.81) con las de `hybrid_margin_mode_v0.2` (97.13 / 89.89 / 93.37). La auditoría fija que ambas deben conservarse, pero con etiquetas explícitas de método. La muestra es intencional y no probabilística.

### Issue #2

El Issue de transcripción todavía declaraba Parte IV en curso sólo hasta digital 106 y 102 páginas `full_page`, aunque el cuerpo gramatical ya había sido representado hasta digital 132. El Issue fue corregido durante esta auditoría y ahora refleja **128 páginas `full_page`**, Partes I–IV completas en capa IA-asistida y el alcance todavía pendiente para vocabulario/numerales.

### Metadatos

`CITATION.cff`, `codemeta.json` y `DATASHEET.md` conservaban versión/estado inicial `0.1.0` o metadatos de proyecto en etapa conceptual. Fueron actualizados a un estado de desarrollo activo sin sugerir una release estable inexistente.

## Correcciones ejecutadas

Durante esta auditoría se sincronizaron:

- `README.md`;
- `ROADMAP.md`;
- `COVERAGE.md`;
- `CHANGELOG.md`;
- `CITATION.cff`;
- `codemeta.json`;
- `DATASHEET.md`;
- Issue #2 de transcripción.

La serie de desarrollo vigente queda denominada **`0.2.0-dev`**. Esta denominación no implica DOI ni release archivada.

## Pendientes posteriores a la auditoría

1. revisar documentación secundaria adicional por cifras obsoletas mediante búsqueda de `1,680`, `12 entradas`, `0.1.5-dev`, `102 páginas` y expresiones equivalentes;
2. incorporar una prueba automatizada de consistencia de métricas/documentación cuando se implemente CI;
3. retomar el cierre lexicográfico de pp.133–134 y después escalar la reconciliación;
4. mantener esta auditoría como registro histórico, no como archivo que se reescriba retroactivamente.

## Regla de autoridad

La sincronización documental no cambia el estado epistemológico de los datos. Ninguna unidad IA-asistida se promueve a `human_verified` por efecto de esta auditoría.
