numbers = [1, 2, 3, 4, 5, 6]
numbers[2] = 1000  # mutable
numbers_tuple = (1, 2, 3, 4, 5, 6)
# numbers_tuple[2] = 1000   # immutable

person = []

# movie = [100, 2009, "Whatever Works", "Woody Allen"]


dct1 = {"id": 100, "year": 2009, "title": "Whatever Works", }
dct2 = {"director": "Woody Allen"}
movie = {**dct1, **dct2}
movie["director"]

s = {2, 3, 4, 5, 1, 1, 1, 6}
cond = 1 in s
print(s)


a = [1, 2, 3]
b = [4, 5, 6]
# [1, 2, 3 , 4, 5, 6]
# a = a + b
a.extend(b)






