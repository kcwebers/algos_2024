# exploring lists more in depth 

# List comprehension via W3 schools
# https://www.w3schools.com/python/python_lists_comprehension.asp

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
# ['apple', 'banana', 'mango']

# vs

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
# x
# for x in fruits
# if "a" in x

# statement is saying that each item from list 'fruits' that meets the criteria
# will be added to the 'newlist'
# basically pulls the final condition of newlist.append(x) to the front of the statement
# the newlist will be built off of 'x' as it meets the requirements of the loop and if statements

print(newlist)
# ['apple', 'banana', 'mango']