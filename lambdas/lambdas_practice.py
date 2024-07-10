# via w3 : https://www.w3resource.com/python-exercises/lambda/index.php

# 1. Write a Python program to create a lambda function that adds 15 to a given number 
# passed in as an argument, also create a lambda function that multiplies argument x with 
# argument y and prints the result.
# Sample Output:
# 25
# 48

x = lambda n : n + 15
y = lambda x, y : print(x * y)

print(x(10))
y(5, 3)
y(4, 12)

# 2. Write a Python program to create a function that takes one argument, 
# and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

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

# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

subj_grades =[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subj_grades.sort(key = lambda x : x[1])
print(subj_grades)
subj_grades.sort(key = lambda x : x[0])
print(subj_grades)
# ** for the .sort() function, the parameter 'key' indicates the corting criteria(s)
# so, the above is saying to look at each index, and sort based on the specific part of the tuple
# see also https://www.w3schools.com/python/ref_list_sort.asp

# 4. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]


