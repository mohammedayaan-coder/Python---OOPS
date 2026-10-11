class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm²"

    @property
    def height(self):
        return f"{self._height:.1f}cm²"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def width(self, new_height):
        if new_height > 0:
            self.height = new_height
        else:
            print("height must be greater than zero")
    
shape = Rectangle(6,8)

shape.width = 0

print(shape.width)
print(shape.height)