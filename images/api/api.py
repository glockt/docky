#Import the flask module
import json
from flask import Flask, escape, request, jsonify
from waitress import serve

#Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

#Create a route decorator to tell the application, which URL should be called for the #described function and define the function

@app.route('/')
def index():
    return return_error('no api call defined')

@app.route('/greeting')
def greeting():
    name = request.args.get('name', '')
    if name in (None, ''):
        return return_error('following request argument must be filled: name')
    return jsonify({'greeting': 'Hello', 'name': escape(name)})

def return_error(message):
	return jsonify({'error': escape(message)}) 

#Create the main driver function
if __name__ == '__main__':
    #call the run method
    serve(app, host='0.0.0.0', port=8081)
