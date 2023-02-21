class Zoo:
    _animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
            Zoo._animals += 1
        elif species == 'fish':
            self.fishes.append(name)
            Zoo._animals += 1
        else:
            self.birds.append(name)
            Zoo._animals += 1
    def get_info(self,species):
        result = None
        if species == 'mammal':
            result = f"""Mammals in {self.name}: {', '.join(self.mammals)}
Total animals: {Zoo._animals}"""
        elif species == 'fish':
            result = f"""Fishes in {self.name}: {', '.join(self.fishes)}
Total animals: {Zoo._animals}"""
        else:
            result = f"""Birds in {self.name}: {', '.join(self.birds)}
Total animals: {Zoo._animals}"""
        return result

zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())
animal_info = input().split()
while len(animal_info) > 1:
    species, name = animal_info
    zoo.add_animal(species, name)

    animal_info = input().split()

this_animal = animal_info[0]
print(zoo.get_info(this_animal))
