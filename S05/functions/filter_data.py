data = [1, 2, 3, 4, 5, 6, 7]
out = []

for i in data:
    if i % 2 == 0:
        out.append(i)

f = lambda x: x % 2 == 1
out = [i for i in data if f(i)]
print(out)

res = filter(f, data)
print(list(res))
