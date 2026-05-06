"""Write a Program to print all the Subarray of a list"""
l=list(map(int,input().split()))
k=int(input())
for i in range(0,len(l)-k+1):
    for j in range(i,i+k):
        print(l[j],end=" ")
    print()