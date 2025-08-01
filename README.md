# calculator_assignment
Python Week 1 Assignment. 
Simple Calculator Program
Welcome message
print("Welcome to your first Python calculator program!")
print("This program will perform basic operations on two numbers.")

Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

Perform the calculation
result = 0
if operation == '+':
result = num1 + num2
print(f"{num1} + {num2} = {result}")
elif operation == '-':
result = num1 - num2
print(f"{num1} - {num2} = {result}")
elif operation == '*':
result = num1 * num2
print(f"{num1} * {num2} = {result}")
elif operation == '/':
if num2 != 0: # Check for division by zero
result = num1 / num2
print(f"{num1} / {num2} = {result}")
else:
print("Error: Cannot divide by zero!")
else:
print("Invalid operation! Please enter +, -, *, or /.")

End of program
print("Thank you for using the calculator!")
