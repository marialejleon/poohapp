import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class comidita(object):
    def __init__(self):
        self.comidita = ""
    
    def add_food(self, string):
        self.comidita += string
    
    def read_food(self):
        return self.comidita

poofood = comidita()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Holi Pooh Pooh Pooh Pooh!!!!!</h1>"

@app.route('/test', methods=['GET'])
def test():
    return "<h1>Hello Pooh Test!!!!!</h1>"

@app.route('/food', methods=['POST'])
def hunny_for_pooh():
    food = request.json
    food_element = food["comida"]
    poofood.add_food(food_element)
    # comidita = food_element + comidita
    print(food_element)
    return "200 ok!"

@app.route('/foodforpooh', methods=['GET'])
def food():
    
    return poofood.read_food()

app.run(host="0.0.0.0")
