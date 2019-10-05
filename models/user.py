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

    def __init__(self, name, email, password, rg, cpf, birthdate):
        self.name = name
        self.email = email
        self.password = password
        self.rg = rg
        self.cpf = cpf
        self.birthdate = birthdate
    
    def to_json(self):
        return {
            "user_id": self.user_id,
	        "name": self.name,
	        "email": self.email,
	        "password": self.password,
	        "rg": self.rg,
	        "cpf": self.cpf,
	        "birthdate": str(self.birthdate),
            "dt_create": str(self.dt_create),
            "dt_update": str(self.dt_update),
            "active": self.active
        }
    
    def Create(self):
        print(self)
        db.session.add(self)
        db.session.commit()    
