from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .database import db
from marshmallow import Schema, fields, ValidationError
from flask_login import UserMixin

QuestionBookmarksSchema = Schema.from_dict(
    {
        "bookmarkedQid": fields.Integer(),
        "owner_id" : fields.Str()
    }
)

class QuestionBookmark(UserMixin, db.Model):
    __tablename__ = 'questionBookmarks'
    bookmarkedQid = db.Column(db.Integer, primary_key=True, autoincrement=True)

    parentQuestion_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serializeQuestionBookmark(self) :
        schema = QuestionBookmarksSchema()
        result = schema.dump(self)
        return result

    def __repr__(self):
        return '<bookmarked Question %r' % self.bookmarkedQid