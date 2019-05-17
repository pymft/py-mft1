my_set = {1, 2, 3, 1, 2, 1, 1, 1, 1}

print(my_set)
print(type(my_set))

print(len(my_set))
condition = 1 in my_set
print(condition)

s1 = {1, 2, 3, 4, 6.01, 9}
s2 = {1, 2, 3, 4, 5, 7}
s = s1.union(s2)
print(s)

for i in s1:
    print(i)