from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .database import db
from marshmallow import Schema, fields, ValidationError
from flask_login import UserMixin

AnswerLikesSchema = Schema.from_dict(
    {
        "likedAid": fields.Integer(),
        "owner_id" : fields.Str()
    }
)

class AnswerLike(UserMixin, db.Model):
    __tablename__ = 'answerLikes'
    likedAid = db.Column(db.Integer, primary_key=True, autoincrement=True)

    parentAnswer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serializeAnswerLike(self) :
        schema = AnswerLikesSchema()
        result = schema.dump(self)
        return result

    def __repr__(self):
        return '<liked answer %r' % self.likedAid