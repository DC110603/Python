"""2. Given two lists:
a = [1, 2, 3, 4] b = [10, 20, 30, 40]
Use map() with a lambda to create a new list containing the sum of corresponding
elements.
What happens if the lists are of unequal length?"""

a = [1, 2, 3, 4,5,6]
b = [10, 20, 30, 40]

print(list(map(lambda x,y: x+y,a,b)))

# The result set consists common number of items in a list the rest are left