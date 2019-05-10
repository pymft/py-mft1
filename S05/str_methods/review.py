def unique_words(text):
    for c in ".,()":
        text = text.replace(c, " ")

    words = text.lower().split()

    uniques = list(set(words))
    repeats = []
    for u in uniques:
        repeats.append([u, words.count(u)])
    return repeats


text = """The only significant advantage that bubble 
sort has over most other algorithms, even quicksort, 
but not insertion sort, is that the ability to detect 
that the list is sorted efficiently is built into 
the algorithm. When the list is already sorted
 (best-case), the complexity of bubble sort is 
 only O(n). By contrast, most other algorithms, 
 even those with better average-case complexity,
 perform their entire sorting process on the set 
 and thus are more complex. However, not only does
  insertion sort share this advantage, but it also 
  performs better on a list that is substantially 
  sorted (having a small number of inversions)."""

res = unique_words(text)
f = lambda x: x[1]

mx = max(res, key=f)
print(mx)

res.sort(key=f, reverse=True)
print(res)
