from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .database import db
# app = Flask(__name__)
# db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.String(270), nullable=True)

    likes = db.Column(db.Integer, default=0, nullable=False)
    
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    # user = db.relationship('User',backref=db.backref('questions', lazy=True))

    #Foreign keys
    #Reports => []
    #Answers => []

    def __repr__(self):
        return '<Question %r' % self.title

    @property
    def serialize(self):
        return {
            'id': self.id,
            'pub_date': self.pub_date,
            'title': self.title,
            'body': self.body,
            'likes': self.likes
        }