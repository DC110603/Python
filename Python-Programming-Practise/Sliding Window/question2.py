"""Write a program to print first negative value in a sublist whose size is k"""
l=list(map(int,input().split()))
k=int(input())
for i in range(0,len(l)-k+1):
    for j in range(i,i+k):
        if l[j]<0:
            print(l[j],end=" ")
            break