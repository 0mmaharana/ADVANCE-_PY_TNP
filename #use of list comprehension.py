# #use of list comprehension
# #exl: taking two input at a time
# x,y=[int(q) for q in input("Enter two value: ").split()]
# print("1st Number is: {} and 2nd number is {}".format(x,y)) 
# print(" 1st number is ",x," and 2nd number is ",y)

#ex2: taking three input at a time
x, y, z =[int(x) for x in input("Enter three value: ") .split()]
print("x= {}, y= {}, z= {}".format(x,y,z)) 
print("x=",x,"y=",y,"z=",z)