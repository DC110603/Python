"""Write program to print the following series which is shown in Given Examples.
Input 1  :    10
             -12
Output 1:
50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, (-5), (-10), (-15), (-20), (-25), (-30),
 (-35), (-40), (-45), (-50), (-55), (-60)"""

s=int(input("Enter Starting Range:"))
e=int(input("Enter Ending  Range:"))
c=0
if s>e:
    for i in range(s,e-1,-1):
        if c>0:
            print(",",end=" ")
        if i<0:
            print(f"({i*5})",end="")
        else:
            print(f"{i*5}",end="")
        c+=1
else:
    for i in range(s,e+1):
        if c>0:
            print(",",end=" ")
        if i<0:
            print(f"({i*5})",end="")
        else:
            print(f"{i*5}",end="")
        c+=1

