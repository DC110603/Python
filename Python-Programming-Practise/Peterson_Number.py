def facto(n):
    if n == 0:
        return 1
    return n*facto(n-1)

a=input()
if int(a)>100 and int(a)<1000:
    digit1=int(a[0])
    digit2=int(a[1])
    digit3=int(a[2])
    fact1=facto(digit1)
    fact2=facto(digit2)
    fact3=facto(digit3)
    if (fact1+fact2+fact3) == int(a):
        print(f"{a} is a Peterson Number")
    else:
        print("Not a Peterson Number")
else:
    print("You can only give 3 digit number")