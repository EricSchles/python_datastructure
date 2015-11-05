#Intro

The database `mongo_esc` is an extremely simple database.

##The Basics:

###Connecting

```
>>> from client import DB
>>> db = DB()
>>> db.connect()
```

###Putting Data In && Getting Data Out

```
>>> from client import DB
>>> db = DB()
>>> db.connect()
>>> db.change_db("eric")
>>> parameters={"keys":None,"values":None,"document":{"answer to everything":42}}
>>> db.get_data("schles",parameters=parameters)
[{u'answer to everything': 42}]
>>> parameters={"keys":["answer to everything"],"values":None,"document":None}
>>> db.get_data("schles",parameters=parameters)
[{u'answer to everything': 42}]
>>> parameters={"keys":None,"values":[42],"document":None}
>>> db.get_data("schles",parameters=parameters)
[{u'answer to everything': 42}]
>>> db.save_data("schles",{"thingsz":"happy"})
```




