# CHD — perfil TEI lexicográfico experimental v0.1

Fecha: 21 de agosto de 2026.

## Objetivo

Este perfil introduce una vista TEI P5 determinista del vocabulario histórico de `ALC1737`. La proyección busca compatibilidad conceptual con las prácticas actuales de diccionarios TEI y con **TEI Lex-0 0.9.5**, pero **no declara todavía conformidad Lex-0**: falta incorporar una validación externa contra el schema oficial de Lex-0 como gate independiente.

Referencias de diseño:

- TEI P5 Dictionaries: https://tei-c.org/release/doc/tei-p5-doc/en/html/DI.html
- TEI Lex-0 0.9.5: https://lex0.org/

## Principios

1. El JSONL curatorial sigue siendo la representación canónica de CHD; TEI es un derivado reproducible.
2. Cada artículo histórico se proyecta como `<entry type="mainEntry" xml:lang="es">` con `xml:id` igual al `articleId` persistente.
3. La guía castellana se proyecta como `<form type="lemma"><orth>…</orth></form>`.
4. Las formas históricas etiquetadas por la fuente como cahítas se representan como `<cit type="translation"><quote xml:lang="und">…</quote></cit>`.
5. `xml:lang="und"` es deliberado: el exportador no identifica automáticamente el rótulo histórico `Cahita` con una lengua moderna ni asigna por analogía un código ISO contemporáneo.
6. Las remisiones `Buſca` se conservan con `<xr type="related"><lbl>Buſca</lbl><ref type="entry">…</ref></xr>`.
7. Sólo las **60 resoluciones estrictas `exact_unique`** reciben `ref/@target`. Las 90 remisiones `not_located` permanecen como referencias sin puntero.
8. Las **40 aristas editoriales** de la vista revisada no se incorporan a esta proyección canónica inicial; su autoridad sigue diferenciada de la igualdad estricta.
9. Las fórmulas `Lo miſmo` no se transforman en remisiones ni en formas cahítas; permanecen en la transcripción histórica y su capa de revisión propia.
10. Cada entrada incluye localización, transcripción histórica y estado CHD como notas derivadas para preservar trazabilidad.

## Cabecera TEI

La cabecera se deriva de `data/source/alc1737/metadata.json` y registra:

- título del recurso derivado;
- responsabilidad CHD;
- licencia de datos/capas originales CC BY 4.0, sin relicenciar reproducciones históricas de terceros;
- descripción bibliográfica de `ALC1737`;
- declaración editorial de no inferencia;
- español como working language;
- `und` como etiqueta técnica de la lengua meta histórica no normalizada.

La autoría histórica disputada no se resuelve en la exportación: la política de CHD continúa preservando el anonimato de portada y separando las atribuciones secundarias.

## QA inicial

`scripts/validate_tei_export.py` exige:

- doble exportación byte-a-byte idéntica;
- XML bien formado en namespace TEI;
- 2,302 `<entry>` con `xml:id` únicos;
- una lemma `<orth>` por artículo;
- todas las formas de lengua meta con `xml:lang="und"`;
- 150 remisiones canónicas;
- exactamente 60 `@target` estrictos y todos resolubles a un `xml:id` exportado;
- ninguna arista editorial o fuzzy;
- ninguna inferencia de identidad lingüística moderna, préstamo o equivalencia semántica;
- `teiLex0ConformanceClaimed=false` hasta incorporar validación externa.

## Siguiente gate TEI

Antes de marcar TEI como cerrado para v1.0 debe ejecutarse validación contra el **schema estable de TEI Lex-0 0.9.5** y corregirse cualquier incompatibilidad del perfil. Sólo después debe cambiarse la bandera de conformidad. Si alguna restricción Lex-0 entra en conflicto con la fidelidad histórica de CHD, debe documentarse una personalización o una desviación explícita; no debe alterarse silenciosamente la fuente para satisfacer el schema.
