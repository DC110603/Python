l=[[10],[20,30],[40],[50],[60,70,80,90]]
# To access every list we can linearly search
# for i in l:
    # print(i)

# we can perform indexing
# print(l[4][3])

l1=[[10,20,30,40,50,60,70,80,90],
    [90,80,7060,50,40,30,20,10,120],
    [40,30,20,10,60,70,50,90,100],
    [50,30,20,10,60,70,50,90,100]]
# to access every element in the list
for i in range(0,len(l1)):
    for j in range(len(l1[i])):
        print(l1[i][j],end=" ")
    print()

for i in range(0,len(l)):
    print(l[i])



