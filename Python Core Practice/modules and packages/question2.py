"""2. Create a Python package that contains two or more modules. Each module should
define classes with attributes and methods2. Then create another module outside
the package, import the package modules, and create a subclass that inherits
from at least one of the classes. Finally, create objects of both parent and
child classes."""
from mypackage.package1 import Student
from mypackage.package2 import Teacher

class Books(Student):
    def __init__(self,name,branch,book):
        super().__init__(name,branch)
        self.book=book
    def show(self):
        print(f"Book borrowed: {self.book}")
std1=Student("Deekshith","CSM")
std1.show()
teacher1=Teacher("Naveena","Life Lessons")
teacher1.show()
books1=Books("Naveena","Life sciences","IKIGAI")
books1.show()