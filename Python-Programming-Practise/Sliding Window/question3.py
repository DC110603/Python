"""Write a program to print maximum sum of a subarray whose size is k
ex:- 10 20 30 10 20 30 40 50 60 20 30 10
k=3
op:-[40, 50, 60] 150
"""

l=list(map(int,input().split()))
k=int(input())
"""
max_su=0
max_ar=[]
for i in range(0,len(l)-k+1):
    su=0
    su_ar=[]
    for j in range(i,i+k):
        su+=l[j]
        su_ar.append(l[j])
    if su>max_su:
        max_su=su
        max_ar=su_ar
print(max_ar,max_su)
"""
su=-10**6
max_su=sum(l[0:k])
max_ar=l[0:k]
for i in range(1,len(l)):
    max_su-=l[i-k]
    max_su+=l[i]
    if su>max_su:
        max_su=su
        max_ar=l[i:i+k]
print(max_ar,max_su)
