#Create a program to demonstrate list comprehensions with a practical example.
# Example: Create a list of squares of even numbers from 0 to 10
even_squares = [x**2 for x in range(11) if x % 2 == 0]
print(even_squares)