l = [1, 2, 3, 4, 7, 8, 10, 13, 15, 18, 19, 33, 42, 36, 37]
key = int(input())
s = 0
e = len(l) - 1
c=0
while s <= e:
    mid = (s + e) // 2
    if l[mid] == key:
        print(f"{l[mid]} Found at index {mid}")
        c+=1
        break
    elif key > l[mid]:
        s = mid + 1
    else:
        e = mid - 1
if c==0:
    print("Element Not Present in the List")
