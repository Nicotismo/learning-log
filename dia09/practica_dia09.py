#1. Pares. Imprime los pares del 1 al 20, ahora con range. 

for num in range(1,21):
    if num % 2 == 0:
        print(num)

for num in range (2,21,2):
    print (num)

#Cuenta regresiva de obra. Empieza con dias = 5 y, con un while, 
#imprime “Faltan X días para terminar el techo” hasta llegar a 0. 

dias = 5

while dias >0:
    print(f'Faltan {dias} dias para terminar el techo')
    dias = dias -1
else:
    print('Techo terminado')

#Sumar áreas hasta escribir 0. Pide áreas con float(input()) y súmalas mientras el usuario no escriba 0. Al final, imprime el total. 

total = 0
area = float(input('Dime el área (0 para terminar): '))

while area > 0:
    total = total + area
    area = float(input('Dime el área (0 para terminar): '))

print(f'Área total: {total} pies²')

#Lista numerada. Con materiales = ["asfalto", "metal", "teja"] y enumerate, imprime 1. asfalto, 2. metal y 3. teja. 
#Pista: enumerate empieza en 0, así que suma 1 o prueba start=1.

lista = ['asfalto', 'metal', 'teja']
for item, material in enumerate(lista, start=1):
    print(f'{item}, {material}')

#Cliente y área. Con clientes = ["Ana", "Luis", "Marta"], areas = [1200, 850, 3100] y zip, imprime Ana: 1200 pies² y así con los demás.

clientes = ['Ana', 'Luis', 'Marta']
areas = [1200, 850, 3100]

for item1, item2 in zip(clientes, areas):
    print (f'Cliente: {item1} {item2} pies cuadrados')