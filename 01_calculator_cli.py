def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    return a / b


def get_number(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print("That's not a number. Try again.")


def get_operation():
    print("\nOperations:")
    print("  +  add")
    print("  -  subtract")
    print("  *  multiply")
    print("  /  divide")
    op = input("Enter operation (+, -, *, /): ").strip()
    return op


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
        print("Unknown operation")
        return None


def main():
    print("=== Simple Calculator ===")
    while True:
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        op = get_operation()
        result = calculate(a, b, op)
        if result is not None:
            print(f"Result: {result}")

        again = input("Calculate again? (y/n): ").lower().strip()
        if again != "y":
            break

    print("Bye!")


if __name__ == "__main__":
    main()
