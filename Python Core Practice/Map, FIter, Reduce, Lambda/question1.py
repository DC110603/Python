"""1.  Use map() with a lambda to add 5 to every element of the following nested
list [[1, 2], [3, 4], [5, 6]]"""

li=[[1, 2], [3, 4], [5, 6]]
li2=list(map(lambda x: list(map(lambda x: x + 5, x)),li))
print(li2)