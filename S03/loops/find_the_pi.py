limit = 1000
answer_1 = 0
answer_2 = 0

i = 0

while i < limit:
    i = i + 1
    answer_1 = answer_1 + 1 / i ** 4
    answer_2 = answer_2 + 1 / i ** 2

pi_approximate_1 = (answer_1 * 90) ** 0.25
pi_approximate_2 = (answer_2 * 6) ** 0.5
pi_real = 3.141592653589793238462643383279502884

print("new", pi_approximate_1)
print("pi ", pi_real)
print("old", pi_approximate_2)
