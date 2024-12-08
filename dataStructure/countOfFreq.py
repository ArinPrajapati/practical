# Create a program to count the frequency of each character in a string.

def count_of_freq(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


print(count_of_freq('google.com'))