# Write a function to check if a given string is a palindrome.

def isPalindrome(string):
    return string == string[::-1]

print(isPalindrome("madam"))

