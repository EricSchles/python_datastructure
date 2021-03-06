import requests as req
import json
#from server import app
class DB:
    def __init__(self):
        #self._start_server()
        self.server = "http://localhost:5002/"
    #def _start_server(self):
    #    app.run()
    def connect(self):
        req.post(self.server+"connect")
    def change_db(self,collection):
        if type("") == type(collection):
            req.post(self.server+"change_db/"+collection)
        else:
            print "sorry, wrong type, collection must be a string"
    def save_data(self,collection,document):
        if type("") == type(collection) and type(document) == type({}):
            req.post(self.server+"save_data/"+collection+"/"+json.dumps(document))
        else:
            print "collection must be of type string and document must be a dictionary"
    def get_data(self,collection,parameters=None):
        if type("") == type(collection):
            if parameters==None:
                parameters = {
                    "keys":None,
                    "values":None,
                    "document":None
                }
            result = req.post(self.server+"get_data/"+collection+"/"+json.dumps(parameters))
            return json.loads(result.text)
        else:
            if type(parameters) != type({}):
                print """
                collection must be a string and parameters must be in a dictionary of the following form:  { 'keys': [key1,key2,..],'values':[value1,value2,..], 'document': {"some specific document": "goes here" } }"""
            else:
                print "collection must be a string"
