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
        "bookmarked": fields.Boolean(),
        "department": fields.Str(),
        "commaSeparatedTags": fields.Str(),
        "owner_id": fields.Integer(),
        "owner" : fields.Str()
    }
)

user_likes_identifier = db.Table('user_likes_identifier', 
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)
user_dislikes_identifier = db.Table('user_dislikes_identifier', 
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

class Question(UserMixin, db.Model):
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

    userLikes = db.relationship('User', secondary=user_likes_identifier)
    userDisLikes = db.relationship('User', secondary=user_dislikes_identifier)


    def serializeQuestion(self) :
        schema = QuestionSchema()
        result = schema.dump(self)
        answerIds = [answer.id for answer in list(self.answerIds)]
        userLikes = [user.id for user in list(self.userLikes)]
        userDisLikes = [user.id for user in list(self.userDisLikes)]
        result['answerIds'] = answerIds
        result['userLikes'] = userLikes
        result['userDisLikes'] = userDisLikes

        return result
        
    def __repr__(self):
        return '<Question %r' % self.title

    