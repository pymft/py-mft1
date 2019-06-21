class Area:
    def __get__(self, instance, owner):
        if isinstance(instance, Rectangle):
            return instance.width * instance.height

        elif isinstance(instance, Circle):
            return 3.1415 * instance.radius ** 2

    def __set__(self, instance, value):
        ratio = (value / instance.area) ** 0.5

        if isinstance(instance, Rectangle):
            instance.width *= ratio
            instance.height *= ratio

        elif isinstance(instance, Circle):
            instance.radius *= ratio


class Rectangle:
    area = Area()

    def __init__(self, a, b):
        self.width = a
        self.height = b


class Circle:
    area = Area()

    def __init__(self, r):
        self.radius = r


r1 = Rectangle(10, 2)
c1 = Circle(4)


print(r1.area, c1.area, c1.radius)
c1.area = 200
print(r1.area, c1.area, c1.radius)
#
# r.area = 1000
# Rectangle.area = 1000000000
# print(r, r.width, r.height, r.area)
# print(r2, r2.width, r2.height, r2.area)
# print(r3, r3.width, r3.height, r3.area)
