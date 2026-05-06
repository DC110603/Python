"""Q7. Create a class Employee with:
•	instance attributes: name, base_salary
•	class variable: bonus_rate = 0.1
•	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
•	class method: update_bonus(cls, new_rate) → updates bonus for all employees
•	static method: is_valid_salary(sal) → checks if salary > 0
Create two employees, show final salaries, update bonus rate, and show again.
"""
class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            return True
        return False
emp1=Employee("swadeep",150)
emp2=Employee("Deekshith",30000)
print(emp1.final_salary()) #Final salary of Employee 1
print(emp2.final_salary()) #Final salary of Employee 2
Employee.update_bonus(0.2) #upadated the Bonus rate
print(emp1.final_salary()) #Final salary of Employee 1 After Updating bonus rate
print(emp2.final_salary()) #Final salary of Employee 2 After Updating bonus rate
print(Employee.is_valid_salary(emp1.base_salary)) #Checking if salary is valid
print(Employee.is_valid_salary(emp2.base_salary)) #Checking if salary is valid