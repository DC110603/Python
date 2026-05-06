from module1 import Animal
from module2 import Walkable
class Dog(Animal,Walkable):
    def __init__(self,name):
        super().__init__(name)
    def show(self):
        print("Dog")

