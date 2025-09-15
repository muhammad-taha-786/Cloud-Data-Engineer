# class Car():
#     def __init__(self,name,model,color):
#         self.name = name
#         self.model = model
#         self.color = color  

#     def start(self):
#         print(f"My Car Name is {self.name} and Model is {self.model} and Color is {self.color}   ")
        
#     def stop(self):
#         print("car stopped")

# my_car = Car("Civic", 2024, "White")

# print(my_car.name)
# print(my_car.model)
# print(my_car.color)
# my_car.start()
# my_car.stop()


# class Property():
#     def __init__(self, location, acres, price, property_type):
#         self.location = location
#         self.acres = acres
#         self.price = price
#         self.property_type = property_type

#     def display_info(self):
#         print(f"Property Type: {self.property_type}")
#         print(f"Location: {self.location}")
#         print(f"Acres: {self.acres}")
#         print(f"Price: ${self.price}")

# my_property = Property("Pakistan Karachi", 5, 5000000, "Residential")

# print(my_property.location)
# print(my_property.acres)
# print(my_property.price)
# print(my_property.property_type)

# my_property.display_info()



class Portal():
    def __init__(self, std_name, std_age, std_class, std_roll_no):
        self.std_name = std_name
        self.std_age = std_age
        self.std_class = std_class
        self.std_roll_no = std_roll_no
        
    def display_info(self):
        print(f"Student Name: {self.std_name}")
        print(f"Student Age: {self.std_age}")
        print(f"Student Class: {self.std_class}")
        print(f"Student Roll No: {self.std_roll_no}")

my_student = Portal("Ali", 16, "10th Grade", 23)
# print(my_student.std_name)
# print(my_student.std_age)
# print(my_student.std_class)
# print(my_student.std_roll_no)
my_student.display_info()