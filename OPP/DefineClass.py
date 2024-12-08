# Define a class Rectangle and calculate the area and perimeter of a rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(10, 20)

print(r.area())  # 200
print(r.perimeter())  # 60