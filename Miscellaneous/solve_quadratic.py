import cmath

# Write a Python script to solve a quadratic equation.
def solve_quadratic(a, b, c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    
    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    
    return sol1, sol2

# Example usage
a = 1
b = 5
c = 6
solution1, solution2 = solve_quadratic(a, b, c)
print(f"The solutions are {solution1} and {solution2}")