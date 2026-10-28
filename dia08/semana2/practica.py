#####PRACTICA#####

#Clasificar techos. Pide los pies² con float(input()). Si son menos de 1000, imprime “Techo pequeño”. 
# Si van de 1000 a 2500, imprime “Mediano”. Si son más, imprime “Grande”.

x = float(input('Dime los pies del techo: '))
if x < 1000:
    print('Small roof')
elif x <= 2500:
    print('Medium roof')
else:
    print('Big roof!')

#Clasificar una lista de áreas. Recorre [1200, 850, 3100, 2000] con for e 
#imprime cada área con su categoría.

areas = [1200, 850, 3100, 2000, 500, 5000]

for area in areas:
    if area < 1000:
        print(f'{area} pies²: Small Area')
    elif area <= 2500:
        print(f'{area} pies²: Medium Area')
    else:
        print(f'{area} pies²: Big Area')

#Área total. Suma las áreas de esa lista. 
areas = [1200, 850, 3100, 2000, 500, 5000]
total = 0

for area in areas:
    total = total + area
print (total)      

#Precios por material. Usa este diccionario: precios = {"asfalto": 4.5, "metal": 9.0, "teja": 12.0}. 
# Recórrelo con for material, precio in precios.items(): e imprime una línea por material.

precios = {"asfalto": 4.5, "metal": 9.0, "teja": 12.0}

for material, precio in precios.items():
    print(f'{material} cuesta ${precio} por pie²')
   
    
