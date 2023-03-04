substring = input()
string = input()
while True:
    partitions = string.partition(substring)
    string = partitions[0] + partitions[2]
    if substring not in string:
        break
print(string)
