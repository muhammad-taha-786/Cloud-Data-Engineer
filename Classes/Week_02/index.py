# name = 'Muhammad Taha'
# age = 20
# weight = 55.69
# print("My Name is : ", name)
# print("My Age : ", age)
# print("My Weight : ", weight)

# print(type(name))
# print(type(age))
# print(type(weight))

# isPresent = True
# a = None
# print(type(isPresent))
# print(type(a))

# num1 = 10
# num2 = 10
# sum = num1 + num2

# # print(sum)

# fullName = input("Enter Your Name : ")
# print(fullName)


# age = int(input('Enter Your Age'))
# print(age)

# price = float(input("Your Price : "))
# print(price)

# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age : "))

# print("Your Name is : ", name, "And Your Age is : ", age)

# Conditional Statement 

# light = input("Light : ") 
# if(light == "red") : 
#     print("Stop")
# elif(light == "Yellow") :
#     print("Look")
# elif(light == "Green") : 
#     print("GO") 
# else : print("Light is broken ")

# mark = int(input("Enter Your Marks"))

# if(mark >= 90) : 
#     print("A+")
# elif(mark>= 50) : 
#     print("B") 
# elif(mark >= 30) :
#     print("F")
# else : print("Please Correct Enter Your Marks")

# A = int(input("A : "))
# G = input("M/F : ")

# if ((A == 1 or A == 2) and G == "M") :
#     print("Fess is 100")
# elif(A == 3 or A == 4 or G == "F"):
#     print("Fess is 200")
# elif(A == 5 or G == "M") : 
#     print("Fess is 300")
# else : print("NO Fess")


# Ternary Operators 
# food = input("Food : ")
# eat = "Yes" if food == "cake" else "No"
# print(eat)

# food = input("Enter Your Food ")
# print("Sweets") if food == "cake" or food == "candies" else print("Not Sweets") 

# age = int(input("Enter Your Age : "))
# vote = ("Yes you are eligible for vote", "No you are not eligible for vote") [age < 19]
# print(vote)


# Types of Operators 

# Arthmatic Operators 

# a = 2
# b = 10

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b) #Reminder 
# print(a ** b) #a^b 

# Relational Operators 

# a = 10
# b = 30 

# print(a == b)
# print(a != b)
# print(a >= b)
# print(a > b)
# print(a <= b)
# print(a < b)

# Assignment Operators 

# num = 10
# # num = num + 10
# num += 10
# num -= 10
# num *= 10
# # num /= 10
# # num %= 10
# # num **= 10
# print(num)

# Logical Operators 
# Not
# a = 50
# b = 30 
# print( not False)
# print(not (a > b))
# print( not True)

# And OR
# val1 = True
# val2 = False
# print("The AND Operator is : ", val1 and val2)
# print("The OR Operator is : ", val1 or val2)

# Type Conversion 
# a = int("2")
# b = 4.25

# print(a + b)

# Practice Questoin 
# Q -1
# print("Enter any Two: ")
# a = int(input("First Number : "))
# b = int(input("Second Number : "))
# c = a+b 
# print("Your Number Is : ", c)

# Q - 2
# side = float(input("Enter Square Side : "))
# print("Ares Is : ", side * side)

# Q - 3
# a = float(input("Enter First Number : "))
# b = float(input("Enter Second Number : "))
# print("Your Average Number Is : ", (a + b) /2)

# String Functions 
# str = "Hello World"
# print(str.endswith("world"))

# str = "hello World"
# print(str.capitalize())

# str = "Hello World"
# print(str.replace("Hello", "Taha"))

str = "Hello World"
print(str.find("l"))