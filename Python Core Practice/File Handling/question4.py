"""Write a program that opens a file in read mode, reads the first 10 characters,
prints the current cursor position using tell(), moves the cursor back to the
beginning using seek(0), and reads the full content again."""

with open ("sample.txt", "r") as file:
    content=file.read(10)
    print(content)
    print(file.tell())
    file.seek(0)
    print(file.tell())
    print(file.read())

