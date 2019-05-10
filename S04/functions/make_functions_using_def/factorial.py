def factorial(n):
    i = 0
    s = 1
    while i < n:
        i += 1    # i = i + 1
        s *= i    # s = s * i
    return s


def combination(n, m):
    a = factorial(n)
    b = factorial(m) * factorial(n - m)
    res = a // b
    return res


def pascal_row(n):
    row = []

    for i in range(n+1):
        temp = combination(n, i)
        row = row + [temp]
    return row


def pascal(n):
    for i in range(n):
        print(pascal_row(i))


print(pascal(10))