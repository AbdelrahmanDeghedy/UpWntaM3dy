from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

from .database import db
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

user_likes_identifier = db.Table('user_likes_identifier', 
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)
user_bookmarks_identifier = db.Table('user_bookmarks_identifier', 
    db.Column('question_id', db.Integer, db.ForeignKey('questions.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

user_liked_Answers_identifier = db.Table('user_liked_Answers_identifier', 
    db.Column('answer_id', db.Integer, db.ForeignKey('answers.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

user_bookmarked_Answers_identifier = db.Table('user_bookmarked_Answers_identifier', 
    db.Column('answer_id', db.Integer, db.ForeignKey('answers.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)

class User(db.Model):
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

    userLikes = db.relationship('Question', secondary=user_likes_identifier, lazy='subquery', backref=db.backref('userLikes', lazy=True))
    userBookmarks = db.relationship('Question', secondary=user_bookmarks_identifier, lazy='subquery', backref=db.backref('userBookmarks', lazy=True))

    userAnswerLikes = db.relationship('Answer', secondary=user_liked_Answers_identifier, lazy='subquery', backref=db.backref('userLikedAnswers', lazy=True))
    userAnswerBookmarks = db.relationship('Answer', secondary=user_bookmarked_Answers_identifier, lazy='subquery', backref=db.backref('userBookmarkedAnswers', lazy=True))

    def serializeUser(self) :
        schema = UserSchema(exclude=['password'])
        result = schema.dump(self)
        questionIds = [question.id for question in list(self.questionIds)]
        result['questionIds'] = questionIds

        answerIds = [answer.id for answer in list(self.answerIds)]
        result['answerIds'] = answerIds

        likedQuestions = [question.id for question in list(self.userLikes)]
        result['likedQuestionIds'] = likedQuestions

        bookmarkedQuestions = [question.id for question in list(self.userBookmarks)]
        result['bookmarkedQuestionIds'] = bookmarkedQuestions

        likedAnswers = [question.id for question in list(self.userAnswerLikes)]
        result['likedAnswerIds'] = likedAnswers

        bookmarkedAnswers = [question.id for question in list(self.userAnswerBookmarks)]
        result['bookmarkedAnswerIds'] = bookmarkedAnswers

        return result
    
    def __repr__(self):
        return f'{self.universityId}' 


