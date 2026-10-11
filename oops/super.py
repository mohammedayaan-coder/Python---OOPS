class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self):
        r = self.radius
        print(3.14 * r * r)

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)    
        self.side = side

    def area(self):
        s = self.side
        print(s*s)

class Triangle(Shape):
    def __init__(self, color, is_filled, height, base):
        super().__init__(color, is_filled)
        self.height = height
        self.base = base

circle = Circle("blue", "Yes", 5)
circle.area()

square = Square("Red", "No", 10)
square.area()
