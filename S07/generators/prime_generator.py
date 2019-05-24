import time
import math
import random

# def is_prime(n):
#     """
#     Miller-Rabin primality test.
#     A return value of False means n is certainly not prime. A return value of
#     True means n is very likely a prime.
#     """
#     if n != int(n):
#         return False
#     n = int(n)
#     # Miller-Rabin test for prime
#     if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
#         return False
#
#     if n == 2 or n == 3 or n == 5 or n == 7:
#         return True
#     s = 0
#     d = n - 1
#     while d % 2 == 0:
#         d >>= 1
#         s += 1
#     assert (2 ** s * d == n - 1)
#
#     def trial_composite(a):
#         if pow(a, d, n) == 1:
#             return False
#         for i in range(s):
#             if pow(a, 2 ** i * d, n) == n - 1:
#                 return False
#         return True
#
#     for i in range(8):  # number of trials
#         a = random.randrange(2, n)
#         if trial_composite(a):
#             return False
#
#     return True


def is_prime(n):
    limit = int(math.sqrt(n))
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


# def prime_generator(stop):
#     i = 2
#     while i < stop:
#         if is_prime(i):
#             yield i
#         i += 1

def prime_generator(num):
    i = 2
    counter = 0
    while counter < num:
        if is_prime(i):
            counter += 1
            yield i
        i += 1


t_start = time.time()
gen = prime_generator(100000)

sum_primes = 0

for p in gen:
    sum_primes += p

t_stop = time.time()
print("Elapsed time = ", t_stop- t_start)
print(sum_primes)