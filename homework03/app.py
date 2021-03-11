import json
from flask import flask, request

app = Flask(__name__)

def getdata():
    with open("animals.json", "r") as json_file:
        userdata = json.load(json_file)

    return userdata

@app.route('/animals', methods=['GET'])
def get_animals():
    animals = getdata()
    return animals

@app.route('/animals/head/<string:head_id>', methods=['GET'])
def get_bunny_heads():
    animals = getdata()
    bunny_heads = []
    for i in animals:
        if (i['head:'] == head):
            bunny_heads.append(i)

    return jsonify(bunny_heads)

@app.route('/animals/legs/<int:leg_input>', methods=['GET'])
def get_six_legs():
    animals = getdata()
    leg_list = []
    for i in animals:
        if (i['legs'] == leg_input):
            leg_list.append(i)

    return jsonify(leg_list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
