# a = int(input("Enter any Number"))
# print(f"Multiplication table of {a}")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as e :
#     print(e)

# print("Some important line of code")
# print("End of program")


try:
    num = int(input("Enter an integer"))
    a = [3,6]
    print(a[num])
except ValueError:
    print("number is not a integer")
except IndexError:
    print("Index Error")