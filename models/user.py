from flask import jsonify
from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(20))
    rg = db.Column(db.String(14))
    cpf = db.Column(db.String(14))
    birthdate = db.Column(db.DateTime())
    dt_create = db.Column(db.DateTime())
    dt_update = db.Column(db.DateTime())
    active = db.Column(db.Boolean())

def __init__(self, name, email, rg, cpf, birthdate):
        self.name = name
        self.email = email
        self.rg = rg
        self.cpf = cpf
        self.birthdate = birthdate
