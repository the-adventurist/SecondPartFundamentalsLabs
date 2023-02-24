list_of_letters = input().split(', ')
dict_letters_witH_ascii_values = {k: ord(k) for k in list_of_letters}
print(dict_letters_witH_ascii_values)
