##Range for iteration

mylist = [1,2,3]

for num in range(0,10):
    print(num)

#To enumarate


index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcde'

for item in enumerate (word):
    print(item)

### Zip function
mylist_1 = [1,2,3]
mylist_2 = ['a', 'b', 'c']

for item in zip(mylist_1, mylist_2):
    print(item)

#Min function

mylist = [10,20,30,40,50,100]
min(mylist) #It will give me the minimum value of mylist

#Max Function

mylist = [10,20,30,40,50,100]
max(mylist) #It will give me the maximum value of mylist

#Import functions from a library

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) #This will shuffle the list completely random

from random import randint
randint(0,100) #This will return a random integer from that range


############### List Comprehensions
#List comprehensions are a unique way to create a list in python

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)

#Another example
mylist = [x for x in range (0,11) if x%2==0] #x%2==0 is to grab just the even numbers of the list in range between 0 to 11

#Another example
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp +32) for temp in celcius] #This will do the convertion from celcius to fahreinheit
#Now lets break it down

fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp +32))

#If in comprehension
results = [x if x%2==0 else 'ODD' for x in range (0,11)]
#[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

#Nested loop
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
#[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]
#Comprehensive way
mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
#[200, 400, 600, 400, 800, 1200, 600, 1200, 1800]
