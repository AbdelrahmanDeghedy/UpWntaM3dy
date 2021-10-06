from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .database import db
from marshmallow import Schema, fields, ValidationError
from flask_login import UserMixin

AnswerBookmarksSchema = Schema.from_dict(
    {
        "bookmarkedAid": fields.Integer(),
        "owner_id" : fields.Str()
    }
)

class AnswerBookmark(UserMixin, db.Model):
    __tablename__ = 'answerBookmarks'
    bookmarkedAid = db.Column(db.Integer, primary_key=True, autoincrement=True)

    parentAnswer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serializeAnswerBookmark(self) :
        schema = AnswerBookmarksSchema()
        result = schema.dump(self)
        return result

    def __repr__(self):
        return '<bookmarked answer %r' % self.bookmarkedAid