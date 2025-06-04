import json

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


def run_tests():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 2) == 3
    assert calc.multiply(3, 4) == 12
    assert calc.divide(10, 2) == 5
    print("All tests passed.")


if __name__ == "__main__":
    calc = Calculator()
    run_tests()

    # CLI interaction
    print("\nWelcome to Calculator!")
    print("Choose operation: add, subtract, multiply, divide")
    op = input("Operation: ").strip().lower()
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if op == "add":
            result = calc.add(x, y)
        elif op == "subtract":
            result = calc.subtract(x, y)
        elif op == "multiply":
            result = calc.multiply(x, y)
        elif op == "divide":
            result = calc.divide(x, y)
        else:
            print("Unknown operation.")
            result = None

        if result is not None:
            print("\nResult:", result)
            print("JSON Response:")
            print(json.dumps({"operation": op, "x": x, "y": y, "result": result}, indent=2))

    except Exception as e:
        print("Error:", e)
