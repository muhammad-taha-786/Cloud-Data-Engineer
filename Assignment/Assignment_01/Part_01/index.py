#Part -1 Python Basics (Variables)

#Q1 : Print Your Name with your Father name and Date of birth using suitable escape sequence charactor

name = "Muhammad Taha"
fname = "Muhammad Imran"
dob = "01-January-2004"

print(name , fname , dob)


#Q2 : Write your small bio using variables and print it using print function

name = "Muhammad Taha"
age = 21
learning = "Cloud Data Engineering"

print("My name is ", name, "My age ", age, "And i'm currently enroll ", learning, "course")

#Q3 : Write a program in which use all the operators we can use in Python

a = 10
b = 5
print("\n----------------Arithmatic Operators-------------------\n")
print("10 + 5 = ", a + b)
print("10 - 5 = ", a + b)
print("10 * 5 = ", a * b)
print("10 / 5 = ", a / b)
print("10 % 5 = ", a % b)
print("10 ** 5 = ", a ** b)
print("10 // 5 = ", a // b)

print("\n----------------Comparison Operators-------------------\n")
print("10 == 5 =", a == b)
print("10 != 5 =", a != b)
print("10 > 5 =", a > b)
print("10 < 5 =", a < b)
print("10 >= 5 =", a >= b)
print("10 <= 5 =", a <= b)

print("\n----------------Logical Operators-------------------\n")

x = True
y = False

print("X AND Y", x and y)
print("X OR Y", x or y)
print("X NOT", not x )



#Q4 : Completes the following steps of small task:
#Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
#Mention Variable of Total Marks and assign 300 to it
#Calculate Percentage

English = 55
islamiat = 75
math = 89
total_marks = 300
obtained_marks = English + islamiat + math
percentage_marks = (obtained_marks / total_marks) * 100
print(percentage_marks)




