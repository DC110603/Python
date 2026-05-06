""""Write a program to perform Addition, Subtraction, Multiplication and Division of 2 Numbers
based on the user inputs by using Switch condition.(+ , - , * , /, %)."""
num1=int(input("enter Number 1: "))
num2=int(input("Enter Number 2: "))
s=input("Enter any of the symbols + , - , * , /, % : ")
if s=="+":
    print(f"Addition of {num1} and {num2} is {num1+num2}")
elif s == "-":
    print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
elif s == "*":
    print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
elif s == "/":
    print(f"Division of {num1} and {num2} is {num1 / num2}")
elif s == "%":
    print(f"Modulo Division of {num1} and {num2} is {num1 % num2}")
else:
    print("Invalid Input")