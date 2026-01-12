sentence = input("Enter sentence: ")
words = sentence.split()
longest = 0
for word in words:
    if len(word) > longest:
        longest = len(word)
print("Length of longest word:", longest)
