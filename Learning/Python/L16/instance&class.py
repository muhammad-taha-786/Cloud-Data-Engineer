class Cat:

    spices = "Felis catus"  #class variable

    def __init__(self, name):
        self.name = name #instance variable

c1 = Cat("Milo")
c2 = Cat("Luna")

print(c1.name, c1.spices)
print(c2.name, c2.spices)
