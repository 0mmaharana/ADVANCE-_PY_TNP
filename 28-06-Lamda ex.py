l=lambda a: a+10
print(l(5))
#here x is a class function type
#a is the argument value
#a+10 is the expression 
#ex2:
a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
result=lambda a,b:a**b
print(result(a,b))
#ex3:
x=lambda l,m,n:l+m+n
p,q,r=[int(y)for y in input("enter 3 no.s : ").split()]
print(x(p,q,r))
#ex4
pow=lambda num: num**3
list1=[int(i) for i in input ("Enter 10 no.: ").split()]
z=map(pow,list1)
print(list(z))
#ex5
list2=[int(i) for i in input ("Enter 10 no.: ").split()]
z=map(lambda num: num**3,list2)
print(list(z))