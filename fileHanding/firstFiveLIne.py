# Create a script to display only the first 5 lines of a file.


def firstFiveLines(file):
    with open(file, mode="r") as f:
        for i in range(5):
            print(f.readline(), end="")
            

firstFiveLines("test.txt")