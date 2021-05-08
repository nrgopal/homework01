import json
from flask import Flask, request
import jobs
from datetime import datetime

app = Flask(__name__)

def getdata():
    with open("Austin_COVID-19_Complaint_Cases.json", "r") as json_data:
        userdata = json.load(json_data)
    return userdata

@app.route('/helloworld', methods = ['GET'])
def hello_world():
    return 'hello world'

### Update the complaints dataset
@app.route('/update', methods=['GET'])
def update():
    uuid = request.args.get('uuid')
    head = request.args.get('head')
    body = request.args.get('body')
    arms = request.args.get('arms')
    legs = request.args.get('legs')
    tails = request.args.get('tails')

    if head is not None:
        rd.hset(uuid, 'head', head)
    if body is not None:
        rd.hser(uuid, 'body', body)
    if arms is not None:
        rd.hset(uuid, 'arms', arms)
    if legs is not None:
        rd.hset(uuid, 'legs', legs)
    if tails is not None:
        rd.hset(uuid, 'tails', tails)

    return str(uuid + 'has been updated')

### Query complaints from a range of dates
@app.route('/query', methods = ['GET'])
def query():
    data = getdata()
    start_date = input('Enter start of range: ')
    end_date = input('Enter end of range: ')
    start_range = datetime.strptime(start_date, '%Y-%m-%d')
    end_range = datetime.strptime(end_date, '%Y-%m-%d')
    query_list = []

    for complaint in data:
        date = datetime.strptime(complaint['OPENDATE'], '%Y-%m-%d')
        if ((date >= start_range) and (date <= end_range)):
            query_list.append(complaint)

    print("Query completed." + "\n")

    return str(query_list)

### Select a complaint by CASENUMBER
@app.route('/select/<CASENUMBER:id>')
def select(id):
    data = getdata()
    selected_complaint = []

    for complaint in data:
        if (complaint['CASENUMBER'] == str(id)):
            print(complaint)
            return complaint

    return("")

### Edit a complaint by CASENUMBER
@app.route('/edit/<CASENUMBER:id>')
def edit(id):
    data = getdata()
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

### Delete complaints within a range of dates
@app.route('/delete', methods=['GET'])
def delete():
    data = getdata()
    start_date = input('Enter start of range: ')
    end_date = input('Enter end of range: ')
    start_range = datetime.strptime(start_date, '%Y-%m-%d')
    end_range = datetime.strptime(end_date, '%Y-%m-%d')
    deleted_list = data

    for complaint in data:
        date = datetime.strptime(complaint['OPENDATE'], '%Y-%m-%d')
        if ((date >= start_range) and (date <= end_range)):
            delete_case = complaint['CASENUMBER']
            for deletion in deleted_list:
                if (deletion['CASENUMBER'] == delete_case):
                    deleted_list.remove(deletion)

    with open('COVID-19_complaints_after_deletion.json', 'w') as f:
        json.dump(deleted_list, f, indent=2)

    return("Complaints have been deleted." + "\n")

### Possibly compute the zipcode with the most complaints?
@app.route('/zipcode', methods = ['GET'])
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

### Count the total number of complaints
@app.route('/total', methods = ['GET'])
def total():
    data = getdata()
    number_of_complaints = len(data)

    return("Total number of COVID-19 complaints: " + str(number_of_complaints) + "\n")

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
