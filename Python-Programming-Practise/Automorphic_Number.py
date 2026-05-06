n=int(input())
squareofN=n**2
st=str(squareofN)
if  len(st) == 2 :
    if int(st[1]) == n:
        print("Automorphic number")
elif len(st) == 3:
    if int(st[1]+st[2]) == n:
        print("Automorphic number")
elif len(st) == 4:
    if int(st[2]+st[3]) == n:
        print("Automorphic number")