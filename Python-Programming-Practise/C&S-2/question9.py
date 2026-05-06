"""Write a Program to Print the Alternative Even Numbers Between the Given Numbers?
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
            if c%2==1:
                if c>1:
                    print(",",end=" ")
                print(i,end="")
