from sql_alchemy import db

class ImageModel(db.Model):
    __tablename__ = "image"

    id = db.Column(db.Integer, primary_key=True)
    imageBase64 = db.Column(db.String())
    dt_create = db.Column(db.DateTime())
    active = db.Column(db.Boolean())

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("UserModel", back_populates="image", uselist=False)
    
    def __init__(self, imageBase64):
        self.imageBase64 = imageBase64

    def to_json(self):
        return {
            "id": self.id,
            "imageBase64": self.imageBase64,
            "dt_create": str(self.dt_create),
            "active": self.active
        }
    
    def Create(self):
        db.session.add(self)
        db.session.commit()