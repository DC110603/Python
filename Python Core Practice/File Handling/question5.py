"""Create a custom context manager using a class that opens a file in write mode
in the __enter__ method, writes a line to the file, closes the file in the
__exit__ method, and properly prints or logs any exception information received
in __exit__."""


class FileManager:

    def __init__(self, filename,mode):
        self.filename = filename
        self.mode=mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        if self.mode == "r":
            print("File opened successfully.")
        elif self.mode == "w":
            print("File opened successfully.")
        return self.file


    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed successfully.")
        if exc_type:
            print("\nException Type :", exc_type)
        return False

try:
    with FileManager("sample.txt","r") as file:
        content=file.read()
        print(content)

except Exception as e:
    print("\nException handled outside:", e)