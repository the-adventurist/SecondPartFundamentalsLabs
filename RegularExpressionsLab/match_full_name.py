import re
names = input()
pattern = r'\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b'

full_name = re.findall(pattern, names)

print(' '.join(full_name))
