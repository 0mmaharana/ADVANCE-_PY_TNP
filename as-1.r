#1.Write a program to input your marks for three subjects then find sum and percentage.
math = int(input("Enter marks for math: "))
science = int(input("Enter marks for science: "))
social = int(input("Enter marks for social: "))
english = int(input("Enter marks for english: "))
hindi = int(input("Enter marks for hindi: "))
odia = int(input("Enter marks for odia: "))
total_marks = math + science + social + english + hindi + odia
percentage = (total_marks / 600) * 100
print("Total marks :",total_marks)
print("percentage :",percentage)