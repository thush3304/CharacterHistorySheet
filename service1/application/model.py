from . import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    era = db.Column(db.String(30), nullable=False)
    prof = db.Column(db.String(30), nullable=False)
    char = db.Column(db.String(30))
