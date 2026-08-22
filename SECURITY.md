# Seguridad e integridad del repositorio

Cahíta Histórico Digital es software y datos de investigación. Los reportes de seguridad deben distinguir vulnerabilidades técnicas de problemas de integridad científica, aunque ambos pueden afectar la confianza en el recurso.

## Qué reportar como seguridad

Son especialmente relevantes:

- exposición accidental de credenciales, tokens o secretos;
- dependencias o workflows con riesgo de ejecución no autorizada;
- inyección de comandos o uso inseguro de entradas externas;
- acciones de GitHub que pudieran mover/sobrescribir tags o releases inmutables;
- manipulación no detectada de manifests, checksums o artefactos publicados;
- contenido malicioso incorporado a archivos destinados a procesamiento automatizado.

No publique secretos reales dentro de un issue público. Contacte al mantenedor a través del perfil institucional/ORCID indicado en `CITATION.cff` cuando el reporte requiera discreción.

## Integridad científica

Estos problemas no son necesariamente vulnerabilidades de software, pero deben tratarse con prioridad:

- cambio silencioso de IDs persistentes;
- modificación de datos congelados sin nuevo manifest/versionado;
- promoción no justificada a `humanVerified=true`;
- sustitución de `ALC1737` por OCR o testimonio secundario sin trazabilidad;
- falsificación o pérdida de procedencia;
- hashes/documentación que no correspondan a los bytes publicados;
- asignación automática de identidad lingüística moderna no sustentada.

Para esos casos puede abrirse un issue con la plantilla de error de datos/software, evitando reproducir información sensible si la hubiera.

## Versiones soportadas

La release científica estable es `v1.0.0`. El tag es inmutable y permanece como referencia reproducible. `main` contiene mantenimiento post-release y futuras mejoras; una corrección en `main` no modifica retrospectivamente los bytes de v1.0.0.

## Dependencias y CI

La QA de GitHub Actions valida contratos, corpus, derivados, Lex-0, freezes y paquetes. `requirements-dev.txt` mantiene un rango acotado para `jsonschema`; Jing se instala únicamente en el entorno CI para la validación externa de TEI Lex-0.

Las actualizaciones de dependencias deben comprobar reproducibilidad y no deben utilizarse como razón para reescribir una release histórica.

## Divulgación y respuesta

Al recibir un reporte válido:

1. se identifica si afecta `main`, una release publicada o ambos;
2. se conserva evidencia mínima reproducible;
3. se corrige en una rama/PR trazable;
4. se ejecuta QA completa;
5. si una release publicada está afectada, se documenta el incidente y se publica una versión posterior; no se mueve el tag histórico para ocultar el problema.

## Materiales de terceros

CHD no relicencia facsímiles, digitalizaciones o archivos externos. Los reportes sobre disponibilidad, derechos o integridad de esos materiales deben distinguir la infraestructura CHD del proveedor/custodio original.
