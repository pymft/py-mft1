f = open('file.txt', mode='r')
text = f.read()
f.close()
print(text)

with open('file.txt', mode='r') as f:
    text = f.read()

print(text)