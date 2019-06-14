class Vector:
    name = "vector"      # class variable

    def __init__(self, *args):
        # temp = all([isinstance(a, (int, float)) for a in args])
        self.dims = args    # instance variable


    @property
    def length(self):
        return sum(d ** 2 for d in self.dims) ** 0.5

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Vector(x_new, y_new)

    def __mul__(self, other):
        if isinstance(other, Vector):
            x_new = self.x * other.x
            y_new = self.y * other.y
            return Vector(x_new, y_new)
        elif isinstance(other, (int, float)):
            x_new = self.x * other
            y_new = self.y * other
            return Vector(x_new, y_new)



v1 = Vector(10, 2)
print(v1.length)
v2 = Vector(1, 1, 1, 1)
print(v2.length)
#
# v1 = Vector(1, 2)
# v2 = Vector(10, 20)
#
# v4 = v1 * 5
# print(v1.x, v1.y)
# print(v2.x, v2.y)
# print(v4.x, v4.y )
#
# # v1.compute_length()
# # Vector.compute_length(v1)
#
#
# v3 = v1 + v2
# # v3 = v1.__add__(v2)
# # v3 = Vector.__add__(v1, v2)
# print(v3.length)

#
#
