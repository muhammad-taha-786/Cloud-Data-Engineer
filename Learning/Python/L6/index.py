# Match Case Statements in Python

x = int(input("Enter any number: "))

match x:
    case 0:
        print("X is Zero")
    case 1:
        print("X is one")
    case 2:
        print("X is Two")
    case 3:
        print("X is Three")
    case _:
        print(x)
