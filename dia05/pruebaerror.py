with open('prueba.txt', 'w') as f:
    f.write('Tejas\nClavos\nMembrana')

with open('prueba.txt', 'r') as f:
    contenido = f.read()
print (contenido)

with open('prueba.txt', 'r') as f:
    lineas = f.readlines()
    print(lineas)

#Ahora agregar una linea sin borrar
with open('prueba.txt', 'w') as f:
    f.write('Canales\n')
#IF I WANT TO ADD SOMETHING AND INSTEAD OF USING 'A' USE 'W' IT WILL OVERRIDE EVERYTHING

