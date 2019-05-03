def my_sort(lst):
    lst2 = lst.copy()
    lst_sorted = []

    while lst2:
        mx = min(lst2)
        lst_sorted.append(mx)
        lst2.remove(mx)

    return lst_sorted


input_values = [1, 2, 3, 4, 2, 1]

sorted_values = my_sort(input_values)

print(sorted_values)
print(input_values)

