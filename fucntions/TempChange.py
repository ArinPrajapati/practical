# Write a function to convert Celsius to Fahrenheit and vice versa.


def celsiusToFahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(celsiusToFahrenheit(0))  # 32.0
print(fahrenheitToCelsius(32))  # 0.0