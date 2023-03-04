banned_words = input().split(', ')
text = input()

for current_banned_word in banned_words:
    while True:
        partitions = text.partition(current_banned_word)
        replacer = '*' * len(partitions[1])
        text = partitions[0] + replacer + partitions[2]
        if current_banned_word not in text:
            break
print(text)
