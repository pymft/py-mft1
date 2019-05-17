data = [1, 2, 3, 4, 5, 6, 7]
f = lambda x: x ** 2

data2 = [1, 4, 9, 16, 25, 36, 49]
f = lambda x: -x
data3 = [-1, -2, ...]

data = [(1, 2), (3, 4), (5, 6), (1.5, 1.5), (1,2)]
f = lambda x: x[0]**2 + x[1]**2
data1 = [f((1, 2)), f((3, 4)), f((5, 6)), f((1.1, 1.1))]
print(min(data, key=f))
# print(data1)
# print(min(data))
