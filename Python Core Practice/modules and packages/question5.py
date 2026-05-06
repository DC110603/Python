"""5. Create three modules:
Module A: class Animal
Module B: class Walkable
Module C: class Dog that inherits from both Animal and Walkable
Demonstrate method resolution order (MRO) by calling overridden methods2 and
printing the MRO"""
from question5.module3 import Dog
animal1=Dog("Dog1")
print(animal1.__mro__)