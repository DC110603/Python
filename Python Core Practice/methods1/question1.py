""""Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed
"""
class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>Student.passing_marks:
            return True
        return False
std1=Student("Swadeep",39)
std2=Student("Deekshith",96)
if std1.is_passed():
    print("Pass")
else:
    print("Fail")
if std2.is_passed():
    print("Pass")
else:
    print("Fail")