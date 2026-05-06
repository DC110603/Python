""".  What happens if the lambda passed to reduce() accepts only one parameter or
three parameters? Explain the output or error."""
from functools import reduce

li = [10, 20, 30, 40, 50]
li2 = reduce(lambda x: x > 0, li)
print(li2)

#TypeError: <lambda>() takes 1 positional argument but 2 were given
#TypeError: <lambda>() missing 1 required positional argument: 'z'