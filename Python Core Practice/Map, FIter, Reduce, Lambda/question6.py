"""6.  Use filter() to remove all vowels from a string and print the final string."""

st="abcdefghijklmnopqrstuvwxyz"
st2=list(filter(lambda x: x not in ["a","e","i","o","u"],st))
print(st2)
