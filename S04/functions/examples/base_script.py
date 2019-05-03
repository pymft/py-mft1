lst = [1, 2, 3, 4, 2, 1]
lst_sorted = []

while lst:
    mx = min(lst)
    lst_sorted.append(mx)
    lst.remove(mx)

print(lst_sorted)