# Write a function to calculate the GCD of two numbers.


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(12, 14))  # 2