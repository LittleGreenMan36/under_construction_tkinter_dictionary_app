from get_info import Word

word = input('Word: ')

word = Word(word.upper())
# it is in the format - [[Meanings], [Synonyms], [Antonyms]]
print(word.get_info())
