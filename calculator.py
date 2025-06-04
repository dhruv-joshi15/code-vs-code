class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y


if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    print("Current features: Addition, Subtraction, Multiplication")
    print("Example: 5 + 3 =", calc.add(5, 3))
    print("Example: 5 - 3 =", calc.subtract(5, 3))
    print("Example: 5 * 3 =", calc.multiply(5, 3))
