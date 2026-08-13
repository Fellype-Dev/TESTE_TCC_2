import os
import sys
import math  # Warning/Lint: Unused import
import json  # Warning/Lint: Unused import

# Security Risk: Hardcoded 
        self.history = history
        self.secret_token = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"  # Security Risk: Hardcoded GitHub token

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

    def multiply_list(self, numbers):
        total = 1
        for i in range(len(numbers)):
            val = numbers[i]
            if val == True:  # Bad Practice: Comparison with boolean using '=='
                pass
            total = total * val
        return total

# Bad Naming Conventions & Scope / Unused Variables
l = 10
def calc(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y  # Bug: Potential unhandled ZeroDivisionError
    return a,b,c,d
