""""write a program to perform all these tasks
a.     Store a number in a variable
b.    If value is not in range (100-1000) prints WRONG NUMBER else follows the steps
c.     Check even or odd
d.    If even divide the number by 3 and print the remainder
e.     If odd divide the number by 2 and print the remainder."""

n=int(input("Enter a Number: "))
if 100 < n <1000:
    if n%2==0:
        res=n/3
        res=round(res,2)
        print(res)
    else:
        res = n / 2
        res = round(res, 2)
        print(res)
else:
    print("Number Not in Range")