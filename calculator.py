def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Main Program
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation: +, -, *, /")
operator = input("Enter operator: ")

if operator == '+':
    print("Result:", add(num1, num2))
elif operator == '-':
    print("Result:", subtract(num1, num2))
elif operator == '*':
    print("Result:", multiply(num1, num2))
elif operator == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operator")
