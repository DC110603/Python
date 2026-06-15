def merge_intervals(l):
    l.sort(key=lambda x: x[0])
    res=[l[0]]
    for i in range(1,len(l)):
        if res[-1][-1] >=l[i][0]:
            if res[-1][-1] < l[i][-1]:
                res[-1][-1]=l[i][-1]
        else:
            res.append(l[i])
    return res


l=[[1,3],[2,6],[8,10],[15,18]]
"""o/p=[[1,6],[8,10],[15,18]]"""

l1=[[2,4],[8,10],[4,6],[2,7]]
"""o/p=[[2,7],[8,10]]"""

print(merge_intervals(l1))