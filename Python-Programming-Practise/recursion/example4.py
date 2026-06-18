# factors of a given  number

def factorsOfNum(n,i):
    if i==n:
        return
    if n%i==0:
        print(i)
    factorsOfNum(n,i+1)

factorsOfNum(10,1)