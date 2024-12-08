# Create a program to reverse a string without using slicing.

def reverse_string(string):
    reversed_string = ''
    for i in range(len(string)):
        reversed_string += string[len(string) - i - 1]
    return reversed_string
