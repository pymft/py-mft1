lst = [("the", 10), ("is", 60), ("whatever", 90)]
diff = [10,  60, 90]
# f = lambda x: x[1]
#
# diff = [f(lst[0]), f(lst[1]), f(lst[2]), ]

max_value = max(diff)
indx = diff.index(max_value)
print(lst[indx])
