def costo(area):
    resultado = area * 45000   # usa un nombre distinto a "costo"
    return resultado              # ¿qué variable quieres devolver?

# fuera de la función (sin sangría):
total = costo(120)             
print(total)

################ TUPLE UNPACKING WITH PYTHON FUCTIONS

stock_prices = [('APPLE', 200),('GOOGLE', 400),('MICROSOFT',100)]
for item in stock_prices:
    print(item)

#Regular way of unpacking
for ticker,price in stock_prices:
    print(ticker)
    #this will return 
    #APPLE
    #GOOGLE
    #MICROSOFT

#How to do the unpacking with a function

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    #placeholders variables
    current_max = 0 #This is going to start at 0 and compare each employee hours to the current max hours and if they beat the current hours it will reset the current max to the hours value and reset employee of the month with the name of the employee
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    #return
    return (employee_of_month,current_max)
employee_check(work_hours) #This will return ('Cassie', 800)
name,hours = employee_check(work_hours) #This will unpack the name and the hours from the employee of the month

######################### INTERACTIONS BETWEEN FUNCTIONS

example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)

#Example with game

mylist = [' ','O',' ']
shuffle_list(mylist) 

def player_guess():
    guess=''

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1 or 2")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

#INITIAL LIST
mylist = [' ','O',' ']
#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)
#USER GUESS
guess = player_guess()
#CHECK GUESS
check_guess(mixedup_list, guess)