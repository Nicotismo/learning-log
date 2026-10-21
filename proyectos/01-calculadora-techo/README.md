# 🏠 Calculadora de costo de techo

Mini proyecto 1 de mi ruta de aprendizaje de **Python → Ingeniería de Datos**.

## ¿De qué se trata?

Cuando se cotiza un techo hay que responder rápido tres preguntas:
**¿cuántos squares necesito?, ¿cuánto le cobro al cliente? y ¿le alcanza su presupuesto?**

Este script de consola hace esa estimación como se hace en la industria del techado:
mide el techo en **squares** (1 SQ = 100 pies²), suma el desperdicio de material,
calcula el costo de material y de mano de obra, aplica el margen de ganancia y
compara el precio final con el presupuesto del cliente.

Lo construí a partir de mi experiencia como Project Manager en proyectos de techos.
Todos los valores son **ficticios** y solo sirven para practicar.

## ¿Cómo calcula?

| Paso | Fórmula |
|------|---------|
| Área | largo × ancho (pies²) |
| Squares | área × 1.10 (10 % de desperdicio) ÷ 100 |
| Costo de material | squares × costo del proveedor por SQ |
| Mano de obra | squares × USD 300 |
| Subtotal | material + mano de obra |
| Precio al cliente | subtotal × 1.25 (25 % de margen) |

Además:
- Calcula el precio al cliente con **los 3 materiales** para compararlos.
- Indica si el precio **alcanza el presupuesto** del cliente (`True` / `False`).
- Indica si es un **techo grande** (más de 2000 pies²).

## Datos base (ficticios)

| Material | Costo del proveedor (USD por SQ) |
|----------|---------------------------------:|
| Asfalto (shingle) | 150 |
| Metal | 250 |
| Teja | 80 |

| Parámetro | Valor |
|-----------|------:|
| Mano de obra | USD 300 por SQ |
| Desperdicio | 10 % |
| Margen | 25 % |

Para cambiar cualquier valor, basta con editar las variables de la sección `Datos base` del script.

## Cómo ejecutarlo

Requisitos: Python 3 instalado.

```bash
python techo.py
```

## Ejemplo de uso

```text
Dime el largo del techo (pies): 40
Dime el ancho del techo (pies): 30
Material (asfalto/metal/teja): metal
Presupuesto del cliente (USD): 10000

----- RESUMEN -----
Área: 1200.0 pies² | Squares con desperdicio: 13.2
Material: metal
Costo material: USD 3300.0
Mano de obra:   USD 3960.0
Subtotal:       USD 7260.0
Precio cliente: USD 9075.0
Comparación (asfalto, metal, teja): [7425.0, 9075.0, 6270.0]
¿Alcanza el presupuesto? True
¿Techo grande? False
```

## Lo que practiqué

- Variables y operaciones con números decimales (`float`, `round`)
- Entrada de datos con `input()` y conversión de texto a número
- Métodos de strings (`.lower()` para aceptar mayúsculas)
- Diccionarios (costo de cada material) y listas (comparación de precios)
- Comparadores (`<=`, `>`) que devuelven `True` / `False`
- Formato de salida con f-strings

## Limitaciones (a propósito, por ahora)

- Si el material no es `asfalto`, `metal` ni `teja`, el programa falla con `KeyError`. Todavía no he visto `if` ni manejo de errores.
- Si escribes letras en vez de números en las medidas, falla con `ValueError`.
- Supone un techo rectangular, sin inclinación (pitch).
- El cálculo de los 3 materiales se repite en 3 líneas porque aún no he visto bucles.

## Próximas versiones

- [ ] Validar el material y las medidas con `if/elif/else` y `try/except`
- [ ] Reemplazar las 3 líneas de comparación por un bucle `for`
- [ ] Redondear los squares hacia arriba (en la vida real no se compra 0.2 de square)
- [ ] Ajustar el área según la inclinación del techo
- [ ] Guardar cada cotización en un CSV y, más adelante, en una base de datos

---
*Parte de mi repo [learning-log](../../): de Project Manager a Ingeniero de Datos.*