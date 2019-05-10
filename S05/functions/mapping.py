# f = lambda x: x**2
def f(x):
    return x[1] + x[0]


data = [(1, 2), (3, 4), (5, 6), (1.5, 1.5), (1, 2)]

# {2k | k \in N }
out = [f(v) for v in data]
# out = map(f, data)
# print(max(out))

# out = []
# for v in data:
#     out.append(f(v))


print(list(out))
