""""Write a Program to Print the Biggest Number out of the Given three Numbers?"""
a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))
c=int(input("Enter Number 3: "))
if a>b and a>c:
    print(f"{a} is Greater among the numbers")
elif b>a and b>c:
    print(f"{b} is Greater among the numbers")
else:
    print(f"{c} is Greater among the numbers")