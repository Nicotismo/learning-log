with open('materiales.txt', 'w') as f:
    f.write('Tejas\nClavos\nMembrana')

with open('materiales.txt', 'r') as f:
    contenido = f.read()
print (contenido)

with open('materiales.txt', 'r') as f:
    lineas = f.readlines()
    print(lineas)

#Ahora agregar una linea sin borrar
with open('materiales.txt', 'a') as f:
    f.write('Canales\n')

#### COMPARADORES PRACTICA
precio_tejas = 45.5
presupuesto = 40

print(precio_tejas > presupuesto)   # ¿45.5 es mayor que 40?
#This will return True

#COMPARACION ENCADENADA
pies = 1800
print(500 < pies < 3000)# ¿1800 está entre 500 y 3000?
#IT WILL RETURN TRUE
print(500 < pies and pies < 3000) #With and just if everything is true

#Reto con Diccionario
techo = {'material': 'asfalto', 'pies2': 1800, 'costo_pie2': 4.25}
costo_total = techo['pies2'] * techo['costo_pie2'] #techo['pies2'] saca el valor 1800 del diccionario
print(costo_total)

#Ahora usemos los comparadores
techo['material'] == 'asfalto' #That will return True
costo_total <= 8000 #That will return true