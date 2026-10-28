hungry = True

if hungry: 
    print('FEED ME')
else:
    print('Im not hungry')

#### another example
loc = 'Bank'

if loc == 'auto shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('money is cool')
else: 
    print('I do not know much')
    #This will return 'money is cool'

#Last Example

name = 'Sammy'
if name == 'Frankie':
    print('Hello Frankie!')
elif name == 'Sammy':
    print('Hello Sammy!')
else: 
    print('What is your name?')


#FOR LOOPS

#Syntax of a for loop

my_identable = [1,2,3]
for item_name in my_identable:
    print(item_name)

##########################

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

for num in mylist:
    #Check for the numbers even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)
#This will return 55 as result, note: if we idented to the for loop it will run the sum for evey number until the end

#Another example with string
mystring = 'Hello World'
for letter in mystring: 
    print(letter)
    #This will return every single letter from the string

#With tuples
mylist = [(1,2), (3,4), (5,6), (7,8)]
for item in mylist:
    print (item)
    #every tuple is an item so it will return 4 tuples in pairs 

#Tuple packing
for (a,b) in mylist:
    print(a)
    #This will return
    1
    3
    5
    7 #First item in every tuple in mylist

#with Dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)
    #This returns the keys
    #k1
    #k2
    #k3
#or
for item in d.items():
    print(item)
    #This will return the key and value like the tuples
    ('k1', 1)
    ('k2', 2)
    ('k3', 3)
    #Important note if you have a very large dictionary there is no warranty that things
    # are going to be sorted

######## WHILE LOOPS #########
#While loops will continue to execute a block of code while some condition remains True.
#For example, while my pool is not full, keep filling my pool with water

#Syntax of a while loop
while some_boolean_condition:
    #do something
else: 
    #do something different

#Examples

x = 0
while x < 5:
    print(f'The current value of x is {x}') 
    x = x + 1
else:
    print("X IS NOT LESS THAN 5")

##SOME KEYWORDS##
# break: Breaks out of the current closest enclosing loop
# continue: Goes to the top  of the closest enclosing loop
# pass: Does nothing at all

#Example
x = [1,2,3]
for item in x:
    #comment
    pass
print ('end of my script')

#Example with continue
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
    #This will print SMMY it will remove the letter 'a' from the string

#Example with break
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        break
    print(letter)
    #This will break out from the closest enclosing loop and it will return in this case
    #Just thew letter 's'

#another example
x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
    #This will return just 0,1 because its break it out in 2 


areas = [1200, 850, 3100, 2000, 500, 5000]

for area in areas:
    if area <=1200:
        print (f'{area} pies cuadrados: Small Area')
    elif area <= 3100:
        print (f'{area} pies cuadrados: Medium Area')
    else:
        print (f'{area} pies cuadrados: Big Area!')