""" Write a program that opens a file using a context manager, reads all lines
using readlines(), and prints only the lines that contain more than 10
characters."""

with open("example.txt","r") as file:
    content=file.readlines()
    for i in content:
        if len(i)>10:
            print(i)