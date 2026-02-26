class emp:
    def _init_(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print(self.id,self.name)

emp1=emp("vardhan",100)
emp2=emp("hulk",123)
emp1.display()
emp2.display()