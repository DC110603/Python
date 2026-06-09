l=[10,3,77,35,23,67,45,33,90,88,12,11,1,4]\

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)