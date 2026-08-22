# Estándar científico del repositorio

Este documento define el estándar interno de calidad para Cahíta Histórico Digital (CHD). Su propósito es impedir que el crecimiento del repositorio reduzca trazabilidad, claridad epistemológica o reproducibilidad.

## 1. Identidad versionada

Toda release estable debe tener versión explícita, tag inmutable, changelog, CFF, CodeMeta, manifiesto y checksums. La identidad binaria de una release se comprueba desde su tag y no desde merge-refs temporales de pull requests.

**Evidencia v1.0.0:** `CITATION.cff`, `codemeta.json`, `CHANGELOG.md`, `release/github_release_attestation_v1.0.0.json`.

## 2. Autoridad documental

La fuente primaria y las capas derivadas deben distinguirse. Una reimpresión, OCR o testimonio de control no sustituye silenciosamente a `ALC1737`.

**Evidencia:** `SOURCES.md`, `PROVENANCE.md`, `EDITORIAL_POLICY.md`, `data/source/`.

## 3. IDs estables y procedencia

Los objetos científicos publicados deben conservar identificadores estables y trazabilidad hacia fuente, página, columna/zona y operaciones editoriales relevantes. Los cambios post-release no reutilizan IDs para objetos distintos.

**Evidencia:** schemas, `data/lexicon/provenance/`, validadores de IDs y freeze científico.

## 4. Contratos de datos formales

Los objetos estructurados deben validarse contra contratos explícitos. Los cambios incompatibles a contratos publicados requieren nueva versión/freeze, no deriva silenciosa.

**Evidencia v1.0.0:** 22 JSON Schema Draft 2020-12 + 4 metadatos de alcance, fijados en `release/v1_contract_manifest.json`.

## 5. Reproducibilidad

Los derivados científicos se regeneran desde fuentes canónicas mediante scripts versionados. Cuando un producto se declara determinista, CI debe comprobarlo mediante doble construcción o comparación byte-a-byte.

**Evidencia:** `.github/workflows/qa.yml`, `scripts/export_*`, `scripts/validate_*`, builders de release.

## 6. Estados de autoridad explícitos

Validación técnica, revisión editorial IA-asistida y verificación filológica humana no son sinónimos. `humanVerified` sólo cambia con evidencia humana identificable.

**Evidencia v1.0.0:** `humanVerified=0`; 22 recolaciones publicadas como `frozen_open_uncertainty`.

## 7. Interoperabilidad sin sobreinterpretación

Un estándar externo se adopta sólo cuando puede representar el objeto sin introducir inferencias no sustentadas. TEI Lex-0 es el perfil lexical primario de v1.0.0. CLDF queda diferido como proyección analítica post-v1 porque no debe aplanar automáticamente la microestructura histórica español→cahíta ni imponer identidad lingüística moderna.

## 8. Metadatos y citabilidad

El repositorio debe ofrecer metadata humana y machine-readable: README, CFF, CodeMeta, project metadata y JSON-LD. El DOI sólo se incorpora después de una asignación real y comprobable.

## 9. Calidad y límites visibles

Toda métrica positiva debe acompañarse de su alcance y sus límites. Una cobertura estructural completa no se presenta como edición crítica completa. Los problemas irresueltos permanecen localizables.

**Evidencia:** `QUALITY_REPORT.md`, `COVERAGE.md`, `DATASHEET.md`, `FAIR_ASSESSMENT.md`.

## 10. Gobernanza y reutilización responsable

La fuente histórica se publica con fidelidad documental; los puentes hacia lenguas y comunidades contemporáneas requieren capas separadas, evidencia adicional y responsabilidad ética. La apertura no confiere autoridad normativa.

**Evidencia:** `GOVERNANCE.md`, `CONTRIBUTING.md`, `DATA_LICENSE.md`.

## 11. Superficie pública de reutilización

Una persona externa debe poder entender qué es el recurso, descargar una versión estable, consultar el corpus, identificar sus formatos, saber cómo citarlo y reportar un problema sin conocer la historia interna del proyecto.

**Evidencia:** README ES/EN, `docs/DATA_PRODUCTS.md`, `scripts/query_lexicon.py`, plantillas de issues y PR.

## 12. Preservación

GitHub no sustituye un repositorio archivístico. Cada release estable debe aspirar a depósito externo y DOI, manteniendo la correspondencia exacta con la identidad publicada.

**Estado v1.0.0:** GitHub Release publicada y atestada; depósito archivístico/DOI pendiente en issue #169.

## Criterio para cambios futuros

Un cambio se considera de calidad sólo si mejora acceso, trazabilidad, interoperabilidad, documentación o evidencia sin reducir fidelidad, reproducibilidad o claridad de autoridad. Las “mejoras” que exigen inferir equivalencias no demostradas, borrar incertidumbre o reescribir retrospectivamente una release no cumplen este estándar.
