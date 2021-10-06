import sys
from flask import request, jsonify

from Models.Question import Question
from Models.User import User
from Models.QuestionLikes import QuestionLike
from Models.QuestionBookmarks import QuestionBookmark
from Controllers.UserController import getCurrnetUser, currnetUser
from flask_sqlalchemy import SQLAlchemy

from server.app.validators.validation import *
from cerberus import Validator

from flask_jwt_extended import jwt_required
from flask_cors import cross_origin


db = SQLAlchemy()

@jwt_required()
@cross_origin()
def questions_get():
    questions = Question.query.filter().all()
    questionsList = [question.serializeQuestion() for question in questions]
    
    return { 
        'msg' : 'success',
        'length' : len(questionsList),
        'questions': questionsList
     }
import json

@jwt_required()
@cross_origin()
def questions_post():

    departments = ['CCE', 'EME', 'CAE', 'CSE'] #Add all departments
    reqData = request.get_json()
    questions_schema = {
    'title':{'required':True,'type':'string', 'maxlength':140},
    'body':{'type':'string','nullable':True},
    'department':{'type':'string', 'required':True, 'allowed':departments},
    'commaSeparatedTags': {'type':'string', 'check_with':check_tags}
    }
    reqData = request.get_json()
    validator = Validator(questions_schema)
    validated = validator.validate(reqData)

    if validated:
        title = reqData.get("title", None)
        body = reqData.get("body", None)
        department = reqData.get("department", None)
        commaSeparatedTags = reqData.get("commaSeparatedTags", None)
    else:
        return jsonify({ "msg" : validator.errors}), 400
    
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()

    newQuestion = Question(
                    title = title,
                    body = body,
                    department = department,
                    commaSeparatedTags = commaSeparatedTags,
                    owner = currentUserObject
                )
    
    db.session.close_all()
    db.session.add(newQuestion)
    db.session.commit()

    
    return {
        "msg": "success",
        "Created Question": newQuestion.serializeQuestion()
    }

def find_question_by_id (qid) :
    return Question.query.filter_by(id = qid).first()

@jwt_required()
@cross_origin()
def questions_edit (qid):
    editedQuestion = Question.query.filter_by(id = qid).first()
    db.session.close_all()

    #Instead of returning None it returns the old value
    reqData = request.get_json()
    title = reqData.get("title", editedQuestion.title)
    body = reqData.get("body", editedQuestion.body)
    department = reqData.get("department", editedQuestion.department)
    commaSeparatedTags = reqData.get("commaSeparatedTags", editedQuestion.commaSeparatedTags)


    editedQuestion.title = title
    editedQuestion.body = body
    editedQuestion.department = department
    editedQuestion.commaSeparatedTags = commaSeparatedTags
    
    
    db.session.add(editedQuestion)
    db.session.commit()

    
    return jsonify ({
        "msg": "success",
        "Updated Question": editedQuestion.serializeQuestion()
    })

@jwt_required()
@cross_origin()
def questions_delete (qid) :
    deletedQuestion = Question.query.filter_by(id = qid).first()
    
    
    db.session.close_all()
    db.session.delete(deletedQuestion)
    db.session.commit()

    
    return {
        "msg": "success",
    }

@jwt_required()
@cross_origin()
def questions_like (qid) :
    if QuestionLike.query.filter_by(likedQid = qid).first() :
        return { 'msg' : 'already liked!' }

    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()

    editedQuestion = Question.query.filter_by(id = qid).first()
    editedQuestion.likes += 1
    
    db.session.close_all()
    db.session.add(editedQuestion)
    db.session.commit()

    likedQuestion = QuestionLike(
                            likedQid = qid,
                            owner = currentUserObject
                        )
    db.session.close_all()
    db.session.add(likedQuestion)
    db.session.commit()

    return { 
            'msg' : 'success',
            'likedQuestions' : likedQuestion.serializeLike()
           }

@jwt_required()
@cross_origin()
def questions_dislike (qid) :
    if not (QuestionLike.query.filter_by(likedQid = qid).first()) :
        return { 'msg' : 'already disliked!' }

    likedQues = QuestionLike.query.filter_by(likedQid = qid).first()
    
    editedQuestion = Question.query.filter_by(id = qid).first()
    editedQuestion.likes -= 1
    
    db.session.close_all()
    db.session.add(editedQuestion)
    db.session.commit()

    db.session.delete(likedQues)
    db.session.commit()
    db.session.close_all()

    return { 
            'msg' : 'success',
           }

@jwt_required()
@cross_origin()
def questions_bookmark (qid) :
    if QuestionBookmark.query.filter_by(bookmarkedQid = qid).first() :
        return { 'msg' : 'already bookmarked!' }

    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()

    bookmarkedQuestion = QuestionBookmark(
                            bookmarkedQid = qid,
                            owner = currentUserObject
                        )
    db.session.close_all()
    db.session.add(bookmarkedQuestion)
    db.session.commit()

    return { 
            'msg' : 'success',
            'likedQuestions' : bookmarkedQuestion.serializeQuestionBookmark()
           }

@jwt_required()
@cross_origin()
def questions_removeBookmark (qid) :
    if not (QuestionBookmark.query.filter_by(bookmarkedQid = qid).first()) :
        return { 'msg' : 'already not bookmarked!' }

    bookmarkedQuestion = QuestionBookmark.query.filter_by(bookmarkedQid = qid).first()
    
    db.session.close_all()
    db.session.delete(bookmarkedQuestion)
    db.session.commit()

    return { 
            'msg' : 'success',
           }



@cross_origin()
def optionsHanlder() :
    return "OK", 200