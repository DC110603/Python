l = [1, 2, 3, 4, 7, 8, 10, 13, 15, 18, 19, 33, 42, 36, 37]
key=int(input())
for i in l:
    if i == key:
        print(f"{i} found at {l.index(i)}")
        break
else:
    print("Element not Present")