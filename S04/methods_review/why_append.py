import time


limit = 50000

t1 = time.time()
lst = []
for i in range(limit):
    lst.append(i)
t2 = time.time()

meth_1 = t2 - t1
print(meth_1, "append")


t1 = time.time()
lst = []
for i in range(limit):
    lst = lst + [i]
t2 = time.time()

meth_2 = t2 - t1
print(meth_2, "adding lists together, lose the `id`")
print(meth_2/meth_1, "ratio")

