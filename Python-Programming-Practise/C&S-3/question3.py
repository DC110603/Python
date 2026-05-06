""""Write a program to print following pattern
if input is 10 and -5
output will be 10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6
 """
s=int(input())
e=int(input())
c=0
if s<e:
    for i in range(s,e+1):
        c+=1
        if c>1:
            print(",",end="")
        print(f"{i}@{i+1}",end="")
else:
    for i in range(s,e-1,-1):
        c += 1
        if c > 1:
            print(",", end="")
        print(f"{i}@{i - 1}", end="")
