from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
import pickle

app = Flask(__name__)
#username,password = pickle.load(open("username_password.pickle","r"))
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://"+username+":"+password+"@localhost/database"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command("db",MigrateCommand)

from app import views,models
