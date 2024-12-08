#Create a program to find and replace a word in a text file.

def findAndReplaceWord(file, word, newWord):
    with open(file, mode="r+") as f:
        content = f.read()
        content = content.replace(word, newWord)
        f.seek(0)
        f.write(content)
        f.truncate()
        
findAndReplaceWord("test.txt", "occaecat", "74")