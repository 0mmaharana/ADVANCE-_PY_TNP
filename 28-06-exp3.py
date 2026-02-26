def sqr(num):
    return num**2
list1=[1,2,3,4,5]
for x in map (sqr,list1):
    print(x)
#ex2
def pow(num):
    return num**3
list2=[int (g )for g in input("Enter 10 no.s: ").split()]
for y in map(pow,list2):
    print(y)
z=map(pow,list2)
print(list(z))