class myclass:
    def __init__(self):
        a=0
        b=0
        c=0
    def accept(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
    def sum(self):
        self.result=self.a+self.b+self.c
    def display(self):
        print("sum is:",self.result)
obj=myclass()
n1=float(input("Enter 1st no.: "))
n2=float(input("Enter 2nd no.: "))
n3=float(input("Enter 3rd no.: "))
obj.accept(n1,n2,n3)
obj.sum()
obj.display()