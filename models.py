from flask_login import UserMixin
from __init__ import db

class User(UserMixin,db.Model):
    id = db.Column(db.String(256), primary_key=True)
    email = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(256))
    name = db.Column(db.String(256))
