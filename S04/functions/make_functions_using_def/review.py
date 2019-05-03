def f_2(x):
    if x % 2 == 0:
        res = x ** 2
    else:
        res = x ** 3

    return res


num = 10

print(f_2(10))
print(f_2(5))

