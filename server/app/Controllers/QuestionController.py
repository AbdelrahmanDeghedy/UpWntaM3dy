import sys
from flask import request, jsonify

from Models.Question import Question
from Models.User import User
from Models.QuestionLikes import QuestionLike
from Models.QuestionBookmarks import QuestionBookmark
from Controllers.UserController import getCurrnetUser, currnetUser
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import jwt_required

from flask_cors import cross_origin


db = SQLAlchemy()

@jwt_required()
@cross_origin()
def questions_get():
    questions = Question.query.filter().all()
    questionsList = [question.serializeQuestion() for question in questions]
    questionsList.reverse()
    # questionsList = sorted(questionsList, key = lambda k : k['pub_date'], reverse=True)

    
    return { 
        'msg' : 'success',
        'length' : len(questionsList),
        'questions': questionsList
     }
import json

@jwt_required()
@cross_origin()
def questions_post() :
    reqData = request.get_json()
    title = reqData.get("title", None)
    body = reqData.get("body", None)
    department = reqData.get("department", None)
    commaSeparatedTags = reqData.get("commaSeparatedTags", None)
    
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
def questions_edit (qid) :
    reqData = request.get_json()
    title = reqData.get("title", None)
    body = reqData.get("body", None)
    department = reqData.get("department", None)
    commaSeparatedTags = reqData.get("commaSeparatedTags", None)


    editedQuestion = Question.query.filter_by(id = qid).first()
    db.session.close_all()


    editedQuestion.title = title if title != None else find_question_by_id(qid).title
    editedQuestion.body = body if body != None else find_question_by_id(qid).body
    editedQuestion.department = department if department != None else find_question_by_id(qid).department
    editedQuestion.commaSeparatedTags = commaSeparatedTags if commaSeparatedTags != None else find_question_by_id(qid).commaSeparatedTags
    
    
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