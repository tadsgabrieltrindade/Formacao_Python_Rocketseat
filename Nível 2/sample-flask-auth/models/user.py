from app import db
from flask_login import UserMinin

class User(db.Model, UserMinin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    # def __init__(self, id, username, password):
    #     self.id = id
    #     self.username = username
    #     self.password = password
        