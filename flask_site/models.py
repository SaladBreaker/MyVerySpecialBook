from .app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), unique=False, nullable=True)
    title = db.Column(db.String(200), unique=False, nullable=True)
