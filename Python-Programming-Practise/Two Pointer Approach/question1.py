"""Two Sum (pair with given sum)
"""#
l=list(map(int,input().split()))
target=int(input())
d={}
s=0
for i in range(0,len(l)):
    res=target-l[i]
    if res in d:
        print(d[res],i)
        break
    d[l[i]]= i
