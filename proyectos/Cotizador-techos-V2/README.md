# Roof Quote Calculator v2 🏠

A simple Python command-line tool that classifies roofs by size and estimates their cost based on area and roofing material.

Built during **Week 2** of my journey from Project Manager to Data Engineer, using only Python fundamentals (no functions or libraries yet).

## What it does

1. Starts with a sample list of roofs (name, area in ft², material).
2. Lets the user **add new roofs** from the terminal until they type `fin`.
3. **Classifies** each roof by size:
   - Small: under 500 ft²
   - Medium: 500–999 ft²
   - Big: 1,000 ft² or more
4. **Calculates the cost** of each roof: `area × price per ft² of the material`.
5. Prints a **summary**: total cost, most expensive and cheapest roof.

> All data is synthetic. No real client data is used.

## How to run it

```bash
python cotizador.py
```

Type a roof name, its area and its material (`asfalto`, `metal` or `teja`), or type `fin` to see the results.

## Example output

```
Nombre del techo (o fin): Taller
Area en ft²: 800
Tipo de material: metal
Agregaste: Taller
Nombre del techo (o fin): fin
Casa A (Small asfalto) : 1575.0
Bodega (Big metal) : 10800.0
Local (Medium teja) : 4320.0
Taller (Medium metal) : 7200.0
Total : 23895.0 Mas caro : 10800.0 Mas barato: 1575.0
```

## Python concepts used

- Lists and dictionaries (material prices as key–value pairs)
- `while` loop with `input()` and a stop word
- `for` loop with `zip()` to iterate over several lists at once
- `if / elif / else` for classification
- Accumulating results with `.append()`
- Built-in functions: `sum()`, `max()`, `min()`, `int()`
- f-strings for output

## What I learned

- `zip()` stops at the shortest list, so all lists must grow together, or data gets silently lost.
- Keep responsibilities separate: the `while` loop **collects** data and the `for` loop **calculates**.
- Storing a value in a variable (like `categoria`) and printing once is cleaner than repeating `print()` in every branch.

## Next improvements

- [ ] Validate the material: show a warning instead of crashing (`KeyError`) if it's not in the price list
- [ ] Format costs as currency (e.g. `$10,800.00`)
- [ ] Refactor into functions (coming in Week 3)
- [ ] Save the quotes to a CSV file