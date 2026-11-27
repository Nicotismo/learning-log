## Día 1 — 12 oct 2026
- Aprendí: instalar Python, VS Code y Git; clonar un repo.
- Me trabó: (recordar un poco los comandos de git bash)
- Mañana: Python Bootcamp, introducción y línea de comandos.

## Día 2 — 13 oct 2026
- Aprendí: a navegar en PowerShell y la diferencia entre / y //.
- Me trabó: Entender un poco el para que me sirve navegar entre carpetas.
- Sigue: tipos de datos, números y strings.

## Día 3 — 14 oct 2026
- **Aprendí:** la diferencia entre `/` (siempre da float) y `//` (división entera), con `%` para el residuo; slicing con `[inicio:fin]` (el fin no se incluye), índices negativos y `[::-1]` para invertir; `.strip()` y `.title()` para limpiar texto; f-strings con formato de moneda `{total:,.2f}`; y convertir números a texto con `str()`.
- **Me trabó:** el error `'str' object is not callable`. Era porque escribí `print = (...)` y sobrescribí la función `print`. Lección: nunca usar nombres de Python (`print`, `str`, `list`...) como variables, y reiniciar la terminal después de un error así.
- **Sigue:** listas, diccionarios, tuplas y sets. Terminar las 9 variaciones si me faltaron. Ya estoy usando Git Bash en vez de PowerShell.
## Día 4 — 19 oct 2026
- Aprendí: las 4 colecciones y cuándo usar cada una.
- Me trabó: Saber como diferenciar entre diccionarios y sets
- Sigue: mañana es el mini proyecto de la calculadora de techo
## Día 5 — 20 oct 2026
Aprendí: leer y escribir archivos y comparar valores con and/or/not.
Me trabó: Entender el porqué se abren o llaman archivos
Sigue: mini proyecto de calculadora de costo de techo.
## Día 6 — 21 oct 2026
Aprendí: input()` siempre devuelve texto, así que hay que convertirlo con `float()` y guardarlo en una variable. Usé diccionarios para los costos por square, listas para comparar materiales, comparadores que dan True/False y f-strings para el resumen.
Me trabó: quise pedir largo y ancho en un solo `input()` (se necesita uno por dato) y metí una asignación dentro de `round()` (primero se calcula, luego se redondea y al final se guarda). También tuve que convertir pies² a squares (÷100) para que el precio cuadrara con cómo se cotiza en la vida real.
Sigue: jue 22 · Assessment Test de la Sección 3 (lecciones 35–36), capítulo 1 de *Fundamentals of Data Engineering* y post en LinkedIn sobre este proyecto.
## Día 7 — 22 oct 2026
Aprendí:Repasé la Sección 3 con el Assessment Test (lecciones 35–36): indexing, slicing, listas, diccionarios anidados y sets. También actualicé mi perfil de LinkedIn (titular, sector, Open to Work) y escribí mi primer post sobre mi cambio de carrera.
Me trabó: sacar un valor de un diccionario anidado / recordar la sintaxis de slicing [::-1] / no alcancé a leer el capítulo 1 de FoDE
Sigue: Sección 5 del Bootcamp: if/elif/else y bucles for (vie 23).
## Día 8 — 23 oct 2026
Aprendí: if/elif/else y for sobre listas y diccionarios.
Me trabó: Entender bien como llamar las variables en los loop
Sigue: while, range y operadores útiles.
## Día 9 — 26 oct 2026
Aprendí: range(inicio, fin, paso)` genera números sin usar `if`, por ejemplo los pares con `range(2, 21, 2)`. Un `while` necesita tres partes: valor inicial, condición para seguir y algo que la acerque a falsa. Patrón de `input` en un `while`: pedir el primer dato antes del bucle y el siguiente al final de cada vuelta. `enumerate` y `zip` entregan pares que se desempaquetan con dos variables en el `for`.
Me trabó: escribir una condición del `while` que se vuelva falsa (con `dias <= 5` el bucle no paraba nunca). Olvidar el valor inicial (`dias = 5`) en el notebook. Usar una sola variable con `enumerate`/`zip` e imprimir tuplas. Faltaban los dos puntos después del `if`.
Sigue: mañana, list comprehensions. El miércoles, el Statements Assessment Test.
## Día 10 — 27 oct 2026
- Aprendí: list comprehensions con filtro [x for x in lista if ...] y con if/else ['a' if ... else 'b' for x in lista]; in, min(), max() y sum().
- Me trabó: el orden de las partes, y que en la comprehension no va .append() ni print(), solo el valor.
- Sigue: Statements Assessment Test (Sección 5).
## Día 11 — 28 oct 2026
- Aprendí: .split() para recorrer palabras, len() y % para pares, FizzBuzz con if/elif/else y and, comprehensions con strings.
- Me trabó: el orden de las condiciones en FizzBuzz y que range no incluye el número final.
- Sigue: cerrar Sección 5 y rehacer los ejercicios difíciles de semanas 1–2.
## Día 12 — 29 oct 2026
- Aprendí: a hacer while con acumulador y a desempacar dos variables con enumerate, zip y .items(); que una list comprehension es un for en una línea; y la diferencia entre función (max(lista)) y método (lista.append()).
- Me trabó: confundir max.costos con max(costos), y dónde va el .items() (en el for, no en el in).
- Sigue: mini proyecto de techos con condicionales y bucles + LinkedIn + revisión mensual (vie 30).
## Día 13 — 30 oct 2026
**Qué aprendí:** a combinar `while` + `input()` para agregar datos hasta escribir "fin", a recorrer tres listas con `zip()` y a guardar resultados con `.append()` para usar `sum()`, `max()` y `min()` al final.

