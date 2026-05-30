"""• Write a program using a context manager that opens a file in read mode, uses a
loop to read the file in small chunks (for example, 5 characters at a time),
prints the cursor position after each read using tell(), uses seek() to move to
a specific position, and continues reading from there"""

from contextlib import contextmanager

@contextmanager
def open_file(fname, mode="r"):
    file = open(fname, mode)

    try:
        print("Opened file")
        yield file
    finally:
        file.close()
        print("FILE CLOSED")
with open_file("sample.txt") as file:
    content = file.read()
    file.seek(0)
    while file.tell() < len(content):
        print(file.read(5))
        file.seek(file.tell() -2)
