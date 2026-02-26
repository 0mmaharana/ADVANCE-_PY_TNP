# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return self.x+other.x , self.y+other.y    
# p1=point(1,2)   
# p1=point(4,3)   
# #ex2
# try:
#     x=int(input("Enter 1st no. "))
#     y=int(input("Enter 2nd no. "))
#     print(x/y)
# except ZeroDivisionError:
#     print("2nd no. is 0")
#ex3
# try:
#     fileptr=("file7.text","r")

# except IOError:
#     print("file not found")
# else:
#     print("file opened")
#     fileptr.close()
#     print("File closed")
# finally:
#     print("It is just final statement")
#     print("----end----")
# #ex4
class myerror(Exception):
    pass
class smallvalue(myerror):
    pass
class largevalue(myerror):
    pass
n=10
try: 
    i=int(input("Enter no. "))
    if(i<n):
            raise smallvalue
    elif(i>n):
            raise largevalue
    else:
            print("Correct entry: 10")

except smallvalue:
       print("Error: It is less than 10")
except largevalue:
       print("Error: It is greater than 10")        
