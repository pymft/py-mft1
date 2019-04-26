left = lambda lst: lst[:len(lst) // 2] + lst[:len(lst) // 2][::-1]
right = lambda lst: lst[len(lst) // 2:][::-1] + lst[len(lst) // 2:]

inp = list(range(1, 41))
print(left(inp))

