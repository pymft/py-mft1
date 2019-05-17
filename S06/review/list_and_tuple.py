lst = [1.1, True, len, [1, 2, 3]]
print(lst[0])

print(lst[2]("hello"))
print(len("hello"))

print(lst[-1][0])

print(id(lst), lst)
lst.append(100)
# lst = lst + [100]
print(id(lst), lst)
