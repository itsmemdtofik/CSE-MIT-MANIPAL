def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("This is a simple calculator made in python.")
print("1. Addition-'+'")
print("2. Subtraction-'-'")
print("3. Multiplication-'*'")
print("4. Division-'/'")
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
choice = input("Enter the operator to do the desired computation: ")
if choice =="1":
    print(f'{num1} + {num2} = {add(num1, num2)}')
if choice == "2":
    print(f'{num1} - {num2} = {subtract(num1, num2)}')
if choice == "3":
    print(f'{num1} * {num2} = {multiply(num1, num2)}')
if choice == "4":
    print(f'{num1} * {num2} = {divide(num1, num2)}')
