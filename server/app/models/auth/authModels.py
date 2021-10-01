from flask_login import UserMixin

from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    universityId = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String(270), nullable=False)
    picture = db.Column(db.String, nullable=False)
    department = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f'<User {self.name}>' 