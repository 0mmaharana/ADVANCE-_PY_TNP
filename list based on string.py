#ex1
#creating a list based on characters of agiven string
mystring="Hello world"
mylist=[x for x in mystring]
print(mylist)

#ex2
#create a list having elements from 1 to n, where n is given as input
n=int(input("Enter a no.")) 
mylist=[x for x in range(1,n+1)]
print(mylist)
