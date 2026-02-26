#ex1 use of continue
fruits=["apple","banana","cherry","guava","banana","orange"]
for x in fruits:
    if x=="banana":
        continue
    print(x) 

#ex range()
for x in range(6):
    print(x,end=' ')
print()
for x in range(0,6):
    print(x,end=' ')
print()
for x in range(10,30,3):
    print(x,end=' ')    
print()
for x in range(50,0,-5):
    print(x,end=' ')    
