nombres, areas, materiales = [], [], []
nombre = ""            # valor inicial ANTES del while
while nombre != "fin":
    nombre = input("Nombre (o 'fin'): ")
    if nombre != "fin":
        area = int(input("Área en m2: "))
        material = input("Material del techo: ")
        nombres.append(nombre)
        areas.append(area)
        materiales.append(material)
print(nombres, areas, materiales)             # fuera del while
###################


def costo_techo(area, precio_m2):
    # calcula el costo y devuélvelo con return
    return area * precio_m2
print(costo_techo(80, 50000))   # debería mostrar 4000000


#3

def categoria(costo):
    if costo < 1000000:
        return "pequeño"
    elif costo < 4000000:
        return "mediano"
    else:
        return "grande"
print(categoria(4000000))

#4

clientes = [("Ana", 80), ("Luis", 150), ("Pedro", 15)]

def resumen(clientes):
    for nombre, area in clientes:          # tuple unpacking: dos nombres separados por coma
        costo = costo_techo(area, 50000)   # ¿qué variable del for es el área?
        cat = categoria(costo)              # ¿qué le pasas: area o costo?
        print(nombre, costo, cat)        # nombre, costo y cat

resumen(clientes)