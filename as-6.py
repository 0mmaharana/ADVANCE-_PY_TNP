#6.Display simple interest and compound interest.
P = float(input('Enter principle amount: '))
T = float(input('Enter time: '))
R = float(input('Enter rate: '))
SI = (P*T*R)/100
CI = P * ( (1+R/100)**T - 1)
print("simple interest :",SI)
print("compound interest :",CI)
