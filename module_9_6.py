def all_variants(text):
    i = 0
    while i != len(text):
        yield text[i]
        i += 1
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            yield text[i] + text[j]
    else:
        yield text


a = all_variants("abc")
for v in a:
    print(v)
