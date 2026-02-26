#ex1 finding factorial using recursion
def fact(p):
    if p==1:
        return 1
    else:
        return(p*fact(p-1))
num=int(input("Enter a num:"))
print("Factorial value is ",fact(num))

#ex2 sum of natural no.s using recursion
def natural_num(n):
    if (n== 1):
        return 1
    else:
        return(n + natural_num(n - 1))
n=int(input("Enter a +ve num:"))
print("Sum of natural no.s is ",natural_num(n))

#Ex3:  Fibonaci series
def fibo(a,b,f):
    if (f>0):
        c=a+b
        print(c)
        fibo(b,c,f-1)
x=-1
y=1
f=int(input("enter a no."))
fibo(x,y,f)

#Write a program to test a num is prime or not using recursive function