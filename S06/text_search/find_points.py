inp = """
0.0    0.1      1.2
1.2         2.0    6.0 
8.2    9.1    0.2
"""

res = inp.split('\n')
data = [[float(d) for d in row.split()] for row in res if row != ""]

print(data)