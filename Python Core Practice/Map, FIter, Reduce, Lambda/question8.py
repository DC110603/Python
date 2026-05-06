"""8.  Given a list of integers, use map() with id() to print the memory address
of each element.
Example: [10, 350, 10, 350, 20] — explain why some addresses repeat."""

li=[10, 350, 10, 350, 20]
li2=list(map(lambda x: id(x),li))
print(li2)

# both the integer objects are less than 256 so they point out to the same memory location 