import wikipedia

print(wikipedia.search(input("Enter phrase >>> ")))
phrase = wikipedia.page(input)
print(phrase.title)
print(wikipedia.summary(input))
print(phrase.url)
