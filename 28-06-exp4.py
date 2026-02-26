def myfun(x):
    if (x<18):
        return False
    else:
        return True
ages=[10,7,5,21,22,23]
adults= filter(myfun,ages)
for x in adults:
    print(x)
#ex2 on filter()
def find(x):
    return(len(x)%2==0)
str1=input("Enter a sentence: ")
list1=str1.split()
result=filter(find,list1)
print(list(result))