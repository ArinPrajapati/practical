from itertools import permutations

# Create a program to find all the permutations of a given string.
def find_permutations(s):
    return [''.join(p) for p in permutations(s)]

if __name__ == "__main__":
    s = input("Enter a string: ")
    perms = find_permutations(s)
    print("Permutations of the string are:")
    for perm in perms:
        print(perm)