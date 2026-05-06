"""Write program to print the following series which is shown in Given Examples.
Input 1   : 100
            1000
Output 1 : 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000"""

s=int(input("Enter Starting Range: "))
e=int(input("Enter Ending Range:"))
d=int(input("Enter the Difference you want between the range: "))
for i in range(s,e+1,d):
    print(i,end=" ")