"""Write a program to print sum of squares of the numbers in given range .
if starting range is Greater than ending range print "INVALID RANGE"""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range: "))
if s>e:
    print("Invalid Range")
else:
    for i in range(s,e+1):
        print((i**2),end=" ")

