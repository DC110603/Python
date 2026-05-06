"""Write program to print the following series which is shown in Given Examples.
 1, even, 3, even, 5, even, 7, even, 9, even, 11, even, 13, even, 15, even, 17, even, 19,
  even, 21, even, 23, even, 25, even, 27, even, 29, even, 31, even, 33, even, 35, even"""
n=int(input("Enter how many numbers of digits you want : "))
c=0
for i in range(1,n+1):
    c+=1
    if c>1:
        print(",",end=" ")
    if i%2==0:
        print("even",end="")
    else:
        print(i,end="")