class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.height = b
        self.__area = self.width * self.height

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio = (value / self.area) ** 0.5
        self.width *= ratio
        self.height *= ratio


r = Rectangle(10, 2)
print(r.width, r.height, r.area)
r.width = 1
print(r.width, r.height, r.area)
r.area = 8
print(r.width, r.height, r.area)
