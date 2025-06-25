def add(x, y):
    """Add two numbers."""
    return x + y
def subtract(x, y):
    """Subtract two numbers."""
    return x - y
def multiply(x, y):
    """Multiply two numbers."""
    return x * y   
def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def modulus(x, y):
    """Return the modulus of two numbers."""
    return x % y   
def exponent(x, y):
    """Return x raised to the power of y."""
    return x ** y
def floor_divide(x, y):
    """Return the floor division of two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x // y
def absolute(x):
    """Return the absolute value of a number."""
    return abs(x)
def square_root(x):
    """Return the square root of a number."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x ** 0.5
def logarithm(x, base=10):
    """Return the logarithm of x to the specified base."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    import math
    return math.log(x, base)


def get_input():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /, %, **, //, abs, sqrt, log): ").strip().lower()
        return num1, num2, operation
    except ValueError:
        print("Invalid input. Please enter numeric values.") 
        return None, None, None
    
    
    
def calculate(num1, num2, operation):
        if operation == '+':
            return add(num1, num2)
        elif operation == '-':
            return subtract(num1, num2)
        elif operation == '*':
            return multiply(num1, num2)
        elif operation == '/':
            return divide(num1, num2)
        elif operation == '%':
            return modulus(num1, num2)
        elif operation == '**':
            return exponent(num1, num2)
        elif operation == '//':
            return floor_divide(num1, num2)
        elif operation == 'abs':
            return absolute(num1)
        elif operation == 'sqrt':
            return square_root(num1)
        elif operation == 'log':
            base = float(input("Enter base for logarithm (default 10): ") or 10)
            return logarithm(num1, base)
        else:
            print("Invalid operation.")
            return None
    def main():
        while True:
        num1, num2, operation = get_input()
            if num1 is None or num2 is None:
                continue
        result = calculate(num1, num2, operation)
        if result is not None:
            print(f"Result: {result}")
        if input("Do you want to perform another calculation? (yes/no): ").strip().lower() != 'yes':
            break
if __name__ == "__main__":
    main()
