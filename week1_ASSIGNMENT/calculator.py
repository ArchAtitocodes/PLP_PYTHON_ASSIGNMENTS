# Enhanced Basic Calculator Program

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /, %, **, //): ")

# Perform the calculation based on the operation
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
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Error: Cannot perform modulus by zero.")
elif operation == '**':
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
elif operation == '//':
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    else:
        print("Error: Cannot perform floor division by zero.")
else:
    print("Invalid operation. Please choose from +, -, *, /, %, **, //.")
