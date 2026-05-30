""" Create a custom context manager using @contextmanager from the contextlib
module that opens a file, yields the file object, and ensures the file is closed
even if an exception occurs."""

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):

    file = open(filename, mode)

    try:
        yield file

    finally:
        file.close()
        print("File closed")

with open_file("sample.txt", "w") as f:
    f.write("Hello World\n")


