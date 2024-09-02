from .db import db, environment, SCHEMA

class Image(db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {"id": self.id,
                "image": self.image}
