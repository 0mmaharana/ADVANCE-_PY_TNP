#generatin of triangle with stars
n=int(input("how many rows to print?"))
i,j=0,0
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*",end=" ")
