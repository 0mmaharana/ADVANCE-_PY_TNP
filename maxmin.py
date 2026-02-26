def findmaxmin(list1):
    large=max(list1)
    small=min(list1)
    return(large,small)
list1=[int(x) for x in input("Enter 10 no.s:").split()]
x,y=findmaxmin(list1)
print("largest=",x,"smallest",y)