class Party:
    def __init__(self):
        self.people = []


party = Party()
person = input()
while person != 'End':
    party.people.append(person)
    person = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
