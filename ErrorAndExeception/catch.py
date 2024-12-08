#Create a program to raise and catch a custom exception.
class CustomException(Exception):
    pass

def risky_function():
    raise CustomException("Something went wrong!")

try:
    risky_function()
except CustomException as e:
    print(f"Caught an exception: {e}")