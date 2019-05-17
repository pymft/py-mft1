def find_all(text, pat):
    ind = -1
    out = []
    while True:
        ind = text.find(pat, ind + 1)
        if ind == -1:
            break
        out.append(ind)

    return out



sequence = "LSLLSSSSLSLSMSMLLMLSLSLSMSMSMSMSMSLMLLLSSSLLS"
print(find_all(sequence, "SMS"))


