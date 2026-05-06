def power_of_num(x,n):
    if n==0:
        return 1
    return x*power_of_num(x,n-1)
x=2
n=5
print(power_of_num(x,n))