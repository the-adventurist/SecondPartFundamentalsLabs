word_sequence = [x.lower() for x in input().split()]
dict_word_occurrences = {}
for k in word_sequence:
    if k not in dict_word_occurrences:
        dict_word_occurrences[k] = 0
    dict_word_occurrences[k] += 1
for word, times_occur in dict_word_occurrences.items():
    if times_occur % 2 == 1:
        print(word, end=' ')
