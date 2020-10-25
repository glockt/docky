#Import the flask module
import json
from flask import Flask, escape, request, jsonify
from waitress import serve

#Create a Flask constructor. It takes name of the current module as the argument
app = Flask(__name__)

#Create a route decorator to tell the application, which URL should be called for the #described function and define the function

@app.route('/api')
def index():
    name = request.args.get("name", "World")
    return jsonify({'greeting': 'Hello', 'name': escape(name)})

#Create the main driver function
if __name__ == '__main__':
    #call the run method
    serve(app, host="0.0.0.0", port=8081)
