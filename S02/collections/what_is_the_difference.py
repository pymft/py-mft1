# list is mutable
# tuples are immutable  ---> unable to be changed!

lst = [1, 2, 3, 4, 5]
print(lst)
lst[2] = 1000
print(lst)
del lst[-1]
print(lst)
print(lst[4])

