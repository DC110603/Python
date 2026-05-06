""""Q1. Create a class Student that:
•	Keeps track of the total number of students created.
•	Determines whether a student passed or failed based on a shared passing mark.
•	Provides a method to curve marks by increasing everyone’s marks by a percentage.
•	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
Demonstrate:
1.	Creating multiple students.
2.	Applying a grading curve.
3.	Displaying updated results with letter grades.
"""
class Student:
    total_number_students=0
    passing_marks=40
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name
        Student.total_number_students+=1
    def curve_marks(self,percentage):
        perc=(self.marks/percentage)
        return self.marks+perc
    def result(self):
        if self.marks>Student.passing_marks:
            return True
        return False
    def convert_marks(self):
        if 80 < self.marks <=100:
            return "A"
        elif 60 < self.marks <=79:
            return "B"
        elif 40 < self.marks <=59:
            return "C"
        else:
            return "F"

std1=Student("swadeep",69)
std2=Student("Deekshith",39)
print(std1.marks) #Marks before Changing
print(std2.marks) #Marks before Changing
print(Student.total_number_students) #Checking Total number of Students
print(std1.curve_marks(8)) #Increasing student marks by 8 percent
print(std2.curve_marks(9)) #Increasing student percentage by 9 percent
print(std1.convert_marks()) #Converting student marks to grade
print(std2.convert_marks()) #Converting student marks to grade
print(std1.result())
print(std2.result())