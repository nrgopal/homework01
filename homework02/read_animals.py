#!/usr/bin/env python3

import json
import random
import sys

with open(sys.argv[1], 'r') as f:         
    animals = json.load(f)             

random_animal = random.randrange(0, 21)

# print(animals['animals'][random_animal])
    
def breed_animals():

    parent1 = random.choice(animals['animals'])
    parent2 = random.choice(animals['animals'])

    offspring_head = parent1['head'] + '-' + parent2['head']
    offspring_body = parent1['body'] + '-' + parent2['body']
    offspring_arms = parent1['arms'] + parent2['arms']
    offspring_legs = parent1['legs'] + parent2['legs']
    offspring_tails = parent1['tails'] + parent2['tails']

    offspring = {'head' : offspring_head, 
                 'body' : offspring_body,
                 'arms' : offspring_arms,
                 'legs' : offspring_legs,
                 'tails' : offspring_tails
    }

    print('Parent 1: ')
    print(parent1)
    print('Parent 2: ')
    print(parent2)
    print('Offspring: ')
    print(offspring)

    breed_animals.parent1 = parent1
    breed_animals.parent2 = parent2
    breed_animals.offspring = offspring


breed_animals()
