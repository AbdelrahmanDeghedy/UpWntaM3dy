from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .database import db
from marshmallow import Schema, fields, ValidationError
from flask_login import UserMixin

QuestionLikesSchema = Schema.from_dict(
    {
        "likedQid": fields.Integer(),
        "owner_id" : fields.Str()
    }
)

class QuestionLike(UserMixin, db.Model):
    __tablename__ = 'questionLikes'
    likedQid = db.Column(db.Integer, primary_key=True, autoincrement=True)

    parentQuestion_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serializeLike(self) :
        schema = QuestionLikesSchema()
        result = schema.dump(self)
        return result

    def __repr__(self):
        return '<liked question %r' % self.likedQid