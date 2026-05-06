""""Write a program to find the average of all even numbers in the given range.
if the starting range is Greater than ending range then print """
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
    print(su/c)