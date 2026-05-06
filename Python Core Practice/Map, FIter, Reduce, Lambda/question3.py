"""3.  Use functools.reduce() with a lambda to find the largest number from a given
list Dynamically """

from functools import reduce
from functools import reduce

numbers = [12, 45, 7, 89, 23, 56,100]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print(largest)
