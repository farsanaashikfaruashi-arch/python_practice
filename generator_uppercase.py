def uppercase_chars(text):
    for ch in text:
        yield ch.upper()
for c in uppercase_chars("PyThOn"):
    print(c)
