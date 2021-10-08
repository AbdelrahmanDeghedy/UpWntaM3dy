from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .database import db
from marshmallow import Schema, fields, ValidationError
from flask_login import UserMixin

AnswerSchema = Schema.from_dict(
    {
        "id": fields.Integer(),
        "pub_date": fields.Date(),
        "body": fields.Str(),
        "likes": fields.Integer(),
        "parentQuestion_id": fields.Integer(),
        "owner_id" : fields.Str()
    }
)

answer_user_likes_identifier = db.Table('answer_user_likes_identifier', 
    db.Column('answer_id', db.Integer, db.ForeignKey('answers.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)
class Answer(UserMixin, db.Model):
    __tablename__ = 'answers'
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    body = db.Column(db.String(270), nullable=True)
    likes = db.Column(db.Integer, default=0, nullable=False)

    parentQuestion_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    userLikes = db.relationship('User', secondary=answer_user_likes_identifier)


    def serializeAnswer(self) :
        schema = AnswerSchema()
        result = schema.dump(self)
        userLikes = [user.id for user in list(self.userLikes)]
        result['userLikes'] = userLikes
        return result

    def __repr__(self):
        return '<Answer %r' % self.id