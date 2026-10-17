try:
    # Use try/except to catch non-numeric inputs (e.g., if a user types a letter)
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
except ValueError:
    print("error: invalid numeric input. Please enter numbers only.")
    exit() # Exits the script early if the input is bad

op = input("enter the operation (+, -, *, /): ")

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b,):
    return a*b

def divide(a, b):
    # Use try/except to catch division by zero natively
    try:
        return a/b
    except ZeroDivisionError:
        return "error: division by zero"

if op == "+":
    print("the result is: " + str(add(a, b)))
elif op == "-":
    print("the result is: " + str(subtract(a, b)))
elif op == "*":
    print("the result is: " + str(multiply(a, b)))
elif op == "/":
    print(" the result is: " + str(divide(a, b)))
else:
    print("invalid operation")

def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "invalid operation"
