"""Write program to print the following series which is shown in Given Examples.
1, 3, divisible by five, 7, 9, 11, 13, divisible by five, 17, 19, 21, 23, divisible by five
"""
s=int(input())
c=0
for i in range(1,s+1):
        if i%2==1:
            if i%5==0:
                print("Divisible by five")
            else:
                print(i,end=" ")
