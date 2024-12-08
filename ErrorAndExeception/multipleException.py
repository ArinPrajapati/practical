#Write a Python script to handle multiple exceptions in a single block.
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except Exception as e:
    print("An unexpected error occurred:", e)