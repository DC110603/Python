""""Q10. Create a class Member that:
•	Has a shared BMI limit for “fit” status.
•	Each member stores name, height, weight.
•	Has a method to calculate BMI and check fit status.
•	Provides a function to update BMI limit for all members.
•	Offers a tool to check if height and weight entered are valid numbers.
Demonstrate:
1.	Creating multiple members.
2.	Updating BMI standard.
3.	Displaying fit status and input validity.
"""


class Member:
    bmi_limit = 18.5

    def __init__(self, name, height, weight):
        if Member.validity_check(height,weight):
            self.name = name
            self.height = height
            self.weight = weight

    def calculate_bmi(self):
        bmi = self.weight / (self.height) ** 2
        bmi=round(bmi,2)
        if Member.bmi_limit < bmi <= 25:
            return f"{bmi}-fit"
        elif bmi > 25:
            return f"{bmi}-OverWeight"
        elif bmi < Member.bmi_limit:
            return f"{bmi}-UnderWeight"
        return None

    @classmethod
    def update_bmi(cls,new_rate):
        cls.bmi_limit=new_rate

    @staticmethod
    def validity_check(x,y):
        return x>0 and y>0


mem1=Member("swadeep",1.7,65)
mem2=Member("Dekshith",1.8,68)
print(mem1.calculate_bmi())
print(mem2.calculate_bmi())
Member.update_bmi(22)
print("Body Mass Index after Updating the BMI limit")
print(mem1.calculate_bmi())
print(mem2.calculate_bmi())