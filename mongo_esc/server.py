from flask import Flask, request, jsonify
import requests
from database_store import DB
import json
app = Flask(__name__)
db = DB()

@app.route("/connect", methods=["GET","POST"])
def connect():
    db.connect()
    return 'True'

@app.route("/change_db/<collection>",methods=["GET","POST"])
def change_db(collection=None):
    db.change_db(collection)
    return 'True'

@app.route("/save_data/<collection>/<document>",methods=["GET","POST"])
def save_data(collection,document):
    document = json.loads(document)
    db.save_data(collection,document)
    return 'True'

@app.route("/get_data/<collection>/<parameters>",methods=["GET","POST"])
def get_data(collection,parameters):
    parameters = json.loads(parameters)
    keys=parameters["keys"]
    values=parameters["values"]
    document=parameters["document"]
    result = db.get_data(collection,keys=keys,values=values,document=document)
    return json.dumps(result)

@app.route("/",methods=["GET","POST"])
def index():
    return "Congradulations, you are now running Mongo-ESC"

app.run(
    debug=True,
    port=5002,
    host="0.0.0.0"
)
