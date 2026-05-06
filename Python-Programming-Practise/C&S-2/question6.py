""""Write a program to print sum of all even numbers in between the Given Numbers
if no even numbers print NO NUMBERS
if starting range is greater than ending range then print INVALID RANGE"""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range: "))
if s>e:
    print("Invalid Range")
else:
    c=0
    su=0
    for i in range(s,e+1):
        if i%2==0:
            c+=1
            su+=i
    if c==0:
        print("No Numbers")
    else:
        print(f"Sum of all Even Numbers in the given Range is {su}")