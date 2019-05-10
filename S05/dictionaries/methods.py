dct = {"hello": 2, "the": 6}

print(dct["the"])

dct["the"] = 100

dct[[1, 2]] = 10
print(dct["the"])
print(list(dct.keys()))
print(list(dct.values()))
print(list(dct.items()))

print(dct)
