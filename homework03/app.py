import json
from flask import Flask, request                                                                                                                                                                                   
app = Flask(__name__)

def getdata():
    with open("animals.json", "r") as json_file:
        userdata = json.load(json_file)

    return userdata

@app.route('/animals', methods=['GET'])
def get_animals():
    animals = getdata()
    return animals

@app.route('/animals/head', methods=['GET'])
def get_bunny_heads():
    animals = getdata()                                                                                                                                                                                                head = request.args.get('head')
    return json.dumps([x for x in animals if x['head'] == head]) 

@app.route('/animals/legs', methods=['GET'])
def get_six_legs():
    animals = getdata()
    legs = int(request.args.get('legs')
    return json.dumps([x for x in animals if x['legs'] == legs)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0') 
