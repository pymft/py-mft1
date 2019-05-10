data = [(1, 2), (3, 4), (5, 6), (1.5, 1.5), (1, 2)]
f = lambda x: (x[1]**2 + x[0]**2)**0.5
print(data)
data.sort(key=f)
print(data)
