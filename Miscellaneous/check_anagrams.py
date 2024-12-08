# Create a program to check if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    # Remove any whitespace and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')