from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(32), index=True)
    first_name = db.Column(db.String(32), index=True)
    last_name = db.Column(db.String(32), index=True)
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), index=True)
    nationality = db.Column(db.String(64), index=True)
    cell = db.Column(db.String(64), index=True)
    street = db.Column(db.String(64), index=True)
    street_number = db.Column(db.Integer, index=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(64), index=True)
    country = db.Column(db.String(64), index=True)
    postcode = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

