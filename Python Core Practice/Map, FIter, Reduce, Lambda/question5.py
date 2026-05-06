"""5.  Use map() on a string to convert each character into its ASCII value
(using ord()). Print the result list."""

li=[65,66,67,68,69,70,71]
li2=list(map(lambda x: chr(x),li))
print(li2)


lis=["A","B","C","D","E"]
lis2=list(map(lambda x: ord(x),lis))
print(lis2)