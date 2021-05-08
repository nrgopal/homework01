### These were attempted routes to edit and analyze the local dataset post submitting CRUD jobs.

import json
from flask import Flask, request
import jobs
from datetime import datetime

app = Flask(__name__)

def getdata():
    with open("Austin_COVID-19_Complaint_Cases.json", "r") as json_data:
        userdata = json.load(json_data)
    return userdata

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

### Delete complaints by jobid parameter
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

### Count the total number of complaints
@app.route('/total', methods = ['GET'])
def total():
    data = getdata()
    number_of_complaints = len(data)

    return("Total number of COVID-19 complaints: " + str(number_of_complaints) + "\n")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
