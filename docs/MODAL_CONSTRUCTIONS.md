# Sistema histórico de construcciones modales en ALC1737

## Alcance

Las reglas 205–234 de la Parte III desarrollan un bloque que el propio impreso denomina **TIEMPOS MODALES**. Cahíta Histórico Digital lo trata como un subsistema documental independiente porque combina partículas, tiempos, voz, configuración de `vn supuesto` / `dos supuestos`, reglas de caso y conjuntos extensos de ejemplos.

La representación máquina-legible inicial se encuentra en [`data/grammar/modal_constructions_part_iii_p077_p086.jsonl`](../data/grammar/modal_constructions_part_iii_p077_p086.jsonl) y sigue [`schemas/modal-construction.schema.json`](../schemas/modal-construction.schema.json).

## Principio editorial

`vn supuesto` y `dos supuestos` son categorías metalingüísticas del *Arte* de 1737. CHD no las reemplaza silenciosamente por términos modernos como oración monoclausal, biclausal, subordinada, sujeto correferente o sujeto disjunto. Esas comparaciones podrán construirse después en una capa analítica separada.

Del mismo modo, `presente`, `pretérito`, `plusquam perfecto`, `activa`, `passiva`, `accusativo` y las denominaciones de partículas se registran primero con el valor que les atribuye la fuente.

## Arquitectura documentada

### `ſi` y `antes` con `vn supuesto` — reglas 207–209

La fuente prescribe `teca` añadido al presente de activa o passiva para cubrir los tiempos del paradigma. Los verbos possessivos y otros acabados en `c` se presentan como excepción: el presente mismo sirve para los tiempos sin recibir `teca`. Para `antes`, el texto introduce además `queheri / caheri`.

### `como`, `quando`, `aunque`, `despues` con `vn supuesto` — reglas 210–212

El marcador general es `cari`; el plusquamperfecto usa `cacari`. `despues` incorpora `ſu`, cuya forma passiva es `ſuua`. El bloque muestra que el gramático concibe estas formas como una combinación sistemática de partícula modal, tiempo y voz.

### Seis partículas con `dos supuestos` — reglas 213–219

Para `ſi`, `antes`, `como`, `quando`, `aunque` y `despues`, la fuente resume una distribución `yo / co / caco` según el tiempo. La regla 219 añade una generalización sintáctica del propio gramático: en construcciones de dos supuestos debe ponerse en accusativo la persona que hace y sobre la cual “apela” la partícula modal.

### `porque` — reglas 220–222

El *Arte* distingue nuevamente `vn supuesto` y `dos supuestos`. En el primer caso distribuye `teca` y `tuca`; en el segundo aparecen `ituca`, `tuca` y `tuco`. La lectura exacta de una de las asignaciones del plusquamperfecto en la regla 220 permanece abierta y por eso el registro correspondiente conserva estado `unresolved`.

### `para / paraque` — reglas 223–228

Con `vn supuesto`, la fuente distingue `varecari`, `rocacari` y `poea / poeate`, relacionándolos con autorreferencia/reflexividad, referencia a otra persona o acción conjunta, y voluntad o disposición. Con `dos supuestos`, emplea `iyaacari` y `teeiacari`. La regla 228 ofrece además una explicación composicional histórica de estas llamadas “partículas verbales”, que CHD conserva como análisis de la fuente, no como etimología moderna validada.

### `como ſi` — reglas 229–234

Con `vn supuesto`, la fuente usa `ten` y `tzaua`; `ten` se restringe a primeras personas y `tzaua` sirve a todas. La regla 230 documenta la reducción `tzaua → tza` por “elegancia” y proporciona una pequeña serie paradigmática.

Con `dos supuestos`, aparecen `ven / veni`; al combinarse con nombres, la fuente introduce `tuco`. La regla 234 vuelve a oponer `ten / tzaua` frente a `ven / veni` según la configuración de la pregunta y la respuesta.

## Valor científico

Este bloque permite estudiar simultáneamente la metalengua gramatical jesuítica, la subordinación y modalidad descritas en 1737, la interacción entre voz y partículas, la arquitectura de ejemplos y la posible variación histórica. La utilidad científica depende de mantener separadas tres capas: **texto fuente**, **estructuración CHD** e **interpretación lingüística moderna**.

## Estado

Cobertura documental inicial: reglas 207–234, páginas digitales 77–86 / impresas 63–72. Estado dominante: `machine_corrected_unverified`, con lecturas `unresolved` explícitas donde el facsímil y la extracción textual no permiten seguridad suficiente. No existe todavía revisión humana independiente.
