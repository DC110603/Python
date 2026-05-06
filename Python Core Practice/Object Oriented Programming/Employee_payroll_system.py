"""3. You are building an employee payroll system.
Create a class Employee that stores:
• An employee’s name (should be freely accessible).
• The department they work in (should be accessible only to subclasses).
• The employee’s salary (should never be directly accessed or modified from outside
the class).
Ensure that:
• The salary value cannot be accidentally overridden or accessed using its original
name.
• Any attempt to access salary directly from outside clearly demonstrates how Python
internally alters such names.
Create a subclass Manager that:
• Introduces its own salary-related logic.
• Demonstrates what happens when a subclass defines an attribute with the same name
as one in the parent class.
Explain:
• Why Python intentionally makes private variables harder (not impossible) to access.
• How this protects large systems from accidental misuse.
• Why naming rules matter in inheritance hierarchies. """
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,designation,salary):
        self.name=name
        self._designation=designation
        self.__salary=salary
    @property
    def get_salary(self):
        return self.__salary
    @get_salary.setter
    def get_salary(self,new_sal):
        if new_sal > self.__salary:
            self.__salary = new_sal

    def call(self):
        return f"He is an Employee"

    def __str__(self):
        return f"{self.name} is an {self._designation}"
    def __repr__(self):
        return f"{self.name}"

class Manager(Employee):
    def __init__(self, name, designation, salary):
        super().__init__(name, designation, salary)

    def call(self):
        return f"He is an Employee and his designation Manager "


man1=Manager("Illegal smile Swadeep","Manager",22000)
print([man1])
print(man1.call())

