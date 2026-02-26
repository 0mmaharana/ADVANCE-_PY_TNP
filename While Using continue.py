#Use of continue
#print a series of natural no. except divisible by 3
i=1
while(i<=20):
    i+=1
    if(i%3==0):
        continue
    print(i)
else:
    print("While execution completed")    