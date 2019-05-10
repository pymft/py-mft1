def shift_max(lst):
    is_sorted = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            is_sorted = False
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return is_sorted


def bubble(lst):
    while True:
        is_sorted = shift_max(lst)
        if is_sorted:
            break


lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(lst)
bubble(lst)
print(lst)
