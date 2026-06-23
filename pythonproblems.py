# Python Basic Practice Problems

print("===== Python Basic Practice Problems =====")

# 1. Addition of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)

# 2. Even or Odd Check
number = int(input("\nEnter a number to check Even/Odd: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

# 3. Find Largest of Three Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)
print("Largest number is:", largest)

# 4. Multiplication Table
n = int(input("\nEnter a number for multiplication table: "))

print(f"\nMultiplication Table of {n}")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 5. Factorial of a Number
fact_num = int(input("\nEnter a number to find factorial: "))

factorial = 1
for i in range(1, fact_num + 1):
    factorial *= i

print("Factorial =", factorial)

print("\n===== Program Completed Successfully =====")