import json
import random

with open('animals.json', 'r') as f:
    animals = json.load(f)

random_animal = random.randrange(0, 21)

print(animals['animals'][random_animal])
    
