num1 = float(input(" enter a number:"))
num2 = float(input(" enter a second number:"))
opr = input("enter an operator (+, -, *, /) choose one:")


if opr == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif opr == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif opr == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif opr == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator chosen.")