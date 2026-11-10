##METHODS AND FUNCTIONS
#Functions in python allow us to create blocks of code that can be easily executed many times
#without needing to contstantly rewrite the entire block of code


#DEF KEYWORD

# def name_of_function():
#    """
#   Docstring explains function.
 #   """


def say_hello(name):
    print(f'Hello {name}')
say_hello('Jose') #This will print 'Hello Jose'

#Return keyword

def add_num(num1,num2):
    return num1+num2
#Then if you call add_num(10,30) it will return 30 

#Functions with logic

def even_check(number):
    result = number % 2 == 0
    return result

even_check(20) # This will return as true, or if I enter an odd numeber will return false

#################

#RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass #pass is don't do anything

    return False

check_even_list([2,4,5]) #This will return True, but if we change to an odd number it will return False

######################

def check_even_list(num_list):
    #Return all the even numbers in a list

    #placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass #pass is don't do anything

    return even_numbers

check_even_list([1,2,3,4,5]) #This will just return the even numbers 2 and 4

###### PRACTICE

#1. area_techo(largo, ancho) debe devolver el área.

def area_techo(largo, ancho):
    return(largo * ancho)
print(area_techo(400, 600)) 

#2. costo_techo(area, precio_m2) devuelve el costo. Después úsala junto con la anterior en una sola línea.

def costo_techo(area, precio_m2):
    return(area * precio_m2)
print(costo_techo(area_techo(400, 600), 100))

#3. categoria(costo) devuelve "pequeño", "mediano" o "grande" con if/elif/else.
def categoria(costo):
    if costo < 1000000:
        tipo = 'small'          # pon aquí el texto "pequeño"
    elif costo <=3000000 :               # ¿qué condición va aquí? mira la tabla
        tipo = 'medium'
    else:
        tipo = 'Big'
    return tipo             # un solo return, fuera del if pero dentro del def

print(categoria(500000))     # debería decir: pequeño
print(categoria(3000000))    # debería decir: mediano
print(categoria(9000000))    # debería decir: grande

#4. es_par(n) devuelve True o False. 

def even_check(num):
    return num % 2 == 0
print(even_check(7))

#5. Función vs método: escribe en comentarios por qué es max(costos) y no costos.max(), 
# y por qué es nombres.append(x) y no append(nombres, x)

# max(costos): max es una FUNCIÓN, va sola y recibe la lista entre paréntesis.
#   costos.max() da error porque las listas no tienen ese método.
# nombres.append(x): append es un MÉTODO de la lista, va después del punto.
#   append(nombres, x) da error porque append no existe como función suelta.