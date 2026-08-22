# Cahíta Histórico Digital — decisión de alcance CLDF para v1.0

Fecha: 21 de agosto de 2026.

## Decisión

Para **v1.0**, Cahíta Histórico Digital adopta **TEI Lex-0 0.9.5 como representación interoperable lexicográfica primaria** y **no incluye una proyección CLDF como requisito de release**.

CLDF queda explícitamente diferido como **derivado analítico futuro**, condicionado a una segmentación lingüística y editorial adicional que permita construir entradas, sentidos y/o formas sin convertir decisiones históricas de `ALC1737` en supuestos modernos.

Esta decisión cierra el gate de alcance `final_cldf_lex0_scope_decision`; no significa que CLDF sea incompatible con CHD ni que se descarte para versiones posteriores.

## Fundamento

`ALC1737` está organizado históricamente como un vocabulario **castellano → cahíta**. La capa canónica de CHD preserva esa arquitectura mediante 2,302 artículos históricos, guías castellanas, formas cahítas crudas, remisiones y transcripciones. Esa unidad curatorial no equivale automáticamente a un inventario moderno de lemas cahítas.

El módulo `Dictionary` de CLDF modela diccionarios mediante `EntryTable` y `SenseTable`. Una proyección CLDF técnicamente válida podría construirse de varias maneras, pero elegir ahora entre, por ejemplo, guía castellana como `Headword`, forma cahíta como `Headword`, variantes como entradas separadas o agrupadas, o artículos sin forma como entradas sin sentido, introduciría decisiones analíticas que la fuente no resuelve por sí sola.

TEI Lex-0 ofrece actualmente una representación más fiel al objetivo de v1.0 porque permite conservar la microestructura artículo por artículo, las remisiones y la trazabilidad sin normalizar retrospectivamente la orientación histórica del diccionario.

## Lo que sí queda dentro de v1.0

- JSON/JSONL/CSV curatoriales y derivados deterministas;
- representación canónica histórica de 2,302 artículos;
- grafo estricto y vista editorial de remisiones;
- capas explícitas de incertidumbre y recolación;
- concordancia gramatical y auditoría de cobertura;
- proyección TEI de 2,302 entradas;
- validación externa contra el Relax NG oficial archivado de TEI Lex-0 0.9.5;
- paquete científico reproducible con manifiesto y hashes.

## Lo que CLDF no debe afirmar automáticamente

Una futura proyección CLDF no deberá, salvo validación explícita:

- identificar el rótulo histórico `Cahita` con una identidad lingüística moderna concreta;
- convertir cada forma cruda en un lema moderno;
- colapsar variantes históricas;
- inferir cognación, préstamo o equivalencia semántica;
- transformar remisiones `Buſca` o fórmulas `Lo miſmo` en relaciones lexicográficas modernas por mera similitud;
- presentar el vocabulario como corpus paralelo moderno.

## Condiciones para reabrir CLDF

CLDF puede incorporarse en una versión posterior cuando exista una política explícita y validada para:

1. unidad de entrada de lengua objeto;
2. relación entre artículo histórico, forma, variante y sentido;
3. identificación lingüística y códigos de lengua;
4. tratamiento de remisiones y anáforas;
5. mapeo de procedencia desde cada fila CLDF al `articleId` canónico;
6. validación automática con la implementación de referencia `pycldf`.

Cuando esas condiciones se cumplan, la opción preferente a evaluar será **CLDF Dictionary** como derivado, no como sustituto del JSONL curatorial ni de TEI Lex-0.

## Consecuencia de release

El paquete v1.0 no queda bloqueado por ausencia de CLDF. El gate de interoperabilidad se considera satisfecho mediante TEI Lex-0 0.9.5 validado externamente; CLDF pasa al backlog científico posterior a v1.0.
