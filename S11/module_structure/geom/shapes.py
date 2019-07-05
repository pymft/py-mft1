from .base import Geometry


class Rectangle(Geometry):
    def __init__(self, a, b):
        self.width = a
        self.height = b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


class Circle(Geometry):
    def __init__(self, r):
        self.radius = r
