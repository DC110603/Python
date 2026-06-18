"""Even numbers between range"""

def nums(s,e):
    if s>e:
        return
    if s%2==0:
        print(s)
    nums(s+1,e)

s=int(input("Enter starting range: "))
e=int(input("Enter ending range: "))
nums(s,e)