import requests
import json
import random

print requests.post("http://localhost:5000/add", data = json.dumps({"data":"5"})).text
print requests.get("http://localhost:5000/size").text
print requests.post("http://localhost:5000/get_element", data = json.dumps({"data":"0"})).text
print requests.post("http://localhost:5000/pretty_print").text
print requests.post("http://localhost:5000/remove", data = json.dumps({"data":"5"})).text

