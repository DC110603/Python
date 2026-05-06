""""Q8. Create a class Course with:
•	class variable total_students
•	instance variable student_name
•	instance method enroll() → increments total_students
•	class method show_total(cls) → prints total students
•	static method is_eligible(age) → returns True if age ≥ 18
Demonstrate enrolling multiple students and show total count.
"""
class Course:
    total_students=0
    def __init__(self,name):
        self.name=name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        if age>=18:
            return True
        return False

std1=Course("swadeep")
std1.enroll()
std2=Course("Deekshith")
std2.enroll()
print(Course.total_students)