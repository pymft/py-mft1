lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

left = lst[:len(lst)//2] + lst[:len(lst)//2][::-1]
right = lst[len(lst)//2:][::-1] + lst[len(lst)//2:]
print(left)
print(right)