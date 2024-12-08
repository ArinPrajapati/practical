#Write a program to validate user input and raise a ValueError if the input is invalid.
def validate_input(user_input):
    if not user_input.isdigit():
        raise ValueError("Invalid input: Input must be a number.")
    return int(user_input)

try:
    user_input = input("Enter a number: ")
    validated_input = validate_input(user_input)
    print(f"Validated input: {validated_input}")
except ValueError as e:
    print(e)