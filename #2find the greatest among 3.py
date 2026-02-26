# 2finding greatest no.
a=float(input("Enter 1st no."))
b=float(input("Enter 2nd no."))
c=float(input("Enter 3rd no."))

#(Or) a,b,c=[int(x) for x in input("Enter 3 no.s:").split()]
print(a) if(a>b and a>c) else print(b) if(b>c) else print(c)