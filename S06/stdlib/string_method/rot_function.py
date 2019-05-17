def rot_2(c):
    inps = 'abcdefghijklmnopqrstuvwxyz'
    indx = inps.index(c)
    outs = 'cdefghijklmnopqrstuvwxyzab'
    return outs[indx]


text = ""
for c in "fcjjm":
    text += rot_2(c)

print(text)
