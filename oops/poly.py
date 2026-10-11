from abc import ABC, abstractmethod

class Shape():
    @abstractmethod
    def area(self):
        pass

class Circel(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circel(5), Square(5), Triangle(2,6)]

for shape in shapes:
    print(f"{shape.area()}cm²")
