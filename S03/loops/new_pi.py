limit = 1000
# target = 1.64493406684822643647
# s = 2
target = 1.08232323371113819152
s = 4
answer_1 = 0
i = 0
err = (answer_1 - target) / target

while abs(err) > 0.00000000001:
    i = i + 1
    answer_1 = answer_1 + 1 / i ** s
    err = (answer_1 - target) / target


print(i)