**Qué me trabó:** dónde poner el `.append()` y el `print` (dentro o fuera del for/if), y usar `costo` en vez de `costos` en el resumen. Aprendí que `zip()` se detiene en la lista más corta y que el while debe agregar datos y el for solo calcular.

**Qué sigue:** publicar el post en LinkedIn. El lunes empiezo la Semana 3 con funciones en el Python Bootcamp.

## Día 14 — 09 NOV 2026
- **Aprendí:** a crear funciones con def; return entrega el valor y print solo lo muestra; una función puede recibir lo que devuelve otra (costo_techo(area_techo(...))).
- **Me trabó:** cuándo usar return y cuándo print; confundí función con método (las listas no tienen .max(), es max(costos)); en el while del cotizador se me olvidaron los .append().
- **Sigue:** tuple unpacking y funciones que interactúan entre sí (Sección 6).

## Día 15 — 10 NOV 2026
Aprendí: la diferencia entre return y print, que una comparación ya devuelve True/False, y cómo devolver y desempaquetar una tupla.
Me trabó: al principio, dónde poner el 120 (en la llamada, no dentro del def) y no repetir el nombre de la función en una variable.
Sigue: el reto 6 y luego *args y **kwargs.

## Día 16 · Lun 23 nov 2026
- **Qué aprendí:** volví a armar el while con input() del cotizador. Pasé el cotizador a funciones: costo_techo() con return, categoria() con if/elif/else y resumen() con tuple unpacking (for nombre, area in clientes). Entendí que return le entrega el resultado a otra función y print solo lo muestra.
- **Qué me trabó:** había olvidado el while después de dos semanas; que < no incluye el mismo número (4000000 < 4000000 es False); entender de dónde salía "pequeño"/"grande" (viene del return de categoria).
- **Qué sigue:** mañana *args y **kwargs + Function Practice Exercises (Overview y Warmups).

## Día 17 · mar 24 nov 2026 (versión corta, 60 min)
- **Aprendí:** `*args` recibe muchos valores como tupla y `**kwargs` recibe valores con nombre como diccionario. Hice `suma_areas(*args)` con `sum(args)`, `techo_mas_grande(*args)` con `max(args)` y `ficha_cliente(**kwargs)` con `for clave, valor in kwargs.items()`.
- **Me trabó:** en `ficha_cliente` imprimí `kwargs` entero en vez de la clave y el valor de cada vuelta.
- **Sigue:** video de Warmups, `cotizar(material, *areas)` y el reto `pares(*args)`; después los Function Practice Exercises nivel 1 y 2.

## Día 18 · mié 25 nov 2026

- **Aprendí:** completé los quick function exercises #1–#10 de la Sección 6 (incluido pick evens y skyline con enumerate y .upper()/.lower()). En VS Code hice cotizar(material, *areas), es_grande(area) y contar_grandes(*areas).
- **Me trabó:** usé args % 2 sobre la tupla completa en vez de recorrer cada número con un for; y dejé .append() vacío.
- **Sigue:** lección 56 (si no la vi) y 57–59, Function Practice Exercises (soluciones y niveles 1 y 2).

## Día 19 · Jue 26 nov 2026 (sesión de 1 h)
- **Qué aprendí:** Function Practice Warmup (lección 56): `lesser_of_two_evens`, `animal_crackers` y `makes_twenty`. `min()` y `max()` son funciones y reciben los valores separados por coma. Con `palabras[0][0]` el primer índice elige la palabra y el segundo la letra, y los dos empiezan en 0. `and`/`or` sirven para preguntas de True/False, no para juntar valores. Un `return` con una comparación ya devuelve True o False sin necesitar `if`.
- **Qué me trabó:** usé `return a and b` y `max(a or b)` en vez de `min(a, b)` y `max(a, b)`. También me confundí con los índices de `palabras[0][1]` y `palabras[1][0]`.
- **Qué sigue:** lección 57 (Solutions) si no la terminé, luego lección 58, Level 1 (old_macdonald, master_yoda, almost_there).