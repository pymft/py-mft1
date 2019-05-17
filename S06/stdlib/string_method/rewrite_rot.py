inps = 'abcdefghijklmnopqrstuvwxyz'
outs = 'cdefghijklmnopqrstuvwxyzab'


res = {c: m for c, m in zip(inps, outs)}
#
print(res)

text = "hello"
out = [res[c] for c in text]
print(out)