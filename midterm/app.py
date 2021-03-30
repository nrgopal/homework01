import json
from flask import Flask, request
from datetime import datetime
import redis

app = Flask(__name__)

def getdata():
    with open("animals.json", "r") as json_data:
        userdata = json.load(json_data)
    return userdata

@app.route('/animals/query', methods = ['GET'])
def query():
    data = getdata()
    animal_list = data['animals']
    start_date = input('Enter start of range: ')
    end_date = input('Enter end of range: ')
    start_range = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
    end_range = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')
    query_list = []

    for animal in animal_list:
        date = datetime.strptime(animal['created_on'], '%Y-%m-%d %H:%M:%S.%f')
        if ((date >= start_range) and (date <= end_range)):
            query_list.append(animal)

    query = {}
    query['query range of dates: '] = query_list

    print("Query completed." + "\n")

    return query

@app.route('/animals/select/<uuid:id>')
def select(id):
    data = getdata()
    animal_list = data['animals']
    selected_animal = []

    for animal in animal_list:
        if (animal['uid'] == str(id)):
            print(animal)
            return animal

    return("")
  
 @app.route('/animals/edit/<uuid:id>')
 def edit(id):
    data = getdata()
    animal_list = data['animals']
    edit_animal = []

    edit_arms = input('Edit number of arms (int) : ')

    for animal in animal_list:
        if (animal['uid'] == str(id)):
            animal['arms'] = edit_arms
            edit_animal.append(animal)

    edit = {}
    edit['updated stats'] = edit_animal

    edited_animals = {}
    edited_animals['animals'] = animal_list

    with open('animals.json', 'w') as f:
        json.dump(edited_animals, f, indent=2)

    print("Edit was made to animal." + "\n")  
    
    return edit

@app.route('/animals/delete', methods=['GET'])
def delete():
    data = getdata()
    animal_list = data['animals']
    start_date = input('Enter start of range: ')
    end_date = input('Enter end of range: ')
    start_range = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S.%f')
    end_range = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S.%f')
    deleted_list = animal_list

    for animal in animal_list:
        date = datetime.strptime(animal['created_on'], '%Y-%m-%d %H:%M:%S.%f')
        if ((date >= start_range) and (date <= end_range)):
            delete_uid = animal['uid']
            for deletion in deleted_list:
                if (deletion['uid'] == delete_uid):
                    deleted_list.remove(deletion)

    deleted = {}
    deleted['animals'] = deleted_list
   
    with open('animals.json', 'w') as f:
        json.dump(deleted, f, indent=2)
    
    print("Animals have been deleted." + "\n")

    return deleted

@app.route('/animals/average', methods = ['GET'])
def average():
    data = getdata()
    animal_list = data['animals']
    total_legs = 0;
    leg_average = 0;
    number_of_animals = len(animal_list)
    for animal in animal_list :
        total_legs += animal['legs']

    leg_average = int(total_legs/number_of_animals)

    return("Average number of legs: " + str(leg_average) + "\n")

@app.route('/animals/total', methods = ['GET'])
def total():
    data = getdata()
    animal_list = data['animals']
        number_of_animals = len(animal_list)

    return("Total number of animals: " + str(number_of_animals) + "\n")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

rd = redis.StrictRedis(host='redis', port6379, db=0)

with open('animals.json', 'w') as f:     
