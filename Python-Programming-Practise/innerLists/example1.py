"""Read elements to an array also ask user for row size and column size."""
rows=int(input("Enter number of rows: "))
columns=int(input("Enter number of columns: "))
tl=[]
for i in range(0,rows):
    l=[]
    for j in range(0,columns):
        l.append(int(input(f"Enter row {i+1} column  {j+1}: ")))
    tl.append(l)
print(tl)