from app import app
from flask import render_template,request
from app.models import Data
from app import db
import json

@app.route("/add",methods=["GET","POST"])
def add():
    dicter = json.loads(request.data)
    data = Data(int(dicter["data"]))
    db.session.add(data)
    db.session.commit()
    return "successfully added "+str(dicter["data"])
    
    
@app.route("/remove",methods=["GET","POST"])
def remove():
    dicter = json.loads(request.data)
    Data.query.filter_by(data=int(dicter["data"])).delete()
    return "successfully deleted "+str(dicter["data"])

@app.route("/size",methods=["GET","POST"])
def size():
    return str(Data.query.count())

@app.route("/get_element",methods=["GET","POST"])
def get_element():
    dicter = json.loads(request.data)
    return str([d.data for d in Data.query.filter_by(id=int(dicter["data"])).all()])

@app.route("/pretty_print",methods=["GET","POST"])
def pretty_print():
    return str([d.data for d in Data.query.all()])
