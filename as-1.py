#1.Write a program to input your marks for three subjects then find sum and percentage.
sub1 = int(input("Enter marks for sub1: "))
sub2 = int(input("Enter marks for sub2: "))
sub3 = int(input("Enter marks for sub3: "))
total_marks = sub1+sub2+sub3
percentage = (total_marks / 300) * 100
print("Total marks :",total_marks)
print("percentage :",percentage)