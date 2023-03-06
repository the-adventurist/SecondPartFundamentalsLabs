import re
phones = input()
pattern = r"\+359(-| )2(\1)\d{3}(\1)\d{4}"

correct_phones = re.finditer(pattern, phones)

list_of_phones = []
for phone in correct_phones:
    list_of_phones.append(phone.group())

print(', '.join(list_of_phones))


