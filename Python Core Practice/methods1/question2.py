""""Q2. Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances.
"""
class Employee:
    company_name="TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_name(cls,new_name):
        cls.company_name=new_name

emp1=Employee("Swadeep")
print(emp1.company_name)
Employee.change_name("Google")
print(emp1.name,"Works at",emp1.company_name)