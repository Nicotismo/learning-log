def myfun(a,b):
    # Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

#*args will help to pass as much parameters as we want
#*args recibe muchos valores y los guarda como tupla.

def myfun(*args):
    return sum(args) * 0.05
#I can keep adding as many numbers as I want
myfun(40,60,100,1,34)

#**kwargs recibe valores con nombre y los guarda como diccionario.

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

#Combination

def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')


##Ejercicios

#1suma_areas(*args) devuelve la suma de todas las áreas.

def suma_areas(*args):
    return sum (args)

#2 techo_mas_grande(*args) devuelve el área mayor.

def techo_mas_grande(*args):
    return max(args)

#3 ficha_cliente(**kwargs) imprime cada dato. 

def ficha_cliente(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

ficha_cliente(nombre="Ana", ciudad="Cali", area=80)

