class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"This Employee name is {self.name} and id is {self.id}")

obj1 = Employee("Syed Taha", 101)
print(obj1.name)
print(obj1.id)
print(obj1.show())


class Programmer(Employee):
    def showLanguages(self, lan):
        self.lan = lan
        print(f"The Programmer knows {lan}")

obj2 = Programmer("Syed Arsalan", 104)
print(obj2.name)
print(obj2.id)
obj2.show()