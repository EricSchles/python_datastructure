import json
import random
import hashlib
from glob import glob
import os

class DB:
    def __init__(self):
        pass

    def save_data(self,collection,document):
        if os.getcwd() == "dbs":
            return "No DB specified" #make this an exception
        else:
            if not os.path.exists(collection):
                os.mkdir(collection)
            os.chdir(collection)
            file_name = hashlib.sha256(str(random.randint(0,1000000))).hexdigest()
            while file_name in glob("*"):
                file_name = hashlib.sha256(str(random.randint(0,1000000))).hexdigest()
            json.dump(document,open(str(file_name),"w"))
            os.chdir("../")

    def get_data(self,collection,document=None,keys=None,values=None,ids=None):
        search_params = [keys,values,ids]
        to_return = []
        to_search = []
        if document == None:
            os.chdir(collection)
            if any(search_params):
                for doc in glob("*"): to_search.append(json.load(open(doc,"r")))
                if keys:
                    for doc in to_search:
                        for key in doc.keys():
                            if key in keys:
                                to_return.append({key:doc[key]})
                if values:
                    for doc in to_search:
                        for value in values:
                            for key in doc.keys():
                                if value == doc[key]:
                                    to_return.append({key:doc[key]})
                if ids:
                    for Id in ids:
                        if Id in glob("*"):
                            to_return.append(json.load(open(Id),"r"))
        elif document:
            os.chdir(collection)
            for doc in glob("*"): to_search.append(json.load(open(doc,"r")))
            for doc in to_search:
                if doc == document:
                    if any(search_params):
                        if keys:
                            for key in doc.keys():
                                if key in keys:
                                    to_return.append({key:doc[key]})
                        if values:
                            for value in values:
                                for key in doc.keys():
                                    if value == doc[key]:
                                        to_return.append({key:doc[key]})
                    else:
                        to_return.append(doc)
        os.chdir("../")
        return to_return

    def create_db(self,db_name):
        if db_name == "dbs":
            return "can't name your datastore dbs" #make this an exception
        os.mkdir(db_name)

    def change_db(self,db_name):
        if not os.path.exists(db_name):
            if not self.create_db(db_name):
                return "can't name your datastore dbs" #make this an exception
        os.chdir(db_name)

    def connect(self):
        if not os.path.exists("dbs"):
            os.mkdir("dbs")
        os.chdir("dbs")
