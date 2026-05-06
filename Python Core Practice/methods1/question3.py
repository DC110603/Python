""""Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance
"""
class MathOps:
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        return False
obj=MathOps()
print(obj.is_even(5))
print(MathOps.is_even(4))