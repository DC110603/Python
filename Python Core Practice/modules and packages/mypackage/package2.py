"""2. Create a Python package that contains two or more modules. Each module should
define classes with attributes and methods2. Then create another module outside
the package, import the package modules, and create a subclass that inherits
from at least one of the classes. Finally, create objects of both parent and
child classes."""
class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def show(self):
        print(f"Name of the Faculty: {self.name}  subject: {self.subject}")
