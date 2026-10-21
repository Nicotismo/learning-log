#How to open a file
#This exercise will require several lines of code.
#Write a script that opens a file named 'test.txt' , writes 'Hello World'  to the file, 
#then closes it.

x = open('test.txt', 'w')
x.write('Hello World')
x.close()
#This will create a txt file cause there's no file with test.txt name, and it will write 
#'Hello World', then it will close it.

##################### We can use logical operators to combine comparisions
#and
#or
#not

1 < 2 > 3
#This is going to be truth
1 == 1 and 2 == 2
#This is going to be truth but the 'and' will require everything to be truth
100 == 1 or 2 == 2
#This is going to be true just because 'or' operator just needs one conditions to be truth
#This is to make it readable
#Not operator returns the oposite bolean of what you just did, for example
1 == 1 # We know is true
not(1 == 1) #This will return false


