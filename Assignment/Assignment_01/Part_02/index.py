#Part -2 Python Basics (Conditional Statements)

#Q1 : A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

salary = float(input("Enter your Salary"))
year = int(input("Enter year "))

if year > 5:
    bonus = salary * 0.5
    print("You are eligible for bonus ")
    print("Your bonus amount", bonus)
    print("Net Salary after bonus", salary + bonus)
else:
    print("Sorry, No bonus ")



#Q2 : Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible

user = int(input("Enter your age"))

if user > 17: 
    print("Yes, You are eligible for voting")
else:
    print("Sorry, you are not eligible ")
    


#Q3 : Write a program to check whether a number entered by user is even or odd.

num = int(input("Enter Number: "))

if num % 2 == 0:
    print(num, " is Even")
else:
    print(num, " is Odd")

# Q4 : Write a program to check whether a number is divisible by 7 or not. Show Answer

num = int(input("Enter Number: "))

if num % 7 == 0:
    print(num, "is divisible by 7")
else:
    print(num, "is not divisible by 7")

# Q5 : Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye"

num = int(input("Enter Number: "))

if num % 5 == 0:
    print(num, "Hello")
else:
    print(num, "Bye4")

# Q6: Write a program to display the last digit of a number.


num = int(input("Enter Number: "))

last_digit = num % 10
print("The last digit is : ", last_digit)


# Q7 : Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length = float(input("Enter Length"))
breadth = float(input("Enter Breadth"))

if length == breadth:
    print("It is Square")
else:
    print("Is is Rectangle")



# Q8 : Take two int values from user and print greatest among them.

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

if num1 > num2: 
    print(num1, "is Greatest")
elif num2 > num1:
    print(num2, "is Greatest ")
else: 
    print("Both number are same")

# Q9 : A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter the Quantity"))
cost_per_unit = 100
total_cost = quantity * cost_per_unit

if total_cost > 1000: 
    discount = total_cost * 0.10
    total_cost -= discount
    print("You got a 10% discount!")

print("Total cost to pay", total_cost)

# Q10 : A school has following rules for grading system:
# a. Below 25 - F b. 25 to 45 - E c. 45 to 50 - D d. 50 to 60 - C e. 60 to 80 - B f. Above 80 - A Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter Your Marks "))

if marks < 25: 
    grade = "F"
elif marks >= 25 and marks < 45:
    grade = "E"
elif marks >= 45 and marks < 50:
    grade = "D"
elif marks >= 50 and marks < 60:
    grade = "C"
elif marks >= 65 and marks < 80:
    grade = "B"
else:
    grade = "A"

print("Your Grade is : ", grade)


# Q11 : A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user Number of classes held Number of classes attended. And print percentage of class attended Is student is allowed to sit in exam or not.

classes_held = int(input("Enter total number of classes held :"))
classes_attended = int(input("Enter number of classes attended :"))

attendance_percentage = (classes_attended / classes_held) * 100
print("Attendence Percentage : ", attendance_percentage, "%")

if attendance_percentage >= 75:
    print("You are allowed to sit in the exam ")
else:
    print("Sorry, you are NOT allowed to sit in the exam")


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
    

# Q13 : Write a program to check if a year is leap year or not. If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year = int(input("Enter a year"))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Q14 : Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR"

age = int(input("Enter your age "))
gender = input("Enter your Gender (M/F)").upper()
material_status = input("Enter your Material Status (Y/N)").upper()

if gender == "F":
    print("You will work in urban areas ")
elif gender == "M":
    if 20 <= age <= 40:
        print("You may work anywhere")
    elif 40 <= age <= 60:
        print("You  will work in urban areas ")
    else:
        print("Error: Invalid age")
else:
    print("Error: Invalid Gender")

# Q15 : Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750

units = int(input("Enter number of units consumed: "))

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + ((units - 300) * 10)

print("Total bill amount is Rs.", bill)

# Q16 : Take input of age of 3 people by user and determine oldest and youngest among them

age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))

if age1 >= age2 and age1 >= age3:
    oldest = age1
elif age2 >= age1 and age2 >= age3:
    oldest = age2
else:
    oldest = age3

if age1 <= age2 and age1 <= age3:
    youngest = age1
elif age2 <= age1 and age2 <= age3:
    youngest = age2
else:
    youngest = age3

print("Oldest age is:", oldest)
print("Youngest age is:", youngest)
