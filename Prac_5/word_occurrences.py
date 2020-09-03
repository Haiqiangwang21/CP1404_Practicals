from collections import Counter

word_occurrences = {}
text_input = input("Enter a string: ")
words = text_input.split()

for word in words:
    count = word_occurrences.get(word, 0)
    word_occurrences[word] = count + 1

words = Counter(words).keys()

longest_word = max((len(word) for word in words))
for word in words:
    print("{:{}} : {} ".format(word,longest_word, word_occurrences[word]))