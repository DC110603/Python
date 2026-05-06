"""Write a program to print all Odd Numbers in Given Range.
if starting range is greater than ending range print "INVALID RANGE"""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range: "))
if s>e:
    print("Invalid Range")
else:
    for i in range(s,e+1):
        if i%2==1:
            print(i,end=" ")
