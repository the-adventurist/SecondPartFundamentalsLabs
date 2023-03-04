some_text = input().split()

result_string = ''

for word in some_text:
    result_string += word * len(word)

print(result_string)
