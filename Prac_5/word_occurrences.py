word_ot_count = {}
text_input = input("Enter a string: ")
words = text_input.split()

for word in words:
    count = word_ot_count.get(word, 0)
    word_ot_count[word] = count + 1

words = list(word_ot_count.keys())

longest_word = max(len(word) for word in words)
for word in words:
    print("{:{}} : {} ".format(word, longest_word, word_ot_count[word]))
