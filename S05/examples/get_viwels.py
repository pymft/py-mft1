def get_vowels(text):
    words = text.split()
    res = []
    for w in words:
        if w[0] in 'aeoui':
            res.append(w)

    return res

def get_vowels_2(text):
    words = text.split()
    res = [w for w in words if w[0] in "aeiou"]
    return res


def get_vowels_2(text):
    f = lambda w: w[0] in "aeiou"
    words = text.split()
    return filter(f, words)


vowels = get_vowels("Returns a abcdef string where a specified value is replaced with a specified value")
print(vowels)