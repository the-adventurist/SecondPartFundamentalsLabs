import re
dates = input()
pattern = r'(\d{2})(/|-|\.)([A-Z][a-z]{2})(\2)(\d{4})'

correct_dates = re.finditer(pattern, dates)

for current_date in correct_dates:
    print(f"Day: {current_date.group(1)}, Month: {current_date.group(3)}, Year: {current_date.group(5)}")
