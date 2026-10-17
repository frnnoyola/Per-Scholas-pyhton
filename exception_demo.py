# exception_demo.py

def safe_divide(a, b):
    """Return a / b, or raise a ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Test safe_divide with different values
test_values = [
    (10, 2),
    (20, 4),
    (15, 0),
]

for a, b in test_values:
    try:
        result = safe_divide(a, b)
        print(f"{a} / {b} = {result}")

    except ValueError as error:
        print(f"Error: {error}")

    finally:
        print("Division operation completed")


# Demonstrate catching a generic exception
try:
    value = int("not_a_number")
    print(value)

except Exception as error:
    print(f"A general error occurred: {error}")