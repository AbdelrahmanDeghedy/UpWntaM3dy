import sys
from flask import request, jsonify

from Models.Question import Question
from Models.Answer import Answer
from Models.User import User
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
    answer = Answer.query.filter_by(id = aid).first()
    
    if int(answer.id) in list(currentUserObject.serializeUser()['likedAnswerIds']) :
        return { 'msg' : 'already liked!' }


    answer.userLikedAnswers.append(currentUserObject)
    answer.likes +=1 
    
    db.session.close_all()
    db.session.add(answer)
    db.session.commit()
    db.session.close_all()

    return {
        'msg':'Question liked successfully!'
    }

@jwt_required()
@cross_origin()
def dislike_answer (aid) :
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    answer = Answer.query.filter_by(id = aid).first()
    
    if int(answer.id) not in list(currentUserObject.serializeUser()['likedAnswerIds']) :
        return { 'msg' : 'already disliked!' }


    answer.userLikedAnswers.remove(currentUserObject)
    answer.likes -=1 
    
    db.session.close_all()
    db.session.add(answer)
    db.session.commit()
    db.session.close_all()

    return {
        'msg':'Question disliked successfully!'
    }

@jwt_required()
@cross_origin()
def bookmark_answer (aid) :
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    answer = Answer.query.filter_by(id = aid).first()
    
    if int(answer.id) in list(currentUserObject.serializeUser()['bookmarkedAnswerIds']) :
        return { 'msg' : 'already bookmarked!' }


    answer.userBookmarkedAnswers.append(currentUserObject)
    
    db.session.close_all()
    db.session.add(answer)
    db.session.commit()
    db.session.close_all()

    return {
        'msg':'Question bookmarked successfully!'
    }


@jwt_required()
@cross_origin()
def removeBookmark_answer (aid) :
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    answer = Answer.query.filter_by(id = aid).first()
    
    if int(answer.id) not in list(currentUserObject.serializeUser()['bookmarkedAnswerIds']) :
        return { 'msg' : 'already not bookmarked!' }


    answer.userBookmarkedAnswers.remove(currentUserObject)
    
    db.session.close_all()
    db.session.add(answer)
    db.session.commit()
    db.session.close_all()

    return {
        'msg':'bookmarked removed successfully!'
    }
    

@cross_origin()
def optionsHanlder() :
    return "OK", 200