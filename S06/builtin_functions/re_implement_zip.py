def my_zip(a, b):
    out = []
    for i in range(len(a)):
        out.append((a[i], b[i]))

    return out


def my_enumeratep(a):
    out = []
    for i in range(len(a)):
        out.append((i, a[i]))

    return out




lst1 = [1, 2, 3]
lst2 = [10, 20, 30]

res = my_enumeratep(lst2)
print(res)

# [(1, 10), (2, 20), (3, 30)]