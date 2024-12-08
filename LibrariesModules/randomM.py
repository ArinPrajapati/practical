import random
import string

# Create a program to generate a random password using the random module.
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
password_length = 12
print(f"Generated password: {generate_password(password_length)}")