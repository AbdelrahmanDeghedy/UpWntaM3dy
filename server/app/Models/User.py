<<<<<<< HEAD:server/app/models/auth/authModels.py
from flask_login import UserMixin
||||||| 215d456:server/app/auth/models.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database import db
from flask_login import UserMixin
>>>>>>> AO:server/app/Models/User.py

<<<<<<< HEAD:server/app/models/auth/authModels.py
from app import db
||||||| 215d456:server/app/auth/models.py
app = Flask(__name__)
=======
>>>>>>> AO:server/app/Models/User.py

<<<<<<< HEAD:server/app/models/auth/authModels.py
class User(UserMixin, db.Model):
||||||| 215d456:server/app/auth/models.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/deghedy/Desktop/UpWntaM3dy/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
=======
class User(UserMixin, db.Model):
    __tablename__ = 'users'
>>>>>>> AO:server/app/Models/User.py
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