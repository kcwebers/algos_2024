# via w3 : https://www.w3resource.com/python-exercises/lambda/index.php

# ============================================================================
# 1. Write a Python program to create a lambda function that adds 15 to a given number 
# passed in as an argument, also create a lambda function that multiplies argument x with 
# argument y and prints the result.
# Sample Output:
# 25
# 48
# ============================================================================

x = lambda n : n + 15
y = lambda x, y : print(x * y)

print(x(10))
y(5, 3)
y(4, 12)

# ============================================================================
# 2. Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
# ============================================================================

def multiplier(n):
    return lambda x : x * n

doubler = multiplier(2)
tripler = multiplier(3)
quader = multiplier(4)
quinter = multiplier(5)

print(doubler(15))
print(tripler(15))
print(quader(15))
print(quinter(15))

# ============================================================================
# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# ============================================================================

subj_grades =[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subj_grades.sort(key = lambda x : x[1])
print(subj_grades)
subj_grades.sort(key = lambda x : x[0])
print(subj_grades)
# ** for the .sort() function, the parameter 'key' indicates the corting criteria(s)
# so, the above is saying to look at each index, and sort based on the specific part of the tuple
# see also https://www.w3schools.com/python/ref_list_sort.asp

# ============================================================================
# 4. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
# ============================================================================

cellphone_models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
cellphone_models.sort(key = lambda x : x['color'])
print(cellphone_models)

# ============================================================================
# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
# ============================================================================

numbas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# quickie list comprehension!
# evens = [x for x in numbas if x % 2 == 0]
# odds = [x for x in numbas if x % 2 != 0]
# print(evens)
# print(odds)


# filter(function, iterable)
# via w3 schools : https://www.w3schools.com/python/ref_func_filter.asp
# filter outputs as an Iterable (not list) and needs to be converted
# via https://www.simplilearn.com/tutorials/python-tutorial/filter-in-python

# evens
# numbas = list(filter(lambda x : x % 2 == 0 , numbas))
# print(numbas)
# odds
numbas = list(filter(lambda x : x % 2 != 0 , numbas))
print(numbas)

# ============================================================================
# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# ============================================================================

numbas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# quickie list comprehension practice!
# squared = [x**2 for x in numbas]
# tripped = [x**3 for x in numbas]
# print(squared)
# print(tripped)

# squared = []
# for i in numbas:
#     squared.append(lambda i : i**2)
# print(squared) 
# WRONG!
# for i in numbas:
#     lambda i : i**2
# print(numbas)
# WRONG!

# map(function, iterables) 
# The map() function executes a specified function for each item in an iterable. 
# The item is sent to the function as a parameter.
# returns an iterable, needs to convert back to a list
# via w3schools

squared = list(map(lambda i : i**2, numbas))
print(squared)
tripped = list(map(lambda i : i**3, numbas))
print(tripped)

# ============================================================================
# 7. Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False
# ============================================================================

# **my notes: doesn't mention being case sensistive


def check_word(word):
    return lambda letter : letter == word[0].lower()

check_first_letter = check_word("Hello")
# print(check_first_letter("h"))
# print(check_first_letter("q"))

# w3 schools response
starts_with = lambda x: True if x.startswith('P') else False
# this answer isn't as dynamic as I thought because the character can't be apssed in
# is the character is static then this works

# breakdown of w3 lambda
# lambda x : <------ input
# lambda x : True <--- return True 
# if x.startswith('P') <------ if the input starts with 'P'
# else False <--------- else return False

# .startswith() https://www.w3schools.com/python/ref_string_startswith.asp
# string method, method is case sensitive!

# more dynamic
check_beginning_letter = lambda x , y : True if x.startswith(y) else False
# print(check_beginning_letter("Hello", "h")) # False
# print(check_beginning_letter("Hello", "H")) # True
# print(check_beginning_letter("Hello", "z")) # False

check_beginning_letter = lambda x , y : True if x[0].lower() == y.lower() else False
print(check_beginning_letter("Hello", "h")) # True
print(check_beginning_letter("Hello", "H")) # True
print(check_beginning_letter("Hello", "z")) # False


# ============================================================================