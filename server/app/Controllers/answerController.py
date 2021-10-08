import sys
from flask import request, jsonify

from Models.Question import Question
from Models.Answer import Answer
from Models.User import User
from Models.AnswerBookmarks import AnswerBookmark
from flask_sqlalchemy import SQLAlchemy
from Controllers.UserController import getCurrnetUser

from flask_jwt_extended import jwt_required

from flask_cors import cross_origin

import json

db = SQLAlchemy()

@jwt_required()
@cross_origin()
def create_answer(qid):
    reqData = request.get_json()
    body = reqData.get("body", None)
    if body==None:
        return jsonify({ "msg" : "Please enter a valid answer!"}), 400

    question = Question.query.filter_by(id = qid).first()
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()

    newAnswer = Answer(
                body = body,
                parentQuestion = question,
                owner = currentUserObject
            )

    db.session.close_all()
    db.session.add(newAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
        'answer': newAnswer.serializeAnswer()
     }

@jwt_required()
@cross_origin()
def get_answers (qid) :
    questionAnswers = Answer.query.filter_by(parentQuestion_id = qid).all()
    questionAnswers = [answer.serializeAnswer() for answer in questionAnswers]

    return {
        'msg' : 'success',
        'length': len(questionAnswers),
        'Answers' : questionAnswers
    }

@jwt_required()
@cross_origin()
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
@cross_origin()
def delete_answer(aid):

    deletedAnswer = Answer.query.filter_by(id = aid).first()

    db.session.close_all()
    db.session.delete(deletedAnswer)
    db.session.commit()
    
    return { 
        'msg' : 'success',
     }

@jwt_required()
@cross_origin()
def like_answer (aid) :
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    answer = Question.query.filter_by(id = aid).first()
    if int(currentUserObject.id) in list(answer.serializeQuestion()['userLikes']) :
        return { 'msg' : 'already liked!' }
        
    answer.userLikes.append(currentUserObject)
    answer.likes += 1
    db.session.close_all()
    db.session.add(answer)
    db.session.commit()
    return { 
            'msg' : 'The answer has been disliked!'
           }


@jwt_required()
@cross_origin()
def bookmark_answer (aid) :
    if AnswerBookmark.query.filter_by(bookmarkedAid = aid).first() :
        return { 'msg' : 'already bookmarked!' }
    
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()

    bookmarkedAnswer = AnswerBookmark(
                            bookmarkedAid = aid,
                            owner = currentUserObject
                        )
    db.session.close_all()
    db.session.add(bookmarkedAnswer)
    db.session.commit()

    return { 
            'msg' : 'success',
            'bookmrkedAnswers' : bookmarkedAnswer.serializeAnswerBookmark()
           }

@jwt_required()
@cross_origin()
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

@cross_origin()
def optionsHanlder() :
    return "OK", 200