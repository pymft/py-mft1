indx = [0, 1, 2, 3]
lst1 = [10, 20, 30, 40]
lst2 = [11, 22, 33, 44]

out = zip(indx, lst1, lst2)

for i, v, u in out:
    print(i, v, u)