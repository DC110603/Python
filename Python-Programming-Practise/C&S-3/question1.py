""""Write program to print the following series which is shown in Given Examples.
Input 1  : 10
          -12
Output 1:
5*10, 5*9, 5*8, 5*7, 5*6, 5*5, 5*4, 5*3, 5*2, 5*1, 5*0,
5*(-1), 5*(-2), 5*(-3), 5*(-4), 5*(-5), 5*(-6), 5*(-7), 5*(-8), 5*(-9), 5*(-10), 5*(-11), 5*(-12)
"""
s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending of the Range: "))
if s==0 or e==0:
    print("Invalid Range")
else:
    c=0
    if s>0 and e<0:
        for i in range(s,e-1,-1):
            c+=1
            if c>1:
                print(",",end=" ")
            if i >=0:
                print(f"{5}*{i}",end="")
            else:
                print(f"{5}*({i})",end="")
    else:
        c=0
        for i in range(s,e+1):
            c+=1
            if c>1:
                print(",",end=" ")
            if i >=0:
                print(f"{5}*{i}",end="")
            else:
                print(f"{5}*({i})",end="")