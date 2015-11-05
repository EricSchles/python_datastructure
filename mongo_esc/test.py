import requests
from client import DB
db = DB()
db.connect()
db.change_db("thing")
db.save_data("thing",{"hello":"there"})
parameters={"keys":None,"values":None,"document":{"hello":"there"}}
print db.get_data("thing",parameters=parameters).text

