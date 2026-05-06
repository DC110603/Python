"""Q5. Create a class Temperature with:
•	instance attribute celsius
•	a static method to_fahrenheit(celsius)
•	an instance method show_conversion() that uses the static method to print both values.
"""
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius*(9/5))+32
    def show_conversion(self,c):
        f=Temperature.to_fahrenheit(c)
        return f,c
temp1=Temperature(41)
print(temp1.show_conversion(temp1.celsius)) # returns both fahrenheit and celsius
print(Temperature.to_fahrenheit(35)) # returns only Fahrenheit