"""Factorial of a number"""

def fact(n):
    if n<=1:
        return 1
    res=n*fact(n-1)
    return res

num=int(input("Enter a number: "))
print(fact(num))