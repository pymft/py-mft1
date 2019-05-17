def f_filter(x):
    return x < 5


def f_map(x):
    return x ** 2


data = [1, 2, 3, 4, 5, 6, 7, 8]

out = [f_map(i) for i in data if f_filter(i)]

# for i in data:
#     if i % 3 == 0:
#         out.append(i)


print(data)
print(out)
