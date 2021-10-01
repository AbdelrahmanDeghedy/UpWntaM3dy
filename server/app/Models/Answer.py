from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .database import db

class Answer(db.Model):
    __tablename__ = 'answers'
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    body = db.Column(db.String(270), nullable=True)

    likes = db.Column(db.Integer, default=0, nullable=False)
    dislikes = db.Column(db.Integer, default=0, nullable=False)

    #Date and Time
    #Foreign keys
    #Reports => []
    #User => one user

    def __repr__(self):
        #self.question
        return '<Answer %r' % self.id