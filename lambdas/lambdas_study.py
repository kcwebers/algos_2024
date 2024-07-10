# via learnpython.com : https://www.learnpython.org/en/Lambda_functions

# Normally we define a function using the def keyword somewhere in the code and call it whenever we need to use it.
def sum(a , b):
    return a + b
a = 1
b = 2
c = sum(a , b)
# print(c)

# lambdas are inline functions that are defined at the same place they are used:
# your_function_name = lambda inputs : output
a = 1
b = 2
sum = lambda x , y : x + y
c = sum(a,b)
# print(c)
# Here we are assigning the lambda function to the variable sum, and upon giving the arguments i.e. a and b, it works like a normal function.

# Exercise
# Write a program using lambda functions to check if a number in the given list is odd. 
# Print "True" if the number is odd or "False" if not for each element.

l = [2,4,7,3,14,19]
for i in l:
    evens_odds = lambda i : i % 2 == 0
    # print(evens_odds(i))

# via w3schools : https://www.w3schools.com/python/python_lambda.asp

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Add 10 to argument a, and return the result:
x = lambda a : a + 10
# print(x(5)) 

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
# print(x(5, 6))

# Check if age is higher than 21
ages = [16, 23, 24, 17, 29, 19]
for i in ages:
    my_function = lambda i : i > 21
    # print(my_function(i))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument 
# will be multiplied with an unknown number:

# Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
# 'mydoubler' is the moniker for the returned lambda function / the name of the lambda
# therefore the 'myfunc' call inputs the value of 'n'
# and the 'mydoubler' handles the input for the lambda ('a')
print(mydoubler(11))

# Or, use the same function definition to make a function that always triples the number you send in:
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
# the same function&lambda can then beused to handle different scenarios
