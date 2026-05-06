""""Write a program to find the count of even numbers in given range.
if no even numbers print NO NUMBERS
if Strating range is greater than ending range print INVALID RANGE
"""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range: "))
if s>e:
    print("Invalid Range")
else:
    c=0
    for i in range(s,e+1):
        if i%2==0:
            c+=1
    if c==0:
        print("No Numbers")
    else:
        print(f"There are {c} Even Numbers in the given Range")