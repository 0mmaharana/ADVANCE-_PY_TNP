#ex2 of if statement with multiple inputs
p=int(input("Enter the mark of 1st subject"))
q=int(input("Enter the mark of 2nd subject"))
r=int(input("Enter the mark of 3rd subject"))
if(p>q) and (p>r):
    print("%d is big"%p)
else:
    print("%d is not big"%p)

#ex2 of if statement with input and list comprehension
x,y,z=[int(s) for s in input("enter 3 nos").split()]
if(x>y) and (x>z):
    print("%d is big"%x)
else:
    print("%d is not big"%x)    

#ex2 if statement with multiple inputs
a,b,c=input("enter 3 nos").split(sep=' ')
a=int(a)
b=int(b)
c=int(c)
if(a>b and a>c):
    print("%d is big"%a)
else:
    print("%d is not big"%a)    

    