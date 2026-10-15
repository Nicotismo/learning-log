##Tipos de datos en Python
#Integers -- int -- Whole numbers such as 1, 2, 3, -1, -2, -3
#floats -- float -- Numbers with decimal points such as 1.0, 2.5, -3.14
#strings -- str -- Textual data such as "Hello", "Python", "Data"
#lists -- list -- Ordered collections of items such as [1, 2, 3], ["apple", "banana", "cherry"]
#Dictionaries -- dict -- Key-value pairs such as {"name": "Alice", "age": 30}, {"city": "New York", "country": "USA"}
#Tuples -- tuple -- Ordered, immutable collections of items such as (1, 2, 3), ("apple", "banana", "cherry")
#sets -- set -- Unordered collections of unique items such as {1, 2, 3}, {"apple", "banana", "cherry"}
#Booleans -- bool -- True or False values used for logical operations

#Variables Example
my_income = 5000  # Integer
tax_rate = 0.1  # Float
my_taxes = my_income * tax_rate  # Float
print(my_taxes)  # Output: 500.0

#Simple Hello World Example
print("Hello World")  # Output: Hello World

#Grabbing characters from a string
my_string = "Hello World"
my_string[0]  # Output: 'H'
my_string[1]  # Output: 'e'
my_string[5]  # Output: 'o'
#Grabbing in reverse
my_string[-1]  # Output: 'd'
#Grabbing a range of characters
my_string[0:5]  # Output: 'Hello'
#Grabbing a range of characters with a step
my_string[0:5:2]  # Output: 'Hlo'
#Grabbing a range with jumping
my_string[::2]  # Output: 'HloWrd'


#Strings Concatination
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Output: 'John Doe'
#anotther example
Name = "Pam"
Last_letters = Name[1:]  # Output: 'am'
print(Last_letters)  # Output: 'am'
'P' + Last_letters  # Output: 'Pam'

#Print Formatting with strings
#Using the format method
print("Hello, {}".format("Alice"))  # Output: 'Hello, Alice'
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))  # Output: 'The quick brown fox'
print('The {b} {q} {f}'.format(f='fox', q='quick', b='brown'))  # Output: 'The brown quick fox'

#Float Formatting
result = 100/777
print("The result was {}".format(result))  # Output: 'The result was 0
print("The result was {r:1.3f}".format(r=result))  # Output: 'The result was 0.129'

#f-Strings (Python 3.6+)
name = "Alice"
print(f"Hello, {name}")  # Output: 'Hello, Alice'