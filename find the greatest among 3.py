#find the greatest among 3
x = int(input("enter 1st number:"))
y = int(input("enter 2nd number:"))
z = int(input("enter 3rd number:"))
if(x>y and x>z):
    print("%d is big"%x)
    print("1st phase")
elif(y>z):
    print("%d is big"%y)
    print("2nd phase")
else:
    print("%d is big"%z)
    print("last phase")