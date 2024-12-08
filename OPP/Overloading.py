# Write a program to demonstrate method overloading in Python.


class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Two arguments: {a}, {b}")
        elif a is not None:
            print(f"One argument: {a}")
        else:
            print("No arguments")


# Create an instance of the Example class
example = Example()

# Call the display method with different numbers of arguments
example.display()
example.display(10)
example.display(10, 20)
