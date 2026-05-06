n=int(input())
if n>=100 and n<1000:
    l=""
    for i in range(1,4):
        su=n*i
        l=l+str(su)
    if "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" in l:
        print("Fascinating Number")
    else:
        print("Not a Fascinating Number")
else:
    print("Not in range")

