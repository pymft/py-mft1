def fact(n):
    out = 1
    i = 0
    while i < n:
        i += 1
        out = out * i
    return out


def combination(n, m):
    a = fact(n)
    b = fact(m) * fact(n - m)
    res = a // b
    return res



res = combination(10, 2)
print(res)

