"""Digits of a number using recursion"""

def digitsofnumber(n):
    if n<=0:
        return
    print(n%10)
    digitsofnumber(n//10)

digitsofnumber(293)