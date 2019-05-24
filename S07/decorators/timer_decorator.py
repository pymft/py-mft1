import time
import math

def timeit(f):
    def inner(*args):
        t1 = time.time()
        out = f(*args)
        t2 = time.time()
        print("elapsed time = {:.3f} (ms)".format(1000*(t2-t1)))
        return out
    return inner

@timeit
def is_prime(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False

    return result

@timeit
def is_prime_2(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

@timeit
def is_prime_3(n, m):
    limit = int(math.sqrt(n))
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


is_prime_3(101, 1)
is_prime_2(101)
