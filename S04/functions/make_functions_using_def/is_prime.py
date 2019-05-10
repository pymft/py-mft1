import math
import time


def is_prime(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False

    return result


def is_prime_2(n):
    """

    :param n:
    :return:
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_3(n):
    """
    check prime numbers, a bit faster than before

    examples
    --------
    >>> is_prime_3(101)
    True
    >>> is_prime_3(10)
    False

    :param n:
    :return:
    """
    limit = int(math.sqrt(n))
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


t1 = time.time()
answ = is_prime(39916801)

t2 = time.time()
answ = is_prime_2(39916801)

t3 = time.time()
answ = is_prime_3(39916801)

t4 = time.time()

print(t2 - t1)
print(t3 - t2)
print(t4 - t3)
