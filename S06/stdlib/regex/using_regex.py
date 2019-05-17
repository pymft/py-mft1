import re


text = """ """
pat = "([\.\w]+)@([\w\.]+)\.(\w+)"

res = re.findall(pat, text)
print(res)
