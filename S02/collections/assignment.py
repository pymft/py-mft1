lst = [1, 1, 1, 1, 1]
length = len(lst)
mid = length // 2
# mid = int(lst / 2)

right = lst[mid:]
left = lst[:mid]

right_average = sum(right) / (length - mid)
left_average = sum(left) / mid

answer = right_average - left_average

print("left side avg > ", left_average)
print("right side avg> ", right_average)
print("diff of avg --> ", answer)
