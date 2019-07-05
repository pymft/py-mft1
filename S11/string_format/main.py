name = "some name"
num = 1234
lst = [1, 2, 3, 4]

# line = "* " + name + " | " + str(num) + " + " + str(lst[1]) + " = " + str(num + lst[1])
# line = "* {0} | {1} + {2} = {3}".format(name, num, lst[0], num+lst[1])
# line = "* {s} | {i} + {j} = {k}".format(s=name, i=num, j=lst[0], k=num+lst[1])
# line = "*{name:^60}*".format(name=name)
line = f"* {name} | {num} + {lst[1]} = {num + lst[1]}"
print(line)