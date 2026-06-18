"""WAP to count even numbers in a given range"""

def countDigits(s,e):
    count=0
    if s > e:
        return 0
    if s % 2 == 0:
        count+=1
        return count+countDigits(s+1,e)

    return count+countDigits(s+1,e)

print(countDigits(1,10))
