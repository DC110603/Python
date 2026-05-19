"""Count the substrings which are formed by utmost k distinct characters"""
l="entert"
maxs=0
k=3
left=0
right=0
di={}
while right<len(l):
    if l[right] in di:
        di[l[right]]+=1
    else:
        di[l[right]]=1
    while len(di)>k:
        li=l[left]
        di[li]=di.get(li)-1
        if di[li]==0:
            di.pop(li)
        left+=1
    maxs+=right-left+1
    right+=1
print(maxs)

