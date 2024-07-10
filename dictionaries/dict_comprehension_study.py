# via datacamp: https://www.datacamp.com/tutorial/python-dictionary-comprehension

# Dictionary comprehension is a method for transforming one dictionary into another dictionary. 
#During this transformation, items within the original dictionary can be conditionally included 
# in the new dictionary, and each item can be transformed as needed.
# - note how similar to list comprehension this is ! just working within the laws of dictionaries instead !

# The way to do dictionary comprehension in Python is to be able to access the key objects and 
# the value objects of a dictionary.
# - easy wy to access the different elements of a dictionary is via .keys(), .values(). and items()

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
# dictates that for every key (k), the respective value will be doubled(v)
# pulls the key value pairs using the .items() method
print(double_dict1)
# {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

dict1_keys = {k*2:v for (k,v) in dict1.items()}
# dictates that the key will be cdoubled, while the value remains the same
# pulls the key value pairs using the .items() method
print(dict1_keys)
# {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4, 'ee': 5}

# ** Dictionary comprehension is a powerful concept and can be used to substitute for 
# loops and lambda functions. However, not all for loops can be written as a dictionary 
# comprehension, but all dictionary comprehension can be written with a for loop.

numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)
# {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}

# dictionary comprehension
new_dict_comp = {n:n**2 for n in numbers if n % 2 == 0}
print(new_dict_comp)