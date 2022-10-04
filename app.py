# import modules to make it work
from flask import Flask
import dbhelpers as dh
import json
app = Flask(__name__)

@app.get('/animals')

# function that will return in json format
def get_all_animals():
    result = dh.run_statement('CALL return_all()')
    if(type(result) == list):
        animals_json = json.dumps(result, default=str)
        return animals_json
    else:
        return "Something went wrong, try again "

def get_all_dogs():
    result = dh.run_statement('CALL return_all_dogs()')
    if(type(result) == list):
        all_dogs_json = json.dumps(result, default=str)
        return all_dogs_json
    else:
        return "Something went wrong, try again "

def get_all_cats():
    result = dh.run_statement('CALL return_all_cats()')
    if(type(result) == list):
        all_cats_json = json.dumps(result, default=str)
        return all_cats_json
    else:
        return "Something went wrong, try again "

app.run(debug=True)

