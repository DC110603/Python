from functools import reduce

li=[5,10,36,2,85,65,45,20,15]
li2=list(map(lambda x: (x*x)-x,li))
print(li2)
li3=list(filter(lambda x: x if x>=0 and x<=255 else 0,li))
print(li3)
li4=reduce(lambda x,y:x+y,li3)
print(li4)
total=reduce(lambda x,y: x+y,list(filter(lambda x: x if x>=0 and x<=255 else 0,list(map(lambda x: (x*x)-x,li)))))
print(total)