n=int(input())
squareofN = n**2
t=squareofN
su=0
while t>0:
    r=t%10
    su+=r
    t//=10
if su == n:
    print("NEON NUMBER")