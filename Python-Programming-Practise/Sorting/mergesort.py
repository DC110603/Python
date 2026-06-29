def merge(l1: list, l2: list):
    res = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    while j < len(l2):
        res.append(l2[j])
        j += 1
    return res


def split_list(l):
    n=len(l)
    if n==1:
        return l
    mid=n//2
    left_list=split_list(l[0:mid])
    right_list=split_list(l[mid::])
    return merge(left_list,right_list)


l=list(map(int,input().split()))
print(split_list(l))