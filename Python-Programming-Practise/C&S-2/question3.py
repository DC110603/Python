""""Write a Program to Print the following series 2*3,3*4,4*5,......16*17
(Print in two ways – Pattern & Multiplied value) ."""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range: "))
if s>e:
    print("Invalid Range")
else:
    c=0
    for i in range(s,e+1):
        c+=1
        if c>1:
            print(",",end="")
        print(f"{i}*{(i+1)}",end="")
    print()
    c=0
    for i in range(s,e+1):
        c += 1
        if c > 1:
            print(",", end="")
        print(f"{i*(i+1)}",end="")
