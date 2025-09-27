# class MathHelper:

#     @staticmethod
#     def add(a, b):
#         return a + b

#     @classmethod
#     def description(cls):
#         return f"{cls.__name__} help with math operations"
    
# print(MathHelper.add(5,5))
# print(MathHelper.description())


#ANOTHER EXAMPLE
class MathHelper:

    @staticmethod
    def add(a,b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    @classmethod
    def description(cls):
        return f"{cls.__name__} helps with math operations"
    
print(MathHelper.add(5,5))
print(MathHelper.multiply(MathHelper(), 5, 5))
print(MathHelper.description())