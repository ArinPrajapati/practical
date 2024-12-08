# Write a Python program to demonstrate the use of *args and **kwargs.
def demo_args_kwargs(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)


# Example usage
demo_args_kwargs(1, 2, 3, a=4, b=5)
