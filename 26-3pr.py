x=20
y=1.23
z=True
s="om"
def fun(x,y,z,s):
    x=30
    y=3.45
    z=False
    s="nom"
    print("The data inside function:")
    print(x,y,z,s)
fun(x,y,z,s)
print("The data outside function:")
print(x,y,z,s)
