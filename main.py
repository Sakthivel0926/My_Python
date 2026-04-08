import math
import math_operations
import string_operations

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", math_operations.add(num1, num2))
    print("Division:", math_operations.divide(num1, num2))

    print("Square root of first number:", math.sqrt(num1))

    name = input("Enter your name: ")
    print(string_operations.greet(name))

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter valid numbers")

finally:
    print("Program executed successfully")