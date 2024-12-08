# Write a Python program to append content to a file.


def appendContext(file, content):
    with open(file, mode="a") as f:
        f.write("\n")
        f.write(content)


appendContext("test.txt", "This is a new line")
