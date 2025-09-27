class Person:

    def __init__(self, name , country="Unknown"):
        self.name = name
        self.country = country

p1 = Person("Taha", "Pakistan")
p2 = Person("Arslan", "USA")
p3 = Person("Saim")

print(p1.name, p1.country)
print(p2.name, p2.country)
print(p3.name, p3.country)

