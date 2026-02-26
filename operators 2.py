x=40
y=30
r1=x>y
r2=x<y
r3=x==y
print(r1,r2,r3)
print(x>y and x==y)
print(not(x>0))

#ex 1
a=20
b=25
if(a is b):
    print("it is True")
else
    print("it is false")

# ex2
a=int(input("Enter a no.:"))
list1=[2,4,6,8,10]
print(list1)
if(a in list1):
    print("present")
else
    print("not present")

a=int(input("Enter a no.:"))
list1=[1,3,5,7,9]
print(list1)
if(a not in list1):
    print("not exist")
else
    print("exist")

#EXAMPLE 3
n=12
m=14
print("n=")
print(n)
print("m=")
print(m)
print("n&m=")
print(n&m)
print("n|m=")
print(n|m)
print("n^m=")
print(n^m)
print("left shift by 1 bit ")
print(n<<1)
print("right shifted by 2 bits ")
print(n>>2)