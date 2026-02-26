class person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("hello my name is" + self.name)

p1=person("om",32)
p1.display()