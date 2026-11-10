#1. Clasificar: recorre con zip los tres datos de cada techo y clasifica cada uno como pequeño (< 500), mediano (500–999) o grande (≥ 1000). 
#   Pista: if / elif / else, e importa el orden de las condiciones.
#2. Costo por techo: calcula área × precios[material] e imprime Bodega (grande, metal): $10800.0.
#3. Resumen: acumula el costo total y, con una comprehension, crea la lista de costos. Imprime el total, el más caro (max) y el más barato (min).
#4. Agregar techos con while: pide con input() un nombre nuevo y repite hasta que el usuario escriba fin. Pide también área y material, y agrega cada dato a su lista con .append(). 
#   Pista: input() devuelve texto, así que el área necesita int().
#5. Bonus: si el material no está en precios (usa in), imprime un aviso en lugar de que el programa falle.

nombres = ["Casa A", "Bodega", "Local"]
areas = [350, 1200, 600]
materiales = ["asfalto", "metal", "teja"]
precios = {"asfalto": 4.5, "metal": 9.0, "teja": 7.2}
costos = []

nombre = input("Nombre del techo (o fin): ")

while nombre != "fin":
    area = int(input("Area en ft²: "))
    material = input('Tipo de material: ')
    nombres.append(nombre)
    areas.append(area)
    materiales.append(material)
    print(f"Agregaste: {nombre}")
    nombre = input("Nombre del techo (o fin): ")

for nombre, area, material in zip(nombres, areas, materiales):
    if area < 500:
        categoria = 'Small'
    elif area >= 500 and area <= 999:
        categoria = 'Medium'
    else:
        categoria = 'Big'
    costo = area * precios[material]
    costos.append(costo)
    print (f'{nombre} ({categoria} {material}) : {costo}')
print(f'Total : {sum(costos)} Mas caro : {max(costos)} Mas barato: {min(costos)}')

