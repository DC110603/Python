"""2. Build:
• Vehicle base class
• Car, Bike, Auto subclasses
• A Driver class that contains a Vehicle
• A Ride class that:
o Calculates fare differently depending on the type of vehicle (polymorphism)
o Stores driver + vehicle combination
o Protects internal fare formula through encapsulation
Also:
• Use __str__ to print readable ride summaries.
Show how composition + polymorphism interact. """
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,name,vehicle):
        self.name=name
        self.vehicle=vehicle
    @abstractmethod
    def calculate_fare(self, distance):
        pass
class Car(Vehicle):
    base_fare=50
    per_km=26
    def __init__(self, name, vehicle):
        super().__init__(name, vehicle)
    def calculate_fare(self,distance):
        return Car.base_fare + (distance*self.per_km)

class Auto(Vehicle):
    base_fare=30
    per_km=18
    def __init__(self, name, vehicle):
        super().__init__(name, vehicle)
    def calculate_fare(self,distance):
        return Auto.base_fare + (distance*self.per_km)

class Bike(Vehicle):
    base_fare=20
    per_km=11
    def __init__(self, name, vehicle):
        super().__init__(name, vehicle)
    def calculate_fare(self,distance):
        return Bike.base_fare + (distance*self.per_km)

class Ride:
    def __init__(self,driver,vehicle,distance):
        self.driver=driver
        self.vehicle=vehicle
class Driver:
    def __init__(self,name,vehicle):
        self.name = name
        self.vehicle = vehicle

car=Car("dc","car")
print(car.calculate_fare(10))
