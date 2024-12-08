# Write a Python program to swap two numbers without using a temporary variable.
def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2


print(swap(10, 20))