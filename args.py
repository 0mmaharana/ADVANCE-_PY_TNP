#ex1 *args
def myfun(*args):
    print(args)
    print(type(args))

myfun(10)
myfun('a','b','c')
myfun(1,2,3,4,5,6,7)
#ex2
def myshow(*names):
    print(names)
myshow("om","sid","abhi","mannu","AKv")