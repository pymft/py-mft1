lst = [(-4, 100), (2, 1), (1, 90), (-5, 0), (3, 9)]

f = lambda x: x[1] - x[0]

print(lst)
lst.sort(key=f, reverse=True)
print(lst)

mx = min(lst, key=f)
print(mx)

# out = sorted(lst)
# print(lst)
# print(out)