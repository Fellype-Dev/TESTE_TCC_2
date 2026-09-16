


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
