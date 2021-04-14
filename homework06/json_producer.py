import random
import uuid
import datetime
import json
import sys
import petname
import redis

userdata = {"animals":[]}
def add_data(animal):
    userdata["animals"].append(animal)

print (type(userdata))

heads = ["snake", "raven", "lion", "bull", "eagle", "bunny"]

for i in range(0,100):
    uid = str(uuid.uuid4())
    head = random.choice(heads)
    arms = random.randint(2,10)
    legs = random.randint(3,12)
    tails = random.randint(0,2)
    date = str(datetime.datetime.now())

    animal = {}
    animal['uid'] = uid
    animal['head'] = head
    animal['arms'] = arms
    animal['legs'] = legs
    animal['tails'] = tails
    animal['created_on'] = date

    print(json.dumps(animal))

    add_data(animal)

with open('animals.json', 'w') as f:
    json.dump(userdata, f, indent=2)
