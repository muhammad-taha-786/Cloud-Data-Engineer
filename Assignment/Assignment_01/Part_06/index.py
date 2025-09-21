#Q1 - Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math 

class Circle:
    
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius



r = float(input("Enter the radius of the circle: "))  
circle = Circle(r)   

print("Area of circle:", circle.area())
print("Perimeter of circle:", circle.perimeter())



#Q2) Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import datetime  

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")

person = Person(name, country, dob)

print(f"\nName: {person.name}")
print(f"Country: {person.country}")
print(f"Date of Birth: {person.date_of_birth.date()}")
print(f"Age: {person.get_age()} years")


#Q3) Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a / b

calc = Calculator()

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", calc.add(num1, num2))
elif choice == '2':
    print("Result:", calc.subtract(num1, num2))
elif choice == '3':
    print("Result:", calc.multiply(num1, num2))
elif choice == '4':
    print("Result:", calc.divide(num1, num2))
else:
    print("Invalid choice")
