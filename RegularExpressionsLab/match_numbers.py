import re
numbers = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

captured_numbers = re.finditer(pattern, numbers)

for caught_number in captured_numbers:
    print(caught_number.group(), end=' ')


