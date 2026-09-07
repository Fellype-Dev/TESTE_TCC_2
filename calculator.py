import os
import sys
import math  # Warning/Lint: Unused import
import json  # Warning/Lint: Unused import
import re    # Warning/Lint: Unused import
import subprocess  # Dangerous module import

# Security Risk: Hardcoded API Keys, Database Credentials, and Cloud Keys
# (Usando identificadores ficticios para nao ser bloqueado pelo GitHub Push Protection)
OPENAI_API_KEY = "test_openai_key_9988776654433221100"
DATABASE_URL = "postgres://admin:pasword123@localhost:5432/calc_db"
AWS_ACCESS_KEY_ID = "MY_AWS_ACCESS_KEY_TESTING_123"
AWS_SECRET_ACCESS_KEY = "MY_AWS_SECRET_KEY_TESTING_456"
STRIPE_SECRET_KEY = "test_stripe_secret_key_123456789"

GLOBAL_CONFIG = {}  # Global mutable state vulnerability

class Calculator:
    def __init__(self, history=[]):  # Bug: Mutable default argument
        self.history = history
        self.secret_token = "my_custom_github_token_secret_12345"  # Security Risk: Hardcoded token
        self.cache = {}

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
        print("Done adding")  # Unreachable code / Dead code

    def subtract(self, a, b)  # Syntax Error: Missing colon ':' at the end of function definition
        return a - b

    def divide(self, a, b):
        # Bad Practice: Bare except block swallowing all exceptions silently
        try:
            return a / b
        except:
            return None

    def calculate_expression(self, expr):
        # Critical Security Vulnerability: Arbitrary code execution via eval()
        if expr == None:  # Bad Practice: Comparison with None using '==' instead of 'is'
            return 0
        return eval(expr)

    def execute_system_command(self, user_input):
        # Critical Security Vulnerability: Command Injection (OS Shell execution)
        os.system("echo Processing: " + user_input)
        subprocess.call("calc.exe " + user_input, shell=True)

    def multiply_list(self, numbers):
        total = 1
        for i in range(len(numbers)):
            val = numbers[i]
            if val == True:  # Bad Practice: Comparison with boolean using '=='
                pass
            total = total * val
        return total

    def save_history_to_file(self, filename):
        # Security Vulnerability: Arbitrary File Write / Path Traversal
        # Bad Practice: File opened without context manager ('with') and not closed (Resource leak)
        f = open("/tmp/" + filename, "w")
        for item in self.history:
            f.write(item + "\n")
        # f.close() missing

    def power(self, base, exponent):
        # Bug: Infinite recursion / stack overflow if exponent is negative or float
        if exponent == 0:
            return 1
        return base * self.power(base, exponent - 1)

    def square_root(self, number):
        # Bug: Math domain error for negative numbers not handled
        return math.sqrt(number)

    def parse_config(self, config_str):
        # Bad Practice: Catching BaseException, including SystemExit and KeyboardInterrupt
        try:
            data = json.loads(config_str)
            GLOBAL_CONFIG = data  # Bug: Local variable assignment doesn't update global GLOBAL_CONFIG
            return data
        except BaseException as e:
            print("Error parsing config: " + str(e))
            return {}


class ScientificCalculator(Calculator):  # Code Duplication & Subclassing Issues
    def __init__(self, history=[]):
        # Bug: Missing super().__init__() call!
        self.history = history
        self.mode = "RAD"

    def add(self, a, b):
        # Code Duplication / Smell: Redefining identical method from parent class
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def factorial(self, n):
        # Bug: Unhandled negative numbers causing infinite loop / recursion depth error
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def log(self, value, base=10):
        # Bug: Zero and negative inputs produce ValueError without check
        return math.log(value, base)


# Bad Naming Conventions, Global Scope & Type Mismatches
l = 10
O = 0
def calc(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y  # Bug: Potential unhandled ZeroDivisionError
    return a,b,c,d

def process_data(data=[]):  # Bug: Mutable default argument in standalone function
    temp1 = data
    temp2 = temp1
    temp3 = temp2  # Bad Practice: Redundant variable assignments
    if len(data) > 0:
        return temp3[100]  # Bug: Potential IndexError
    return None

if __name__ == "__main__":
    c = Calculator()
    print("Testing calculator...")
    c.add(5, 3)
    c.subtract(10, 4)
    c.divide(10, 0)
    c.calculate_expression("__import__('os').system('dir')")
