"""Search for a number in 2D array."""
l=[[1,2,3],[4,5,6],[7,8,9],[10,11,6]]
target=int(input())
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        if l[i][j]==target:
            print(i,j)
