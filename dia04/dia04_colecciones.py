my_list= [1,2,3]
len(my_list)
#Concatenated
another_list= [4,5]
new_list= my_list + another_list
#Change elements in a list

new_list[0] = 'ONE ALL CAPS'
#Add new item to the end of the list
new_list.append('six')
#Remove an item from the end the list
new_list.pop() # IT will delete the last item in the list, in this case 'six'
#Remove an item from an specific part of the list
new_list.pop(0) # It will remove the first item on the list, you can call it by the number where is located on the list
#If we want to organice a list
new_list= ['a', 'd', 'b', 'c', 'e']
new_list.sort() #This will sort of the list into an alphabetical order

#Lists FAQ

#1. How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?
#You would just add another set of brackets for indexing the nested list, for example: my_list[2][1]

#DICTIONARIES
my_dict = {'key1': 'value1', 'key2': 'value2'}}
#To call the value
my_dict['key1'] #It will return 'value1'
prices_lookup= {'apple': 2.99, 'oranges': 1.99, 'milk': 5}
prices_lookup ['apple'] #It will give me the price of the apple, that in this case is $2.99
#We can also add a list to a dictionary and call it
d = {'L1': [1,2,3]}
d ['L1'] # That should call the list, 1,2,3

#Some methods
d = {'k1': 100, 'k2': 200, 'k3': 300}
d.keys () #This will return all the actual keys K1, K2, K3
d.values () #This will return all the actual values, 100, 200, 300
d.items() #This will return all the pairs 'k1':100, 'k2':200, 'k3':

#####TUPLES
#They are similar to lists, but they are not mutable
#Once an element is inside a tuple, it can be reassingned

t=(1,2,3)
mylist= [1,2,3]
#Tuples are actually going to be necessary when you will like to get data unmutable

####SETS
#Sets are unordered collections of unique elements, meaning there can only be one representative of the same object

myset= set()
#to add something
myset.add(1) #And it will add the number 1 to the set
myset.add(2) #It will add the number 2 without deleting the number 1
#However, if we try to add again the number 2 or 1, it will not let us do it, cause a set shoud contain unique values in there

####BOOLEANS
#Booleans are operators that allow you to convey True or False statements
True
False
#Example
1 == 1 
#That's gonna pop up True



