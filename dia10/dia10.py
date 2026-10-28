areas = [1500, 2300, 1800]
techos = ["Casa A", "Casa B", "Casa C"]

for i, area in enumerate(areas):
    print(i, area)

for nombre, area in zip(techos, areas):
    print(f"{nombre}: {area} pies2")

#Practica

#Cuadrados: crea la lista de los cuadrados del 1 al 10 en una línea. 

cuadrados = []
for x in range(1, 11):
    cuadrados.append(x**2)
print(cuadrados)

#Comprehensive way
newlist = [x**2 for x in range(1, 11)]

#Ejercicio 2
#Pies² a m²: crea areas_m2 con cada área convertida. Pista: round(a * 0.0929, 1).

areas= [1000, 2000, 3000]
metros_cuadrados =[]

for area in areas:
  metros_cuadrados.append(round(area * 0.0929, 1))
print(metros_cuadrados)

#Comprehensive way
areas= [1000, 2000, 3000]
metros_cuadrados = [round(area * 0.0929, 1) for area in areas]
print (metros_cuadrados)

#Ejercicio 3
#	Guarda solo las áreas mayores a 2000	[2300, 3100]

areas = [1500, 2300, 1800, 950, 3100]
techos_grandres = []

for area in areas:
    if area >2000:
        techos_grandres.append(area)
print(techos_grandres)

#Comprehensive way
areas = [1500, 2300, 1800, 950, 3100]
techos_grandres = [area for area in areas if area>2000]

#Ejercicio 4
#Pon “grande” si el área pasa de 2000 y “pequeño” si no

areas = [1500, 2300, 1800, 950, 3100]
etiquetas = []
for area in areas:
    if area > 2000:
        etiquetas.append('Big')
    else:
        etiquetas.append('Small')
print(etiquetas)

#Comprehensive way

etiquetas = ['Big' if area>2000 else 'Small' for area in areas]
print(etiquetas)

#Ejercicio 5
#Revisa si “metal” está en la lista de materiales, y busca el área mínima y la máxima

materiales = ["teja", "metal", "asfalto"]
areas = [1500, 2300, 1800, 950, 3100]

print('metal' in materiales)
print(f"Techo mas pequeno: {min(areas)} pies² , Techo mas grande: {max(areas)}pies²")

#Ejercicio 6
#Suma solo las áreas mayores a 1000

areas = [1500, 2300, 1800, 950, 3100]
total = sum([area for area in areas if area>1000])
print(f"Área total de techos grandes: {total} pies²")