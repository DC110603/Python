""" Write a Python program using a context manager (with) to open a text file in
read mode, read the entire content using read(), and print the number of
characters in the file."""
with open("example.txt","r") as file:
    content=file.read()
    c=0
    for i in content:
        c+=1
    print(c)
