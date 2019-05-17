f1 = open('input.txt', mode='r')
text = f1.read()
n, pat = text.split()
n = int(n)
f1.close()

f2 = open('output.txt', mode='w')

for i in range(1, n+1):
    f2.write(i * pat)
    f2.write('\n')

f2.close()
