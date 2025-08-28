#Part -1 Python Basics (Variables)

#Q1 : Print Your Name with your Father name and Date of birth using suitable escape sequence charactor

# name = "Muhammad Taha"
# fname = "Muhammad Imran"
# dob = "01-January-2004"

# print(name , fname , dob)


#Q2 : Write your small bio using variables and print it using print function

# name = "Muhammad Taha"
# age = 21
# learning = "Cloud Data Engineering"

# print("My name is ", name, "My age ", age, "And i'm currently enroll ", learning, "course")

#Q3 : Write a program in which use all the operators we can use in Python

# a = 10
# b = 5
# print("\n----------------Arithmatic Operators-------------------\n")
# print("10 + 5 = ", a + b)
# print("10 - 5 = ", a + b)
# print("10 * 5 = ", a * b)
# print("10 / 5 = ", a / b)
# print("10 % 5 = ", a % b)
# print("10 ** 5 = ", a ** b)
# print("10 // 5 = ", a // b)

# print("\n----------------Comparison Operators-------------------\n")
# print("10 == 5 =", a == b)
# print("10 != 5 =", a != b)
# print("10 > 5 =", a > b)
# print("10 < 5 =", a < b)
# print("10 >= 5 =", a >= b)
# print("10 <= 5 =", a <= b)

# print("\n----------------Logical Operators-------------------\n")

# x = True
# y = False

# print("X AND Y", x and y)
# print("X OR Y", x or y)
# print("X NOT", not x )



#Q4 : Completes the following steps of small task:
#Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
#Mention Variable of Total Marks and assign 300 to it
#Calculate Percentage

# English = 55
# islamiat = 75
# math = 89
# total_marks = 300
# obtained_marks = English + islamiat + math
# percentage_marks = (obtained_marks / total_marks) * 100
# print(percentage_marks)




#Part -2 Python Basics (Conditional Statements)

#Q1 : A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

# salary = float(input("Enter your Salary"))
# year = int(input("Enter year "))

# if year > 5:
#     bonus = salary * 0.5
#     print("You are eligible for bonus ")
#     print("Your bonus amount", bonus)
#     print("Net Salary after bonus", salary + bonus)
# else:
#     print("Sorry, No bonus ")



#Q2 : Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

# user = int(input("Enter your age"))

# if user > 17: 
#     print("Yes, You are eligible for voting")
# else:
#     print("Sorry, you are not eligible ")
    


#Q3 : Write a program to check whether a number entered by user is even or odd.

# num = int(input("Enter Number: "))

# if num % 2 == 0:
#     print(num, " is Even")
# else:
#     print(num, " is Odd")

# Q4 : Write a program to check whether a number is divisible by 7 or not. Show Answer

# num = int(input("Enter Number: "))

# if num % 7 == 0:
#     print(num, "is divisible by 7")
# else:
#     print(num, "is not divisible by 7")

# Q5 : Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye"

# num = int(input("Enter Number: "))

# if num % 5 == 0:
#     print(num, "Hello")
# else:
#     print(num, "Bye4")

# Q6: Write a program to display the last digit of a number.


# num = int(input("Enter Number: "))

# last_digit = num % 10
# print("The last digit is : ", last_digit)


# Q7 : Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

# length = float(input("Enter Length"))
# breadth = float(input("Enter Breadth"))

# if length == breadth:
#     print("It is Square")
# else:
#     print("Is is Rectangle")



# Q8 : Take two int values from user and print greatest among them.

# num1 = int(input("Enter 1st Number : "))
# num2 = int(input("Enter 2nd Number : "))

# if num1 > num2: 
#     print(num1, "is Greatest")
# elif num2 > num1:
#     print(num2, "is Greatest ")
# else: 
#     print("Both number are same")

    # Q9 : A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

# quantity = int(input("Enter the Quantity"))
# cost_per_unit = 100
# total_cost = quantity * cost_per_unit

# if total_cost > 1000: 
#     discount = total_cost * 0.10
#     total_cost -= discount
#     print("You got a 10% discount!")

# print("Total cost to pay", total_cost)

# Q10 : A school has following rules for grading system:
# a. Below 25 - F b. 25 to 45 - E c. 45 to 50 - D d. 50 to 60 - C e. 60 to 80 - B f. Above 80 - A Ask user to enter marks and print the corresponding grade.

# marks = int(input("Enter Your Marks "))

# if marks < 25: 
#     grade = "F"
# elif marks >= 25 and marks < 45:
#     grade = "E"
# elif marks >= 45 and marks < 50:
#     grade = "D"
# elif marks >= 50 and marks < 60:
#     grade = "C"
# elif marks >= 65 and marks < 80:
#     grade = "B"
# else:
#     grade = "A"

# print("Your Grade is : ", grade)


# Q11 : A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user Number of classes held Number of classes attended. And print percentage of class attended Is student is allowed to sit in exam or not.

# classes_held = int(input("Enter total number of classes held :"))
# classes_attended = int(input("Enter number of classes attended :"))

# attendance_percentage = (classes_attended / classes_held) * 100
# print("Attendence Percentage : ", attendance_percentage, "%")

# if attendance_percentage >= 75:
#     print("You are allowed to sit in the exam ")
# else:
#     print("Sorry, you are NOT allowed to sit in the exam")


# Q12 : Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.


classes_held = int(input("Enter total number of classes held :"))
classes_attended = int(input("Enter number of classes attended :"))

attendance_percentage = (classes_attended / classes_held) * 100
print("Attendence Percentage : ", attendance_percentage, "%")

medical = input("Do you have a medical cause ? (y/n)").lower()

if attendance_percentage >= 75 or medical == 'y':
    print("You are allow to sit in the exam ")
else:
    print("Sorry. you are not allowed to sit int exam")
    