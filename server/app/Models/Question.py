from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .database import db
from flask_login import UserMixin
from marshmallow import Schema, fields, ValidationError


QuestionSchema = Schema.from_dict(
    {
        "id": fields.Integer(),
        "pub_date": fields.Date(),
        "title": fields.Str(), 
        "body": fields.Str(),
        "likes": fields.Integer(),
        "bookmarked": fields.Boolean(),
        "owner_id": fields.Integer(),
        "owner" : fields.Str()
    }
)

class Question(UserMixin, db.Model):
    __tablename__ = 'questions'
    id  = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.String(270), nullable=True)
    likes = db.Column(db.Integer, default=0, nullable=False)
    bookmarked = db.Column(db.Boolean, default=False, nullable=False)
    
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    answerIds = db.relationship('Answer', backref = "parentQuestion")


    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    # user = db.relationship('User',backref=db.backref('questions', lazy=True))

    #Foreign keys
    #Reports => []
    #Answers => []

    def serializeQuestion(self) :
        schema = QuestionSchema()
        result = schema.dump(self)
        answerIds = [answer.id for answer in list(self.answerIds)]
        result['answerIds'] = answerIds
        return result

    def __repr__(self):
        return '<Question %r' % self.title

    