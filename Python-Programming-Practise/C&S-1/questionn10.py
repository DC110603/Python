""""Write a program to print all numbers which are divisible by 11 in given range
if no such numbers print NO NUMBERS
if starting range is greater than ending range then print INVALID RANGE"""

s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range: "))
if s>e:
    print("Invalid Range")
else:
    c=0
    for i in range(s,e+1):
        if i%11==0:
            c+=1
            print(i,end=" ")
    if c==0:
        print("No Numbers in the Range")