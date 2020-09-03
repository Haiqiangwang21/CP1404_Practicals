from collections import Counter

word_occurrences = {}
text_input = input("Text: ")

words = text_input.split()
for word in words:

    unique_words = word_occurrences.get(word, 0)
    word_occurrences[word] = unique_words + 1

words = Counter(words).keys()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_occurrences[word]))