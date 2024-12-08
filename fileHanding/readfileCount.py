import os

def fileCount(file):
    with open(file, mode="r") as f:
        lines = f.readlines()  # Read all lines
        f.seek(0)  # Move the file cursor back to the start
        words = f.read().split()  # Read the entire file content and split into words
        print(f"Number of lines in the file are: {len(lines)}")
        print(f"Number of words in the file are: {len(words)}")


fileCount("basics/evenOdd.py")
