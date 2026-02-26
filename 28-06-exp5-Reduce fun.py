#Reduce fun
from functools import reduce
def fun(x,y):
    return x+y
i=[10,20,30,40,50]
result=reduce(fun,i)
print(result)