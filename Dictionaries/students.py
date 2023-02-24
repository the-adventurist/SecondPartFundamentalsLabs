info = input().split(':')
dict_info = {}

while len(info) > 1:
    name, this_id, course = info
    dict_info.setdefault(course, {}).setdefault(name, this_id)
    info = input().split(':')

course = info[0].split('_')
course = ' '.join(course)
for current_course, details_info in dict_info.items():
    if current_course == course:
        for current_name, current_id in details_info.items():
            print(f'{current_name} - {current_id}')
