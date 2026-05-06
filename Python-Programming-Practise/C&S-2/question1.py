"""Write a program to print all alternative even numbers in the given range
if no numbers then print NO NUMBERS
if starting range is greater than ending range print INVALID INPUTS"""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range: "))
if s>e:
    print("Invalid Inputs")
else:
    c=0
    for i in range(s,e+1):
        if i%2==0:
            c+=1
            print(i,end=" ")
    if c==0:
        print("No Numbers in the Range")