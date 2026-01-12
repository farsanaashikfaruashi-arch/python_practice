def string_chars(text):
    for ch in text:
        yield ch
for c in string_chars("hello"):
    print(c)
