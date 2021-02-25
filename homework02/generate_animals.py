#!/usr/bin/env python3

import json
import petname
import random
import sys

def random_head():
    return(random.choice(['snake', 'bull', 'lion', 'raven', 'bunny']))

def random_body():
    return(random.choice(petname.names)) + '-' + (random.choice(petname.names))

def random_arms():
    num_of_arms = random.randrange(2, 11 ,2)
    random_arms.arms = num_of_arms
    return(num_of_arms)

def random_legs():
    num_of_legs = random.randrange(3, 13, 3)
    random_legs.legs = num_of_legs
    return(num_of_legs)

def num_tails(input_arms, input_legs):
    tails = input_arms + input_legs
    return(tails)

data = {}

data['animals'] = []

for i in range(20):
    data['animals'].append({'head': random_head(), 'body': random_body(), 'arms': random_arms(), 'legs': random_legs(),'tails': num_tails(random_arms.arms, random_legs.legs)})

with open(sys.argv[1], 'w') as f:          
    json.dump(data, f, indent=2)  
