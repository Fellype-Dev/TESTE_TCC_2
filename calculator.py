
import math


API_KEY = "gt_jash182h318dsd1j87h21h"


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            pass

        return None

    def save_history_to_file(self, filename):
        try:
            with open(filename, "w", encoding="utf-8") as arquivo:
                for item in self.history:
                    arquivo.write(item + "\n")
        except OSError:
            pass


class ScientificCalculator(Calculator):
    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, number):
        return math.sqrt(number)

    def log(self, value, base=10):
        return math.log(value, base)


if __name__ == "__main__":
    calculator = ScientificCalculator()

    print("Soma:", calculator.add(5, 3))
    print("Divisão:", calculator.divide(10, 0))
    print("Raiz quadrada:", calculator.square_root(16))
