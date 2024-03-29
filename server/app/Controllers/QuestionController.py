import sys
from flask import request, jsonify

from Models.Question import Question
from Models.User import User
from Controllers.UserController import getCurrnetUser, currnetUser
from flask_sqlalchemy import SQLAlchemy

from validators.validation import *
from cerberus import Validator

from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

from sqlalchemy import desc



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
def questions_post():
    # departments = ['CCE', 'EME', 'CAE', 'CSE'] #Add all departments
    questions_schema = {
    'title':{'required':True,'type':'string', 'maxlength':140},
    'body':{'type':'string','nullable':True},
    # 'department':{'type':'string', 'required':True, 'allowed':departments},
    'department':{'type':'string', 'required':True},
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

    #Instead of returning None it returns the old value (smart, Thanks!)
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
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    question = Question.query.filter_by(id = qid).first()
    
    if int(question.id) in list(currentUserObject.serializeUser()['likedQuestionIds']) :
        return { 'msg' : 'already liked!' }


    question.userLikes.append(currentUserObject)
    question.likes +=1 
    
    db.session.close_all()
    db.session.add(question)
    db.session.commit()
    db.session.close_all()

    return {
        'msg':'Question liked successfully!'
    }

@jwt_required()
@cross_origin()
def questions_dislike (qid) :
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    question = Question.query.filter_by(id = qid).first()
    if int(question.id) not in list(currentUserObject.serializeUser()['likedQuestionIds']) :
        return { 'msg' : 'already disliked!' }
    

    question.userLikes.remove(currentUserObject)
    question.likes -=1 
    
    db.session.close_all()
    db.session.add(question)
    db.session.commit()

    return {
        'msg':'Question disliked successfully!'
    }
    


@jwt_required()
@cross_origin()
def questions_bookmark (qid) :
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    question = Question.query.filter_by(id = qid).first()
    
    if int(question.id) in list(currentUserObject.serializeUser()['bookmarkedQuestionIds']) :
        return { 'msg' : 'already bookmarked!' }


    question.userBookmarks.append(currentUserObject)
    
    db.session.close_all()
    db.session.add(question)
    db.session.commit()
    db.session.close_all()

    return { 
            'msg' : 'success',
           }


@jwt_required()
@cross_origin()
def questions_removeBookmark (qid) :
    currentUserObject = User.query.filter_by(universityId = json.loads(getCurrnetUser().data)['universityId']).first()
    question = Question.query.filter_by(id = qid).first()
    
    if int(question.id) not in list(currentUserObject.serializeUser()['bookmarkedQuestionIds']) :
        return { 'msg' : 'already not bookmarked!' }


    question.userBookmarks.remove(currentUserObject)
    
    db.session.close_all()
    db.session.add(question)
    db.session.commit()
    db.session.close_all()

    return { 
            'msg' : 'success',
           }




@jwt_required()
@cross_origin()
def sort_by_likes():
    #query = session.query(SpreadsheetCells).order_by(SpreadsheetCells.y_index)
    questions = Question.query.filter().order_by(desc(Question.likes))
    questionsList = [question.serializeQuestion() for question in questions]
    
    return { 
        'msg' : 'success',
        'length' : len(questionsList),
        'questions': questionsList
     }

@jwt_required()
@cross_origin()
def sort_by_answersCount () :
    questions = Question.query.filter().all()
    questionsList = [question.serializeQuestion() for question in questions]
    questionsList = sorted(questionsList, key = lambda k : len(k['answerIds']), reverse=True)

    
    return { 
        'msg' : 'success',
        'length' : len(questionsList),
        'questions': questionsList
     }

@jwt_required()
@cross_origin()
def get_tags () :
    questions = Question.query.filter().all()
    tags = []
    for question in questions:
        if question.serializeQuestion()['commaSeparatedTags'] != "":
            for tag in question.serializeQuestion()['commaSeparatedTags'].split(",") :
                tags.append(tag)
    tags = list(set(tags))
                
    
    return { 
        'msg' : 'success',
        'length' : len(tags),
        'tags': tags
     }

@cross_origin()
def optionsHanlder() :
    return "OK", 200
