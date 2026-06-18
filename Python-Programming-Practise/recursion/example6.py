"""WAP to print sum of digits in a given number
"""

def sumOfDigits(s):
    sum=0
    if s<=0:
        return 0
    sum+=(s%10)
    return sum+sumOfDigits(s//10)
print(sumOfDigits(999))