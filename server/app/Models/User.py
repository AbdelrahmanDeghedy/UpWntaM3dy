from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

from .database import db
from flask_login import UserMixin
from marshmallow import Schema, fields, ValidationError


UserSchema = Schema.from_dict(
    {
        "id": fields.Integer(), 
        "name": fields.Str(), 
        "universityId": fields.Integer(), 
        "email": fields.Email(), 
        "password": fields.Str(),
        "points": fields.Integer(),
        "rank": fields.Integer(),
        "bio": fields.Str(), 
        "picture": fields.Str(), 
        "department": fields.Str(), 
    }
)

association_table = db.Table('association',
    db.Column('question_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('like_id', db.Integer, db.ForeignKey('questionLikes.likedQid'), primary_key=True)
)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
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
    questionIds = db.relationship('Question', backref = "owner")
    answerIds = db.relationship('Answer', backref = "owner")
    questionBookmarks = db.relationship('QuestionBookmark', backref = "owner")
    
    answerLikes = db.relationship('AnswerLike', backref = "owner")
    answerBookmarks = db.relationship('AnswerBookmark', backref = "owner")

    questionLikes = db.relationship('QuestionLike', secondary=association_table, backref=db.backref('users', lazy=True))

    def serializeUser(self) :
        schema = UserSchema(exclude=['password'])
        result = schema.dump(self)
        questionIds = [question.id for question in list(self.questionIds)]
        result['questionIds'] = questionIds

        answerIds = [answer.id for answer in list(self.answerIds)]
        result['answerIds'] = answerIds
        
        questionLikes = [like.likedQid for like in list(self.questionLikes)]
        result['likedQuestionIds'] = questionLikes

        questionBookmarks = [bookmark.bookmarkedQid for bookmark in list(self.questionBookmarks)]
        result['bookmarkedQuestionIds'] = questionBookmarks

        answerLikes = [like.likedAid for like in list(self.answerLikes)]
        result['likedAnswerIds'] = answerLikes

        answerBookmarks = [bookmark.bookmarkedAid for bookmark in list(self.answerBookmarks)]
        result['bookmarkedAnswerIds'] = answerBookmarks

        # print (result)
        return result
    
    def __repr__(self):
        return f'{self.universityId}' 


