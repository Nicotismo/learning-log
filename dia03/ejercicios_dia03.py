#1 Ejercicio Area de techo
largo = 40
ancho = 25
Area = largo * ancho
print("El area del techo es: ", Area)  # Output: El area del techo
print("Los SQ del techo son: ", Area/100)

#2 Tipos
print(type(7), type(7.0), type("7"), type(7//2))  

#3 Slicing: con cliente = "Roofing Solutions LLC", saca "Roofing", saca "LLC" con un índice negativo y escribe el texto al revés.
cliente = 'Roofing Solutions LLC'
print(cliente[0:7])  # Output: 'Roofing'
print(cliente[-3:])  # Output: 'LLC'
print(cliente[::-1])

#4 Métodos: limpia " juan PEREZ " para que quede "Juan Perez". Pista: .strip() y .title().
nombre = " juan PEREZ "
nombre_limpio = nombre.strip().title()
print(nombre_limpio)  # Output: 'Juan Perez'

#5 Cotización con f-string: imprime Cliente: Juan Perez | Área: 1000 sq ft | Total: $8,500.00
cliente = "Juan Perez"
area = 1000
total = 8500.00
print(f"Cliente: {cliente} | Área: {area} sq ft | Total: ${total:,.2f}")  # Output: 'Cliente: Juan Perez | Área: 1000 sq ft | Total: $8,500.00'

#6 Error a propósito: ejecuta "Área: " + 1000, lee el TypeError y arréglalo de dos formas: con str() y con f-string.
area = 1000
print("Area: " + str(area))
print(f"Area:  {area}")
