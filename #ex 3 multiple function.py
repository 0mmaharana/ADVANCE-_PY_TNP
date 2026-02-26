#ex 3 multiple function
def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
x=float(input("Enter 1st no.: "))
y=float(input("Enter 2nd no.: "))
tup=cal(x,y)
print(type(tup))
print("Results are",tup)
