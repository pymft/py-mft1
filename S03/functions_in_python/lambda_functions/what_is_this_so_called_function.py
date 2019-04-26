import math
# lst = [1, 2, 3, 4]
test = len
# val = test(lst)
# print(val)
#

distance = lambda x, y: math.sqrt(x**2 + y**2)
len_of_str_pow_two = lambda text: len(text) ** 2
f = lambda x: x ** 2

y = f(2)
print(y)

res = len_of_str_pow_two("hello dude!")
print(res)

d = distance(3, 4)
print(d)
d = distance(12, 5)
print(d)
d = distance(100, 0)
print(d)
d = distance(6, 8)
print(d)