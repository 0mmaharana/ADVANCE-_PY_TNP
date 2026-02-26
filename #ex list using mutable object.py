#ex list using mutable object
def update(list1):
    list1.append(22)
    list1.append(33)
    print("inside",list1)

list1=[10,20,30,40]    
print("\ninitally list contains",list1)
update(list1)
print("outside the function",list1)
#ex2 sum,sub using function
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
a=float(input("Enter 1st no.: "))
b=float(input("Enter 2nd no.: "))
x,y=sum_sub(a,b)
print("sum=",x)
print("sub=",y)
#ex 3 multiple function
def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
#a=float(input("Enter 1st no.: "))
#b=float(input("Enter 2nd no.: "))
tup()
x,y=sum_sub(a,b)
print("sum=",x)
print("sub=",y)
