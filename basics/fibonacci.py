# Write a Python script to print the Fibonacci series up to a given number.

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fibonacci(1000)