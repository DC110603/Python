""""Q5. Create a class Course that:
•	Tracks total courses created.
•	Each course has a title, duration, and enrolled_students.
•	Provides a method to enroll a new student.
•	Allows updating the minimum duration for a valid course across all instances.
•	Has a static function to check if a given duration is realistic (not negative, not too large).
Demonstrate:
1.	Creating multiple courses.
2.	Enrolling students.
3.	Updating minimum duration and checking durations.
"""
class Course:
    total_courses=0
    minimum_duration=6
    def __init__(self,title,duration,enrolled_students):
        if Course.check_duration(duration):
            self.title=title
            self.duration=duration
            self.enrolled_students=enrolled_students
            Course.total_courses+=1
    def enroll(self,no_of_students):
        self.enrolled_students+=no_of_students
    @classmethod
    def update_min_duration(cls,new_duration):
        cls.minimum_duration=new_duration
    @staticmethod
    def check_duration(dur):
        if 5 < dur <= 12:
            return True
        return False
course1=Course("Python",6,35)
course2=Course("Java",7,29)
course3=Course("Full_Stack_Development",14,69)

print("Students enrolled:",course1.enrolled_students)
print("Students enrolled:",course2.enrolled_students)
print("Total no of Courses Created",Course.total_courses) #This object will not be created because the duration is way more high
course1.enroll(3)
course2.enroll(6)
print("Students enrolled after updating:",course1.enrolled_students)
print("Students enrolled after updating:",course2.enrolled_students)

