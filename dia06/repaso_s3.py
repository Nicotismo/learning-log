#Test your knowledge.
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
55*2
220/2
10**2+10
55+55
120-10

#Answer these 3 questions without typing code. Then type code to check your answer.

#What is the value of the expression 4 * (6 + 5) #44

#What is the value of the expression 4 * 6 + 5 #29

#What is the value of the expression 4 + 6 * 5 #34

###Strings
#Con s = 'hello': saca la 'e' por índice, 
#invierte el texto con slicing y saca la 'o' de 2 formas.
s= 'hello'
s[1] #Returns E
s[::-1] #Returns the string in reverse
#Grabbing 'o' in 2 different ways
s[4]
s[-1]

#Crea [0,0,0] de 2 formas distintas y ordena [5,3,4,6,1]
[0]*3
list_2 = [0, 0, 0]
list_3 = [5,3,4,6,1]
list_3.sort()
print(list_3)

#Saca 'hello' de una lista o un diccionario anidado.
list = ['hello', 'world']
print(list[0])
dict = {'word': 'hello'}
dict['word'] #This will return the value in this case 'hello'

#Saca los valores únicos de [1,2,2,33,4,4,11,22,3,3,2]
newlist = [1,2,2,33,4,4,11,22,3,3,2]
print(set(newlist))