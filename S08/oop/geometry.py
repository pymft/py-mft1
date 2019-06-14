import math

class Parallelogram:
    def __init__(self, a, b, angle):
        print("paralleogram", self.__class__)
        self.a = a
        self.b = b
        self.angle = angle

    @property
    def area(self):
        return self.a * self.b * math.sin(math.radians(self.angle))

    @property
    def perimeter(self):
        return (self.a + self.b) * 2


class Diamond(Parallelogram):
    def __init__(self, a, angle):
        print("diamond")
        super().__init__(a, a, angle)


class Rectangle(Parallelogram):
    def __init__(self, w, h):
        print("rect")
        super().__init__(w, h, 90)

#
# class Square(Rectangle):
#     def __init__(self, a):
#         super().__init__(a, a)


class Square(Diamond):
    def __init__(self, a):
        print("square")
        super().__init__(a, 90)

#
# r = Rectangle(10, 4)
# print(r.area, r.perimeter)


s = Diamond(7, 45)
print(s.area, s.perimeter)
#
# print(s, hex(id(s)))
