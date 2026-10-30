#Práctica Usa areas = [350, 420, 515, 0, 600]:

#1.while hasta el 0: suma las áreas hasta topar con el 0. Pista: i = 0 y total = 0 van antes del bucle, la condición es areas[i] != 0, y dentro va i += 1.

areas = [350, 420, 515, 0, 600]
i = 0
total = 0

while areas[i] != 0:
    total = total + areas[i]
    i += 1
print(total)

#2. enumerate: imprime Techo 1: 350 ft². 

areas = [350, 420, 515, 0, 600]

for num, area in enumerate(areas, 1):
    print(f"Techo {num}: {area} ft²")

#3 zip + if: con nombres = ["Casa A", "Casa B", "Bodega", "X", "Local"], 
#imprime solo los techos de más de 400 ft².

areas = [350, 420, 515, 0, 600]
nombres = ["Casa A", "Casa B", "Bodega", "X", "Local"]

for nombre, area in zip(nombres, areas):
    if area > 400:
        print(f'{nombre}:  {area}')

#4 Comprehension: costos = [a * 4.5 for a in areas if a > 0] y luego max() y min() con un f-string.
areas = [350, 420, 515, 0, 600]
costos = [a * 4.5 for a in areas if a > 0]
print (f'Costo mas alto: {max(costos)}\n Costo mas bajo: {min(costos)}')

#Reto: con precios = {"asfalto": 4.5, "metal": 9.0, "teja": 7.2}, 
#si "metal" in precios, recorre .items() con dos variables e imprime los que cuesten más de 5.

precios = {"asfalto": 4.5, "metal": 9.0, "teja": 7.2}

if 'metal' in precios:
    for material, precio in precios.items():
        if precio > 5:
            print(f"{material} {precio}")