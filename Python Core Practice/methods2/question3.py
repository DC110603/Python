""""Q3. Create an Employee class that:
•	Keeps a minimum experience required for promotion (shared across all employees).
•	Stores employee name, experience, and department.
•	Has a method to check eligibility for promotion.
•	Provides a function to update promotion criteria globally.
•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
Demonstrate:
1.	Creating employees from different departments.
2.	Changing promotion criteria.
3.	Displaying eligibility results and department validation.
"""
class Employee:
    min_experience=3
    dept_list=["hr","it","admin","tech","support"]
    def __init__(self,name,exp,dept):
        self.name=name
        self.experience=exp
        self.department=dept
    def eligibility(self):
        if self.experience>=Employee.min_experience:
            return True
        return False
    @classmethod
    def update_min_exp(cls,new_min_exp):
        cls.min_experience=new_min_exp
    @staticmethod
    def check_dept(dept):
        if dept in Employee.dept_list:
            return True
        return False
emp1=Employee("Deekshith",2,"it")
emp2=Employee("Swadeep",4,"hr")
emp3=Employee("Eshwar",1,"House-Keeping")
var1 = f"{emp1.name} is Eligible for Promotion" if emp1.eligibility() else f"{emp1.name} is Not eligible for Promotion"
var2 = f"{emp2.name} is Eligible for Promotion" if emp2.eligibility() else f"{emp2.name} is Not eligible for Promotion"
var3 = f"{emp3.name} is Eligible for Promotion" if emp3.eligibility() else f"{emp3.name} is Not eligible for Promotion"
print(var1) #Checking Eligibility for promotion
print(var2) #Checking Eligibility for promotion
print(var3) #Checking Eligibility for promotion
Employee.update_min_exp(2)
va1 = f"{emp1.name} is Eligible for Promotion" if emp1.eligibility() else f"{emp1.name} is Not eligible for Promotion"
va2 = f"{emp2.name} is Eligible for Promotion" if emp2.eligibility() else f"{emp2.name} is Not eligible for Promotion"
va3 = f"{emp3.name} is Eligible for Promotion" if emp3.eligibility() else f"{emp3.name} is Not eligible for Promotion"
print(va1) #Checking Eligibility for promotion After Updating the Min Experience
print(va2) #Checking Eligibility for promotion After Updating the Min Experience
print(va3) #Checking Eligibility for promotion After Updating the Min Experience
print(Employee.check_dept(emp1.department))
print(Employee.check_dept(emp2.department))
print(Employee.check_dept(emp3.department))