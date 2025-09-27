class Dog:

    def __init__(self, name):
        self.name = name 

    def speak(self):
        print(f"The dog {self.name} says Woof!")

fido = Dog("fido")
print(fido.speak())