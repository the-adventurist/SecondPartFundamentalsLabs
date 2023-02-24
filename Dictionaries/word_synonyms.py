count_of_key_words = int(input())
dict_synonyms = {}

for w in range(0, count_of_key_words * 2, 2):
    current_word = input()
    current_synonym = input()
    if current_word not in dict_synonyms:
        dict_synonyms[current_word] = []
    if current_synonym not in dict_synonyms[current_word]:
        dict_synonyms[current_word].append(current_synonym)

for word, synonyms in dict_synonyms.items():
    print(word, end=' - ')
    print(', '.join(synonyms))
