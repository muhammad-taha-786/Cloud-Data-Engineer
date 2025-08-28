# Q1. Count vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

# Q2. Count uppercase, lowercase, digits, whitespaces
string = input("Enter a string: ")

upper = lower = digit = space = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Whitespaces:", space)


# Q3. Exchange first and last character
string = input("Enter a string: ")

if len(string) > 1:
    new_string = string[-1] + string[1:-1] + string[0]
else:
    new_string = string

print("New string:", new_string)

# Q4. Reverse a string
string = input("Enter a string: ")
new_string = ""

for ch in string:
    new_string = ch + new_string

print("Reversed string:", new_string)

# Q5. Shift string one position left
string = input("Enter a string: ")

if len(string) > 0:
    new_string = string[1:] + string[0]
else:
    new_string = string

print("Shifted string:", new_string)


# Q6. Print initials without split()
name = input("Enter full name (First Middle Last): ")
initials = ""
initials += name[0].upper() + ". "

for i in range(1, len(name)):
    if name[i-1] == " " and name[i] != " ":
        initials += name[i].upper() + ". "

print("Initials:", initials)

# Q7. Check palindrome (without reverse())

string = input("Enter a string: ")

is_palindrome = True
for i in range(len(string)):
    if string[i] != string[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")


# Q8. Display SHIFT pattern
word = "SHIFT"
for i in range(len(word)):
    print(word[i:] + word[:i])


# Q9. Password validation
password = input("Enter a password: ")

if len(password) >= 8:
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    if has_upper and has_lower and has_digit:
        print("Password is valid.")
    else:
        print("Password must contain uppercase, lowercase, and a digit.")
else:
    print("Password must be at least 8 characters long.")
