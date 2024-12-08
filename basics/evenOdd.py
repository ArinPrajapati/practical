# Create a program to check if a given number is odd or even.


def evenOdd(nums):
    if nums % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(evenOdd(10))