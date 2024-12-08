# Write a program to count the occurrence of a specific word in a text file.

def countOccurrence(file, word):
    with open(file, mode="r") as f:
        content = f.read()
        count = content.count(word)
        print(f"The word '{word}' occurs {count} times in the file.")
        
countOccurrence("test.txt", "od")