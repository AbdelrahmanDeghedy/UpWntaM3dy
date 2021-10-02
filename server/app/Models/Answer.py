from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .database import db
from marshmallow import Schema, fields, ValidationError

AnswerSchema = Schema.from_dict(
    {
        "id": fields.Integer(),
        "pub_date": fields.Date(),
        "body": fields.Str(),
        "likes": fields.Integer(),
        "parentQuestion_id": fields.Integer(),
        "parentQuestion" : fields.Str()
    }
)

class Answer(db.Model):
    __tablename__ = 'answers'
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    body = db.Column(db.String(270), nullable=True)
    likes = db.Column(db.Integer, default=0, nullable=False)

    parentQuestion_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)

    #Date and Time
    #Foreign keys
    #Reports => []
    #User => one user

    def serializeAnswer(self) :
        schema = AnswerSchema()
        result = schema.dump(self)
        return result

    def __repr__(self):
        return '<Answer %r' % self.id