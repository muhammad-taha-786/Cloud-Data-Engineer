import calendar


# Q1. Print alternate elements of a list
lst = input("Enter list elements separated by space: ").split()

print("Alternate elements:")
for i in range(0, len(lst), 2):
    print(lst[i])

# Q2. Reverse a list without reverse()
lst = input("Enter list elements separated by space: ").split()
rev_list = []

for i in range(len(lst)-1, -1, -1):
    rev_list.append(lst[i])

print("Reversed list:", rev_list)

# Q3. Find largest number without max()
lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print("Largest number:", largest)


# Q4. Rotate list elements
lst = input("Enter list elements separated by space: ").split()
rotated = lst[-1:] + lst[:-1]

print("Rotated list:", rotated)


# Q5. Delete a word from a string
string = input("Enter a string: ")
word = input("Enter word to delete: ")

new_string = string.replace(word, "")

print("Updated string:", new_string)


# Q6. Convert mm/dd/yyyy to Month Day, Year
date = input("Enter date (mm/dd/yyyy): ")
month, day, year = date.split("/")

month_name = calendar.month_name[int(month)]
print(f"{month_name} {int(day)}, {year}")


# Q7. Capitalize each word
def capitalize_words(sentence):
    result = ""
    capitalize_next = True
    
    for ch in sentence:
        if capitalize_next and ch.isalpha():
            result += ch.upper()
            capitalize_next = False
        else:
            result += ch.lower()
        if ch == " ":
            capitalize_next = True
    return result

sentence = input("Enter a sentence: ")
print("Capitalized:", capitalize_words(sentence))

# Q8. Sum of each row in a matrix
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []
for i in range(m):
    row = [int(x) for x in input(f"Enter row {i+1} elements: ").split()]
    matrix.append(row)

for i in range(m):
    print(f"Sum of row {i+1} =", sum(matrix[i]))


# Q9. Add two matrices
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter first matrix:")
matrix1 = [[int(x) for x in input().split()] for _ in range(m)]

print("Enter second matrix:")
matrix2 = [[int(x) for x in input().split()] for _ in range(m)]

result = [[0]*n for _ in range(m)]

for i in range(m):
    for j in range(n):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Sum of matrices:")
for row in result:
    print(row)


# Q10. Multiply two matrices

m = int(input("Enter number of rows of first matrix: "))
n = int(input("Enter number of columns of first matrix: "))
p = int(input("Enter number of columns of second matrix: "))

print("Enter first matrix:")
matrix1 = [[int(x) for x in input().split()] for _ in range(m)]

print("Enter second matrix:")
matrix2 = [[int(x) for x in input().split()] for _ in range(n)]

result = [[0]*p for _ in range(m)]

for i in range(m):
    for j in range(p):
        for k in range(n):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Product of matrices:")
for row in result:
    print(row)
