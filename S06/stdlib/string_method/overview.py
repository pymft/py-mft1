import string
#
# lst = []
# for i in range(97, 123):
#     lst.append(chr(i))
#
# for c in string.ascii_lowercase:
#     print(ord(c))

text = "hello world!"
out = [ord(c) for c in text]

print(out)

# print(set(string.ascii_lowercase))
# print(set(string.ascii_uppercase))
# print(set(string.ascii_letters))
# print(set(string.punctuation))
