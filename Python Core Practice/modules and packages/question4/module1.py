"""4. Create a package with a module containing an abstract base class (ABC).
Another module in the same package should define concrete subclasses that
implement all abstract methods2. Write a driver program that imports these
classes and demonstrates polymorphism"""
from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour