"""Write a program that creates a file and writes 3 lines using write(), reopens
the same file in append mode, appends 2 more lines, and finally reads and prints
the complete file content."""

with open("sample.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")


with open("sample.txt", "a") as file:
    file.write("This is line 4\n")
    file.write("This is line 5\n")


with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:\n")
print(content)