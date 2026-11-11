#1. costo_techo(area, precio_m2) devuelve el costo.

def area_techo(largo, ancho):
    return largo * ancho
print(area_techo(400, 600)) 

def costo_techo(area, precio_m2):
    return(area * precio_m2)
print(costo_techo(area_techo(400, 600), 100))

#2 es_grande(area) devuelve True si el área es mayor a 150. Pista: return area > 150.

def es_grande(area):
    return area > 150
print(es_grande(200)) #Debe dar true
print(es_grande(90)) #Debe dar false

#3 categoria(costo) devuelve "bajo" si es menos de 5.000.000, "medio" si es hasta 10.000.000 
# y "alto" si es más. Usa if/elif/else con un return dentro de cada rama.

def categoria(costo):
    if costo < 5000000:
        return "bajo"
    elif costo <= 10000000:
        return "medio"
    else:
        return "alto"

print(categoria(3000000))    # bajo
print(categoria(8000000))    # medio
print(categoria(15000000))   # alto

#4 total_cotizaciones(costos) suma la lista con un for, sin usar sum():

def total_cotizaciones(costos):      # costos = la LISTA completa
    total = 0                        # 1. empieza en 0, FUERA del for
    for costo in costos:             # 2. costo = UN número a la vez
        total = total + costo       # 3. ¿qué le sumas en cada vuelta?
    return total                    # 4. FUERA del for (alineado con "for")

print(total_cotizaciones([100, 200, 300]))   # debe dar 600

#5 mas_caro(techos) recibe [("Ana",120),("Luis",200),("Sara",90)] y devuelve el nombre del techo con más área. Pista: for nombre, 
# area in techos: y, antes del for, dos variables: mayor_area = 0 y mayor_nombre = "".

def mas_caro(techos):                    # techos = lista de tuplas (nombre, area)
    mayor_area = 0                       # el área más grande vista hasta ahora
    mayor_nombre = ""                    # el nombre de ese techo
    for nombre, area in techos:          # desempaqueta cada tupla
        if area > mayor_area:                # ¿este techo supera al récord?
            mayor_area = area          # actualiza el récord
            mayor_nombre = nombre        # y guarda su nombre
    return (mayor_nombre, mayor_area)                        # ¿qué pide el ejercicio devolver?

print(mas_caro([("Ana",120),("Luis",200),("Sara",90)]))   # debe dar Luis