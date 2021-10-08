from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .database import db
from marshmallow import Schema, fields, ValidationError


QuestionSchema = Schema.from_dict(
    {
        "id": fields.Integer(),
        "pub_date": fields.Date(),
        "title": fields.Str(), 
        "body": fields.Str(),
        "likes": fields.Integer(),
        "department": fields.Str(),
        "commaSeparatedTags": fields.Str(),
        "owner_id": fields.Integer(),
        "owner" : fields.Str()
    }
)


class Question(db.Model):
    __tablename__ = 'questions'
    id  = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(200), default="", nullable=False)
    body = db.Column(db.String(270), default="", nullable=True)
    department = db.Column(db.String(270), nullable=True)
    commaSeparatedTags = db.Column(db.String(270), default="", nullable=True)
    likes = db.Column(db.Integer, default=0, nullable=False)
    
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    answerIds = db.relationship('Answer', backref = "parentQuestion")

    def serializeQuestion(self) :
        schema = QuestionSchema()
        result = schema.dump(self)
        
        answerIds = [answer.id for answer in list(self.answerIds)]
        result['answerIds'] = answerIds

        return result
        
    def __repr__(self):
        return '<Question %r' % self.title

    