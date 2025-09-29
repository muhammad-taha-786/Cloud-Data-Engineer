#Reading a file

# with open("myfile.txt", "r") as f:
#     print(f.read())


# Writting a file

# with open("write.txt", "w") as f:
#     print(f.write("Hello, My name is John "))
#     f.write("I am a software developer")

#Append a file

with open("append.txt", "a") as f:
    print(f.write("Hello, My name is Syed Taha "))
    f.write("I am a software developer")
    f.write("\nI love coding")