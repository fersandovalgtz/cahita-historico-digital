# Parte III — reglas 189–206

## Alcance

Este lote estructura de manera continua las reglas **189–206** del comienzo de la Parte III del *Arte*, a partir de las transcripciones completas de las páginas digitales 69–76 y su cotejo previo contra el facsímil ALC1737.

Se crea un objeto `ALC1737-gr-0189` … `ALC1737-gr-0206` por cada número impreso. Los objetos de regla no sustituyen los paradigmas tabulares ya existentes: cuando una regla y un paradigma representan dimensiones distintas del mismo pasaje, ambas capas coexisten.

## Mapeo de páginas

- p.69: reglas 189 y comienzo de 190;
- p.70: continuación de 190, regla 191 y paradigma presente no numerado;
- p.71: paradigmas temporales no numerados y comienzo de 192;
- p.72: continuación de 192 y reglas 193–195;
- p.73: reglas 196–198 y comienzo de 199;
- p.74: continuación de 199 y reglas 200–202;
- p.75: reglas 203–205 y comienzo de 206;
- p.76: continuación de 206.

## Decisiones editoriales principales

### Regla 190 y paradigmas

La regla 190 contiene explícitamente la distribución de terminaciones temporales por las denominaciones históricas Tehuecos, Hiaquis y Mayos. `ALC1737-gr-0190` estructura la regla como tal; `ALC1737-par-0002` continúa siendo la vista paradigmática/comparativa. La existencia de ambos objetos no implica duplicación accidental: son dos representaciones con granularidad y función distintas.

### Regla 191 y paradigma presente

La regla 191 describe la formación de la voz pasiva mediante `ua` y el futuro pasivo en `naua`. La tabla `CONJUGACION DEL VERBO... Eria amar` que sigue en p.70 no lleva número impreso propio y permanece en `ALC1737-par-0001`. No se absorbe esa tabla dentro de la regla 191.

### Regla 192

La regla declara tres maneras de formar el futuro imperfecto. La primera (`naque` activa / `naua` pasiva) es clara. La partícula exacta de la segunda formación no está resuelta con seguridad en la transcripción vigente; por ello `ALC1737-gr-0192` mantiene `reviewStatus: unresolved` en ese punto y no normaliza la lectura.

### Reglas 198–200

Se conservan tres números distintos. La regla 198 fija las partículas optativas `hau` / `amatuc`; la 199 describe la formación con `uaua`; la 200 describe la formación con `na` y su distribución histórica. Esto confirma que el paradigma `ALC1737-par-0003`, anclado a `[198, 200]`, no debe absorber la regla 199.

### Regla 206

La regla comienza al pie de p.75 y continúa en p.76. En p.76 el impreso vuelve a mostrar `206.` al introducir `Lo tercero`. CHD conserva esta anomalía como nota material dentro de **un solo objeto de regla 206**, ya que el contenido es una secuencia continua de supuestos generales para los tiempos modales. No se crea una segunda regla 206 artificial.

## Autoridad y estados

Todos los objetos conservan `humanVerified: false`. La estructuración procede de la capa de transcripción IA-asistida ya cotejada contra el mismo testimonio y no se presenta como edición filológica humana.

Las incertidumbres de forma se conservan localmente. En particular, el lote no reconstruye la partícula incierta de la segunda formación de la regla 192 ni usa ejemplos dudosos para inferir morfología.

## Efecto esperado en la auditoría

Antes de este lote, las reglas 190, 198 y 200 ya producían reclamaciones a través de paradigmas; las otras quince reglas del tramo 189–206 permanecían sin reclamación estructurada. Por tanto, el incremento esperado de cobertura es de **15 reglas**, no de 18. El conteo definitivo debe tomarse de `scripts/export_grammar_rule_coverage.py` y `CHD QA`.
