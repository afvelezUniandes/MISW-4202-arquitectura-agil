from . import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), nullable=False)