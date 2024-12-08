# Write a Python script to calculate the sum of digits of a given number.
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Example usage:
number = 12345
print(f"The sum of digits of {number} is {sum_of_digits(number)}")