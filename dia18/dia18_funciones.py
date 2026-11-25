#Ejercicio 1: cotizar(material, *areas)
#Recibe un material y varias áreas. Devuelve el costo total: la suma de las áreas por el precio del material.

#teja → 45000 por m²
#zinc → 30000 por m²
#cualquier otro → 25000 por m²

def cotizar(material, *areas):
    total_area = sum(areas)
    if material == "teja":
        precio = 45000
    elif material == "zinc":
        precio = 30000
    else:
        precio =  25000
    return total_area * precio

print(cotizar("teja", 50, 30))   # debe dar 3600000
print(cotizar("zinc", 100))      # debe dar 3000000

#Ejercicio 2: es_grande(area)
#Devuelve True si el área es mayor a 100 y False si no.

def es_grande(area):
    return area > 100

print(es_grande(150))  # True
print(es_grande(80))   # False

#Ejercicio 3: contar_grandes(*areas)
#Cuenta cuántas áreas pasan de 100.

def contar_grandes(*areas):
    contador = 0              
    for area in areas:        
        if area > 100:
            print('Es Grande')
            contador += 1
    return contador           # fuera del for

print(contar_grandes(50, 120, 200, 90))  # debe dar 2