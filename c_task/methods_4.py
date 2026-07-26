class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @classmethod
    def description(cls):
        return f"Это калькулятор"


print(Calculator.add(1, 2))
print(Calculator.multiply(4, 5))
print(Calculator.description())
