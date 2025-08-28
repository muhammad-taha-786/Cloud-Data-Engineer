# Q1. Print numbers 1 to 10 (for loop)
for i in range(1, 11):
    print(i, end=" ")

# Q2. Print numbers 20 to 1 (while loop)
i = 20
while i >= 1:
    print(i, end=" ")
    i -= 1

# Q3. Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")

# Q4. Print numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i, end=" ")

# Q5. Print odd numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i % 2 != 0:
        print(i, end=" ")

# Q6. Print "Happy Birthday!" five times
for i in range(5):
    print("Happy Birthday!")

# Q7. Series of squares
n = int(input("Enter a number: "))
print("The first", n, "terms of the series are:")
for i in range(1, n+1):
    print(i*i, end=" ")

# Q8. Multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Q9. Arithmetic progression (AP)
a = 3
d = 4
for i in range(8):
    print(a + i*d, end=" ")

# Q10. Geometric progression (GP)
a = 2
r = 3
for i in range(6):
    print(a * (r**i), end=" ")

# Q11. Sum of 1 to n
n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum from 1 to", n, "is:", total)


# Q12. Sum of reciprocals
n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n+1):
    total += 1/i
print(f"The sum of reciprocals from 1 to {n} is: {total:.2f}")

# Q13. Running total (5 numbers)
total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    total += num
print("The final running total is:", total)

# Q14. Factorial
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial of", n, "is", fact)


# Q15. Power calculation (no ** or math.pow)
base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1

if exp > 0:
    for i in range(exp):
        result *= base
elif exp < 0:
    for i in range(-exp):
        result *= base
    result = 1 / result

print(f"{base} ^ {exp} = {result}")
