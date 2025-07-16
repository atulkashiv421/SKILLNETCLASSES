# Arithmetic operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator(a, b, operator):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)
    elif operator == '*':
        return multiply(a, b)
    elif operator == '/':
        return divide(a, b)
    else:
        return "Error: Invalid operator"

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    result = calculator(num1, num2, operator)
    print("Result:", result)
