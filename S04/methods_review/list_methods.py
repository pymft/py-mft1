# check the full methods of list : https://docs.python.org/3/tutorial/datastructures.html

lst = [1, 2, 3, 4, 1, 1, 1]
res = lst.count(1)
print(res)
print(id(lst), lst)
lst.append(10)
print(id(lst), lst)

lst.insert(1, 100)

print(id(lst), lst)

lst.extend([-1000])
print(id(lst), lst)

lst.remove(100)
print(id(lst), lst)

value = lst.pop(-1)
print(value, 'has been removed ')
print(id(lst), lst)