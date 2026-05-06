def fact_of_num(n):
    if n==0:
        return 1
    smalloutput = fact_of_num(n-1)
    output = smalloutput * n
    return output
n=int(input())
print(fact_of_num(n))