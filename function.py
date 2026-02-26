def greet(p):
    print("hello",p)
    return(p)
print(greet("sam"))

#+ve equivalent
def absvalue(num):
    if num>=0:
        return num
    else:
        return(-num)
x=int(input("enter a -ve no.")) 
y=absvalue(x)
print("positive equivalent is",y)

def fun():
    q=100
    print("'x value is ",q)
fun()
print("x value in outside",q)

def show():
    print("Hello boss")
    global r
    print(r)
    r="hii"
