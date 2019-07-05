import glob

relation = {}
relation_rev = {0:[]}
list_of_files = glob.glob('./files/*.txt')
for f in list_of_files:
    parent = open(f).read()
    child = f[8:-4]
    child = int(child)
    parent = int(parent)
    relation[child] = parent
    relation_rev[child] = []

for child in relation:
    if relation[child] == 0:
        print(child, relation[child])

for child in relation:
    parent = relation[child]
    relation_rev[parent].append(child)


for parent in relation_rev:
    if relation_rev[parent] == []:
        print(parent)


