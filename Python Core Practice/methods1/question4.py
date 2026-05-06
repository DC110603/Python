""""Q4. Create a class Car with:
•	instance attribute mileage
•	class attribute wheels = 4
Add an instance method display_specs() that prints mileage and wheels.
Then change wheels using a class method, and print again.
"""
class Car:
    wheels = 4
    def __init__(self,mileage):
        self.mileage = mileage
    def display_specs(self):
        return self.mileage,self.wheels
    @classmethod
    def change_wheels(cls,a):
        cls.wheels=a
car2=Car(6)
car1=Car(26)
print(car1.display_specs())
print(car2.display_specs())
Car.change_wheels(12)
print(car1.display_specs())
print(car2.display_specs())