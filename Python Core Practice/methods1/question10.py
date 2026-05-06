"""Q10. Create a class Student with:
•	class variable passing_marks = 40
•	instance attributes name, marks
•	instance method result() → prints pass/fail using class variable
•	class method update_passing_marks(cls, new_marks)
•	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
Use all three in a program that:
1.	Creates students
2.	Updates the passing criteria
3.	Displays grade category and result"""
class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            return "Pass"
        return "Fail"
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if 80 < marks <=100:
            return "A"
        elif 60 < marks <=79:
            return "B"
        elif 40 < marks <=59:
            return "C"
        else:
            return "F"