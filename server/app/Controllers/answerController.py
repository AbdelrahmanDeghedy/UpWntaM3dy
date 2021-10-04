import sys
from flask import request, jsonify

from Models.Question import Question
from Models.Answer import Answer
from Models.User import User
from Models.AnswerLikes import AnswerLike
from Models.AnswerBookmarks import AnswerBookmark
from flask_sqlalchemy import SQLAlchemy
from Controllers.UserController import getCurrnetUser

from flask_jwt_extended import jwt_required


db = SQLAlchemy()

@jwt_required()
def create_answer(qid):
    reqData = request.get_json()
    body = reqData.get("body", None)

    question = Question.query.filter_by(id = qid).first()
    print (question)

    newAnswer = Answer(
                body = body,
                parentQuestion = question,
                owner = getCurrnetUser()
            )

    db.session.close_all()
    db.session.add(newAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
        'answer': newAnswer.serializeAnswer()
     }

@jwt_required()
def get_answers (qid) :
    questionAnswers = Answer.query.filter_by(parentQuestion_id = qid).all()
    questionAnswers = [answer.serializeAnswer() for answer in questionAnswers]

    return {
        'msg' : 'success',
        'length': len(questionAnswers),
        'Answers' : questionAnswers
    }

@jwt_required()
def edit_answer(aid):
    reqData = request.get_json()
    body = reqData.get("body", None)

    editedAnswer = Answer.query.filter_by(id = aid).first()
    db.session.close_all()

    editedAnswer.body = body if body != None else edit_answer.body

    db.session.add(editedAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
        'editedAnswer': editedAnswer.serializeAnswer()
     }

@jwt_required()
def delete_answer(aid):

    deletedAnswer = Answer.query.filter_by(id = aid).first()

    db.session.close_all()
    db.session.delete(deletedAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
     }

@jwt_required()
def like_answer (aid) :
    if AnswerLike.query.filter_by(likedAid = aid).first() :
        return { 'msg' : 'already liked!' }
    likedAnswer = AnswerLike(
                            likedAid = aid,
                            owner = getCurrnetUser()
                        )
    db.session.close_all()
    db.session.add(likedAnswer)
    db.session.commit()

    return { 
            'msg' : 'success',
            'likedAnswers' : likedAnswer.serializeAnswerLike()
           }

@jwt_required()
def dislike_answer (aid) :
    if not (AnswerLike.query.filter_by(likedAid = aid).first()) :
        return { 'msg' : 'already disliked!' }

    likedAnswer = AnswerLike.query.filter_by(likedAid = aid).first()
    
    db.session.close_all()
    db.session.delete(likedAnswer)
    db.session.commit()

    return { 
            'msg' : 'success',
           }

@jwt_required()
def bookmark_answer (aid) :
    if AnswerBookmark.query.filter_by(bookmarkedAid = aid).first() :
        return { 'msg' : 'already bookmarked!' }
    bookmarkedAnswer = AnswerBookmark(
                            bookmarkedAid = aid,
                            owner = getCurrnetUser()
                        )
    db.session.close_all()
    db.session.add(bookmarkedAnswer)
    db.session.commit()

    return { 
            'msg' : 'success',
            'bookmrkedAnswers' : bookmarkedAnswer.serializeAnswerBookmark()
           }

@jwt_required()
def removeBookmark_answer (aid) :
    if not (AnswerBookmark.query.filter_by(bookmarkedAid = aid).first()) :
        return { 'msg' : 'already not bookmarked!' }

    bookmarkedAnswer = AnswerBookmark.query.filter_by(bookmarkedAid = aid).first()
    
    db.session.close_all()
    db.session.delete(bookmarkedAnswer)
    db.session.commit()

    return { 
            'msg' : 'success',
           }