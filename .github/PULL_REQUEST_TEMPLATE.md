## Tipo de cambio

- [ ] Corrección textual / filológica
- [ ] Datos o schema
- [ ] Software / QA / reproducibilidad
- [ ] Documentación / metadatos
- [ ] Interoperabilidad / exportación
- [ ] Otro

## Qué cambia

Describa el cambio y su alcance. Si afecta datos históricos, identifique `sourceId`, páginas, IDs o capas pertinentes.

## Evidencia y autoridad

- Fuente/evidencia consultada:
- ¿Modifica una lectura histórica? Sí / No
- ¿Modifica un contrato publicado? Sí / No
- ¿Cambia `humanVerified`? Sí / No
- Si la respuesta anterior es Sí: persona revisora, evidencia y alcance de la revisión:

> `humanVerified=true` no se usa para indicar simplemente que CI pasó o que una corrección parece plausible.

## Compatibilidad y procedencia

- [ ] Conservo IDs publicados cuando la identidad del objeto no cambia.
- [ ] No sustituyo silenciosamente `ALC1737` por OCR/reimpresiones de control.
- [ ] No introduzco equivalencias modernas de yaqui/mayo como lecturas de 1737.
- [ ] Si cambio schema/contratos, documento la nueva política de freeze/versionado.
- [ ] Si genero un derivado, puede regenerarse desde fuentes canónicas o explico por qué no.

## QA

- [ ] Ejecuté o espero que CI ejecute la batería CHD QA.
- [ ] El cambio mantiene `project-metadata.json` y documentación pública sincronizados cuando corresponde.
- [ ] Añadí/actualicé pruebas o validadores si el cambio crea una nueva invariante.

## Impacto en release

- [ ] No altera retrospectivamente el tag `v1.0.0`.
- [ ] Si es post-release, distingo claramente cambios de `main` de la identidad inmutable de v1.0.0.

## Notas adicionales

Incluya incertidumbres, decisiones descartadas o trabajo posterior relevante.
