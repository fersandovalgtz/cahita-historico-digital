# Cahíta Histórico Digital — publicación atestada v1.0.0

Fecha de comprobación: **22 de agosto de 2026**.

## Estado

Cahíta Histórico Digital **v1.0.0 está publicado como GitHub Release estable y su integridad ha sido atestada reproduciblemente**. El cierre aquí descrito es técnico y de publicación; no equivale a validación filológica humana integral.

## Identidad inmutable

- versión: `1.0.0`;
- tag: `v1.0.0`;
- commit del tag: `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`;
- GitHub Release: `https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0`;
- publicada: `2026-08-22T05:34:07Z`;
- estado: estable, `isDraft=false`, `isPrerelease=false`.

El tag fue comprobado nuevamente después de los commits post-release y continúa resolviendo al commit de publicación anterior. Los commits documentales posteriores de `main` no alteran la identidad de v1.0.0.

## Assets publicados

La Release contiene exactamente tres assets:

1. `cahita-historico-digital-v1.0.0.zip` — 1,076,296 bytes — SHA-256 `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`;
2. `RELEASE_MANIFEST.json` — 67,757 bytes — SHA-256 `05970080840ed0cde9c4ca67b40432b492ba2f0afadade5efe2b9d0f60b8cb79`;
3. `SHA256SUMS.txt` — 222 bytes — SHA-256 `8ffc5addb8389f8181152e98097aba8a3c4ae7486342bdbfaea046d9e59ba3e2`.

## Método de atestación

La comprobación durable se conserva en `release/github_release_attestation_v1.0.0.json`.

La atestación no depende de un hash observado durante una pull request. El workflow post-release:

1. resuelve la Release estable `v1.0.0`;
2. descarga sus tres assets;
3. confirma que el tag apunta a `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`;
4. reconstruye el paquete desde el tag inmutable en un worktree aislado;
5. exige identidad de bytes y SHA-256 entre el ZIP publicado y el reconstruido;
6. exige identidad entre el `RELEASE_MANIFEST.json` publicado y el reconstruido;
7. verifica `SHA256SUMS.txt` contra los bytes descargados;
8. comprueba `version=1.0.0`, `sourceCommit`, DOI nulo, `archivalDepositStatus=pending` y `humanVerifiedCount=0`.

Todos esos controles resultaron verdaderos.

## Nota sobre el hash de QA pre-merge

El SHA-256 `45ed1f5e4f6ce101c574dec8a91ffa3c4694050cd4366d70f20c644c40043903` apareció durante una corrida de QA de la PR de release. No es la identidad final del ZIP publicado porque `RELEASE_MANIFEST.json` incorpora `sourceCommit`, y el merge-ref sintético de una PR no es el commit definitivo del tag. Por esa razón se sustituyó el contrato inicial de atestación por comparación contra reconstrucción desde el tag. El SHA-256 archivístico correcto del ZIP publicado es `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`.

## Estado científico conservado

La Release mantiene, entre otros invariantes:

- 2,302 artículos lexicográficos históricos;
- 2,072 candidatos canónicos reconstruibles;
- 150 remisiones `Buſca`;
- 22 recolaciones publicadas como incertidumbres abiertas, sin destinos forzados;
- 302 objetos gramaticales y 1,215 filas de evidencia;
- TEI Lex-0 0.9.5 validado externamente con Jing;
- freeze científico de 267 archivos / 2,698,997 bytes;
- 26 contratos v1.0 congelados;
- `humanVerified=0`.

## Gate restante

La publicación GitHub está cerrada. El único gate externo pendiente es **preservación archivística**:

- habilitar/confirmar el repositorio en Zenodo;
- archivar `v1.0.0`;
- obtener DOI de versión y, cuando corresponda, Concept DOI;
- sincronizar los DOI reales al repositorio mediante cambios post-release, sin mover el tag.

Ese trabajo se rastrea en el issue #169.
