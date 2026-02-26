class myclass:
    x=25
obj=myclass()
print(obj.x)
#OOP program
class emp:
    empid=2
    empname="om"
    def display(self):
        print(self.empid,self.empname)
obj=emp()
obj.display()
obj1=emp()
obj1.empid=2
obj1.empname="Abhi"
obj1.display()