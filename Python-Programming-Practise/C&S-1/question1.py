""""Write a program to find sum of all the numbers in given range
if starting index is greater than ending index print INVALID RANGE"""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending of the Range: "))
if s>e:
    print("Invalid Range")
else:
    su=0
    for i in range(s,e+1):
        su+=i
    print(f"The sum of numbers between {s} and {e} is {su}")
