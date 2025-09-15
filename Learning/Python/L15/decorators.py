def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello, I am Taha")

def add(a, b):
    print(a + b)

add(5, 7)
hello()