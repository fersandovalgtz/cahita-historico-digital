# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas; esos candidatos no equivalen automáticamente a artículos históricos publicados.

La secuencia curatorial principal contiene ahora **673 artículos históricos estructurados**. El tramo selectivo continuo **pp.138–177 está completo**; además existe el piloto de p.134. Todos los objetos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

## Cobertura curatorial vigente

| Tramo | Artículos |
|---|---:|
| p.134 piloto | 12 |
| p.138 | 33 |
| p.139 | 39 |
| p.140 | 36 |
| p.141 | 10 |
| p.142 | 10 |
| artículo trans-página 141–142 | 1 |
| pp.143–145 | 42 |
| p.146 | 25 |
| pp.147–177 | 465 |
| **Total principal** | **673** |

Quedan fuera del pase curatorial inicial **p.133 y pp.135–137**, además de la revisión exhaustiva de todos los candidatos geométricos. Por tanto, el cierre del tramo 138–177 es un hito de cobertura selectiva, no una afirmación de exhaustividad lexicográfica.

## Identificadores y procedencia

La reconciliación de p.165 eliminó la colisión histórica del antiguo piloto `000013`–`000016`; las cuatro remisiones fueron migradas a `000490`–`000493` y la operación quedó documentada en `data/lexicon/provenance/p165_pilot_id_reconciliation.json`.

`scripts/validate_lexicon_ids.py` permanece como control de unicidad de `articleId`, parseo JSONL y coherencia entre `reviewStatus` y `humanVerified`.

## Remisiones y anáforas

Las remisiones `Buſca` se modelan como relaciones documentales. Los lotes pp.169–177 incorporan, entre otras:

- `Piedra de que ſe ſacan navajas → pedernal prieto`;
- `Piel → pelo`;
- `Platicar con otro → parlar`;
- `Placer regocijo → gozo`;
- `Plazo poner → ſeñalar dia`;
- `Pleyto aver → pelear`;
- `Premiar → pagar`;
- `Prieto → negro`;
- `Redondo → bola`;
- `Reglar con regla → rayar`;
- `Reñir → regañar`;
- `Rueda → redonda coſa`;
- `Saliva → eſcupitina`;
- `Saltar → brincar`;
- `Sepultar → enterrar`;
- `Sobrar → quedar`;
- `Socorrer → ayudar`;
- `Tener con las manos → agarrar`;
- `Tentar con las manos → palpar`;
- `Tocar → palpar`;
- `Traſponer plantas → plantar`;
- `Vadear el Rio → paſſar el Rio por vado`;
- `Viejo → anciano`;
- `Viento → ayre`.

`Lo miſmo` sigue tratado como anáfora distinta de `Buſca`. En p.169 aparece `Plato. Lo miſmo.`, que permanece `unresolved` sin transferencia automática de la forma precedente.

## Catchwords y fronteras

Los reclamos tipográficos continúan en una capa de paratexto separada del corpus de artículos. Los nuevos controles resuelven:

- p.168 `Pie-` → p.169 `Piedra de que ſe ſacan navajas`;
- p.169 `Por` → p.170 `Por donde?`;
- p.170 `Que-` → p.171 `Querella`;
- p.171 `Relam-` → p.172 `Relampago`;
- p.172 `Rubio,` → p.173 `Rubio, ò rubia coſa`;
- p.173 `S` → p.174 inicio de la serie S;
- p.174 `Tar-` → p.175 `Tarde`;
- p.175 `Tor-` → p.176 `Tortuga`;
- p.176 `Vn par` → p.177 `Vn par. Huipalai.`.

La anomalía `Lucer-` de p.161→162 continúa abierta y no se reconstruye por conjetura. La discontinuidad F→H entre pp.157–158 permanece registrada como `ALC1737-gap-0001`.

## Final material del vocabulario

La p.177 concluye el vocabulario alfabético con la serie de V y `Vomitar`. La p.178 cambia de estructura: termina X/Z y abre `NOMBRES NUMERALES`; las pp.178–180 se modelan por ello como **capa gramatical de numerales**, no como prolongación indiferenciada del corpus lexicográfico.

## Próximo frente

1. Retroceder a p.133 y pp.135–137 para cerrar el hueco del pase curatorial inicial.
2. Reconciliar sistemáticamente los **2,072 candidatos** con artículos, paratexto y falsos positivos.
3. Resolver anáforas `Lo miſmo` y grafo completo de `Buſca` mediante operaciones editoriales explícitas.
4. Preparar exportaciones de producción y TEI Lex-0 sólo después de estabilizar la microestructura.
