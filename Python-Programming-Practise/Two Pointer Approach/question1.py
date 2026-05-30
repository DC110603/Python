"""Two Sum (pair with given sum)
"""#
def twoSum(l,target):
    d={}
    for i in range(0,len(l)):
        res=target-l[i]
        if res in d:
            return d[res],i
        d[l[i]]= i

print(twoSum([2,2,7,11,15],9))
