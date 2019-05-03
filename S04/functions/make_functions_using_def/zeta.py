def zeta(s, limit):
    res = 0
    for i in range(1, limit + 1):
        res = res + 1 / i ** s
    return res


for i in [100, 1000, 10000, 100000]:
    val = zeta(2, i)
    pi_approximate_2 = (val * 6) ** 0.5
    print(i,'\t',  pi_approximate_2)
