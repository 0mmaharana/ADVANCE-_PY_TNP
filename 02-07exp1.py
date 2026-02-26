# #OOP program
# class emp:
#     empid=2
#     empname="om"
#     def display(self):
#         print(self.empid,self.empname)
# obj=emp()
# obj.display()
# obj1=emp()
# obj1.empid=2
# obj1.empname="Abhi"
# obj1.display()
#OOP program2
class lib:
    bookid=1
    bookname="ok"
    bookauthor="om"
    bookcoast=500.69
    bookqty=5
    def accept(self):
        self.bookid=int(input("Enter the book id "))
        self.bookname=input("Enter the book name ")
        self.bookauthor=input("Enter the book Author ")
        self.bookcoast=float(input("Enter the book coast "))
        self.bookqty=int(input("Enter the book Quantity "))
    def display(self):
            print("Information about book: ")
            print(self.bookid,self.bookname,self.bookauthor, self.bookcoast,self.bookqty)
obj3=lib()
obj3.accept()
obj3.display()