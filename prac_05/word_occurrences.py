"""
Word Occurrences
Estimate: 35 minutes
Actual:   43 minutes
"""
word_to_count = {}
text = "I love love apples green apples red apples"
# text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(word_to_count.keys())
words.sort()

width = max((len(word) for word in words))
for word in words:
    print(f"{word:{width}} : {word_to_count[word]}")
