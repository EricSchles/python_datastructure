from app import db

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.Integer)

    def __init__(self,data):
        self.data = data

    def __str__(self):
        return repr(self.data)
    
